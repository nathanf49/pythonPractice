def containsDuplicate(self, nums: List[int]) -> bool:
    if len(set(nums)) == len(nums):
        return False  # sets contain each element once by definition so if the set is the same length as the list each num will appear once
    else:
        return True