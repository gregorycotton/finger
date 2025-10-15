#!/usr/bin/env python3
import sys
import os

username = sys.stdin.readline().strip()

if not username or not username.isalnum():
    sys.exit(0)

plan_file = os.path.join('/home', username, '.plan')

try:
    with open(plan_file, 'r') as f:
        sys.stdout.write(f.read())
except FileNotFoundError:
    sys.stdout.write(f"Login: {username}\t\t\t\tName: ???\n")
    sys.stdout.write("No Plan.\n")
except Exception:
    pass

sys.exit(0)
