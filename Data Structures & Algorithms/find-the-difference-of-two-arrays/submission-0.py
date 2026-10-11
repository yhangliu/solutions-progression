class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)

        set2 = set(nums2)

        arr1 = []
        arr2 = []
        ans = []

        for num in set1:
            if num not in set2:
                arr1.append(num)
        for num in set2:
            if num not in set1:
                arr2.append(num)
        ans.append(arr1)
        ans.append(arr2)
        return  ans

