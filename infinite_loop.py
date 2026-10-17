def has_triplet_sum(nums: list[int], target: int) -> bool:
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    return True
    return False


if __name__ == "__main__":
    print(has_triplet_sum([1, 2, 3], 6))