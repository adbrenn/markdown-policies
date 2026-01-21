#!/usr/bin/env python3
"""
Panther SIEM Log Sources Lister

This script queries Panther's GraphQL API to list all configured log sources
in your Panther instance.
"""

import os
import json
import sys
from typing import Dict, List, Any, Optional
import argparse

try:
    import requests
except ImportError:
    print("Error: 'requests' library is required. Install it with: pip install requests")
    sys.exit(1)


class PantherClient:
    """Client for interacting with Panther SIEM GraphQL API."""
    
    def __init__(self, api_url: str, api_token: str):
        """
        Initialize Panther client.
        
        Args:
            api_url: Panther GraphQL API endpoint (e.g., https://your-instance.runpanther.io/public/graphql)
            api_token: Panther API token with 'View Log Sources' permission
        """
        self.api_url = api_url.rstrip('/')
        if not self.api_url.endswith('/graphql'):
            self.api_url = f"{self.api_url}/public/graphql"
        self.api_token = api_token
        self.headers = {
            'Authorization': f'Bearer {api_token}',
            'Content-Type': 'application/json'
        }
    
    def list_sources(self, cursor: str = "") -> Dict[str, Any]:
        """
        Query Panther API to list all log sources.
        
        Args:
            cursor: Pagination cursor for retrieving additional results
            
        Returns:
            Dictionary containing the API response
        """
        query = '''
        query ListSources($cursor: String) {
          sources(input: { cursor: $cursor }) {
            edges {
              node {
                integrationId
                integrationLabel
                integrationType
                createdAtTime
                createdBy {
                  ... on User {
                    id
                  }
                  ... on APIToken {
                    id
                  }
                }
                health {
                  status
                  lastReceivedEventTime
                }
              }
            }
            pageInfo {
              hasNextPage
              endCursor
            }
          }
        }
        '''
        
        variables = {"cursor": cursor} if cursor else {}
        
        try:
            response = requests.post(
                self.api_url,
                json={'query': query, 'variables': variables},
                headers=self.headers,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error querying Panther API: {e}", file=sys.stderr)
            if hasattr(e, 'response') and e.response is not None:
                try:
                    error_data = e.response.json()
                    print(f"API Error: {error_data}", file=sys.stderr)
                except:
                    print(f"Response: {e.response.text}", file=sys.stderr)
            raise
    
    def get_all_sources(self) -> List[Dict[str, Any]]:
        """
        Retrieve all log sources, handling pagination.
        
        Returns:
            List of all log source nodes
        """
        all_sources = []
        cursor = ""
        has_next_page = True
        
        while has_next_page:
            result = self.list_sources(cursor)
            
            # Check for GraphQL errors
            if 'errors' in result:
                print(f"GraphQL Errors: {result['errors']}", file=sys.stderr)
                break
            
            data = result.get('data', {})
            sources_data = data.get('sources', {})
            edges = sources_data.get('edges', [])
            
            for edge in edges:
                all_sources.append(edge.get('node', {}))
            
            page_info = sources_data.get('pageInfo', {})
            has_next_page = page_info.get('hasNextPage', False)
            cursor = page_info.get('endCursor', "")
        
        return all_sources


def format_timestamp(timestamp: Optional[int]) -> str:
    """Format Unix timestamp to readable string."""
    if not timestamp:
        return "N/A"
    try:
        from datetime import datetime
        return datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')
    except:
        return str(timestamp)


def print_sources_table(sources: List[Dict[str, Any]], verbose: bool = False):
    """Print log sources in a formatted table."""
    if not sources:
        print("No log sources found.")
        return
    
    print(f"\nFound {len(sources)} log source(s):\n")
    
    if verbose:
        # Detailed output
        for i, source in enumerate(sources, 1):
            print(f"{'='*60}")
            print(f"Source #{i}")
            print(f"{'='*60}")
            print(f"ID:              {source.get('integrationId', 'N/A')}")
            print(f"Label:           {source.get('integrationLabel', 'N/A')}")
            print(f"Type:            {source.get('integrationType', 'N/A')}")
            print(f"Created:         {format_timestamp(source.get('createdAtTime'))}")
            
            created_by = source.get('createdBy', {})
            if created_by:
                print(f"Created By:      {created_by.get('id', 'N/A')}")
            
            health = source.get('health', {})
            if health:
                print(f"Status:          {health.get('status', 'N/A')}")
                print(f"Last Event:      {format_timestamp(health.get('lastReceivedEventTime'))}")
            print()
    else:
        # Compact table format
        print(f"{'ID':<40} {'Label':<30} {'Type':<20} {'Status':<10}")
        print("-" * 100)
        for source in sources:
            source_id = source.get('integrationId', 'N/A')[:38]
            label = source.get('integrationLabel', 'N/A')[:28]
            source_type = source.get('integrationType', 'N/A')[:18]
            health = source.get('health', {})
            status = health.get('status', 'N/A')[:8] if health else 'N/A'
            print(f"{source_id:<40} {label:<30} {source_type:<20} {status:<10}")


def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Load configuration from JSON file."""
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return json.load(f)
    return {}


def main():
    """Main entry point for the Panther log sources lister."""
    # Try to load environment variables from .env file
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass  # dotenv is optional
    
    parser = argparse.ArgumentParser(
        description='List log sources from Panther SIEM',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage with config file
  python list_panther_sources.py
  
  # Use environment variables
  export PANTHER_API_URL="https://your-instance.runpanther.io"
  export PANTHER_API_TOKEN="your-token"
  python list_panther_sources.py
  
  # Verbose output
  python list_panther_sources.py --verbose
  
  # Save to JSON file
  python list_panther_sources.py --output sources.json
        """
    )
    parser.add_argument('--config', default='config.json', help='Path to configuration file')
    parser.add_argument('--url', help='Panther API URL (overrides config)')
    parser.add_argument('--token', help='Panther API token (overrides config)')
    parser.add_argument('--output', help='Output file for JSON results')
    parser.add_argument('--verbose', '-v', action='store_true', help='Show detailed information')
    parser.add_argument('--json-only', action='store_true', help='Output only JSON (no table)')
    
    args = parser.parse_args()
    
    # Load configuration
    config = load_config(args.config)
    panther_config = config.get('panther', {})
    
    # Get API URL and token from various sources (priority: CLI args > env vars > config file)
    api_url = (
        args.url or
        os.getenv('PANTHER_API_URL') or
        panther_config.get('api_url') or
        os.getenv('PANTHER_URL')
    )
    
    api_token = (
        args.token or
        os.getenv('PANTHER_API_TOKEN') or
        panther_config.get('api_token') or
        os.getenv('PANTHER_TOKEN')
    )
    
    # Validate required parameters
    if not api_url:
        print("Error: Panther API URL is required.", file=sys.stderr)
        print("Provide it via --url, PANTHER_API_URL env var, or config.json", file=sys.stderr)
        sys.exit(1)
    
    if not api_token:
        print("Error: Panther API token is required.", file=sys.stderr)
        print("Provide it via --token, PANTHER_API_TOKEN env var, or config.json", file=sys.stderr)
        sys.exit(1)
    
    # Initialize client and fetch sources
    try:
        client = PantherClient(api_url, api_token)
        print("Querying Panther API for log sources...")
        sources = client.get_all_sources()
        
        # Save to file if requested
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(sources, f, indent=2)
            print(f"✓ Results saved to: {args.output}")
        
        # Print output
        if not args.json_only:
            print_sources_table(sources, verbose=args.verbose)
        else:
            print(json.dumps(sources, indent=2))
        
        print(f"\n✓ Successfully retrieved {len(sources)} log source(s)")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()

