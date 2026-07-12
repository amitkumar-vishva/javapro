# ----------------------------------------------------------------------------
#         Strings
# ----------------------------------------------------------------------------

# String :- String characters (letters, numbers, symbols, spaces) ka sequence hoti hai, jo single quotes (' ') ya double quotes (" ") ke andar likhi jati hai.

# Example :- 

# name = "hello"
# print(name)

# -------------------------------------------------------------------------
#         ord() Function
# -------------------------------------------------------------------------

# ord() kisi ek character ka Unicode number return karta hai.
# print(ord('A')) #65

# -------------------------------------------------------------------------
#         chr() Function
# -------------------------------------------------------------------------

# chr() kisi Unicode number ko uske character mein convert karta hai.

# print(chr(65))  #A

# -------------------------------------------------------------------------
#         indexing in string
# -------------------------------------------------------------------------

# ----> Positive indexing

# Character:   P    y    t    h    o    n
# Index:       0    1    2    3    4    5

# name ="python"
# print(name[0])  # p
# print(name[1])  # y
# print(name[2])  # t

# ----> Negitive indexing

# Character:   P    y    t    h    o    n
# Negative:   -6   -5   -4   -3   -2   -1

# word = "Python"
# print(word[-1]) # n

# *************Important Rule**************

# Agar index nahi mila to ye erro ayega (IndexError)

# ***********************String Immutable hoti hai**********************

# jo badal nahi sakta hai
# Tum string ke kisi character ko directly change nahi kar sakte.

# ---------------------------------------------------------------------------
#                      Type Conversion
# --------------------------------------------------------------------------

# Ek data type ko dusre data type mein badalna Type Conversion kehlata hai.

# String → Integer

# age = "20"
# age = int(age)
# print(type(age))



# ****************** There are 2 types of conversion and . Implicit Explicit ********************

# Implicit Type Conversion :- python automatically khud change kar de
# Explicit Type Conversion :- programmer khud data type change kare

# 1. Implicit Type Conversion (Automatic Conversion)

    # Jab Python khud automatically ek data type ko doosre data type mein convert karta hai,
    # use implicit type conversion kehte hain.

# example :-

# a = 10
# b = 2.5
# c = a + b
# print(c)
# print(type(c))    # 12.5
                    # <class 'float'>


# 2. Explicit Type Conversion (Manual Conversion)

    # jab programmer khud data type convert karta hai, use explicit type conversion kehte hain.    
    # Isme hum functions use karte hain:

    # int() Integer
    # float() Float
    # complex() Complex
    # str() String
    # list() List
    # tuple() Tuple
    # set() Set
    # dict() Dictionary
    # bool() Boolean


# ----------------------------------------------------------------------------------------------
#         input / Output
# ----------------------------------------------------------------------------------------------

# Note : -  Python By defalut string leta hai us ko bata na padta hai ki input kya le rahe hai

# name = input("Enter Your name : ")
# print(type(f"Welcome to {name} kumar python first program"))


# age = input("Enter Your age : ")
# print(type(f"Welcome to {age} kumar python first program"))

# age = int(input("Enter the number : "))
# print(type(age))

# or

# age = input("Enter the number : ")
# age = int(age)
# print(type(age))




