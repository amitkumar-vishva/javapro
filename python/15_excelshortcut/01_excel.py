# ctrl +    :- Add new column, row bhi add kar sakte hai
# ctrl -    :-remove add new column, row bhi remove kar sakte hai
# ctrl + shift + right arrow or left arrow or top arrow or bottom arrow :- ye up down karne ke liye hai

# ctrl + r    :- ye right side ki row ko fill karta hai
# ctrl + d       :- ye column ko fill karta hai, in ka use remdom number fill karne ke liye hota hai,=RANDBETWEEN(bottom, top) es ka use karte hai


# Relative Reference: Copy करने पर Cell Reference बदलता है।
# Example: =A1+B1 → Copy करने पर =A2+B2

# Absolute Reference: Copy करने पर Cell Reference Fix रहता है क्योंकि उसमें $ का उपयोग किया जाता है।
# Example: =A1*$B$1 → Copy करने पर =A2*$B$1

# jab ham ko kisi specification cell ka pura data highlight karna ho to ham, conditional formating --> new role --> then selected
# es me formula (=$C2="Sales") ase lagega


# Mumbi-2021215
# Pune-454545
# Dubi-7878778
# Pakistan-363636
# agar muje es me se Mumbi nikalni hai (=LEFT(A2,FIND("-",A2,1)-1)) es formula ka use karunga,
# agar code nikalna hai to (=RIGHT(A2,LEN(A2)-FIND("-",A2))) ye find kaunga



# -------------------------------------------------------------------------------
#     Data Cleaning and Preparation (chepter - 03)
# -------------------------------------------------------------------------------
# ------ topics -------
        # Remove duplicates
        # Remove blank rows
        # Remove blank space 
        # Change Case using formula(UPPERCASE,LOWERCASE,PROPER)
        # Fix negative stock values
        # Split data


# -----------  Remove duplicates value -------------

# SHORT CUT     SELECT TABLE THEN (ALT + A + M)
# job hi duplicates value hogi bo remove ho jayegi

# DATA --> REMOVE DUPLICATE 

# -----------  Remove blank rows -------------

# ctrl + g(go to) --> spcial --> blank -->  ok

# -----------  Remove blank space -------------

# as pass ke space ko remove karna
# trim() es ki help se kisi bhi name ka as pass ka space remove kar sakte hai
# SUBSTITUTE() Use: Jab kisi word ya character ko dusre se replace karna ho.
# EXAMPLE :- WH188Q12K  -OUTPUT-> HR188Q12K     (=SUBSTITUTE(A2,"WH","HR"))
# EXAMPLE :-      987-654-3210  -OUTPUT-> 9876543210       (=SUBSTITUTE(C3,"-",""))

# Jab ham kisi col se kisi col ko banate hai tab bha par ham ko (alt+v+v) ka use karte hai


# -------------------------------------------------------------------------------
#     LOGICAL FUNCTION (chepter - 04)
# -------------------------------------------------------------------------------
# IF, NESTING IF, 
# IFS :-  एक से अधिक Conditions।
# ,AND/OR

# =IFS(
# A2>=75000,A2*20%,
# A2>=50000,A2*15%,
# A2<50000,A2*10%
# )

# -------------------------------------------------------------------------------
#               SORT AND FILTER (chepter - 05)
# -------------------------------------------------------------------------------
# FILTER LAGANE KE LIYE (ALT + A + T)

# -------------------------------------------------------------------------------
#               VLOOKUP,MATCH AND INDEX (chepter - 06)
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
#               STATISTICAL FORMULAS (chepter - 07)
# -------------------------------------------------------------------------------
# SUMIF | SUMIFS
# COUNTIF, COUNTIFS
# AVERAGEIF, AVERAGEIFS
# MAXIF, MAXIFS
# MINIF, MINIFS
