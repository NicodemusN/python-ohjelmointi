# Toimii

def count_words(sentence):
    lst = sentence.split()
    
    x = 0
    for i in range(len(lst)):
        x += 1
    
    return x

a = input("Anna lause: ")

print("Sanojen määrä lauseessa: ", end="")
print(count_words(a))