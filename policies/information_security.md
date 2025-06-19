# Information Security Policy

**Version:** 1.0  
**Last Updated:** 2025-06-18  
**Owner:** Security Team  

## Purpose

The purpose of this Information Security Policy is to define the organization's approach to managing information security risks and to establish responsibilities for protecting data and technology assets. This policy ensures that appropriate controls are in place to safeguard information in accordance with business needs, legal requirements, and security best practices.

This policy supports compliance with SOC 2 and ISO/IEC 27001 standards.

## Scope

This policy applies to:
- All employees, contractors, vendors, and third parties
- All systems, networks, applications, and data owned, leased, or managed by the company
- All environments, including on-premises, cloud, and hybrid infrastructures

## Objectives

- Protect information assets from unauthorized access, disclosure, alteration, or destruction
- Ensure data availability to authorized users when required
- Maintain the integrity and accuracy of business data
- Comply with legal, regulatory, and contractual obligations
- Promote a culture of security awareness and responsibility

## Policy

### 1. **Governance and Risk Management**
- An information security management program shall be maintained, led by the Security Team.
- Periodic risk assessments will be conducted to identify threats and evaluate control effectiveness.
- Security policies will be reviewed at least annually and updated as needed.

### 2. **Asset Management**
- All information assets must be inventoried and classified according to the [Data Classification Policy](./data_classification.md).
- Owners must be assigned to all critical assets to ensure accountability.

### 3. **Access Control**
- Access to information systems must follow the [Access Management Policy](./access_management.md).
- Role-based access control (RBAC) must be implemented with least privilege principles.
- Multi-factor authentication (MFA) is required for administrative and sensitive systems.

### 4. **Cryptographic Controls**
- Encryption must be used to protect data at rest and in transit, following the [Encryption Policy](./encryption_policy.md).
- Cryptographic key management must follow secure practices and be documented.

### 5. **Physical and Environmental Security**
- Physical access to systems that store or process sensitive data must be restricted to authorized personnel.
- Server rooms, data centers, and other sensitive areas must have appropriate environmental controls (e.g., temperature, fire suppression).

### 6. **Operations Security**
- Logging and monitoring must be implemented as described in the [Logging and Monitoring Policy](./logging_monitoring.md).
- Systems must be regularly updated and patched to mitigate known vulnerabilities.
- Change management processes must be documented and followed for all production changes.

### 7. **Communications and Network Security**
- Network boundaries must be protected using firewalls, segmentation, and intrusion detection systems.
- Internal and external communications must be encrypted when transmitting Confidential or Restricted data.

### 8. **Supplier and Vendor Management**
- Third-party providers must be assessed and monitored as described in the [Vendor Management Policy](./vendor_management.md).
- Contracts must include security and privacy obligations.

### 9. **Incident Management**
- All security incidents must be reported and handled according to the [Incident Response Policy](./incident_response.md).
- Incident logs and investigation outcomes must be retained and reviewed.

### 10. **Business Continuity and Backup**
- Critical data must be backed up regularly according to the [Data Backup Policy](./data_backup.md).
- Disaster recovery and business continuity plans must be maintained and tested.

### 11. **Security Awareness and Training**
- All personnel must complete security awareness training upon onboarding and annually thereafter.
- Specialized training will be provided to staff in high-risk roles (e.g., engineering, admin).

---

## Responsibilities

| Role               | Responsibility                                             |
|--------------------|-------------------------------------------------------------|
| Executive Leadership | Support and sponsor security initiatives                  |
| Security Team      | Develop, enforce, and monitor security controls             |
| Engineering/IT     | Implement and maintain secure systems and infrastructure     |
| All Employees      | Comply with security policies and report suspicious activity |

---

## References

- **SOC 2 Trust Services Criteria:** CC1.1–CC1.5, CC6.1–CC7.5
- **ISO/IEC 27001 Controls:** A.5 through A.18 (framework coverage)

---

## Review and Maintenance

This policy must be reviewed at least annually or when significant changes occur to the business, infrastructure, or regulatory landscape. Updates must be approved by the Security Team and communicated to all stakeholders.
