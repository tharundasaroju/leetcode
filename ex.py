def longestArithSeqLength(nums) -> int:
    max_len = 0
    total = len(nums)
    for i in range(total):
        if(max_len < total - i):
            for j in range(i+1, total, 1):
                if(max_len - 2 < total - j):
                    length = 2
                    diff = nums[j] - nums[i]
                    curr = nums[j] + diff
                    flag = True
                    index = j
                    while(flag):
                        try:
                            curr_arr = nums[index+1:]
                            index = index + curr_arr.index(curr) + 1
                            length = length +1
                            print(i, j, index, nums[j], curr, diff, total, max_len, length)
                            curr = curr + diff
                        except:
                            flag = False
                    if(length > max_len):
                        max_len = length
                else:
                    break
        else:
            break
    return max_len

print(longestArithSeqLength([0,1,1,1,0,1,1,1,1,0,1,0,0,0,1,1,0,1,1,1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,1,1,1,0,1,0,1,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,0,0,1,0,1,0,1,0,0,0,1,1,0,1,1,0,1,1,1,1,0,0,0,1,0,1,0,1,1,0,1,1,0,1,1,1,1,0,0,0,1,1,1,1,1,0,1,1,0,0,0,1,0,0,1,1,1,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,1,1,1,1,0,0,0,1,1,1,1,0,1,1,0,0,0,0,1,0,1,1,1,1,0,1,0,0,1,1,1,0,0,0,1,0,0,1,0,0,1,1,1,0,1,1,1,0,0,1,0,1,0,0,0,0,1,0,0,1,0,1,1,0,0,0,0,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,0,1,0,1,1,1,1,1,0,1,1,1,0,0,0,0,1,0,0,1,1,1,1,1,1,0,1,1,0,0,1,1,0,1,1,0,0,1,1,1,1,0,0,0,1,1,0,1,1,1,0,1,1,0,1,1,0,0,0,1,1,1,1,0,1,1,1,1,1,0,1,0,0,0,1,0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,1,0,1,0,1,1,1,0,0,1,0,0,1,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,0,0,0,1,1,1,0,0,0,1,1,0,1,0,0,0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,0,1,0,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,1,0,1,0,1,0,1,1,1,0,0,0,0,1,1,1,0,1,1,1,0,1,0,0,0,1,1,0,0,1,0,0,1,1,1,1,0,1,1,1,1,0,0,0,0,1,0,0,1,1,0,0,1,1,1,0,0,1,0,0,1,0,0,1,1,1,0,0,1,1,1,1,0,0,0,1,1,1,0,0,1,0,1,0,1,1,0,1,0,0,0,0,0,1,1,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,1,1,1,0,1,0,1,1,0,0,0,0,1,1,0,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1,1,0,1,0,0,1,1,1,0,1,0,0,1,0,0,0,0,1,1,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,0,0,1,0,0,1,1,1,1,0,0,1,0]))