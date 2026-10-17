import pytest

from email_utils_review_exercise import (
    get_domain,
    is_valid,
    local_part,
    masked_email,
)


@pytest.mark.parametrize(
    "address",
    ["user@example.com", "first.last@mail.example.org", "a+b@sub.example.co"],
)
def test_is_valid_accepts_basic_addresses(address):
    assert is_valid(address)


@pytest.mark.parametrize(
    "address",
    [
        "plainaddress",
        "user@",
        "@example.com",
        "a..b@example.com",
        "user@-example.com",
        "user@example-.com",
        None,
    ],
)
def test_is_valid_rejects_malformed_addresses(address):
    assert not is_valid(address)


def test_extractors_return_parts_from_valid_address():
    address = "first.last@example.com"
    assert get_domain(address) == "example.com"
    assert local_part(address) == "first.last"


@pytest.mark.parametrize("extract", [get_domain, local_part])
def test_extractors_raise_for_invalid_address(extract):
    with pytest.raises(ValueError, match="Invalid email address"):
        extract("missing-at-sign")


def test_masked_email_masks_local_part_and_caps_visible_characters():
    assert masked_email("jordan@example.com") == "jo****@example.com"
    assert masked_email("jo@example.com", show=8) == "jo@example.com"


@pytest.mark.parametrize("show", [-1, 1.5, "2", True])
def test_masked_email_rejects_invalid_show(show):
    with pytest.raises(ValueError, match="show must be a non-negative integer"):
        masked_email("jordan@example.com", show=show)


def test_masked_email_raises_for_invalid_address():
    with pytest.raises(ValueError, match="Invalid email address"):
        masked_email("not-an-email")
