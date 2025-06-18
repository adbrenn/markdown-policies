# Data Classification Policy

**Version:** 1.0  
**Last Updated:** 2025-06-18  
**Owner:** Security Team  

## Purpose

The purpose of this policy is to ensure that all company data is appropriately classified based on sensitivity, value, and regulatory requirements. Proper data classification supports effective security controls, access management, and risk mitigation.

This policy supports compliance with SOC 2 and ISO/IEC 27001 standards.

## Scope

This policy applies to:
- All employees, contractors, and third-party users
- All data processed, stored, or transmitted using company-owned or managed systems
- All forms of data, including digital, printed, or spoken formats

## Policy

### 1. **Classification Categories**

All company data must be classified into one of the following categories:

#### a. **Restricted**
- **Definition:** Data that, if disclosed, could cause significant harm to the company, customers, or partners.
- **Examples:** Customer PII, payment card data, credentials, security keys, encryption keys, legal documents, incident response records
- **Controls:**
  - Strong access control (need-to-know basis)
  - Encryption at rest and in transit
  - Logging and monitoring of access
  - Prohibited from storage on personal or unmanaged devices

#### b. **Confidential**
- **Definition:** Internal-use-only data that could cause moderate harm if disclosed.
- **Examples:** Internal emails, business strategies, HR files, internal system documentation
- **Controls:**
  - Access based on role
  - Encryption in transit (and at rest when stored in cloud systems)
  - Not shared externally without approval

#### c. **Internal**
- **Definition:** General company information not intended for public release.
- **Examples:** Meeting notes, project updates, internal reports, most Slack discussions
- **Controls:**
  - Available to employees
  - No external sharing unless explicitly approved

#### d. **Public**
- **Definition:** Data approved for external publication or widely available information.
- **Examples:** Marketing materials, blog posts, job descriptions, open-source code
- **Controls:**
  - No restrictions, but still subject to accuracy and brand guidelines
  - Approved through communications or marketing

---

### 2. **Labeling Requirements**

- All documents and systems must clearly indicate the classification level using headers, footers, or metadata when applicable.
- Email subject lines or footers may include labels such as `[RESTRICTED]` or `[CONFIDENTIAL]`.

---

### 3. **Handling Guidelines**

| Classification | Storage Requirements | Transmission Requirements | Access Control |
|----------------|-----------------------|----------------------------|----------------|
| Restricted     | Encrypted storage, limited locations | Encrypted (TLS 1.2+) | Need-to-know, logged |
| Confidential   | Approved internal systems | Encrypted (TLS 1.2+) | Role-based |
| Internal       | Standard internal platforms | Internal networks or TLS | All employees |
| Public         | Approved repositories | Any | No restriction |

---

### 4. **Responsibility and Enforcement**

- Data owners are responsible for correctly classifying and labeling their data.
- All employees must handle data according to its classification.
- Violations of this policy may result in disciplinary action and/or termination of access.

---

## Responsibilities

| Role             | Responsibility                                         |
|------------------|---------------------------------------------------------|
| Data Owners      | Classify and label data they generate or manage        |
| Security Team    | Provide guidance and monitor for proper classification |
| IT/Engineering   | Implement technical enforcement of classification rules|
| All Employees    | Understand and follow classification guidelines        |

---

## References

- **SOC 2 Trust Services Criteria:** CC6.1, CC6.3, CC6.7
- **ISO/IEC 27001 Controls:** A.5.12, A.5.13, A.5.14

---

## Review and Maintenance

This policy must be reviewed annually and upon significant changes to information handling practices, business needs, or legal/regulatory requirements. The Security Team is responsible for policy maintenance.
