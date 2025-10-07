# Toimii

a = int(input("Anna luku: "))

def is_even(n):
    return(n % 2 == 0)

if is_even(a):
    print("Numero ", a, " on parillinen.")
else:
    print("Numero ", a, " on pariton.")