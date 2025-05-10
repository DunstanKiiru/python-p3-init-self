#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed= "Mutt" ):
        self.name = name
        self.breed= breed

sky = Dog("sky", "Golden Retriever")
print(sky.name)
print(sky.breed)