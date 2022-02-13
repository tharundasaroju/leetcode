def nextClosestTime(time: str) -> str:
    digit_arr = []
    for x in [0,1,3,4]:
        if(time[x] not in digit_arr):
            digit_arr.append(time[x])
    digit_arr.sort()
    length = len(digit_arr)
    
    i = digit_arr.index(time[0])
    j = digit_arr.index(time[1])
    k = digit_arr.index(time[3])
    l = digit_arr.index(time[4])

    final_time = nextTime(digit_arr, time, length, i, j, k, l)
    if(final_time == None):
        final_time = nextTime(digit_arr, time, length)
        if(final_time == None):
            final_time = time
    return final_time

def nextTime(digit_arr, initial_seed, length, i =0, j=0, k=0, l=0):
    print(digit_arr, initial_seed, length, i, j, k, l)
    while i < length:
        if(digit_arr[i] < "3"):
            while j < length:
                if(digit_arr[i] != "2" or digit_arr[j] < "4"):
                    while k < length:
                        if(digit_arr[k] < "6"):
                            while l < length:
                                time = digit_arr[i]+digit_arr[j]+":"+digit_arr[k]+digit_arr[l]
                                print(time)
                                if(time != initial_seed):
                                    return time
                                l += 1
                        l = 0
                        k+=1
                k = 0
                j+=1
        j = 0
        i+=1
    return None

print(nextClosestTime("00:00"))