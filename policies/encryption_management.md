# Encryption Management Policy

**Version:** 1.0  
**Last Updated:** 2025-06-18  
**Owner:** Security Team  

## Purpose

This policy establishes requirements for the encryption of sensitive data to protect its confidentiality and integrity during storage (at rest) and transmission (in transit). The goal is to reduce the risk of data exposure due to unauthorized access or interception, and to support compliance with SOC 2 and ISO/IEC 27001 standards.

## Scope

This policy applies to:
- All data classified as **Confidential** or **Restricted**
- All systems, applications, endpoints, and services that store or transmit such data
- All employees, contractors, and third-party service providers

## Policy

### 1. **General Requirements**
- Encryption must be applied to protect sensitive data at rest and in transit.
- Only industry-standard cryptographic algorithms and libraries may be used.
- Cryptographic keys must be managed securely and rotated according to key management policy.

---

### 2. **Encryption at Rest**
All Confidential or Restricted data must be encrypted when stored on:

- **Databases**
  - Encryption using AES-256 or equivalent is required.
  - Full-disk encryption or database-level encryption must be enabled.

- **File Systems / Storage Volumes**
  - Devices (e.g., servers, laptops, mobile devices) must use full-disk encryption.
  - Cloud storage (e.g., AWS S3, GCP Storage) must have encryption enabled with customer-managed or service-managed keys.

- **Backups**
  - Backup media must be encrypted using the same encryption standards as production data.
  - Encrypted backups must be stored securely with access logging.

- **Endpoints**
  - Company-issued laptops and mobile devices must use full-disk encryption.
  - Removable media (e.g., USB drives) must be encrypted or not permitted unless explicitly approved.

---

### 3. **Encryption in Transit**
Sensitive data transmitted over any network (internal or external) must be encrypted using secure protocols.

- **Protocols**
  - TLS 1.2 or higher is required for all internet-facing services.
  - Deprecated protocols (e.g., SSL, TLS 1.0/1.1, FTP) are prohibited.

- **Email**
  - Emails containing sensitive data must be sent using secure email gateways (e.g., TLS-enforced delivery).
  - Sensitive content should be encrypted using tools such as S/MIME or PGP where feasible.

- **APIs**
  - All API traffic must use HTTPS with TLS 1.2+ and strong cipher suites.
  - Authentication tokens and credentials must never be transmitted in plaintext.

- **Internal Communications**
  - Data exchanged between internal services or microservices must use mutual TLS or equivalent encryption.

---

### 4. **Key Management**
- Keys must be generated, stored, and rotated securely in compliance with the Key Management Policy.
- Keys must not be hardcoded in application source code.
- Hardware Security Modules (HSMs) or cloud-based key management systems (KMS) should be used where applicable.
- Access to cryptographic keys must be restricted and logged.

---

### 5. **Exceptions**
- Any exceptions to this policy must be documented and approved by the Security Team.
- A risk assessment must be performed for any exception and mitigation measures implemented.

---

## Responsibilities

| Role               | Responsibility                                                |
|--------------------|---------------------------------------------------------------|
| Security Team      | Define encryption standards and monitor implementation        |
| Engineering Teams  | Implement encryption in systems and applications              |
| IT Operations      | Enforce full-disk and backup encryption                       |
| All Employees      | Handle data in accordance with encryption and classification policies |

---

## References

- **SOC 2 Trust Services Criteria:** CC6.1, CC6.7, CC7.1
- **ISO/IEC 27001 Controls:** A.8.24, A.8.25, A.8.26
- **NIST SP 800-57:** Key Management Guidelines  
- **NIST SP 800-52:** Guidelines for the Selection and Use of TLS

---

## Review and Maintenance

This policy shall be reviewed at least annually, or upon significant changes to cryptographic technologies or regulatory requirements. The Security Team is responsible for updates and distribution.
