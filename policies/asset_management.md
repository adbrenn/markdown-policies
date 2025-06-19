# Asset Management Policy

**Version:** 1.0  
**Last Updated:** 2025-06-18  
**Owner:** Security Team  

## Purpose

The purpose of this Asset Management Policy is to ensure that all information assets owned or managed by the company are properly identified, inventoried, classified, protected, and maintained throughout their lifecycle. This policy supports data security, operational continuity, and compliance with SOC 2 and ISO/IEC 27001 standards.

## Scope

This policy applies to:
- All physical and digital assets owned, leased, or managed by the company
- All employees, contractors, and third parties who use or manage company assets
- All environments, including cloud, on-premises, and hybrid infrastructure

## Policy

### 1. **Asset Identification and Inventory**
- All information assets must be uniquely identified and documented in an asset inventory.
- The asset inventory must include details such as:
  - Asset type (e.g., laptop, server, SaaS application)
  - Owner or custodian
  - Physical or logical location
  - Classification (e.g., Confidential, Internal, Public)
  - Assigned user (for endpoints)

- The inventory must be:
  - Reviewed and updated at least **quarterly**
  - Maintained in a secure, centralized system
  - Aligned with the [Data Classification Policy](./data_classification_policy.md)

### 2. **Asset Ownership and Responsibility**
- Each asset must have an assigned **owner** responsible for:
  - Maintaining asset accuracy in inventory
  - Ensuring proper classification and usage
  - Approving access to the asset
- Shared assets (e.g., cloud services) must have a designated service owner.

### 3. **Asset Classification**
- Assets must be classified based on sensitivity and business impact using the categories defined in the [Data Classification Policy](./data_classification_policy.md).
- Classification must be applied upon onboarding the asset and periodically reviewed.

### 4. **Acceptable Use and Handling**
- All users must comply with the [Acceptable Use Policy](./acceptable_use_policy.md) when handling company assets.
- Confidential and Restricted data must not be stored on unapproved or unencrypted devices.
- Mobile and endpoint devices must use full-disk encryption and comply with company security standards.

### 5. **Asset Lifecycle Management**

#### a. **Procurement and Deployment**
- All new hardware and software assets must be approved and provisioned through authorized channels.
- All devices must be configured securely before being deployed to end users.

#### b. **Maintenance**
- Assets must be regularly maintained and patched to address known vulnerabilities.
- Licensing for software assets must be tracked and renewed in accordance with vendor terms.

#### c. **Transfer and Reassignment**
- Assets transferred between users must be updated in the inventory.
- Data on the device must be wiped prior to reassignment if applicable.

#### d. **Decommissioning and Disposal**
- When assets are no longer in use, they must be securely decommissioned.
- Storage media must be wiped, degaussed, or physically destroyed before disposal.
- Decommissioning events must be logged and reviewed by the Security or IT team.

### 6. **Cloud and SaaS Assets**
- All cloud services must be inventoried and reviewed for security and compliance requirements.
- Service owners must ensure data handling and access practices follow internal policies and vendor terms.

---

## Responsibilities

| Role               | Responsibility                                               |
|--------------------|---------------------------------------------------------------|
| Security Team      | Define asset requirements, monitor compliance, audit inventory |
| IT/Engineering     | Maintain infrastructure and endpoint asset records             |
| Procurement        | Ensure approved sourcing and licensing of assets               |
| All Employees      | Use and protect assigned assets responsibly                    |

---

## References

- **SOC 2 Trust Services Criteria:** CC6.1, CC7.1, CC9.2
- **ISO/IEC 27001 Controls:** A.5.9, A.5.10, A.5.11, A.5.12

---

## Review and Maintenance

This policy must be reviewed at least annually or upon significant changes to IT infrastructure or asset management processes. The Security Team is responsible for maintaining and updating this policy.
