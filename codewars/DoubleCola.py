def who_is_next(names, r):
    multiple = 1
    numPeople = len(names)
    while r >= numPeople * multiple: # get down to the last set of people and figure out how many of each there are in that set
        r -= numPeople * multiple
        multiple *= 2

    for index in range(numPeople):
        if r in range(index*multiple,((index+1)*multiple)+1): # may have to add/subtract 1 from start/end index?
            return names[index]
    '''
        
    #maxMultiple = multiple
    while multiple > 1: # subtract all people from r who came before last set added to line
        r -= multiple-1 * numPeople
        multiple /= 2

    index = r/maxMultiple#reduce and round the index of the person in the last set to the original people
    if int(index) == index:
        return names[int(index)-1] # have to subtract 1 for indexing
    else:
        return names[int(index)] # don't subtract since we need to round up
    '''
names = ['Sheldon','Leonard','Penny','Rajesh','Howard']
