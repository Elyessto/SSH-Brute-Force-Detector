import re
from collections import defaultdict

logfile = "auth.log"   # change to your log file path

# Regex pattern for SSH invalid user attempts
pattern = re.compile(
    r'Invalid user (?P<user>\S+) from (?P<ip>\S+) port (?P<port>\d+)'
)

# Data structure: { ip: {"count": int, "users": set()} }
attackers = defaultdict(lambda: {"count": 0, "users": set()})

with open(logfile, "r") as f:
    for line in f:
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
