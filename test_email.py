import pytest

from email_utils import is_valid_email


@pytest.mark.parametrize(
	"email",
	[
		"user@example.com",
		"first.last@example.org",
		"user@mail.example.com",  # Sub-domain edge case
	],
)
def test_is_valid_email_accepts_valid_addresses(email):
	assert is_valid_email(email) is True


@pytest.mark.parametrize(
	"email",
	[
		"plainaddress",
		"user@",
		"@example.com",
	],
)
def test_is_valid_email_rejects_invalid_addresses(email):
	assert is_valid_email(email) is False
