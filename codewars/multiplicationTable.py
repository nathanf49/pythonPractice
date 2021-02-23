def multiplication_table(size):
    table = []
    for multiple in range(1,size+1):
        table.append(list(range(multiple,multiple*size+1,multiple))) #range tool takes start, end, stepSize argument which make each set of multiples
    return table # good luck

"""
Your task, is to create NxN multiplication table, of size provided in parameter.

for example, when given size is 3:

multiplication_table(3), [[1,2,3],[2,4,6],[3,6,9]]
"""