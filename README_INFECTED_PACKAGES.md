# Endor Labs - Infected Package Checker

This script checks your Endor Labs tenant for packages that match malicious versions listed in a CSV file. It uses the Endor Labs API to identify if any of the affected packages are present in your environment.

## Prerequisites

1. **Endor Labs CLI (`endorctl`)**: Must be installed and configured
   - Installation instructions: [Endor Labs Documentation](https://docs.endorlabs.com)
   - Ensure `endorctl` is authenticated and has access to your tenant

2. **CSV File**: A file containing affected packages and versions
   - Format: `package,version` (comma-separated)
   - First row should be headers (will be automatically skipped)
   - Example provided: `affected-packages-and-versions.csv.example`

## Installation

1. Make the script executable:
   ```bash
   chmod +x check_infected_packages.sh
   ```

2. (Optional) Install `jq` for better JSON output parsing:
   ```bash
   # macOS
   brew install jq
   
   # Linux (Ubuntu/Debian)
   sudo apt-get install jq
   ```

## Usage

### Basic Usage

Check for infected packages using the default CSV file:

```bash
./check_infected_packages.sh -n your-tenant-name
```

### Specify Custom CSV File

```bash
./check_infected_packages.sh -f my-vulnerabilities.csv -n your-tenant-name
```

### Save Results to File

Save the API response to a JSON file:

```bash
./check_infected_packages.sh -n your-tenant-name -o results.json
```

### Verbose Output

Enable detailed output:

```bash
./check_infected_packages.sh -n your-tenant-name -v
```

### Complete Example

```bash
./check_infected_packages.sh \
  -f affected-packages-and-versions.csv \
  -n my-company \
  -o infected-packages-results.json \
  -v
```

## CSV File Format

The CSV file should follow this format:

```csv
package,version
express,4.17.0
lodash,4.17.20
axios,0.21.0
react,18.0.0
```

**Important:**
- First row must be headers (`package,version`)
- Each subsequent row should contain a package name and version
- Package names should match npm package names
- Versions should be exact version numbers
- Empty lines will be skipped

## Command Line Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--file` | `-f` | Path to CSV file with affected packages | `affected-packages-and-versions.csv` |
| `--namespace` | `-n` | Endor Labs namespace/tenant name | `example` |
| `--output` | `-o` | Save results to file (JSON format) | Output to stdout |
| `--verbose` | `-v` | Enable verbose output | Off |
| `--help` | `-h` | Show help message | - |

## How It Works

1. **Reads CSV File**: Parses the CSV file to extract package names and versions
2. **Formats Query**: Converts the CSV data into the format required by Endor Labs API:
   - Format: `'npm://package@version'`
   - Multiple packages are comma-separated
3. **Queries Endor Labs**: Uses `endorctl` to query the DependencyMetadata resource
4. **Filters Results**: Only checks packages in the main context (`CONTEXT_TYPE_MAIN`)
5. **Groups Results**: Groups by package name and project UUID

## Output

The script outputs:
- **Console**: Status messages and the API response (unless saved to file)
- **File** (if `-o` specified): JSON response from Endor Labs API

### Understanding Results

The API response will show:
- Which packages from your CSV are found in your tenant
- Which projects/workspaces contain these packages
- Dependency metadata for each match

### Example Output

```
Starting infected package check...
CSV File: affected-packages-and-versions.csv
Namespace: my-company

Processing CSV file...
Found packages to check:
  'npm://express@4.17.0'
  'npm://lodash@4.17.20'

Querying Endor Labs API...
✓ Query completed successfully

Infected package check completed!
```

## Troubleshooting

### Error: `endorctl command not found`

**Solution**: Install and configure `endorctl`:
```bash
# Follow Endor Labs installation instructions
# Ensure endorctl is in your PATH
```

### Error: `CSV file not found`

**Solution**: 
- Check that the CSV file exists
- Use `-f` option to specify the correct path
- Ensure you're running the script from the correct directory

### Error: `No valid packages found in CSV file`

**Solution**:
- Verify CSV format is correct (package,version)
- Check that there are data rows (not just headers)
- Ensure package names and versions are not empty

### API Authentication Errors

**Solution**:
- Verify `endorctl` is authenticated: `endorctl auth status`
- Check that you have access to the specified namespace
- Ensure your API token has the necessary permissions

### No Results Returned

This could mean:
- ✅ **Good news**: None of the malicious packages are in your tenant
- ⚠️ **Check**: Verify the package names/versions in your CSV match exactly what's in your dependencies
- ⚠️ **Check**: Ensure the namespace is correct

## Integration with CI/CD

You can integrate this script into your CI/CD pipeline:

```yaml
# Example GitHub Actions
- name: Check for infected packages
  run: |
    ./check_infected_packages.sh \
      -f security-advisory-packages.csv \
      -n ${{ secrets.ENDOR_NAMESPACE }} \
      -o infected-packages.json
      
- name: Upload results
  uses: actions/upload-artifact@v3
  with:
    name: infected-packages-scan
    path: infected-packages.json
```

## Security Notes

- The CSV file may contain sensitive information about vulnerabilities
- Store results files securely
- Consider adding results files to `.gitignore`
- Use secure methods to pass namespace/credentials in CI/CD

## Support

For issues with:
- **This script**: Check the troubleshooting section above
- **Endor Labs API**: Consult [Endor Labs Documentation](https://docs.endorlabs.com)
- **endorctl CLI**: Run `endorctl --help` or check Endor Labs support


