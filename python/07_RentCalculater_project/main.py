# Room rent
# Bijli bill
# Pani will
# Food bill


total_rent=0
divided = 0
room = int(input("Enter The Room Rent : "))
bijli = int(input("Enter The Bijli Bill : "))
pani = int(input("Enter The Pani Bill : "))
food = int(input("Enter The Food Bill : "))
boyes = int(input("Enter the, how many boyes shere this room : "))

total_rent = room+bijli+pani+food+boyes
divided = total_rent/boyes; 

print(f"Total Amount {total_rent} this, and each boyes pay {round(divided,2)} amount")


