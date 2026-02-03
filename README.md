# Regex Data Extraction 
By: Eric Cyril Chuwa

Python regex-based system to extract structured data from raw text with security validation.

## Features
- Extracts 6 data types: Email, URL, Time, Currency, HTML Tags, Hashtags
- Security: 10k char limit, input validation, malformed rejection
- Handles real-world messy data with case insensitivity and multiline support
- Clean CLI output from file input

## Quick Start

1. Save code as `main.py`
2. Create `sample_input.txt` with test data
3. Run: `python main.py`

## File Structure
```
├── main.py
├── sample_input.txt
└── README.md
```

## Output Example
```
=== Data Extraction ===

Results:
----------------------------------------

Email:
  1. john.doe@company.co.uk
  2. support@client-services.com

Url:
  1. https://dashboard.company.co.uk/login

Time:
  1. 14:30
  2. 2:30 PM
```

## Data Types Extracted
- Email addresses
- URLs (http/https)
- Time (24hr + 12hr AM/PM)
- Currency ($1,234.56 format)
- HTML tags (`<div>`, `</p>`)
- Hashtags (`#example`)

## Security Features
- 10k character input limit (DoS protection)
- Strict validation rejects malformed data
- Production-grade error handling

## Tech Details
- Uses `re.IGNORECASE` for case insensitive matching
- Uses `re.DOTALL` for multiline data extraction
- OOP design with `BaseValidator` template pattern

---
**Built for ALU Software Engineering Assignment**
```