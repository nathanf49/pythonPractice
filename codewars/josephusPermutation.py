def josephus(items, k):
    out = []  # list to keep nums in order
    while len(items) > 1:
        '''try:
            out.append(items[k-1]) # index is k-1 since indexing starts at 0
            items = items[k:] + items[:k-1] # adds elements from before the index taken out to the end of items
        except:'''
        index = k
        while index > len(items):
            index -= len(items)
        out.append(items[index-1])
        items = items[index:] + items[:index-1]

    if len(items) == 1: # add last element to output list
        out.append(items[0])

    return out

#test1 = josephus([1,2,3,4,5,6,7,8,9,10],2) # [2, 4, 6, 8, 10, 3, 7, 1, 9, 5])
#test2 = josephus(["C","o","d","e","W","a","r","s"],4) #['e', 's', 'W', 'o', 'C', 'd', 'r', 'a'])
#test3 = josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], 8)
# [8, 16, 24, 32, 7, 17, 26, 2, 12, 22, 33, 11, 23, 3, 15, 29, 10, 27, 9, 28, 14, 1, 21, 18, 6, 5, 13, 20, 31, 30, 19, 4, 25]