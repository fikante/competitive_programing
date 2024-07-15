class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    c.append(nums1[i])
                    nums2.remove(nums1[i])
                    break
        return c