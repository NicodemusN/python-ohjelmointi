# Toimii

def celsius_to_fahrenheit(c):
    f = c * 1.8 + 32
    return f

a = int(input("Anna lämpötila celcius-asteina: "))

print("Lämpötila on fahrenheiteina: ", end="")
print(celsius_to_fahrenheit(a))