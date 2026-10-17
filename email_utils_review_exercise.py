import re

_EMAIL_REGEX = re.compile(
    r"[A-Za-z0-9_%+-]+(?:\.[A-Za-z0-9_%+-]+)*@"
    r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+"
    r"[A-Za-z]{2,}"
)


def is_valid(address: object) -> bool:
    """Return whether address matches a basic email format."""
    return isinstance(address, str) and _EMAIL_REGEX.fullmatch(address) is not None


def get_domain(email_str: str) -> str:
    """Return the domain from a valid email address."""
    if not is_valid(email_str):
        raise ValueError("Invalid email address")
    return email_str.rsplit("@", maxsplit=1)[1]


def local_part(email_str: str) -> str:
    """Return the local part from a valid email address."""
    if not is_valid(email_str):
        raise ValueError("Invalid email address")
    return email_str.split("@", maxsplit=1)[0]


def masked_email(email_str: str, show: int = 2) -> str:
    """Mask all but show leading local-part characters in a valid email."""
    if not is_valid(email_str):
        raise ValueError("Invalid email address")
    if isinstance(show, bool) or not isinstance(show, int) or show < 0:
        raise ValueError("show must be a non-negative integer")

    local, domain = email_str.split("@", maxsplit=1)
    visible = min(show, len(local))
    return f"{local[:visible]}{'*' * (len(local) - visible)}@{domain}"
