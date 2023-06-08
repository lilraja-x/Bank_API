"""
BLOCKLIST.py

This file just contains the BLOCKLIST of the JWT tokens. It will be imported by
app and the logout resource so that tokens can be added to the BLOCKLIST when the
user logs out.
"""

BLOCKLIST = set()