class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            largestNum = None
            for j in range(i+1, len(arr)):
                if largestNum == None or largestNum < arr[j]:
                    largestNum = arr[j]
            arr[i] = largestNum    
        arr[-1] = -1
        return arr