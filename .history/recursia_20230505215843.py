def recursia(bar):
    inputBar = input("Enter bar")
    if recursia(bar) == inputBar[::-1]:
        print("bary polidnroma ")
recursia()