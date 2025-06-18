# Access Management Policy

**Version:** 1.0  
**Last Updated:** 2025-06-18  
**Owner:** Security Team  

## Purpose

The purpose of this policy is to establish a structured and secure approach to managing user access to company systems, applications, and data. This ensures that only authorized individuals can access resources necessary for their job function, minimizing the risk of unauthorized access.

This policy supports compliance with SOC 2 Trust Services Criteria and ISO/IEC 27001 Annex A controls.

## Scope

This policy applies to:
- All employees, contractors, and third-party users.
- All systems, networks, applications, and data owned or managed by the company.

## Policy

### 1. **Access Control Principles**
- Access shall be granted based on the principle of **least privilege** and **need-to-know**.
- Role-based access control (RBAC) is implemented wherever possible.
- All access must be **requested**, **approved**, and **provisioned** via documented workflows.

### 2. **User Access Provisioning**
- New user access must be approved by the hiring manager or resource owner.
- Access is provisioned by the IT or Security team using defined roles and access levels.
- All access requests and approvals must be documented.

### 3. **Authentication**
- All users must authenticate using unique credentials.
- Multi-factor authentication (MFA) is required for:
  - Administrative accounts
  - Remote access
  - Cloud-based services

### 4. **Access Reviews**
- User access must be reviewed at least **quarterly** by managers and system owners.
- Excessive or outdated access must be revoked immediately.
- Access reviews must be documented and retained.

### 5. **Account Termination**
- Upon termination or change of role, user access must be revoked within **24 hours**.
- HR must notify IT/Security immediately upon employee separation.

### 6. **Privileged Access Management**
- Privileged accounts (e.g., root, admin) must be:
  - Strictly controlled
  - Assigned to named individuals (no shared logins)
  - Logged and monitored
- Privileged access must be reviewed **monthly**.

### 7. **Third-Party Access**
- Third parties must sign security agreements before access is granted.
- Access must be time-bound and limited to specific systems and purposes.
- Third-party access is reviewed and reauthorized every **90 days**.

### 8. **Monitoring and Logging**
- All access to sensitive systems must be logged.
- Logs are retained for a minimum of **1 year** and reviewed periodically for anomalies.

## Responsibilities

| Role               | Responsibility                                     |
|--------------------|-----------------------------------------------------|
| IT/Security Team   | Provision, revoke, and audit access                 |
| Managers           | Approve requests and review user access             |
| HR                 | Notify of onboarding/termination events             |
| All Users          | Use access responsibly and report suspicious activity |

## References

- **SOC 2 Trust Services Criteria:** CC6.1, CC6.2, CC6.3, CC7.1
- **ISO/IEC 27001 Controls:** A.5.15, A.5.16, A.5.17, A.5.18

## Review and Maintenance

This policy must be reviewed at least annually or whenever significant changes to access mechanisms occur. The Security Team is responsible for updates and enforcement.

