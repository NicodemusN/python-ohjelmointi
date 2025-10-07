# Toimii
# Voisi tehdä ehkä tiiviimmin? Tämä nyt tällainen "rautalankamalli"

def add(a, b):
    sum = a + b
    print(sum)

def subtract(a, b):
    sub = a - b
    print(sub)

def multiply(a, b):
    mult = a * b
    print(mult)

def divide(a, b):
    div = a / b
    print(div)

n1 = int(input("Anna luku 1: "))
n2 = int(input("Anna luku 2: "))
op = input("Anna laskutoiminto +, -, * tai /: ")

match op:
    case "+":
        print("Summa on ", end="")
        add(n1, n2)
    case "-":
        print("Erotus on ", end="")
        subtract(n1, n2)
    case "*":
        print("Tulo on ", end="")
        multiply(n1, n2)
    case "/":
        print("Osamäärä on ", end="")
        divide(n1, n2)

