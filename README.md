# SSH Log Analyzer

This script parses SSH authentication logs (including compressed `.gz` log files with `zcat`) to identify brute-force attempts.  
It aggregates by **IP address**, showing:

- Number of failed attempts (`Attempts`)
- Number of unique usernames tried (`Unique Users`)
- Which usernames were attempted

## Features
- Reads from rotated/compressed log files (`.gz`) using `zcat`
- Counts failed login attempts per IP
- Tracks unique usernames tried by each IP
- Outputs results in a clean table

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/Elyessto/SSH-Brute-Force-Detector.git
   cd     SSH-Brute-Force-Detector/
   
   ## set your log paths inside the Python scripts 
   python3 Parse_compressed_log_files.py OR python3 Parse_log_files.py
2. Set Your Log Path
   ```bash
   vim Parse_compressed_log_files.py  ==> logfile = "/var/log/auth.log.3.gz"
   vim Parse_log_files.py  ==> logfile = "/var/log/auth.log
3. Run Script
   ```bash
    python3 Parse_compressed_log_files.py or Parse_log_files.py
