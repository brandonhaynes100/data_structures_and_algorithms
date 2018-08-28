
class AnimalShelter(Object):
    """ Holds only dog objects and cat objects.
    Operates using a First-In-First-Out approach
    """
    shelter = list()

    def enqueue(animal):
        if animal.val != 'cat' and animal.val != 'dog':
            raise TypeError
        shelter.append(animal)

    def dequeue(pref):
        animal_found = None
        stack_1 = []
        stack_2 = []
        if(pref != 'cat' and pref != 'dog'):
            raise TypeError

        for animal in shelter:
            if animal.type == pref and not animal_found:
                animal_found = animal
                break
            stack_1.push(animal)
        while shelter.next:
            stack_1.push(shelter.pop)
        while stack_1:
            stack_2.push(stack_1.pop)
        while stack_2:
            shelter.push(stack_2.pop)
            
        return animal_found


class Animal(Object):
    """ Defines animal type
    """
    def __init__(self, species):
        Node(species)


class Node(object):
    def __init__(self, val, _next=None):
        self.val = val
        self._next = _next

    def __str__(self):
        return '{val}'.format(val=self.val)

    def __repr__(self):
        return '<Node | Val: {self.val} | Next: {next}>'.format(val=self.val, next=self._next)
