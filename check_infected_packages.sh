#!/bin/bash
#
# Endor Labs - Infected Package Checker
#
# This script checks your Endor Labs tenant for packages that match
# malicious versions listed in a CSV file.
#
# Usage:
#   ./check_infected_packages.sh [options]
#
# Options:
#   -f, --file FILE          Path to CSV file (default: affected-packages-and-versions.csv)
#   -n, --namespace NAME     Endor Labs namespace (default: example)
#   -o, --output FILE        Output file for results (optional)
#   -v, --verbose           Enable verbose output
#   -h, --help              Show this help message
#

set -euo pipefail

# Default values
CSV_FILE="affected-packages-and-versions.csv"
NAMESPACE="example"
OUTPUT_FILE=""
VERBOSE=false

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Help function
show_help() {
    cat << EOF
Endor Labs - Infected Package Checker

This script checks your Endor Labs tenant for packages that match
malicious versions listed in a CSV file.

Usage:
    $0 [OPTIONS]

Options:
    -f, --file FILE          Path to CSV file containing affected packages
                            (default: affected-packages-and-versions.csv)
    -n, --namespace NAME     Endor Labs namespace/tenant name
                            (default: example)
    -o, --output FILE        Save results to a file (JSON format)
    -v, --verbose           Enable verbose output
    -h, --help              Show this help message

Examples:
    # Basic usage with default CSV file
    $0 -n my-tenant

    # Specify custom CSV file
    $0 -f my-vulnerabilities.csv -n my-tenant

    # Save results to file
    $0 -n my-tenant -o results.json

Requirements:
    - endorctl CLI tool must be installed and configured
    - CSV file must have format: package_name,version
    - First row should be headers (will be skipped)

CSV Format:
    package,version
    express,4.17.0
    lodash,4.17.20
    ...

EOF
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -f|--file)
            CSV_FILE="$2"
            shift 2
            ;;
        -n|--namespace)
            NAMESPACE="$2"
            shift 2
            ;;
        -o|--output)
            OUTPUT_FILE="$2"
            shift 2
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        *)
            echo -e "${RED}Error: Unknown option: $1${NC}" >&2
            show_help
            exit 1
            ;;
    esac
done

# Check if endorctl is installed
if ! command -v endorctl &> /dev/null; then
    echo -e "${RED}Error: endorctl command not found${NC}" >&2
    echo "Please install endorctl and ensure it's in your PATH"
    exit 1
fi

# Check if CSV file exists
if [[ ! -f "$CSV_FILE" ]]; then
    echo -e "${RED}Error: CSV file not found: $CSV_FILE${NC}" >&2
    echo "Please provide a valid CSV file with the -f option"
    exit 1
fi

# Validate CSV file format (should have at least 2 lines: header + data)
if [[ $(wc -l < "$CSV_FILE") -lt 2 ]]; then
    echo -e "${YELLOW}Warning: CSV file appears to be empty or has no data rows${NC}" >&2
fi

if [[ "$VERBOSE" == true ]]; then
    echo -e "${GREEN}Starting infected package check...${NC}"
    echo "CSV File: $CSV_FILE"
    echo "Namespace: $NAMESPACE"
    echo ""
fi

# Build the malicious versions list from CSV
# Format: package@version -> 'npm://package@version'
if [[ "$VERBOSE" == true ]]; then
    echo "Processing CSV file..."
fi

malicious_versions=$(tr -d '\r' < "$CSV_FILE" | awk -F',' '
NR>1 { 
    # Skip empty lines and trim whitespace
    gsub(/^[ \t]+|[ \t]+$/, "", $1)
    gsub(/^[ \t]+|[ \t]+$/, "", $2)
    if ($1 != "" && $2 != "") {
        pkgs[$1"@"$2]=1
    }
}
END {
    first=1
    for (p in pkgs) {
        if(!first) printf ","
        printf "\x27npm://%s\x27", p
        first=0
    }
}')

# Check if we found any packages
if [[ -z "$malicious_versions" ]]; then
    echo -e "${YELLOW}Warning: No valid packages found in CSV file${NC}" >&2
    echo "Please check the CSV format: package,version"
    exit 1
fi

if [[ "$VERBOSE" == true ]]; then
    echo "Found packages to check:"
    echo "$malicious_versions" | tr ',' '\n' | sed 's/^/  /'
    echo ""
    echo "Querying Endor Labs API..."
fi

# Run the endorctl command
# Store output in a variable so we can check for errors and optionally save to file
if [[ -n "$OUTPUT_FILE" ]]; then
    echo "Saving results to: $OUTPUT_FILE"
    if endorctl api list -n "$NAMESPACE" -r DependencyMetadata \
        --traverse \
        --filter="context.type==CONTEXT_TYPE_MAIN and meta.name in [$malicious_versions]" \
        --group-aggregation-paths="meta.name,spec.dependency_data.project_uuid" \
        > "$OUTPUT_FILE" 2>&1; then
        echo -e "${GREEN}✓ Query completed successfully${NC}"
        echo "Results saved to: $OUTPUT_FILE"
        
        # Show summary if output is JSON
        if [[ "$OUTPUT_FILE" == *.json ]]; then
            if command -v jq &> /dev/null; then
                count=$(jq 'length' "$OUTPUT_FILE" 2>/dev/null || echo "N/A")
                echo "Found $count matching package(s)"
            fi
        fi
    else
        echo -e "${RED}✗ Query failed${NC}" >&2
        echo "Check the output file for error details: $OUTPUT_FILE"
        exit 1
    fi
else
    # Output to stdout
    if endorctl api list -n "$NAMESPACE" -r DependencyMetadata \
        --traverse \
        --filter="context.type==CONTEXT_TYPE_MAIN and meta.name in [$malicious_versions]" \
        --group-aggregation-paths="meta.name,spec.dependency_data.project_uuid"; then
        echo -e "${GREEN}✓ Query completed successfully${NC}"
    else
        echo -e "${RED}✗ Query failed${NC}" >&2
        exit 1
    fi
fi

echo ""
echo -e "${GREEN}Infected package check completed!${NC}"


