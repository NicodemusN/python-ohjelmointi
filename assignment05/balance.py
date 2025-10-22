balance = 100
ops = ["deposit", "withdraw", "balance", "quit"]

def menu():
    print("Choose operation: ")

    for i in ops:
        print(f"{i}     ", end="")
    print()

def deposit(x):
    balance = balance + x

def withdraw(x):
    if x <= balance:
        balance = balance - x
    else:
        print("Requested amount exceeds balance!")

def main():
    while True:
        menu()
        user = input()

        if user == ops[0]:
            user_deposit = int(input("Amount to deposit: "))
            deposit(user_deposit)
        elif user == ops[1]:
            user_withdraw = int(input("Amount to withdraw: "))
            withdraw(user_withdraw)
        elif user == ops[2]:
            print(balance)
        elif user == ops[3]:
            break

# debug
# run
main()