import re
import subprocess
from collections import defaultdict

# Path to your compressed log file
logfile = "/var/log/auth.log.4.gz"

# Regex pattern for SSH invalid user attempts
pattern = re.compile(
    r'Invalid user (?P<user>\S+) from (?P<ip>\S+) port (?P<port>\d+)'
)

# Data structure: { ip: {"count": int, "users": set()} }
attackers = defaultdict(lambda: {"count": 0, "users": set()})

# Run zcat and read its output line by line
process = subprocess.Popen(["zcat", logfile], stdout=subprocess.PIPE, text=True)

for line in process.stdout:
    match = pattern.search(line)
    if match:
        ip = match.group("ip")
        user = match.group("user")
        attackers[ip]["count"] += 1
        attackers[ip]["users"].add(user)

# Print results
print(f"{'IP Address':<20}{'Attempts':<10}{'Unique Users'}")
print("-" * 50)
for ip, info in attackers.items():
    print(f"{ip:<20}{info['count']:<10}{len(info['users'])} ({', '.join(info['users'])})")

