def is_merge(s, part1, part2):
    for char in s:
        try: # check if char is the start of part 1
            char == part1[0]
            part1 = part1[1:]
        except: # if part 1 has an index error or loop broke, check if char is the start of part 2
            try:
                if char == part2[0]:
                    part2 = part2[1:]
                else:
                    ValueError
            except:
                return False
    return True


test1 = is_merge('codewars', 'code', 'wars') # True
test2 = is_merge('codewars', 'cdw', 'oears') # True
test3 = is_merge('codewars', 'cod', 'wars') # False