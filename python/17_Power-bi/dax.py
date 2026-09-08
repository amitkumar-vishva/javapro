# -----------------------------------------------------------------------------
#           DAX (Data Analysis Expressions) 
# -----------------------------------------------------------------------------
# DAX power bi ki formula language hai, jiski help se ham data par calculations our analysis karte hai
# jese : - total sale, profit, percentage, year-over-year growth etc.

# -----------------------------------------------------------------------------
#           SUM FORMULA 
# -----------------------------------------------------------------------------
# SUM kya karta hai?
# SUM ka use kisi column ke saare numbers ko add karne ke liye hota hai.

# Syntax:- SUM(TableName[ColumnName])
# Example:- Total Sales = SUM(Sales[Amount])

# “SUM ek aggregation function hai jo kisi numeric column ki values ka total calculate karta hai.”


#Note :-  es me ham ko measure banane padte hai

# 1. Implicit Measure
# Jab Power BI automatically aggregation kar deta hai.

# 2. Explicit Measure
# Jab hum khud DAX formula likhkar measure banate hain.
# Total Sales = SUM(Sales[Amount])



# -----------------------------------------------------------------------------
#           Calculated Column
# -----------------------------------------------------------------------------
# Calculated Column kya hota hai?
# Calculated Column ek naya column hota hai jo hum DAX formula se create karte hain.

# Humein Profit ka column banana hai:
# Profit = Sales[Sales] - Sales[Cost]

# Ab Power BI har row ke liye Profit calculate karega.
# A → 1000 - 700 = 300
# B → 1500 - 900 = 600
# Sabse important point 
# Calculated Column = Row by Row calculation

# Aur iska result table ke andar ek actual column ke form mein store hota hai

# diff b/w calculated column and measure column
# Calculated Column → har row ke liye calculation karna hai
# Measure → total/summary ya dynamic calculation nikalna hai

# Note :-
# Row-wise calculation → Calculated Column ✅
# Total/Summary calculation → Measure ✅

# Example:
# Row-wise:
# Sales + Tax → Calculated Column

# Summary:
# Total Sales, Average Sales, Profit % → Measure

# -----------------------------------------------------------------------------
#          ✅ SUMX
# -----------------------------------------------------------------------------
# SUMX kya karta hai?
# SUMX = har row par calculation karta hai, phir sabka total karta hai.

# Maan lo:

# Product	Qty	    Price
# A	        2	    100
# B	        3	    200
# C	        4	    50

# Tumhe Qty × Price karke total chahiye.

# Total Amount = SUMX(
#     SalesData,
#     SalesData[Qty] * SalesData[Price]
# )

# SUMX kya karega:

# A → 2 × 100 = 200
# B → 3 × 200 = 600
# C → 4 × 50 = 200
# Phir:

# 200 + 600 + 200 = 1000 ✅

# Note :- Diff b/w sum and sumx
# SUM
# SUM sirf ek column ki values ko add karta hai.

# SUMX
# SUMX pehle har row par calculation karta hai, phir us calculation ka total karta hai.

# -----------------------------------------------------------------------------
#           COUNT
# -----------------------------------------------------------------------------
# COUNT kya karta hai?
# COUNT kisi column mein kitni numeric (number) values hain, unko count karta hai.

# Count Sales = COUNT(SalesData[Sales])

# -----------------------------------------------------------------------------
#           COUNTA 
# -----------------------------------------------------------------------------
# COUNTA kya karta hai?
# COUNTA column mein jitni non-empty values hain, unko count karta hai.

# Matlab number + text dono count karega.

# Total Customers = COUNTA(SalesData[Customer])

# COUNT vs COUNTA
# COUNT → Sirf numbers count karta hai.

# COUNTA → Number + Text dono count karta hai, bas blank nahi hona chahiye.

# -----------------------------------------------------------------------------
#           COUNTBLANK 
# -----------------------------------------------------------------------------
# COUNTBLANK kya karta hai?
# COUNTBLANK kisi column mein kitni blank/empty values hain, unko count karta hai.

# Blank Customers = COUNTBLANK(SalesData[Customer])

# -----------------------------------------------------------------------------
#           SWITCH  
# -----------------------------------------------------------------------------
# SWITCH(
#     expression,
#     value1, result1,
#     value2, result2,
#     ...
#     else_result
# )

# Example:-
# Grade =
# SWITCH(
#     TRUE(),
#     [Marks] >= 90, "A",
#     [Marks] >= 75, "B",
#     [Marks] >= 50, "C",
#     "Fail"
# )

# -----------------------------------------------------------------------------
#           DAX (Data Analysis Expressions) 
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#           DAX (Data Analysis Expressions) 
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#           DAX (Data Analysis Expressions) 
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#           DAX (Data Analysis Expressions) 
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#           DAX (Data Analysis Expressions) 
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#           DAX (Data Analysis Expressions) 
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#           DAX (Data Analysis Expressions) 
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#           DAX (Data Analysis Expressions) 
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#           DAX (Data Analysis Expressions) 
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#           DAX (Data Analysis Expressions) 
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#           DAX (Data Analysis Expressions) 
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#           DAX (Data Analysis Expressions) 
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#           DAX (Data Analysis Expressions) 
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#           DAX (Data Analysis Expressions) 
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#           DAX (Data Analysis Expressions) 
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
#           DAX (Data Analysis Expressions) 
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#           DAX (Data Analysis Expressions) 
# -----------------------------------------------------------------------------
# =IF(ISNUMBER(D2),D2,IF(ISNUMBER(SEARCH("/",D2)),DATE(RIGHT(D2,4),LEFT(D2,FIND("/",D2)-1),MID(D2,FIND("/",D2)+1,FIND("/",D2,FIND("/",D2)+1)-FIND("/",D2)-1)),DATE(RIGHT(D2,4),MID(D2,FIND("-",D2)+1,FIND("-",D2,FIND("-",D2)+1)-FIND("-",D2)-1),LEFT(D2,FIND("-",D2)-1))))


# -----------------------------------------------------------------------------
#           DAX (Data Analysis Expressions) 
# -----------------------------------------------------------------------------
