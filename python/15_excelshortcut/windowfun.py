# ------------------------------------------------------------------------------
#     window function kya hai
# ------------------------------------------------------------------------------
    # jo table ki rows par calculation karta hai lekin original rows ko delete ya combine nahi karta hai
# ------> Ranking function

    # row_number()
    # rank()
    # dense_ranke()
    # percent_rank()

# ------> value/analytics

    # lead()
    # lag()
    # first_value()
    # last_value()



# ------------------------------------------------------------------------------
#     simple table
# ------------------------------------------------------------------------------

# Name	Dept	Salary
#     A	IT	     50000
#     B	IT	    60000
#     C	IT	    60000
#     D	HR	    70000
#     E	HR	    50000

# ------------------------------------------------------------------------------
#     row_number()
# ------------------------------------------------------------------------------

# Har row ko unique number deta hai.


# ROW_NUMBER() OVER(
#     PARTITION BY Dept
#     ORDER BY Salary DESC
# )

# Name	    Dept	Salary	 ROW_NUMBER
# D	        HR	    70000	    1
# E	        HR	    50000	    2
# B	        IT	    60000	    1
# C	        IT	    60000	    2
# A	        IT	    50000	    3

# ------------------------------------------------------------------------------
#    rank()
# ------------------------------------------------------------------------------

# Result:

# Name	    Salary	        RANK
# D	        70000	        1
# B	        60000	        2
# C	        60000	        2
# A	        50000	        4
# E	        50000	        4

# ------------------------------------------------------------------------------
#    dense_rank()
# ------------------------------------------------------------------------------

# Name	       Salary	    DENSE_RANK
# D	            70000	        1
# B	            60000	        2
# C	            60000	        2
# A	            50000	        3
# E	            50000	        3






































# ROW_NUMBER()
# → Har row ko unique number deta hai (duplicate value par bhi alag number)

# RANK()
# → Same value = Same rank + Next rank skip hota hai

# DENSE_RANK()
# → Same value = Same rank + Next rank skip nahi hota

# LAG()
# → Previous row ki value laata hai (peeche wali value)

# LEAD()
# → Next row ki value laata hai (aage wali value)

# FIRST_VALUE()
# → Window ki first value ko sab rows me dikhata hai

# LAST_VALUE()
# → Window ki last value ko sab rows me dikhata hai

# PERCENT_RANK()
# → Row ki ranking ko percentage (0 se 1) me batata hai

# PARTITION BY
# → Data ko groups me divide karta hai

# ORDER BY
# → Data ko kisi order me sort karta hai

# OVER()
# → Window Function ka area define karta hai
