class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        insertion_list=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    if nums1[i] in insertion_list:
                        continue
                    else:
                        insertion_list.append(nums1[i])
                    break
        return insertion_list