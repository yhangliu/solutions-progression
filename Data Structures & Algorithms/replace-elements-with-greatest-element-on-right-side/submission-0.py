class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = arr[-1]
        for i in range (len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = greatest
            greatest = max(greatest, temp)
        arr[-1] = -1
        return arr