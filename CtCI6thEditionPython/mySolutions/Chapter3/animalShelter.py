"""
An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat.You may use the built-in L i n k e d L i s t data structure.
"""
from queueClass import queue
from stack import stack


class animalQueue(queue):
    def enqueue(self, animal):
        if type(animal) is dog or type(animal) is cat:
            self.add(animal)
        else:
            raise TypeError("Please only enqueue dogs or cats")

    def dequeueAny(self):
        return self.pull()

    def dequeueDog(self):
        catStack = stack()
        try:
            while type(self.peek()) is not dog and len(self.values) > 0:  # adds cats to a stack until dog is found
                catStack.push(self.pull())
        except:
            while catStack.isEmpty() is False:  # adds cats back to the queue
                self.add(catStack.pop())
            raise Exception("No dogs available")
        adopt = self.pull()  # saves dog
        while catStack.isEmpty() is False:  # adds cats back to the queue
            self.add(catStack.pop())
        return adopt

    def dequeueCat(self):
        dogStack = stack()
        try:
            while type(self.peek()) is not cat and len(self.values) > 0:  # adds cats to a stack until dog is found
                dogStack.push(self.pull())
        except:
            while dogStack.isEmpty() is False:  # adds dogs back to the queue
                self.add(dogStack.pop())
            raise Exception("No cats available")
        adopt = self.pull()  # saves cat
        while dogStack.isEmpty() is False:  # adds dogs back to the queue
            self.add(dogStack.pop())
        return adopt


class dog:
    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        return self.name


class cat:
    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        return self.name


fido = dog()
kirk = dog()
smokey = dog()
whiteClaw = cat()
blackMexican = cat()
tiger = cat()


def main():
    animalShelter = animalQueue()
    animalShelter.enqueue(smokey)
    animalShelter.enqueue(whiteClaw)
    animalShelter.enqueue(kirk)
    animalShelter.enqueue(blackMexican)
    animalShelter.enqueue(fido)
    return animalShelter

if __name__ == "__main__":
    animalShelter = main()