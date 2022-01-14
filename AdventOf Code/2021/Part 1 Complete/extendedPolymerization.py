def ExtendedPolymerization(text, rules, steps):
    """compares all pairs from text and each step to rules and inserts new chars according to rules"""
    for s in range(steps):
        changes = {}
        for i in range(len(text) - 1):
            if text[i:i+2] in rules.keys():
                if text[i:i+2] in changes.keys(): # append index to list of changes 
                    changes[text[i:i+2]].append(i+1)
                else:
                    changes[text[i:i+2]] = [i+1]  # Dictionary makes list of indecies requiring change
        
        text = MakeChanges(text, changes, rules)

    max = 0
    min = 999999
    for letter in set(text):
        if text.count(letter) > max:
            max = text.count(letter)

        elif text.count(letter) < min:
            min = text.count(letter)

    print(max-min)  # 1451 is too low

        
                    
def MakeChanges(text, changes, rules):
    """ This function takes the starting text and list of necessary changes from Extended Polymerization and returns
    the list with the changes made """

    changesAdded = []
    for c in changes:
        for i in changes[c]:
            pad = 0
            changesAdded.sort()
            for change in changesAdded:
                if i > change:
                    pad += 1
            text = text[:i + pad] + rules[c] + text[i + pad:]
            changesAdded.append(i)  # each change increases length of list

    return text
    

if __name__ == '__main__':
    file = 'test_extendedPolymerization.txt'
    steps = 10  # number of loops to make to check rules
    rules = {}  # changes to makes
    with open(file) as f:
        data = f.readlines()
    text = data[0]  # text is first line in data
    text = text[:-1]  # get rid of new line character
    for r in data[2:]:  # read rules into a dictionary
        if r[-2] == ' ':  # last line doesn't have a new line character, so we don't need to skip it
            rules[r[:2]] = r[-1]
        else:
            rules[r[:2]] = r[-2]

    ExtendedPolymerization(text,rules,steps)


"""
--- Day 14: Extended Polymerization ---
The incredible pressures at this depth are starting to put a strain on your submarine. The submarine has polymerization equipment that would produce suitable materials to reinforce the submarine, and the nearby volcanically-active caves should even have the necessary input elements in sufficient quantities.

The submarine manual contains instructions for finding the optimal polymer formula; specifically, it offers a polymer template and a list of pair insertion rules (your puzzle input). You just need to work out what polymer would result after repeating the pair insertion process a few times.

For example:

NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
The first line is the polymer template - this is the starting point of the process.

The following section defines the pair insertion rules. A rule like AB -> C means that when elements A and B are immediately adjacent, element C should be inserted between them. These insertions all happen simultaneously.

So, starting with the polymer template NNCB, the first step simultaneously considers all three pairs:

The first pair (NN) matches the rule NN -> C, so element C is inserted between the first N and the second N.
The second pair (NC) matches the rule NC -> B, so element B is inserted between the N and the C.
The third pair (CB) matches the rule CB -> H, so element H is inserted between the C and the B.
Note that these pairs overlap: the second element of one pair is the first element of the next pair. Also, because all pairs are considered simultaneously, inserted elements are not considered to be part of a pair until the next step.

After the first step of this process, the polymer becomes NCNBCHB.

Here are the results of a few steps using the above rules:

Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
This polymer grows quickly. After step 5, it has length 97; After step 10, it has length 3073. After step 10, B occurs 
1749 times, C occurs 298 times, H occurs 161 times, and N occurs 865 times; taking the quantity of the most common 
element (B, 1749) and subtracting the quantity of the least common element (H, 161) produces 1749 - 161 = 1588.

Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. 
What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?

Your puzzle answer was 2375."""


"""
--- Part Two ---
The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to run more steps of the pair 
insertion process; a total of 40 steps should do it.

In the above example, the most common element is B (occurring 2192039569602 times) and the least common element is H 
(occurring 3849876073 times); subtracting these produces 2188189693529.

Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result. 
What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?

"""