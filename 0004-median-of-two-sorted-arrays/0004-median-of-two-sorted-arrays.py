class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x = len(nums1)
        y = len(nums2)

        low = 0
        high = x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            # Correct partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:

                # If total length is even
                if (x + y) % 2 == 0:
                    return (
                        max(maxLeftX, maxLeftY) +
                        min(minRightX, minRightY)
                    ) / 2.0

                # If total length is odd
                else:
                    return float(max(maxLeftX, maxLeftY))

            # Move towards left
            elif maxLeftX > minRightY:
                high = partitionX - 1

            # Move towards right
            else:
                low = partitionX + 1