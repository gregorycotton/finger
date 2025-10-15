# Finger daemon in Python

Finger daemon for Linux, using `xinetd` to listen for requests.

Requires:
* A Linux-based server,
* Python 3,
* `xinetd` service manager.

Quick Setup:
1.  Place `finger.py` in `/usr/local/bin/` and make it executable,
2.  Create config file in `/etc/xinetd.d/` pointing to the script,
3.  Restart `xinetd` service.
4.  Create `.plan` file in a home directory (e.g., `/home/{user}/.plan`).

Finger me: finger hello@gregorycotton.ca
