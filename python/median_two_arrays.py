from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if m > n:
            m, n, = n, m
            nums1, nums2 = nums2, nums1
        
        # m and nums1 is smaller than n and nums2
        total = m + n
        half = total // 2
        l , r = 0, m - 1

        negative_inf = float('-inf')
        positive_inf = float('+inf')

        # finding the left partition
        while True:    
            left1 = (r + l) // 2 # nums1
            left2 = half - left1 - 2 # nums2
            
            left1_val = nums1[left1] if left1 >= 0 else negative_inf
            right1_val = nums1[left1 + 1] if (left1  + 1) < m else positive_inf
            
            left2_val = nums2[left2] if left2 >= 0 else negative_inf
            right2_val = nums2[left2 + 1] if (left2 + 1) < n else positive_inf
            
            if left1_val <= right2_val and left2_val <= right1_val:
                # perfect left partition
                if total % 2:
                    return min(right1_val, right2_val)
                else:
                    min_val = max(left1_val, left2_val)
                    max_val = min(right1_val, right2_val)

                return (min_val + max_val) / 2

            elif left1_val > right2_val:
                r = left1 - 1
            else:
                l = left1 + 1

# test here
nums1 = [3, 4]
nums2 = [1, 2]
print(Solution().findMedianSortedArrays(nums1, nums2))
