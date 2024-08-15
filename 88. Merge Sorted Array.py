class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # start from the end of the two arrays and put them in place from the back
        m_index = m - 1
        n_index = n - 1

        # result_index tracks where we are from the end of the resulting nums1 array
        result_index = m + n - 1

        while n_index >= 0:
            if m_index >= 0 and nums1[m_index] > nums2[n_index]:
                nums1[result_index] = nums1[m_index]
                m_index -= 1
            else:
                nums1[result_index] = nums2[n_index]
                n_index -= 1
            result_index -= 1


        # overly convoluted, can use n_index to track progress because once n_index runs out, 
        # remaining nums1 is already guaranteed to be sorted

        # while result_index >= 0:
        #     if m_index >= 0 and n_index >= 0:
        #         if nums2[n_index] > nums1[m_index]:
        #             nums1[result_index] = nums2[n_index]
        #             n_index -= 1
        #             result_index -= 1
        #         else:
        #             nums1[result_index] = nums1[m_index]
        #             m_index -= 1
        #             result_index -= 1
        #     elif m_index >= 0:
        #         nums1[result_index] = nums1[m_index]
        #         m_index -= 1
        #         result_index -= 1
        #     else:
        #         nums1[result_index] = nums2[n_index]
        #         n_index -= 1
        #         result_index -= 1