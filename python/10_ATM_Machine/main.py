total_amount = 0
def check_balance():
    global total_amount
    print(f"💰 Your Current Balance: ₹{total_amount}")

def deposit_money():
    global total_amount
    amount=int(input("Enter the amount for deposit "))
    if amount >0:
        total_amount = total_amount+amount
        print(f"✅ ₹{amount} deposited successfully.")
    else:
        print("Plese deposite valid amount 💵 ")

def withdraw_money():
    global total_amount
    amount=int(input("Enter the amount for withdraw "))

    if amount<total_amount:
        total_amount = total_amount - amount
        print(f"✅ ₹{amount} withdraw successfully.")
    else:
        print("Plese withdraw valid amount 💵 ")
    
def exit():
    print("System Off ❌")


while True:
    print("1. 🏦 Check Balance")
    print("2. 💵 Deposit Money")
    print("3. 💸 Withdraw Money")
    print("4. ❌ Exit")

    n=int(input("Enter the number, What Do You Want To You  "))
    if n==1:
        check_balance()
    elif n==2:
        deposit_money()
    elif n==3:
        withdraw_money()
    elif n==4:
        exit()
        break
    else:
        print("Plese Enter the valid no")