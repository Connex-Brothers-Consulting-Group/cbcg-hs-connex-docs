# Rule 04: Security & Cryptographic Kill Switch Governance

## 1. Two-Tier Zero-Knowledge Envelope Encryption
- All customer files, VFS records, and sensitive documents are encrypted via random 256-bit AES-256-GCM Data Encryption Keys (DEKs) with unique 96-bit nonces.
- DEKs are encrypted (wrapped) by Customer-Managed Encryption Keys (CMEKs) residing in Cloud KMS (Google Cloud KMS / AWS KMS).

## 2. Hardware Cryptographic Kill Switch (`KeyAccessRevokedError` -> HTTP 423)
- If a customer disables, revokes, or destroys their CMEK in Cloud KMS, all subsequent read and write requests immediately fail closed with **HTTP 423 Locked** (`KeyAccessRevokedError`).
- Plaintext DEKs reside exclusively in ephemeral Python `ContextVar` per request and are wiped immediately upon request termination.
- Envelope-encrypted files explicitly bypass intermediate caching layers (GCS cache bypass) to guarantee zero-delay revocation enforcement.
- Plaintext unencrypted writes are categorically blocked with **HTTP 412 Precondition Failed** (`NoEncryptionContextError`).

## 3. Statutory Multi-Region Data Sovereignty
- **Republic of Korea (PIPA)**: Permanently isolated in Seoul (`asia-northeast3`).
- **United States & Global (CCPA/GDPR)**: Permanently isolated in Iowa (`us-central1`).
