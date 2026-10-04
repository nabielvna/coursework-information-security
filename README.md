# Information Security Coursework

Coursework for an Information Security class (Institut Teknologi Sepuluh Nopember, 2024). Everything is written in plain Python, without any cryptography library.

| Folder | What it is | How to run |
|---|---|---|
| [`des/`](des) | DES implemented from scratch (encrypts and decrypts text longer than 64 bits) | `cd des && python main.py` |
| [`rsa/`](rsa) | RSA implemented from scratch: key generation, encryption, digital signatures, PEM key storage | `cd rsa && python main.py` |
| [`des-socket-transfer/`](des-socket-transfer) | Assignments 1 and 2: DES used to send encrypted strings between two users over a socket | `python socket_server.py`, then `python socket_client.py` in another terminal |
| [`secure-chat/`](secure-chat) | Assignment 3: end-to-end encrypted chat (RSA + DES) with nonce-based mutual authentication and server-signed public keys | `python server.py`, then `python client.py` in several terminals |

## How the pieces fit together

1. **DES** (assignment 1), then **encrypted transfer over a socket** (assignment 2), in `des-socket-transfer/`.
2. **RSA** and the **encrypted chat** (assignment 3), in `secure-chat/`.
3. The DES and RSA code was later cleaned up into the `des/` and `rsa/` packages. `secure-chat/crypto/DES` and `secure-chat/crypto/RSA` are copies of those packages, so `secure-chat` runs without any extra setup.

`des/` and `rsa/` work both as scripts (`python main.py` from inside the folder) and as packages (`from des import encrypt`).

## Getting a single project

Every project is also published as its own branch (`des`, `rsa`, `des-socket-transfer`, `secure-chat`) that contains only that project, and tagged `<project>-v1.0.0`:

```bash
git clone -b secure-chat --single-branch https://github.com/nabielvna/coursework-information-security.git
```

Alternatively, fetch one folder from `main` with sparse checkout:

```bash
git clone --filter=blob:none --sparse https://github.com/nabielvna/coursework-information-security.git
cd coursework-information-security
git sparse-checkout set secure-chat
```

## License

[MIT](LICENSE)
