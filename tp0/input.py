import sys

def ReadInputs():
    """
    It process the file passed as parameter in the Command Line, and return a list of tuples sorted by the second element.
    """
    args = sys.argv
    if len(args) != 2:
        raise RuntimeError("You should provide a data set")
    res = []
    with open(args[1], 'r') as f:
        first = True
        for line in f:
            if first:
                first = False
                continue
            params = line.rstrip("\n").split(",")
            sI, aI = int(params[0]), int(params[1])
            res.append((sI, aI))

    resSort = sorted(res , key = lambda item: 1/item[1])
    return resSort
