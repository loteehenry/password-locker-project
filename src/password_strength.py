"""Checks strength of password"""

import re

def password_strength(password: str) -> bool:
    if len(password) < 8:
        return False

    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$'
    return bool(re.match(pattern, password))
