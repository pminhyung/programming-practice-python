"""
if문, for문뒤에 콜론 빼먹지 말자
변수 제대로 넣었는지 끝까지 확인하자
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i, j]
                continue