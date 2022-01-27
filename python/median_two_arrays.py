class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if m > n:
            m, n, = n, m
            nums1, nums2 = nums2, nums1
        
        # m and nums1 is smaller than n and nums2
        l = 0
        r = m - 1
        half = (m + n) // 2

        negative_inf = float('-inf')
        positive_inf = float('+inf')

        # finding the left partition
        while True:    
            left1 = (r + l) // 2
            left2 = half - left1 + 2

            if left1 < 0:
                left1_val = nums1[0]
                right1_val = positive_inf
            elif (left1 + 1) >= m:
                left1_val = negative_inf
                right1_val = nums1[m - 1]
            else:
                left1_val = nums1[left1]
                right1_val = nums1[left1 + 1]
            
            left2_val = 0
            right2_val = 0

            if left1_val <= right2_val and left2_val <= right1_val:
                # perfect partition
                pass
            elif left1_val > right2_val:
                r = left1 - 1
                if r < l:
                    l = r
            else:
                l = left1 + 1
