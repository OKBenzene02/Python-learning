# # Heap sort
class Solution:
    def heapify(self, arr, n, i):
        large = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            large = l
        if r < n and arr[large] < arr[r]:
            large = r
        if large != i:
            arr[i], arr[large] = arr[large], arr[i]
            self.heapify(arr, n, large)
    def heapsort(self, arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)

    def sortArray(self, nums: list) -> list:
        self.heapsort(nums)
        return nums

a = Solution()
print(a.sortArray([5,2,3,1]))