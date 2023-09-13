
import input

def main():
    params = input.ReadInputs()
    total, longest, actual = 0, 0, 0
    for t in params:
        total += t[0]
        actual = total + t[1]
        if actual > longest:
            longest = actual
    print("It took: " , longest , "hs")

main()
