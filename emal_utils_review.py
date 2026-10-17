"""email_utils.py

Small email helper utilities: validation, extracting parts, and masking.

Notes:
- The regex used here is intentionally simple and covers common email forms.
  For strict RFC-5322 validation consider higher-quality validators or libraries.
"""

import re
from typing import Tuple

# Simple, anchored regex that captures local and domain parts.
_EMAIL_RE = re.compile(
    r"^(?P<local>[A-Za-z0-9._%+\-]+)@(?P<domain>[A-Za-z0-9.-]+\.[A-Za-z]{2,})$"
)


def is_valid(address: str) -> bool:
    """Return True if address is a valid (simple) email address."""
    return isinstance(address, str) and bool(_EMAIL_RE.fullmatch(address))


def _split_email(addr: str) -> Tuple[str, str]:
    """Return (local, domain) for a validated email, raise ValueError otherwise."""
    if not isinstance(addr, str):
        raise TypeError("email address must be a string")
    m = _EMAIL_RE.fullmatch(addr)
    if not m:
        raise ValueError(f"invalid email address: {addr!r}")
    return m.group("local"), m.group("domain")


def get_domain(addr: str) -> str:
    """Return the domain portion of a validated email address."""
    _, domain = _split_email(addr)
    return domain


def local_part(addr: str) -> str:
    """Return the local part (before @) of a validated email address."""
    local, _ = _split_email(addr)
    return local


def masked_email(e: str, show: int = 2) -> str:
    """
    Mask an email so only `show` characters of the local part remain visible.
    Example: 'alice@example.com' -> 'al***@example.com' (when show=2)

    Raises:
        TypeError if e is not a string.
        ValueError if e is not a valid email or show < 0.
    """
    if not isinstance(e, str):
        raise TypeError("email must be a string")
    if not isinstance(show, int) or show < 0:
        raise ValueError("show must be a non-negative integer")

    local, domain = _split_email(e)

    if show >= len(local):
        masked_local = local
    else:
        masked_local = local[:show] + "*" * (len(local) - show)

    return f"{masked_local}@{domain}"
