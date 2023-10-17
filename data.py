
# Library imports
import json


class Data:

    def __init__(self):
        pass

    def __getitem__(self, index):
        return 6

    def __setitem__(self, key, value):
        pass


if __name__ == "__main__":

    d = Data()

    print(d["pineapple"])
    print(d["oranges"])