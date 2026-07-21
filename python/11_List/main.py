# -----------------------------------------------------------------------------------------
#             List 
# -----------------------------------------------------------------------------------------

# ✅ List create karna
# ✅ Indexing & Slicing
# ✅ Add/Remove elements
# ✅ Loops
# ✅ List methods
# ✅ Nested Lists
# ✅ List Comprehension
# ✅ Practice questions

# Python me List ek ordered aur mutable collection hoti hai, 
# jisme multiple values store ki ja sakti hain aur duplicate values bhi allowed hoti hain.

# ---------------------------------------------------------------------------------
#                          ✅ List create karna
# ---------------------------------------------------------------------------------
# list ko square breakit ke sath me create karte hai

# fruits = ["apple", "banana", "mango"]
# numbers = [10, 20, 30]
# mixed = [1, "hello", 3.5]


# fruits = ["apple", "banana", "mango"]
# print(fruits)


# ---------------------------------------------------------------------------------
#                          ✅ Indexing & Slicing
# --------------------------------------------------------------------------------- 

                    # **************** indexing ****************
# -----> Indexing
# fruits = ["apple", "banana", "mango"]
# print(fruits[0])    #apple
# print(fruits[1])    #banana
# print(fruits[2])    #mango

# -------> Negitive indexing

# fruits = ["apple", "banana", "mango"]
# print(fruits[-1])    #mango
# print(fruits[-2])    #banana
# print(fruits[-3])    #apple

                     # **************** Slicing ****************

# fruits = ["apple", "banana", "mango"]
# print(fruits[0:2])
# print(fruits[:2])
# print(fruits[1:])

# num = [1,2,3,4,5,6,7,8,9,10]
# print(num[1:])  #[2, 3, 4, 5, 6, 7, 8, 9, 10]



# ---------------------------------------------------------------------------------
#                          ✅ Add/Remove elements
# ---------------------------------------------------------------------------------

# ---------> Add elememts

# 1. append() :-  Use: List ke end me ek item add karne ke liye.

# num = [1,2,3,4,5,6,7,8,9,10]
# num.append(100)
# print(num)


# 2. insert() :-  Use: Kisi specific position (index) par item add karne ke liye.

# num = [1,2,3,4,5,6,7,8,9,10]
# num.insert(1,100)   #index 1 par 100 ko dal do
# print(num)

# 3. extend() :-  Use: Ek list me dusri list ke sabhi items add karne ke liye.

# num1 = [1,2,3,4,5,6,7,8,9,10]
# num2 = [11,12,13]
# num1.extend(num2)
# print(num1)


# -----------> Remove elements

# 1. remove() :-  Use: List se kisi value ko remove karne ke liye.

# fruits = ["Apple", "Banana", "Mango"]
# fruits.remove("Banana")
# print(fruits)

# 2. pop() :- Use: List se index ke hisaab se item remove karne ke liye. Agar index na do, to last item remove hota hai.

# fruits = ["Apple", "Banana", "Mango"]
# fruits.pop()
# print(fruits)

# fruits = ["Apple", "Banana", "Mango"]
# fruits.pop(1)
# print(fruits)


# 3. clear()  :-  Use: List ke saare items remove karne ke liye.

# fruits = ["Apple", "Banana", "Mango"]
# fruits.clear()
# print(fruits)

# 4. del  :-  Use: List ya list ke kisi item ko delete karne ke liye.

# fruits = ["Apple", "Banana", "Mango"]
# del fruits[1]
# print(fruits)

# fruits = ["Apple", "Banana", "Mango"]
# del fruits()
# print(fruits)

# ----------->Useful List Methods

# 1. count()  :-  Use: Kisi value kitni baar aayi hai, uski ginti (count) batata hai.

# numbers = [1, 2, 2, 3, 2]
# print(numbers.count(2)) #3

# 2. index()  :-  Use: Kisi value ka pehla index (position) batata hai.

# fruits = ["Apple", "Banana", "Mango"]
# print(fruits.index("Banana"))

# 3. sort()   :-  Use: List ko ascending order me sort karta hai.

# numbers = [5, 2, 8, 1]
# numbers.sort()
# print(numbers)    #[1, 2, 5, 8]

# 4. reverse()

# 5. copy()   :-  Use: List ki copy banata hai.

# list1 = [10, 20, 30]
# list2 = list1.copy()
# print(list2)

# ---------->List Operators

# 1. + (Concatenation)    :-  Use: Do lists ko jodne (combine) ke liye.

# list1 = [1, 2]
# list2 = [3, 4]
# print(list1 + list2)

# 2. * (Repetition)   :-  Use: List ko baar-baar repeat karne ke liye.

# numbers = [1, 2]
# print(numbers * 3)

# 3. in   :-  Use: Check karta hai ki item list me hai ya nahi.

# fruits = ["Apple", "Banana", "Mango"]
# print("Banana" in fruits)

# 4. not in   Use: Check karta hai ki item list me nahi hai.

# fruits = ["Apple", "Banana", "Mango"]
# print("Orange" not in fruits)


# ------> List Functions

# len()
# max()
# min()
# sum()
# sorted()

# -------> List Comprehension (Bahut important)

# a = [i*3 for i in range(5)]
# print(a)

# ------------------------------------------------------------------------------------
#     five item ki list bano
# ------------------------------------------------------------------------------------

# item = ["apple","banana","orange","manago"]
# print(item)   #['apple', 'banana', 'orange', 'manago']

# ------------------------------------------------------------------------------------
#    list me ak new itme add karo
# ------------------------------------------------------------------------------------

# item = ["apple","banana","orange","manago"]
# item.append("hello")
# print(item)

# item = ["apple","banana","orange","manago"]
# item.insert(1,"hello")
# print(item)

# ------------------------------------------------------------------------------------
#     index 2 wale item ko print karo
# ------------------------------------------------------------------------------------
# item = ["apple","banana","orange","manago"]
# print(item[2])

# ------------------------------------------------------------------------------------
#     last wale item ko delete karo
# ------------------------------------------------------------------------------------

# item = ["apple","banana","orange","manago"]
# item.remove("manago")
# print(item)

# ------------------------------------------------------------------------------------
#     list ko reverse karo
# ------------------------------------------------------------------------------------

# item = ["apple","banana","orange","manago"]
# item.reverse()
# print(item)

# ------------------------------------------------------------------------------------
#     list ko sort karo
# ------------------------------------------------------------------------------------

# num = [9,8,7,6,5,4,3,2,1]
# num.sort()
# print(num)

# ------------------------------------------------------------------------------------
#     list ki lenght nikao
# ------------------------------------------------------------------------------------
# item = ["apple","banana","orange","manago"]
# print(len(item))

# ------------------------------------------------------------------------------------
#    check karo ki apple list me hai ya nahi
# ------------------------------------------------------------------------------------

# item = ["apple","banana","orange","manago"]
# print("apple" in item)

# if "apple" in item:
#     print(True)
# else:
#     print(False)

# ------------------------------------------------------------------------------------
#     list ke sabhi elemet ko loop se print karo
# ------------------------------------------------------------------------------------

# enumerate() :- es function ki help se ham index and value find kar sakte hai

# item = ["apple","banana","orange","manago"]
# for i in item:
#     print(i)

# item = ['apple', 'banana', 'orange', 'manago']
# for index, value in enumerate(item):
#     print(index, ":-", value) 


# ------------------------------------------------------------------------------------
#     max and min value find karo
# ------------------------------------------------------------------------------------

# num = [11,55,77,22,10,9,3,2]
# print(max(num))

