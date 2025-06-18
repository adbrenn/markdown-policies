# Vendor Management Policy

**Version:** 1.0  
**Last Updated:** 2025-06-18  
**Owner:** Security Team  

## Purpose

This policy establishes the requirements for evaluating, onboarding, monitoring, and offboarding third-party vendors to ensure they meet the organization’s security, privacy, and compliance expectations.

Effective vendor management helps reduce risk from external service providers, especially those that handle sensitive company or customer data.

## Scope

This policy applies to:
- All third-party vendors, suppliers, partners, and contractors who access, process, or store company information.
- All departments responsible for engaging or managing vendor relationships.

## Policy

### 1. **Vendor Classification**
- Vendors must be classified based on the **criticality and sensitivity** of the services or data involved:
  - **Tier 1:** Vendors with access to sensitive or production data
  - **Tier 2:** Vendors supporting critical infrastructure or systems
  - **Tier 3:** Vendors with no access to sensitive data or systems

### 2. **Vendor Risk Assessment**
- A **security risk assessment** must be completed before engaging any Tier 1 or Tier 2 vendor.
- The assessment includes:
  - Security posture evaluation (SOC 2, ISO 27001, questionnaires)
  - Data handling practices
  - Subprocessor relationships (if applicable)
- Results must be reviewed and approved by the Security Team.

### 3. **Due Diligence and Contractual Requirements**
- All Tier 1 vendors must sign a **Data Processing Agreement (DPA)** or equivalent.
- Contracts must include:
  - Confidentiality and data protection clauses
  - Breach notification timelines (e.g., within 72 hours)
  - Audit rights for compliance verification

### 4. **Onboarding**
- Vendors must be onboarded using a standardized process that includes:
  - Completion of a security questionnaire (e.g., CAIQ, VSA)
  - Assignment of a vendor owner from the business unit
  - Documentation of systems/data the vendor will access

### 5. **Ongoing Monitoring**
- Security and performance of critical vendors must be reviewed at least **annually**.
- Reviews include:
  - Changes in control environment (e.g., updated SOC 2 reports)
  - Data breach or incident history
  - Re-evaluation of vendor classification
- Vendors not meeting requirements must be remediated or offboarded.

### 6. **Access Management**
- Vendors must only be given the minimum necessary access.
- Vendor accounts must be:
  - Approved, documented, and time-bound
  - Reviewed quarterly by the vendor owner
  - Immediately deactivated when no longer needed

### 7. **Incident Management**
- Vendors must notify the company immediately in the event of a suspected or actual data breach.
- Incident response expectations must be documented in the contract.

### 8. **Offboarding**
- Upon termination, vendor access must be removed within **24 hours**.
- All company data must be returned or securely deleted as documented.
- Offboarding activities must be verified and recorded.

## Responsibilities

| Role                | Responsibility                                 |
|---------------------|------------------------------------------------|
| Business Units      | Identify and justify vendor usage              |
| Security Team       | Perform risk assessments, reviews, and audits |
| Legal/Procurement   | Ensure appropriate contracts and DPAs          |
| IT/Operations       | Provision and revoke vendor access             |

## References

- **SOC 2 Trust Services Criteria:** CC1.1, CC3.3, CC9.2
- **ISO/IEC 27001 Controls:** A.5.19, A.5.20, A.5.21

## Review and Maintenance

This policy must be reviewed at least annually or upon major vendor-related changes. Updates are the responsibility of the Security Team.
