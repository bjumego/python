A = int (input("A:"))
B = int (input("B:"))
if A<B:
    for A in range(A,B+1):
        print(A)
else:
    for A in range(A,B-1,-1):
        print(A)       
        