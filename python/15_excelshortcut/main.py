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
#     Data Cleaning and Preparation
# -------------------------------------------------------------------------------

        # ****************** Remove Blank Rows ******************

# ctrl + G = GOTO --> special --> Blank --> ok --> ctrl + (-) 
# trim() es ki help se kisi bhi name ka as pass ka space remove kar sakte hai

# -------------------------------------------------------------------------------
#     Data validatation
# -------------------------------------------------------------------------------

# data --> data validation -->

# -------------------------------------------------------------------------------
#    logical function
# -------------------------------------------------------------------------------
# if, Nesting if, IFS, AND/OR
