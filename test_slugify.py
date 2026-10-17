from app import slugify


def test_slugify_basic_phrase():
    assert slugify("Hello World") == "hello-world", "Should lowercase and hyphenate words"


def test_slugify_multiple_punctuation():
    assert (
        slugify("Hello, world!!! Good?")
        == "hello-world-good"
    ), "Should replace punctuation groups with single hyphens"


def test_slugify_removes_emojis():
    assert slugify("Python 🐍 rocks 🚀") == "python-rocks", "Should remove emojis"
