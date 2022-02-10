class Directory:
    def __init__(self, name, length, parent=None):
        self.name = name
        self.parent = parent
        self.pathLength = length

def lengthLongestPath(input: str) -> int:
    max_length = 0
    current_start = 0
    current_pos = 0
    file_type = False
    prev_dir = None
    current_depth = 0
    prev_depth = 0
    prev_char_tab = False

    for char in input:
        if((char != "\n") and (char != "\t")):
            if(prev_char_tab):
                times_to_go_back = abs(current_depth - prev_depth - (0 if file_type else 1))
                while times_to_go_back > 0:
                    prev_dir = prev_dir.parent
                    times_to_go_back -= 1
                file_type = False
                prev_char_tab = False
                print("after", prev_dir)
            if(char == "."):
                file_type = True
        else:
            prev_char_tab = True
            if(char == "\n"):
                prev_depth = current_depth
                current_depth = 0
                name = input[current_start:current_pos]
                length = (prev_dir.pathLength + 1 if prev_dir !=
                          None else 0) + current_pos - current_start
                if(file_type):
                    if(length > max_length): max_length = length
                else:
                    current_dir = Directory(name, length, prev_dir)
                    prev_dir = current_dir
                current_start = current_pos + 1
            else:
                current_depth += 1
                current_start += 1
        current_pos += 1
    
    if(file_type):
        name = input[current_start:current_pos]
        # print(name)
        length = (prev_dir.pathLength + 1 if prev_dir != None else 0) + current_pos - current_start
        if(length > max_length): max_length = length

    return max_length


# print(lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
# print(lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
print(lengthLongestPath("dir\n        file.txt"))
# cur_dir = Directory("dir1", 4)
# dir_2 = Directory("dir2", 9, cur_dir)
# cur_dir.addChildren(dir_2)
# cur_dir = dir_2
# print(cur_dir.name, cur_dir.parent.name)