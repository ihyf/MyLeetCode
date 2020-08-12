# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 16:20
# @Author  : ihyf
# @File    : TestCase.py
# @Software: PyCharm
# @ Desc :
import unittest


class Solution(object):
    @staticmethod
    def two_sum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None


class TestCase(unittest.TestCase):
    def test_two_sum(self):
        nums = [2, 7, 11, 15]
        target = 9
        s = Solution()
        result = s.two_sum(nums, target)
        self.assertEqual(nums[result[0]] + nums[result[1]], target)

    def test_two_sum_1(self):
        nums = [3, 4, 8, 12, 13]
        target = 12
        s = Solution()
        result = s.two_sum(nums, target)
        self.assertEqual(nums[result[0]] + nums[result[1]], target)


if __name__ == "__main__":
    unittest.main()

