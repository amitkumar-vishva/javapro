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

# 1. SUMIF
# 📌 Definition
# SUMIF का use तब करते हैं जब हमें एक condition के आधार पर numbers को जोड़ना (Sum) हो।

# Syntax
# =SUMIF(range, criteria, sum_range)

# Example
# Sales department की total sales निकालनी है:

# =SUMIF(B2:B7,"Sales",D2:D7)


# 2. SUMIFS
# 📌 Definition
# SUMIFS का use तब करते हैं जब हमें एक से ज्यादा conditions के आधार पर numbers को जोड़ना हो।

# Syntax
# =SUMIFS(sum_range, criteria_range1, criteria1, criteria_range2, criteria2)

# Example
# Agra में Sales department की total sales:

# =SUMIFS(D2:D7,B2:B7,"Sales",C2:C7,"Agra")

# DIFF B/W SUM, SUMIF & SUMIFS
# SUM	❌ No condition	Sabhi numbers ko जोड़ता है	
# SUMIF	🟢 1 condition	Ek condition ke basis par जोड़ता है	
# SUMIFS  🟢🟢 Multiple conditions	Multiple conditions ke basis par जोड़ता है


# 3. COUNTIF
# 📌 Definition
# COUNTIF का use तब करते हैं जब हमें एक condition को पूरा करने वाली cells/entries की संख्या गिननी हो।

# Syntax
# =COUNTIF(range, criteria)

# Example
# Sales department में कितने employees हैं?

# =COUNTIF(B2:B7,"Sales")

# 4. COUNTIFS
# 📌 Definition
# COUNTIFS का use तब करते हैं जब हमें एक से ज्यादा conditions को पूरा करने वाली entries की संख्या गिननी हो।

# Syntax
# =COUNTIFS(criteria_range1,criteria1,criteria_range2,criteria2)

# Example
# Agra में Sales department के कितने employees हैं?

# =COUNTIFS(B2:B7,"Sales",C2:C7,"Agra")

# DIFF B/W COUNT, COUNTIF, COUNTIFS

# COUNT numbers को बिना किसी condition के count करता है।
# COUNTIF एक condition के आधार पर count करता है।
# COUNTIFS multiple conditions के आधार पर count करता है।

# 5. AVERAGEIF
# 📌 Definition
# AVERAGEIF का use तब करते हैं जब हमें एक condition के आधार पर numbers का average निकालना हो।

# Syntax
# =AVERAGEIF(range, criteria, average_range)

# Example
# Sales department की average sales:

# =AVERAGEIF(B2:B7,"Sales",D2:D7)


# 6. AVERAGEIFS
# 📌 Definition
# AVERAGEIFS का use तब करते हैं जब हमें एक से ज्यादा conditions के आधार पर average निकालना हो।

# Syntax
# =AVERAGEIFS(average_range, criteria_range1, criteria1, criteria_range2, criteria2)

# Example
# Agra में Sales department की average sales:

# =AVERAGEIFS(D2:D7,B2:B7,"Sales",C2:C7,"Agra")

# DIFF B/W AVG, AVGIF, AVGIFS

# AVERAGE → सबका Average
# AVERAGEIF → एक condition लगाकर Average
# AVERAGEIFS → कई conditions लगाकर Average
