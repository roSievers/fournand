# Randomly create logic networks with predetermined value.

from random import choice
from itertools import product

class Element:
    def __init__(self, name):
        self.name = name
    def value(self, inputs):
        pass

class Nand(Element):
    def __init__(self, name, in1, in2):
        Element.__init__(self, name)
        self.in1 = in1
        self.in2 = in2
    def value(self, inputs):
        return not (self.in1.value(inputs) and self.in2.value(inputs))
    def __repr__(self):
        return f"{self.in1.name}.out -> {self.name}.in1\n{self.in2.name}.out -> {self.name}.in2,"

class Input(Element):
    def value(self, inputs):
        return inputs[self.name]


def addRandomNand(stack, name):
    in1 = choice(stack)
    in2 = choice(stack)
    stack.append(Nand(name, in1, in2))

def muxTest(in1, in2, sel):
    if sel:
        return in2
    else:
        return in1

def testNetwork(stack):
    for inputs in product([True, False], repeat=3):
        networkValue = stack[-1].value(inputs)
        targetValue = muxTest(*inputs)
        if networkValue != targetValue:
            return False

    return True

def main():
    while True:
        stack = [Input(0), Input(1), Input(2)]
        for i in range(4):
            addRandomNand(stack, f"nand {i}")

        if testNetwork(stack):
            print("Network is valid")

            for element in stack:
                print(element)

            break
        else:
            print("Network is invalid")

if __name__ == "__main__":
    main()
