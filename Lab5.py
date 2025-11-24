import subprocess
from pathlib import Path

BASE_DIR = Path("pki_lab")
CA_DIR = BASE_DIR / "ca"
USERS_DIR = BASE_DIR / "users"
DATA_DIR = BASE_DIR / "data"
SIG_DIR = DATA_DIR / "signatures"


def run(cmd: list[str]) -> None:
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True)


def init_ca():
    for d in [CA_DIR / "private", CA_DIR / "certs", CA_DIR / "crl", USERS_DIR, DATA_DIR, SIG_DIR]:
        d.mkdir(parents=True, exist_ok=True)

    ca_key = CA_DIR / "private" / "ca.key.pem"
    ca_cert = CA_DIR / "certs" / "ca.cert.pem"

    index = CA_DIR / "index.txt"
    serial = CA_DIR / "serial"
    crlnumber = CA_DIR / "crlnumber"

    if not index.exists():
        index.touch()
    if not serial.exists():
        serial.write_text("1000", encoding="utf-8")
    if not crlnumber.exists():
        crlnumber.write_text("1000", encoding="utf-8")

    if not ca_key.exists():
        run([
            "openssl", "genrsa",
            "-out", str(ca_key),
            "4096"
        ])

    if not ca_cert.exists():
        run([
            "openssl", "req",
            "-x509",
            "-new",
            "-nodes",
            "-key", str(ca_key),
            "-sha256",
            "-days", "3650",
            "-out", str(ca_cert),
            "-subj", "/C=MD/O=MyLabCA/CN=My Root CA"
        ])

    print("CA initialized.")


def create_user(username: str):
    user_key = USERS_DIR / f"{username}.key.pem"
    user_csr = USERS_DIR / f"{username}.csr.pem"
    user_cert = USERS_DIR / f"{username}.cert.pem"

    if not user_key.exists():
        run([
            "openssl", "genrsa",
            "-out", str(user_key),
            "2048"
        ])

    if not user_csr.exists():
        run([
            "openssl", "req",
            "-new",
            "-key", str(user_key),
            "-out", str(user_csr),
            "-subj", f"/C=MD/O=MyLabUsers/CN={username}"
        ])

    if not user_cert.exists():
        run([
            "openssl", "ca",
            "-config", str(OPENSSL_CNF),
            "-batch",
            "-in", str(user_csr),
            "-out", str(user_cert),
            "-days", "365",
            "-notext"
        ])

    print(f"User '{username}' created:")
    print("   private key:", user_key)
    print("   certificate:", user_cert)


OPENSSL_CNF = Path("openssl.cnf")


def revoke_user(username: str):
    user_cert = USERS_DIR / f"{username}.cert.pem"
    ca_crl = CA_DIR / "crl" / "ca.crl.pem"

    if not user_cert.exists():
        raise FileNotFoundError(f"User certificate not found: {user_cert}")

    print(f"Revoking {username}...")
    result = subprocess.run([
        "openssl", "ca",
        "-config", str(OPENSSL_CNF),
        "-revoke", str(user_cert)
    ], capture_output=True, text=True)

    if result.returncode == 0:
        print("Success: Certificate marked as revoked.")
    elif "Already revoked" in result.stdout or "Already revoked" in result.stderr:
        print(f"Note: User '{username}' was ALREADY revoked. Continuing...")
    else:
        print(result.stderr)
        raise subprocess.CalledProcessError(result.returncode, result.args)

    run([
        "openssl", "ca",
        "-config", str(OPENSSL_CNF),
        "-gencrl",
        "-out", str(ca_crl)
    ])

    print(f"User '{username}' revocation process complete.")
    print("   CRL updated:", ca_crl)


def sign_file(username: str, infile: Path, sigfile: Path):
    user_key = USERS_DIR / f"{username}.key.pem"
    if not user_key.exists():
        raise FileNotFoundError(f"User key not found: {user_key}")
    if not infile.exists():
        raise FileNotFoundError(f"Input file not found: {infile}")

    sigfile.parent.mkdir(parents=True, exist_ok=True)

    run([
        "openssl", "dgst",
        "-sha256",
        "-sign", str(user_key),
        "-out", str(sigfile),
        str(infile)
    ])

    print(f"File signed by '{username}':")
    print("   input:", infile)
    print("   signature:", sigfile)


def verify_signature(username: str, infile: Path, sigfile: Path):
    user_cert = USERS_DIR / f"{username}.cert.pem"
    if not user_cert.exists():
        raise FileNotFoundError(f"User cert not found: {user_cert}")
    if not infile.exists():
        raise FileNotFoundError(f"Input file not found: {infile}")
    if not sigfile.exists():
        raise FileNotFoundError(f"Signature file not found: {sigfile}")

    tmp_pubkey = USERS_DIR / f"{username}.pubkey.pem"
    run([
        "openssl", "x509",
        "-in", str(user_cert),
        "-pubkey",
        "-noout",
        "-out", str(tmp_pubkey)
    ])

    result = subprocess.run([
        "openssl", "dgst",
        "-sha256",
        "-verify", str(tmp_pubkey),
        "-signature", str(sigfile),
        str(infile)
    ], capture_output=True, text=True)

    print(result.stdout.strip())
    if result.returncode == 0:
        print("Signature is VALID.")
    else:
        print("Signature is INVALID.")


if __name__ == "__main__":
    init_ca()

    create_user("alina")

    test_file = DATA_DIR / "message.txt"
    test_file.write_text("Hello World!\n", encoding="utf-8")

    sig_file = SIG_DIR / "message.txt.sig"
    sign_file("alina", test_file, sig_file)

    verify_signature("alina", test_file, sig_file)

    #revoke_user("alice")
