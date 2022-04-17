# @Time       ：2022/4/17 5:14 PM
# @Author     : cj
# File        : leetcode.py
# @Software   : PyCharm
'''
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

输入：nums = [3,2,4], target = 6
输出：[1,2]
'''
class Solution:
    def twoSum(self,nums,target):
        n = len(nums)  # 获取列表中元素数量
        for a in range(n):  # 循环索引，最大值为列表长度
            for b in range(a+1, n):  # 循环索引， n+1是因为不与当前循环的索引值对比， n则为最大列表长度
                if nums[a] + nums[b] == target:  # 如果通过循环索引的方式将两数相加等于 target
                    return [a,b]                 # 则返回a，b下标


if __name__ == '__main__':
    a = Solution()
    result = a.twoSum([3,4,5,6],7)
    print(result)