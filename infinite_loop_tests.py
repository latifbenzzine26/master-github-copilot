from infinite_loop import has_triplet_sum


def test_returns_true_when_distinct_elements_match_target():
    assert has_triplet_sum([1, 2, 3, 4], 9) is True


def test_returns_false_when_no_triplet_matches_target():
    assert has_triplet_sum([1, 2, 3], 20) is False


def test_triplet_requires_three_distinct_indices():
    assert has_triplet_sum([3, 1], 7) is False
    assert has_triplet_sum([3, 3, 1], 7) is True


def test_returns_false_with_fewer_than_three_elements():
    assert has_triplet_sum([], 0) is False
    assert has_triplet_sum([1, 2], 3) is False


def test_supports_negative_numbers():
    assert has_triplet_sum([-5, 2, 4, 10], 1) is True
