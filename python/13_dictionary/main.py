# ----------------------------------------------------------------
#     Dictionary क्या है?
# ----------------------------------------------------------------

# key-value pair
# curly braces {} ka use hota hai

# ----------------------------------------------------------------
#     Dictionary banana
# ----------------------------------------------------------------
# student = {
#     "name": "Rahul",
#     "age": 20,
#     "city": "Delhi"
# }

# ----------------------------------------------------------------
#     value access karna
# ----------------------------------------------------------------
# print(student["name"])
# print(student.get("age"))

# ----------------------------------------------------------------
#     Dictionary banana + value access karna
# ----------------------------------------------------------------
# student = {
#     "name": "Rahul",
#     "age": 20,
#     "city": "Delhi"
# }
# print(student["name"])
# print(student.get("name"))

# ----------------------------------------------------------------
#     New key-value add karna
# ----------------------------------------------------------------
# student["course"]="python"
# print(student)

# ----------------------------------------------------------------
#     value update karna
# ----------------------------------------------------------------

# student["age"]=44
# print(student)

# ----------------------------------------------------------------
#     key-value delete karna
# ----------------------------------------------------------------
# del student["age"]
# print(student)
# or
# student.pop("name")
# print(student)

# ----------------------------------------------------------------
#     Dictionary methods
# ----------------------------------------------------------------
# keys()
# values()
# items()
# get()
# update()
# pop()
# popitem()
# clear()
# copy()

# print(student.keys())
# print(student.values())
# print(student.items())

# student.update({"age":99})
# print(student)

# print(student.popitem())
# print(student) # last wala hat jayega

# याद रखने की ट्रिक
# keys() → सभी Keys
# values() → सभी Values
# items() → Key + Value
# get() → Value प्राप्त करें
# update() → जोड़ें या बदलें
# pop() → एक key हटाएँ
# popitem() → आखिरी item हटाएँ
# clear() → सब हटाएँ
# copy() → नई copy बनाएँ

# ----------------------------------------------------------------
#     using for loop
# ----------------------------------------------------------------
# student = {
#     "name": "Rahul",
#     "age": 20,
#     "city": "Delhi"
# }

# for x,y in student.items():
#     print(x, ":-" ,y)

# ----------------------------------------------------------------
#     Nested Dictionary
# ----------------------------------------------------------------

# dictionary = {
#     "key1": {
#         "subkey1": "value1",
#         "subkey2": "value2"
#     },

#     "key2": {
#         "subkey1": "value3"
#     }
# }

student = {
    1:{
        "name":"sumit",
        "age":21,
        "city": "Delhi"
    },
    2:{
        "name":"abhiram",
        "age":44,
        "city":"suman"
    }
}
print(student[1]["city"]) # first key andar jayo or age ki value print karo