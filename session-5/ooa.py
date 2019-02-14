# Trying object orientated approach

# DEFINE A CLASS (allows objects later)
class Seq:
    """
    Defining a class for representing sequences.
    """

    def __init__(self, str_bases):
        print('New sequence created!')

        # STORE ATTRIBUTES INSIDE CLASSES (data)
        self.str_bases = str_bases

    def len(self):
        return len(self.str_bases)


# DEFINE INHERITANCE (derive classes, reuse methods and add new ones)
class Gene(Seq):
    """
    This class is derived from the Seq Class.
    All the objects of class Gene will inheritate
    the methods from the Seq Class.
    """
    pass


# --Main program

# REMEMBER!
# Step over: skips classes, definitions and everything, and just executes the program step by step.
# Step into: runs every single line, step by step.

# ACCESS CLASSES -> CREATE OBJECTS
s1 = Gene('AGTACACTGGT')
s2 = Seq('CGTAAC')

# ACCESS ATTRIBUTES
str1 = s1.str_bases
str2 = s2.str_bases

# ACCESS METHODS
l1 = s1.len()
l2 = s2.len()

# TAKE CARE!
# Attributes: store data, DO NOT have parenthesis.
# Methods: store functions, have parenthesis.

print('\nSequence 1: {}'.format(str1))
print('-Length: {}'.format(l1))

print('\nSequence 2: {}'.format(str2))
print('-Length: {}'.format(l2))



print('\nTesting')
