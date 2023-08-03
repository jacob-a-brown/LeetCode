'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''

class Solution(object):
    def findMedianSortedArrays_One(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # 1. merge the sorted lists
        # 2. return the middle element (0 + len(merged list) - 1)/2 if an odd number of elements
        # 3. return the average value of the two middle elements if an even number of elements as
        #       {[(0 + len(merged list) - 1)/2 + 0.5] + [(0 + len(merged list) - 1)/2 - 0.5]}/2

        # merge the lists
        merged_list = nums1

        for num2 in nums2:
            elem_inserted = False

            for i in range(len(merged_list)):
                merged_num = merged_list[i]

                if num2 <= merged_num:
                    merged_list.insert(i, num2)
                    elem_inserted = True
                    break

            if elem_inserted is False:
                merged_list.append(num2)

        # odd number of elements
        if len(merged_list) % 2 == 1:
            median_index = int((0 + len(merged_list) - 1)/2)
            median_element = merged_list[median_index]
            return median_element

        # even number of elements
        else:
            median_index_lo = int((0 + len(merged_list))/2 - 1)
            median_index_hi = int((0 + len(merged_list))/2)
            median_elements = [merged_list[median_index_lo], merged_list[median_index_hi]]
            return (median_elements[0] + median_elements[1])/2.0


    def findMedianSortedArrays_Two(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        merged_list = nums1 + nums2
        merged_list.sort()
        print(merged_list)

        # odd number of elements
        if len(merged_list) % 2 == 1:
            median_index = int((0 + len(merged_list) - 1)/2)
            median_element = merged_list[median_index]
            return median_element

        # even number of elements
        else:
            median_index_lo = int((0 + len(merged_list))/2 - 1)
            median_index_hi = int((0 + len(merged_list))/2)
            median_elements = [merged_list[median_index_lo], merged_list[median_index_hi]]
            return (median_elements[0] + median_elements[1])/2.0        

if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    sol1 = Solution().findMedianSortedArrays_One(nums1, nums2)
    print(sol1)

    nums1 = [1, 2]
    nums2 = [3, 4]
    sol2 = Solution().findMedianSortedArrays_Two(nums1, nums2)
    print(sol2)