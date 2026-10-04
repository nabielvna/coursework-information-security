# Basic Secure End-to-End Encrypted Chat System

This project implements a secure chat system with end-to-end encryption, mutual authentication, and server-signed key exchanges. It provides a robust platform for private and authenticated communication between users.

## Overview

This secure chat system uses a hybrid encryption approach combining RSA and DES algorithms:

- [RSA](https://github.com/nabielvna/coursework-information-security/tree/main/rsa) - Asymmetric cryptography algorithm used for key exchange and digital signatures
- [DES](https://github.com/nabielvna/coursework-information-security/tree/main/des) - Symmetric-key algorithm used for encrypting message content

The system consists of several Python modules working together:

- `client.py`: Client-side implementation with E2E encryption and user interface
- `server.py`: Server implementation handling connections and message routing
- `e2e.py`: End-to-end encryption implementation using hybrid RSA/DES
- `nonce_manager.py`: Handles mutual authentication challenges
- `server_signature_manager.py`: Manages server signing of client keys

## Features

- End-to-end encryption using hybrid RSA/DES
- Mutual authentication between clients and server
- Server-signed public key distribution
- Real-time user status updates
- Message integrity verification
- Protection against man-in-the-middle attacks
- Secure message routing
- Simple command-line interface
- Session management
- Automatic key exchange

## Requirements

- Python 3
- Socket library (built-in)
- Threading library (built-in)
- JSON library (built-in)
- Base64 library (built-in)

## Installation

1. Clone the repository and enter the project folder
```bash
git clone https://github.com/nabielvna/coursework-information-security.git
cd coursework-information-security/secure-chat
```

2. Ensure all files are in the correct directory structure:
```
secure-chat/
├── client.py
├── server.py
├── core/
│   ├── e2e.py
│   ├── nonce_manager.py
│   └── server_signature_manager.py
├── crypto/
│   ├── DES/   (copy of the des package)
│   └── RSA/   (copy of the rsa package)
└── utils/
    └── log.py
```

3. Start the server:
```bash
python server.py
```

4. In separate terminal windows, start clients:
```bash
python client.py
```

## Usage

### Starting the Server

1. Run the server script:
```bash
python server.py
```
2. The server will start listening on localhost:5000 by default

### Using the Client

1. Start the client:
```bash
python client.py
```

2. Enter your username when prompted

3. Send messages using the format:
```
recipient:message
```

4. Type 'quit' to exit

### Commands
- `quit`: Exit the chat client
- `recipient:message`: Send a message to specific user

## Technical Details

### Security Architecture

1. End-to-End Encryption
   - RSA 2048-bit key pairs for key exchange
   - DES for message content encryption
   - Hybrid encryption scheme for efficiency
   - Unique session keys per message

2. Authentication System
   - Nonce-based challenge-response
   - Mutual authentication between client and server
   - Server-signed client public keys
   - Session timeout management

3. Message Security
   - Length-prefix framing for secure transmission
   - Message signing for integrity
   - E2E encryption for privacy
   - Server acts only as message router

### Implementation Details

#### Client Architecture
- Handles user registration and authentication
- Manages E2E encryption/decryption
- Maintains list of active users
- Verifies server signatures
- Handles key exchange

#### Server Architecture
- Manages client connections
- Routes encrypted messages
- Signs client public keys
- Broadcasts user status updates
- Handles session management

#### Communication Protocol
1. Client Connection:
   - Nonce challenge from server
   - Client response with encrypted nonce
   - Server verification
   - Client registration
   - Key package distribution

2. Message Flow:
   - Sender encrypts with recipient's public key
   - Server routes encrypted message
   - Recipient decrypts with private key
   - Message integrity verification

## Security Considerations

1. Trust Model
   - Server is trusted for routing only
   - Server cannot read message content
   - Clients verify all signatures

2. Key Management
   - Fresh keys generated per session
   - Server signs client public keys
   - Automatic key exchange

3. Known Limitations
   - No perfect forward secrecy
   - No message persistence
   - Basic key management

## Error Handling

The implementation includes comprehensive error handling for:
- Connection failures
- Authentication errors
- Encryption/decryption failures
- Invalid messages
- User verification errors
- Session timeouts

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

## Acknowledgments

- Uses standard cryptographic primitives (RSA, DES)
- Implements secure messaging practices
- Inspired by modern E2E messaging systems
