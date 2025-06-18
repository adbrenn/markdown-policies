# Password Management Policy

**Version:** 1.0  
**Last Updated:** 2025-06-18  
**Owner:** Security Team  

## Purpose

This policy defines requirements for the creation, management, and protection of passwords used to access company systems, applications, and data. The goal is to mitigate the risk of unauthorized access due to weak or compromised credentials.

This policy supports compliance with SOC 2 and ISO/IEC 27001 security control requirements.

## Scope

This policy applies to:
- All employees, contractors, and third-party users
- All systems, services, and applications that authenticate users via password

## Policy

### 1. **Password Creation**
- Minimum password length: **12 characters**
- Passwords must include a mix of:
  - Uppercase and lowercase letters
  - Numbers
  - Special characters (e.g., `!@#$%^&*`)
- Passwords must not contain easily guessed information such as:
  - Usernames
  - Dictionary words
  - Birthdays or company names

### 2. **Password Management**
- Passwords must be changed immediately if suspected to be compromised.
- Passwords must not be reused across company accounts or platforms.
- Users must not share passwords or write them down in an insecure manner.
- All administrative accounts must have unique, complex passwords.
- Passwords must be stored using secure, salted, and hashed algorithms (e.g., bcrypt, Argon2).

### 3. **Multi-Factor Authentication (MFA)**
- MFA is required for:
  - Remote access to internal systems
  - Cloud-based platforms
  - Administrative and privileged accounts
- MFA must be enforced via software/hardware tokens or biometric authentication.

### 4. **Password Expiration and Reuse**
- Password expiration is not enforced by default, in alignment with NIST SP 800-63B guidelines.
- Users must change passwords:
  - Immediately upon suspected compromise
  - Upon system prompts during incident containment
- A history of the last **5 passwords** must be retained to prevent reuse.

### 5. **Failed Login Attempts**
- Accounts must be locked after **5 consecutive failed login attempts**.
- Lockouts must be enforced for at least **15 minutes** or until reset by an administrator.

### 6. **Password Tools**
- Use of enterprise-approved **password managers** is strongly encouraged.
- Password managers must support encryption and MFA.

### 7. **Service and System Accounts**
- Default system passwords must be changed upon setup.
- Passwords for service accounts must:
  - Be randomly generated
  - Be stored securely (e.g., secrets management tools)
  - Rotate automatically where possible

## Responsibilities

| Role               | Responsibility                                 |
|--------------------|------------------------------------------------|
| All Users          | Create strong passwords and report compromise |
| IT/Security Team   | Enforce technical controls and monitor risks  |
| HR                 | Communicate policy requirements at onboarding |

## References

- **SOC 2 Trust Services Criteria:** CC6.1, CC6.2, CC7.1
- **ISO/IEC 27001 Controls:** A.5.17, A.5.15
- **NIST SP 800-63B**: Digital Identity Guidelines

## Review and Maintenance

This policy must be reviewed annually or following significant changes to authentication mechanisms. The Security Team is responsible for updates and enforcement.
