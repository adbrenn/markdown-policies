#!/usr/bin/env python3
"""
Privacy Impact Assessment (PIA) Agent

This agent analyzes markdown policy files to perform a Privacy Impact Assessment
and submits the results as a Jira ticket to demonstrate completion.
"""

import os
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import glob

try:
    from jira import JIRA
    from jira.exceptions import JIRAError
except ImportError:
    JIRA = None
    JIRAError = None


class PIAAgent:
    """Agent that performs Privacy Impact Assessments on policy documents."""
    
    # Privacy-related keywords to search for
    PRIVACY_KEYWORDS = {
        'pii': ['PII', 'personally identifiable information', 'personal data', 'personal information'],
        'gdpr': ['GDPR', 'General Data Protection Regulation', 'data subject', 'right to erasure'],
        'ccpa': ['CCPA', 'California Consumer Privacy Act', 'consumer privacy'],
        'data_collection': ['data collection', 'collecting data', 'gather information', 'data capture'],
        'data_processing': ['data processing', 'process data', 'data handling', 'data usage'],
        'data_storage': ['data storage', 'store data', 'data retention', 'data retention period'],
        'data_sharing': ['data sharing', 'share data', 'third party', 'vendor', 'subprocessor'],
        'consent': ['consent', 'opt-in', 'opt-out', 'permission', 'authorization'],
        'access_rights': ['access rights', 'right to access', 'data subject rights', 'user rights'],
        'encryption': ['encryption', 'encrypt', 'encrypted', 'cryptographic'],
        'breach': ['breach', 'data breach', 'security incident', 'unauthorized access'],
        'deletion': ['deletion', 'delete data', 'data deletion', 'right to erasure', 'right to be forgotten'],
    }
    
    # Risk indicators
    RISK_INDICATORS = {
        'high': ['restricted', 'sensitive', 'PII', 'payment card', 'credentials', 'encryption keys'],
        'medium': ['confidential', 'internal', 'access control', 'authentication'],
        'low': ['public', 'marketing', 'general information']
    }
    
    def __init__(self, policies_dir: str = "policies", jira_config: Optional[Dict] = None):
        """
        Initialize the PIA Agent.
        
        Args:
            policies_dir: Directory containing policy markdown files
            jira_config: Dictionary with Jira configuration (url, email, api_token, project_key)
        """
        self.policies_dir = Path(policies_dir)
        self.jira_config = jira_config or {}
        self.assessment_results = {
            'timestamp': datetime.now().isoformat(),
            'policies_analyzed': [],
            'findings': [],
            'risks': [],
            'recommendations': [],
            'compliance_status': {}
        }
    
    def analyze_policies(self) -> Dict[str, Any]:
        """
        Analyze all policy files and perform the Privacy Impact Assessment.
        
        Returns:
            Dictionary containing the assessment results
        """
        print("🔍 Starting Privacy Impact Assessment...")
        print(f"📁 Analyzing policies in: {self.policies_dir}")
        
        # Find all markdown policy files
        policy_files = list(self.policies_dir.glob("*.md"))
        
        if not policy_files:
            print(f"⚠️  No markdown files found in {self.policies_dir}")
            return self.assessment_results
        
        print(f"📄 Found {len(policy_files)} policy files")
        
        # Analyze each policy file
        for policy_file in policy_files:
            print(f"  Analyzing: {policy_file.name}")
            self._analyze_policy_file(policy_file)
        
        # Generate overall assessment
        self._generate_assessment()
        
        print("✅ Privacy Impact Assessment completed!")
        return self.assessment_results
    
    def _analyze_policy_file(self, policy_file: Path):
        """Analyze a single policy file for privacy-related content."""
        try:
            with open(policy_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            policy_name = policy_file.stem
            policy_data = {
                'filename': policy_file.name,
                'name': policy_name.replace('_', ' ').title(),
                'word_count': len(content.split()),
                'privacy_keywords_found': {},
                'risk_level': 'low',
                'has_pii_mentions': False,
                'has_gdpr_mentions': False,
                'has_ccpa_mentions': False,
                'data_handling_practices': []
            }
            
            # Search for privacy keywords
            content_lower = content.lower()
            for category, keywords in self.PRIVACY_KEYWORDS.items():
                matches = []
                for keyword in keywords:
                    pattern = re.compile(r'\b' + re.escape(keyword.lower()) + r'\b', re.IGNORECASE)
                    if pattern.search(content):
                        matches.append(keyword)
                
                if matches:
                    policy_data['privacy_keywords_found'][category] = matches
            
            # Check for specific compliance mentions
            policy_data['has_pii_mentions'] = any(
                keyword in content_lower for keyword in ['pii', 'personally identifiable', 'personal data']
            )
            policy_data['has_gdpr_mentions'] = 'gdpr' in content_lower
            policy_data['has_ccpa_mentions'] = 'ccpa' in content_lower or 'california consumer privacy' in content_lower
            
            # Determine risk level
            if any(indicator in content_lower for indicator in self.RISK_INDICATORS['high']):
                policy_data['risk_level'] = 'high'
            elif any(indicator in content_lower for indicator in self.RISK_INDICATORS['medium']):
                policy_data['risk_level'] = 'medium'
            
            # Extract data handling practices
            data_handling_patterns = [
                (r'data.*retention.*(\d+.*(?:day|month|year))', 'retention_period'),
                (r'encrypt.*data', 'encryption'),
                (r'access.*control', 'access_control'),
                (r'third.*party|vendor|subprocessor', 'third_party_sharing'),
                (r'breach.*notification|incident.*response', 'incident_response'),
            ]
            
            for pattern, practice in data_handling_patterns:
                if re.search(pattern, content_lower):
                    policy_data['data_handling_practices'].append(practice)
            
            self.assessment_results['policies_analyzed'].append(policy_data)
            
        except Exception as e:
            print(f"  ⚠️  Error analyzing {policy_file.name}: {str(e)}")
    
    def _generate_assessment(self):
        """Generate overall assessment findings, risks, and recommendations."""
        policies = self.assessment_results['policies_analyzed']
        
        # Count privacy-related findings
        total_policies = len(policies)
        policies_with_pii = sum(1 for p in policies if p['has_pii_mentions'])
        policies_with_gdpr = sum(1 for p in policies if p['has_gdpr_mentions'])
        policies_with_ccpa = sum(1 for p in policies if p['has_ccpa_mentions'])
        high_risk_policies = sum(1 for p in policies if p['risk_level'] == 'high')
        
        # Generate findings
        findings = []
        
        if policies_with_pii > 0:
            findings.append({
                'type': 'PII Handling',
                'severity': 'high',
                'description': f'{policies_with_pii} policy file(s) mention PII or personal data handling',
                'policies': [p['name'] for p in policies if p['has_pii_mentions']]
            })
        
        if policies_with_gdpr > 0:
            findings.append({
                'type': 'GDPR Compliance',
                'severity': 'medium',
                'description': f'{policies_with_gdpr} policy file(s) reference GDPR requirements',
                'policies': [p['name'] for p in policies if p['has_gdpr_mentions']]
            })
        
        if policies_with_ccpa > 0:
            findings.append({
                'type': 'CCPA Compliance',
                'severity': 'medium',
                'description': f'{policies_with_ccpa} policy file(s) reference CCPA requirements',
                'policies': [p['name'] for p in policies if p['has_ccpa_mentions']]
            })
        
        # Identify risks
        risks = []
        
        if high_risk_policies > 0:
            risks.append({
                'level': 'high',
                'description': f'{high_risk_policies} policy file(s) handle high-risk data categories',
                'mitigation': 'Ensure strong encryption, access controls, and monitoring are in place'
            })
        
        # Check for missing privacy controls
        encryption_policies = sum(1 for p in policies if 'encryption' in p['data_handling_practices'])
        access_control_policies = sum(1 for p in policies if 'access_control' in p['data_handling_practices'])
        
        if policies_with_pii > 0 and encryption_policies < policies_with_pii:
            risks.append({
                'level': 'medium',
                'description': 'Not all PII-handling policies explicitly mention encryption requirements',
                'mitigation': 'Review and update policies to ensure encryption is mandated for all PII'
            })
        
        # Generate recommendations
        recommendations = []
        
        if not policies_with_gdpr and not policies_with_ccpa:
            recommendations.append({
                'priority': 'high',
                'description': 'Consider adding explicit GDPR/CCPA compliance language to relevant policies',
                'action': 'Review data classification and access management policies for privacy regulation alignment'
            })
        
        if policies_with_pii > 0:
            recommendations.append({
                'priority': 'high',
                'description': 'Ensure data retention periods are clearly defined for PII',
                'action': 'Review and document specific retention periods for each category of personal data'
            })
        
        recommendations.append({
            'priority': 'medium',
            'description': 'Conduct regular privacy impact assessments as part of policy review cycle',
            'action': 'Schedule annual PIA reviews alongside policy updates'
        })
        
        # Compliance status
        compliance_status = {
            'gdpr': {
                'status': 'partial' if policies_with_gdpr > 0 else 'not_explicit',
                'policies_covering': policies_with_gdpr,
                'total_policies': total_policies
            },
            'ccpa': {
                'status': 'partial' if policies_with_ccpa > 0 else 'not_explicit',
                'policies_covering': policies_with_ccpa,
                'total_policies': total_policies
            },
            'pii_handling': {
                'status': 'covered' if policies_with_pii > 0 else 'not_covered',
                'policies_covering': policies_with_pii,
                'total_policies': total_policies
            }
        }
        
        self.assessment_results['findings'] = findings
        self.assessment_results['risks'] = risks
        self.assessment_results['recommendations'] = recommendations
        self.assessment_results['compliance_status'] = compliance_status
    
    def generate_report(self) -> str:
        """
        Generate a human-readable PIA report.
        
        Returns:
            Formatted report string
        """
        report = []
        report.append("=" * 80)
        report.append("PRIVACY IMPACT ASSESSMENT REPORT")
        report.append("=" * 80)
        report.append(f"Assessment Date: {self.assessment_results['timestamp']}")
        report.append(f"Policies Analyzed: {len(self.assessment_results['policies_analyzed'])}")
        report.append("")
        
        # Executive Summary
        report.append("EXECUTIVE SUMMARY")
        report.append("-" * 80)
        policies = self.assessment_results['policies_analyzed']
        high_risk = sum(1 for p in policies if p['risk_level'] == 'high')
        medium_risk = sum(1 for p in policies if p['risk_level'] == 'medium')
        low_risk = sum(1 for p in policies if p['risk_level'] == 'low')
        
        report.append(f"High Risk Policies: {high_risk}")
        report.append(f"Medium Risk Policies: {medium_risk}")
        report.append(f"Low Risk Policies: {low_risk}")
        report.append("")
        
        # Findings
        report.append("KEY FINDINGS")
        report.append("-" * 80)
        for finding in self.assessment_results['findings']:
            report.append(f"[{finding['severity'].upper()}] {finding['type']}: {finding['description']}")
            if finding.get('policies'):
                report.append(f"  Affected Policies: {', '.join(finding['policies'])}")
        report.append("")
        
        # Risks
        report.append("IDENTIFIED RISKS")
        report.append("-" * 80)
        for risk in self.assessment_results['risks']:
            report.append(f"[{risk['level'].upper()}] {risk['description']}")
            report.append(f"  Mitigation: {risk['mitigation']}")
        report.append("")
        
        # Recommendations
        report.append("RECOMMENDATIONS")
        report.append("-" * 80)
        for rec in self.assessment_results['recommendations']:
            report.append(f"[{rec['priority'].upper()}] {rec['description']}")
            report.append(f"  Action: {rec['action']}")
        report.append("")
        
        # Compliance Status
        report.append("COMPLIANCE STATUS")
        report.append("-" * 80)
        for regulation, status in self.assessment_results['compliance_status'].items():
            report.append(f"{regulation.upper()}: {status['status']}")
            report.append(f"  Policies covering: {status['policies_covering']}/{status['total_policies']}")
        report.append("")
        
        report.append("=" * 80)
        
        return "\n".join(report)
    
    def submit_to_jira(self) -> Optional[str]:
        """
        Submit the PIA assessment results as a Jira ticket.
        
        Returns:
            Jira ticket key (e.g., "PROJ-123") if successful, None otherwise
        """
        if not JIRA:
            print("⚠️  Jira library not installed. Install with: pip install jira")
            return None
        
        if not self.jira_config:
            print("⚠️  Jira configuration not provided")
            return None
        
        required_keys = ['url', 'email', 'api_token', 'project_key']
        if not all(key in self.jira_config for key in required_keys):
            print(f"⚠️  Missing required Jira configuration keys: {required_keys}")
            return None
        
        try:
            print("🔗 Connecting to Jira...")
            jira = JIRA(
                server=self.jira_config['url'],
                basic_auth=(self.jira_config['email'], self.jira_config['api_token'])
            )
            
            # Generate report
            report = self.generate_report()
            
            # Create issue description
            description = self._create_jira_description()
            
            # Create the issue
            issue_dict = {
                'project': {'key': self.jira_config['project_key']},
                'summary': f'Privacy Impact Assessment - {datetime.now().strftime("%Y-%m-%d")}',
                'description': description,
                'issuetype': {'name': self.jira_config.get('issue_type', 'Task')},
            }
            
            # Add labels if specified
            if 'labels' in self.jira_config:
                issue_dict['labels'] = self.jira_config['labels']
            
            print(f"📝 Creating Jira ticket in project {self.jira_config['project_key']}...")
            new_issue = jira.create_issue(fields=issue_dict)
            
            print(f"✅ Jira ticket created successfully: {new_issue.key}")
            print(f"🔗 View ticket: {self.jira_config['url']}/browse/{new_issue.key}")
            
            # Optionally attach the full report as a comment
            if self.jira_config.get('attach_report_as_comment', False):
                new_issue.add_comment(f"Full PIA Report:\n\n{report}")
            
            return new_issue.key
            
        except JIRAError as e:
            print(f"❌ Error creating Jira ticket: {str(e)}")
            return None
        except Exception as e:
            print(f"❌ Unexpected error: {str(e)}")
            return None
    
    def _create_jira_description(self) -> str:
        """Create a formatted description for the Jira ticket."""
        desc = []
        desc.append("h2. Privacy Impact Assessment Results")
        desc.append("")
        desc.append(f"*Assessment Date:* {self.assessment_results['timestamp']}")
        desc.append(f"*Policies Analyzed:* {len(self.assessment_results['policies_analyzed'])}")
        desc.append("")
        
        # Summary
        policies = self.assessment_results['policies_analyzed']
        high_risk = sum(1 for p in policies if p['risk_level'] == 'high')
        desc.append("h3. Executive Summary")
        desc.append(f"* High Risk Policies: {high_risk}")
        desc.append(f"* Medium Risk Policies: {sum(1 for p in policies if p['risk_level'] == 'medium')}")
        desc.append(f"* Low Risk Policies: {sum(1 for p in policies if p['risk_level'] == 'low')}")
        desc.append("")
        
        # Findings
        desc.append("h3. Key Findings")
        for finding in self.assessment_results['findings']:
            desc.append(f"*[{finding['severity'].upper()}]* {finding['type']}: {finding['description']}")
        desc.append("")
        
        # Risks
        desc.append("h3. Identified Risks")
        for risk in self.assessment_results['risks']:
            desc.append(f"*[{risk['level'].upper()}]* {risk['description']}")
            desc.append(f"* Mitigation: {risk['mitigation']}")
        desc.append("")
        
        # Recommendations
        desc.append("h3. Recommendations")
        for rec in self.assessment_results['recommendations']:
            desc.append(f"*[{rec['priority'].upper()}]* {rec['description']}")
            desc.append(f"* Action: {rec['action']}")
        desc.append("")
        
        # Compliance
        desc.append("h3. Compliance Status")
        for regulation, status in self.assessment_results['compliance_status'].items():
            desc.append(f"*{regulation.upper()}:* {status['status']} ({status['policies_covering']}/{status['total_policies']} policies)")
        desc.append("")
        
        desc.append("----")
        desc.append("_This assessment was automatically generated by the PIA Agent._")
        
        return "\n".join(desc)


def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Load configuration from JSON file."""
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return json.load(f)
    return {}


def main():
    """Main entry point for the PIA Agent."""
    import argparse
    import os
    
    # Try to load environment variables from .env file
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass  # dotenv is optional
    
    parser = argparse.ArgumentParser(description='Privacy Impact Assessment Agent')
    parser.add_argument('--policies-dir', default='policies', help='Directory containing policy files')
    parser.add_argument('--config', default='config.json', help='Path to configuration file')
    parser.add_argument('--output', help='Output file for the assessment report (JSON)')
    parser.add_argument('--report', help='Output file for the human-readable report')
    parser.add_argument('--jira', action='store_true', help='Submit results to Jira')
    parser.add_argument('--no-jira', action='store_true', help='Skip Jira submission even if configured')
    
    args = parser.parse_args()
    
    # Load configuration
    config = load_config(args.config)
    jira_config = config.get('jira', {})
    
    # Override with environment variables if present
    if os.getenv('JIRA_URL'):
        jira_config['url'] = os.getenv('JIRA_URL')
    if os.getenv('JIRA_EMAIL'):
        jira_config['email'] = os.getenv('JIRA_EMAIL')
    if os.getenv('JIRA_API_TOKEN'):
        jira_config['api_token'] = os.getenv('JIRA_API_TOKEN')
    if os.getenv('JIRA_PROJECT_KEY'):
        jira_config['project_key'] = os.getenv('JIRA_PROJECT_KEY')
    
    # Initialize agent
    agent = PIAAgent(policies_dir=args.policies_dir, jira_config=jira_config if not args.no_jira else None)
    
    # Run assessment
    results = agent.analyze_policies()
    
    # Save results
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"💾 Assessment results saved to: {args.output}")
    
    # Generate and save report
    report = agent.generate_report()
    print("\n" + report)
    
    if args.report:
        with open(args.report, 'w') as f:
            f.write(report)
        print(f"💾 Report saved to: {args.report}")
    
    # Submit to Jira
    if args.jira and not args.no_jira:
        ticket_key = agent.submit_to_jira()
        if ticket_key:
            print(f"\n✅ PIA Assessment completed and submitted to Jira: {ticket_key}")
        else:
            print("\n⚠️  PIA Assessment completed but Jira submission failed")
    elif jira_config and not args.no_jira:
        # Auto-submit if configured
        ticket_key = agent.submit_to_jira()
        if ticket_key:
            print(f"\n✅ PIA Assessment completed and submitted to Jira: {ticket_key}")


if __name__ == "__main__":
    main()

