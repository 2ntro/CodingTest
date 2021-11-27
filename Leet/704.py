from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1
        # 조건을 왜 이렇게 정했나
        while left <= right:
            # pivotting 왜 이렇게 하는가?
            pivot = left + (right - left) // 2

            if nums[pivot] == target:
                return pivot
            
            elif nums[pivot] != target:
                
                # target이 pivot의 왼쪽에 존재할 때
                if nums[pivot] > target:
                    right = pivot - 1
                # target이 pivot의 오른쪽에 존재할 때
                elif nums[pivot] < target:
                    left = pivot + 1
        return -1