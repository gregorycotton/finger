### Finger daemon

Finger me: `finger hello@gregorycotton.ca`

**Quick setup**: requires Python3 and a unix-like OS that can run `xinetd`.

1.  Place `finger.py` in `/usr/local/bin/` and make it executable,
2.  Create config file in `/etc/xinetd.d/` pointing to the script,
3.  Restart `xinetd` service.
4.  Create `.plan` file in a home directory (e.g., `/home/{user}/.plan`).
