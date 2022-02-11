def kEmptySlots(bulbs: list[int], k: int) -> int:
    min_day = -1
    total = len(bulbs)
    bulbs_order = [False] * total
    current_index = 1
    bulbs_order[bulbs[0]-1] = True
    while(current_index < total):
        bulb = bulbs[current_index]
        bulbs_order[bulb - 1] = True
        _left = bulb - k - 2
        _right = bulb + k
        if(_left >= 0 and bulbs_order[_left]):
            res = True
            for tmp in range(_left+1, bulb - 1, 1):
                if(bulbs_order[tmp]):
                    res = False
                    break
            if(res):
                return current_index + 1      
        if(_right < total and bulbs_order[_right]):
            res = True
            for tmp in range(bulb, _right, 1):
                if(bulbs_order[tmp]):
                    res = False
                    break
            if(res):
                return current_index + 1
        current_index += 1
    

    return min_day

print(kEmptySlots([1,2,3], 1))