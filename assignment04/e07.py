# Toimii

def print_table(n):
    for i in range(10):
        x = (i+1) * n
        print(f"{i+1} x {n} = {x}") # jussin pyynnöstä formatoitu
                                    # periaatteessa turhan monimutkainen

a = int(input("Anna luku: "))
print_table(a)