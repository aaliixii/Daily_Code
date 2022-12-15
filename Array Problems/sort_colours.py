def sortColors(nums):
    '''
        Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects 
        of the same color are adjacent, with the colors in the order red, white, and blue.

        We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

        You must solve this problem without using the library's sort function.


        Example 1:

        Input: nums = [2,0,2,1,1,0]
        Output: [0,0,1,1,2,2]
        Example 2:

        Input: nums = [2,0,1]
        Output: [0,1,2]

    '''

    temp = 0
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp

    print(nums)

    # Follow up: Could you come up with a one-pass algorithm using only constant extra space?
def op_sortColors(nums):

    count_0 = [0 for i in range(0, nums.count(0))]
    count_1 = [1 for i in range(0, nums.count(1))]
    count_2 = [2 for i in range(0, nums.count(2))]

    nums = count_0 + count_1 + count_2

    print(nums)

def main():
    sortColors([2,1,0,1,0,2])
    sortColors([1,0,2])

    op_sortColors([2,1,0,1,0,2])
    op_sortColors([1,0,2])

    
if __name__ == '__main__':
    main()