# ---------------------------------------------------------------------------
#         Loop
# ---------------------------------------------------------------------------
# es me range() function ak kam chalta hai jese 20-1=19
# es me start ki defalut value (0) hoti hai, and step ki defalut value (1) hoti hai


# range(start, stop, step) ----> range(1,21,1)  

# There are two type loop for, while loop

# example:
# ------------------------------------------------------------------------------
#         print 1 to 20 ginti
# ------------------------------------------------------------------------------
# for i in range(1,21,1):
#     print(i)


# ------------------------------------------------------------------------------
#         print reverse 20 to 1
# ------------------------------------------------------------------------------
# for i in range(21,0,-1):
#     print(i)


# ------------------------------------------------------------------------------
#        Table
# ------------------------------------------------------------------------------

# for i in range(5,51,5):
#     print(i)


# n=int(input("Enter the number : "))
# for i in range(1,11):
#     print(n, "*", i,  "=", n*i)


# n=int(input("Enter the number : "))
# for i in range(n,(n*11),n):
#     print(i)


# ------------------------------------------------------------------------------
#        Break
# ------------------------------------------------------------------------------

# for i in range(1,21):
#     if i==15:
#         break
#     else:
#         print(i)


# ------------------------------------------------------------------------------
#        continue
# ------------------------------------------------------------------------------

# for i in range(1,21):
#     if i==15:
#         continue
#     else:
#         print(i)

# ------------------------------------------------------------------------------
#        sum of give number 
# ------------------------------------------------------------------------------

# sumNo=0
# for i in range(1,6):
#     sumNo+=i
# print(sumNo) # 15


# ------------------------------------------------------------------------------
#        factorial 
# ------------------------------------------------------------------------------

# fact=1
# for i in range(1,6):
#     fact*=i
# print(fact) # 120

# ------------------------------------------------------------------------------
#        1 to 50 tak ke sabhi even and odd number print kare
# ------------------------------------------------------------------------------

# for i in range(1,51):
#     if i%2==0:
#         print(i, end=" ")

# for i in range(1,51):
#     if i%2!=0:
#         print(i, end=" ")

# ---------------------------------------------------------------
#      1 se N tak ke sabhi no ke even ko add karo
#  ---------------------------------------------------------------
# sum=0
# num = int(input("Enter the number : "))
# for i in range(1,num+1):
#     if i%2==0:
#         sum +=i
# print(sum)

# ---------------------------------------------------------------
#      kisi bhi number ka square print karo
#  ---------------------------------------------------------------

# result = 0
# n=int(input("Enter the any number : "))
# if n>0 or n<0:
#     result = (n*n)
#     print("Square : ",result)


# ---------------------------------------------------------------
#      kisi bhi number ka cube print karo
#  ---------------------------------------------------------------

# result = 0
# n=int(input("Enter the any number : "))
# if n>0:
#     result = (n*n*n)
#     print("Cube : ",result)
# else:
#     result = (-(n*n*n))
#     print("Cube : ", result)


# ---------------------------------------------------------------
#      Even no ko count karo
#  ---------------------------------------------------------------

# count = 0
# n=int(input("Enter the any number : "))
# for i in range(1,n+1):
#     if i%2==0:
#         count+=1
# print(count)

# ---------------------------------------------------------------
#     kisi no ko reverse karo
#  ---------------------------------------------------------------

# result = 0
# rev=0
# n=int(input("Enter the any number : "))
# while n>0:
#     z = n%10
#     rev = (rev*10)+z
#     n = n//10
# print(rev)

# ---------------------------------------------------------------
#      check karo ki no palindrom hai ya nahi
#  ---------------------------------------------------------------
# result=0
# n = int(input("Enter the number : "))
# temp = n
# while temp>0:
#     z = temp%10
#     result = (result*10)+z
#     temp = temp//10

# if n==result:
#     print("Palindrom no")
# else:
#     print("Not Palindrom")

# ---------------------------------------------------------------
#     check karo ki given number prime no hai ya nahi
#  ---------------------------------------------------------------

n=int(input("Enter the number : "))
if n<=1:
    print("Plese, Enter the valid no !")
else:
    is_prime = True
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            break
    if is_prime:
        print("Prime no")
    else:
        print("Not Prime no")



    
    
