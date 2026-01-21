# Panther SIEM Log Sources Lister

This script queries your Panther SIEM instance to list all configured log sources.

## Installation

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

You can configure Panther access in several ways:

### Option A: Using config.json

Copy the example configuration file:

```bash
cp config.json.example config.json
```

Edit `config.json` and add your Panther credentials:

```json
{
  "panther": {
    "api_url": "https://your-instance.runpanther.io",
    "api_token": "your-panther-api-token"
  }
}
```

### Option B: Using Environment Variables

Set the following environment variables:

```bash
export PANTHER_API_URL="https://your-instance.runpanther.io"
export PANTHER_API_TOKEN="your-panther-api-token"
```

Or use a `.env` file:

```bash
PANTHER_API_URL=https://your-instance.runpanther.io
PANTHER_API_TOKEN=your-panther-api-token
```

### Option C: Command Line Arguments

Pass credentials directly via command line:

```bash
python list_panther_sources.py --url "https://your-instance.runpanther.io" --token "your-token"
```

## Getting a Panther API Token

1. Log in to your Panther Console
2. Navigate to **Settings** → **API Tokens**
3. Click **Create Token**
4. Give it a name and select the **View Log Sources** permission
5. Copy the token (you won't be able to see it again)

## Usage

### Basic Usage

List all log sources:

```bash
python list_panther_sources.py
```

### Verbose Output

Show detailed information about each log source:

```bash
python list_panther_sources.py --verbose
```

### Save to JSON File

Save the results to a JSON file:

```bash
python list_panther_sources.py --output sources.json
```

### JSON Only Output

Output only JSON (useful for scripting):

```bash
python list_panther_sources.py --json-only
```

### Combined Options

```bash
python list_panther_sources.py --verbose --output sources.json
```

## Output Format

The script displays log sources in a table format showing:
- **ID**: Integration ID
- **Label**: Human-readable label
- **Type**: Integration type (e.g., AWS CloudTrail, S3, Syslog)
- **Status**: Health status of the log source

With `--verbose`, additional details are shown:
- Creation timestamp
- Created by (user or API token)
- Last received event time

## Examples

```bash
# List all sources using config file
python list_panther_sources.py

# List sources with environment variables
export PANTHER_API_URL="https://acme.runpanther.io"
export PANTHER_API_TOKEN="abc123..."
python list_panther_sources.py

# Get detailed output and save to file
python list_panther_sources.py --verbose --output panther_sources.json

# Use command line arguments
python list_panther_sources.py \
  --url "https://acme.runpanther.io" \
  --token "abc123..." \
  --verbose
```

## Troubleshooting

### Authentication Errors

If you get authentication errors:
- Verify your API token is correct
- Ensure the token has "View Log Sources" permission
- Check that the token hasn't expired

### Connection Errors

If you can't connect:
- Verify the API URL is correct (should be your Panther instance URL)
- Check your network connection
- Ensure your firewall allows outbound HTTPS connections

### No Sources Found

If no sources are returned:
- Verify you have log sources configured in Panther
- Check that your API token has the correct permissions
- Try using `--verbose` to see more details about the API response

