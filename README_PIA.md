# Privacy Impact Assessment (PIA) Agent

This agent automatically performs a Privacy Impact Assessment on your markdown policy files and can submit the results as a Jira ticket to demonstrate completion.

## Features

- 🔍 **Automated Analysis**: Scans all policy markdown files for privacy-related content
- 📊 **Comprehensive Assessment**: Identifies PII handling, GDPR/CCPA compliance, data handling practices, and risks
- 📝 **Detailed Reporting**: Generates human-readable reports and JSON results
- 🎫 **Jira Integration**: Automatically creates Jira tickets with assessment results
- ⚡ **Easy to Use**: Simple command-line interface with flexible configuration

## Installation

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Configure Jira access (optional but recommended):

   **Option A: Using config.json**
   
   Copy the example configuration file:
   ```bash
   cp config.json.example config.json
   ```
   
   Edit `config.json` with your Jira credentials:
   ```json
   {
     "jira": {
       "url": "https://your-company.atlassian.net",
       "email": "your-email@example.com",
       "api_token": "your-jira-api-token",
       "project_key": "PROJ",
       "issue_type": "Task",
       "labels": ["privacy", "pia", "compliance"]
     }
   }
   ```

   **Option B: Using Environment Variables**
   
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` with your Jira credentials, then load them:
   ```bash
   export $(cat .env | xargs)
   ```

## Getting a Jira API Token

1. Go to https://id.atlassian.com/manage-profile/security/api-tokens
2. Click "Create API token"
3. Give it a label (e.g., "PIA Agent")
4. Copy the token and use it in your configuration

## Usage

### Basic Usage (Analysis Only)

Run the assessment without submitting to Jira:

```bash
python pia_agent.py
```

### Generate Report Files

Save the assessment results and report:

```bash
python pia_agent.py --output assessment_results.json --report pia_report.txt
```

### Submit to Jira

Submit the assessment results as a Jira ticket:

```bash
python pia_agent.py --jira
```

### Full Example

```bash
python pia_agent.py \
  --policies-dir policies \
  --config config.json \
  --output assessment_results.json \
  --report pia_report.txt \
  --jira
```

## Command Line Options

- `--policies-dir`: Directory containing policy markdown files (default: `policies`)
- `--config`: Path to configuration file (default: `config.json`)
- `--output`: Save assessment results as JSON to this file
- `--report`: Save human-readable report to this file
- `--jira`: Submit results to Jira (if configured)
- `--no-jira`: Skip Jira submission even if configured

## What the Agent Analyzes

The PIA agent looks for:

- **PII Handling**: References to personally identifiable information, personal data
- **GDPR Compliance**: GDPR-related language and requirements
- **CCPA Compliance**: California Consumer Privacy Act references
- **Data Collection**: How data is collected
- **Data Processing**: How data is processed and used
- **Data Storage**: Storage and retention practices
- **Data Sharing**: Third-party sharing and vendor relationships
- **Consent Management**: Consent mechanisms
- **Access Rights**: Data subject rights and access controls
- **Encryption**: Cryptographic controls
- **Breach Management**: Incident response and breach notification
- **Data Deletion**: Right to erasure and data deletion practices

## Assessment Output

The agent generates:

1. **Findings**: Key privacy-related findings from policy analysis
2. **Risks**: Identified privacy risks with severity levels
3. **Recommendations**: Actionable recommendations for improvement
4. **Compliance Status**: Status of GDPR, CCPA, and PII handling coverage

## Jira Ticket Format

When submitted to Jira, the ticket includes:

- Executive summary with risk breakdown
- Key findings with severity levels
- Identified risks and mitigations
- Recommendations with priority levels
- Compliance status for major regulations

The ticket summary follows the format: `Privacy Impact Assessment - YYYY-MM-DD`

## Example Workflow

1. **Run the assessment**:
   ```bash
   python pia_agent.py --output results.json --report report.txt
   ```

2. **Review the results**:
   - Check `report.txt` for human-readable findings
   - Review `results.json` for detailed data

3. **Submit to Jira** (if configured):
   ```bash
   python pia_agent.py --jira
   ```

4. **Track completion**: The Jira ticket serves as proof of PIA completion

## Customization

You can customize the agent by modifying:

- `PRIVACY_KEYWORDS`: Add or modify keywords to search for
- `RISK_INDICATORS`: Adjust risk level detection criteria
- Assessment logic in `_generate_assessment()` method
- Jira ticket format in `_create_jira_description()` method

## Troubleshooting

**Jira connection fails:**
- Verify your Jira URL, email, and API token
- Check that your API token has permission to create issues in the project
- Ensure the project key is correct

**No policies found:**
- Verify the `--policies-dir` path is correct
- Check that policy files have `.md` extension

**Missing dependencies:**
- Run `pip install -r requirements.txt`

## Notes

- The agent analyzes markdown files only (`.md` extension)
- Assessment is based on keyword matching and pattern detection
- Results should be reviewed by privacy/compliance professionals
- This tool is designed to assist, not replace, human review


