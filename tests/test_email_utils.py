import pytest

from emal_utils_review import is_valid, get_domain, local_part, masked_email


def test_is_valid_examples():
    assert is_valid("alice@example.com")
    assert is_valid("user.name+tag@example.co.uk")
    assert not is_valid("not-an-email")
    assert not is_valid("alice@@example.com")
    # TLD must be at least 2 chars in the simple regex
    assert not is_valid("a@b.c")


def test_get_domain_and_local_part_valid():
    email = "alice.smith+news@example.co.uk"
    assert get_domain(email) == "example.co.uk"
    assert local_part(email) == "alice.smith+news"


@pytest.mark.parametrize("bad", ["no-at-symbol", "also@@bad", "@missinglocal", "missingdomain@"])
def test_get_domain_local_part_invalid(bad):
    with pytest.raises((ValueError, TypeError)):
        get_domain(bad)
    with pytest.raises((ValueError, TypeError)):
        local_part(bad)


def test_masked_email_basic():
    assert masked_email("alice@example.com") == "al***@example.com"
    assert masked_email("bob@example.com", show=0) == "***@example.com"
    assert masked_email("a@tiny.com", show=10) == "a@tiny.com"  # show >= len(local) keeps local


def test_masked_email_invalid_inputs():
    with pytest.raises((ValueError, TypeError)):
        masked_email("not-an-email")

    with pytest.raises(ValueError):
        masked_email("alice@example.com", show=-1)

    with pytest.raises(ValueError):
        masked_email("alice@example.com", show="two")
