import sys

normal_list = [1, 2, 3, 4, 5]


class CustomSequence:
    """
    this is CustomSequence class
    """
    def __len__(self):
        """
        this is __len__ function
        """
        return 5

    def __getitem__(self, index):
        return "0x{}".format(index)


class FunkyBackwards:

    def __reversed__(self):
        return "BACKWARDS!"


for seq in normal_list, CustomSequence(), FunkyBackwards():
    print("\n{}: ".format(seq.__class__.__name__), end="")
    for item in reversed(seq):
        print(item, end=", ")
    print("\n")


# filename = sys.argv[0]
#
# with open(filename) as file:
#     for index, line in enumerate(file):
#         print("{0}: {1}".format(index+1, line))

print(CustomSequence.__doc__.strip())
print(CustomSequence.__len__.__doc__.strip())
print(dir(CustomSequence.__len__))


def hello(b=None):
    b = b if b else []
    b.append('a')
    print(b)


print(hello())
print(hello())
