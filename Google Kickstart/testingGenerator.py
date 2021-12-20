import random

# format is:
# cases
# number of inputs
# str list of inputs
# number of inputs
# str list of inputs
# ...

def perfectSubarray():
    cases = 1000
    c = 0
    output = [str(cases) + '\n']
    while c <= cases: # number of cases
        output.append(str(random.choice(range(1,25))) + '\n') # random.choice(a) picks a random number from given list a
        a = random.sample(range(0,25), int(output[-1])) # random.sample(a,b) picks a list of length b from list a
        b = ''
        for element in a:
            b += str(element) + ' ' # makes every element a string and adds it to b in proper format
        b = b[:-1] # cuts off last space
        output.append(b + '\n')
        c += 1

    with open('TestData_PerfectSubarray.txt','w+') as file:
        for i in output:
            file.write(i)
        file.close()

def Candies():
    cases = 50000
    c = 0
    output =[str(cases) + '\n']
    while c <= cases:
        out = random.sample(range(1,100),2) # generates numbers describing array/changes
        output.append(str(out[0]) + ' ' + str(out[1]) + '\n')
        # appends design array A B where A is the length of starting array and B is the number of changes
        text = random.sample(range(2,102),out[0]) # generates starting array
        t = ''
        for item in text: # formats text into a string
            t += str(item) + ' '
        t += '\n'
        output.append(t)
        # appends starting array of length out[0]


        for x in range(out[1]): # adds update / queries
            k = random.choice(['U ','Q '])
            if k == 'U ':
                k += str(random.choice(range(1,len(text)+1))) # picks index in text
                k += ' '
                k += str(random.choice(range(1,100))) # picks replacement number
                k += '\n'

            elif k == 'Q ':
                a = random.sample(range(1,len(text)+2),2)
                a.sort() # makes sure they are in order to get a range
                k += str(a[0]) + ' ' + str(a[1]) + '\n'
            try:
                output.append(k)
            except:
                print(k)
            # appends U A B where A is a index and B is the number to update it to
            # or Q A B where A and B are indicies and the sweetness value between them should be returned
        c += 1

    with open('TestData_Candies.txt','w+') as file:
        for i in output:
            file.write(i)
        file.close()


if __name__ == '__main__':
    Candies()

