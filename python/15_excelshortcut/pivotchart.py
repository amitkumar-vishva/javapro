# ------------------------------------------------------------------
#         data set or database
# ------------------------------------------------------------------

# OrderID	    Date	Sales Person	Region	Product	Category	Quantity	Unit Price	Total Sales
# 1001	    02-Jan-26	    Amit	North	Laptop	Electronics	2	55000	110000
# 1002	    03-Jan-26	    Neha	South	Mobile	Electronics	5	18000	90000
# 1003	    04-Jan-26	    Rahul	East	Chair	Furniture	10	2500	25000
# 1004	    05-Jan-26	    Amit	West	Table	Furniture	4	7000	28000
# 1005	    06-Jan-26	    Neha	North	Printer	Electronics	3	12000	36000
# 1006	    07-Jan-26	    Rahul	South	Laptop	Electronics	1	55000	55000
# 1007	    08-Jan-26	    Amit	East	Chair	Furniture	8	2500	20000
# 1008	    09-Jan-26	    Neha	West	Mobile	Electronics	4	18000	72000
# 1009	    10-Jan-26	    Rahul	North	Table	Furniture	2	7000	14000
# 1010	    11-Jan-26	    Amit	South	Printer	Electronics	5	12000	60000
# 1011	    12-Jan-26	    Neha	East	Laptop	Electronics	2	55000	110000
# 1012	    13-Jan-26	    Rahul	West	Chair	Furniture	6	2500	15000
# 1013	    14-Jan-26	    Amit	North	Mobile	Electronics	3	18000	54000
# 1014	    15-Jan-26	    Neha	South	Table	Furniture	5	7000	35000
# 1015	    16-Jan-26	    Rahul	East	Printer	Electronics	4	12000	48000
# 1016	    17-Jan-26	    Amit	West	Laptop	Electronics	1	55000	55000
# 1017	    18-Jan-26	    Neha	North	Chair	Furniture	9	2500	22500
# 1018	    19-Jan-26	    Rahul	South	Mobile	Electronics	6	18000	108000
# 1019	    20-Jan-26	    Amit	East	Table	Furniture	3	7000	21000
# 1020	    21-Jan-26	    Neha	West	Printer	Electronics	2	12000	24000

# Practice Questions (Easy → Hard)

# Level 1 (Basic Pivot Table)

#----> Region wise Total Sales निकालो।

# Row Labels	Sum of Total Sales
# East	            466000
# North	            343000
# South	            522000
# West	            159500
# Grand Total	    1490500

#----> Sales Person wise Total Sales निकालो। ok
#----> Product wise Quantity Sold निकालो। ok
#----> Category wise Total Sales निकालो। ok
#----> Region wise Order Count निकालो।  ok

# पूरे Data को Select करो।
# Insert → PivotTable पर क्लिक करो।
# New Worksheet चुनकर OK दबाओ।
# PivotTable Fields में:
# Region को Rows में Drag करो।
# Order ID को Values में Drag करो।
# अब अगर Values में Sum of Order ID आ रहा है, तो उसे बदलना होगा:
# Values वाले Sum of Order ID पर क्लिक करो।
# Value Field Settings चुनो।
# Count चुनकर OK कर दो।

# Level 2

#----> North Region में किस Product की Sales सबसे ज्यादा है? ok
#----> किस Sales Person ने सबसे ज्यादा Sales की? ok
#----> Electronics Category की Total Sales कितनी है?
#----> Furniture Category की Total Quantity कितनी है?
# Region और Category दोनों के अनुसार Sales निकालो।

# Level 3

# Month Wise Sales निकालो।
# Sales Person + Product के अनुसार Sales Report बनाओ।
# Average Sales per Order निकालो।
# Maximum Sale किस Order की है?
# Minimum Sale किस Order की है?
# Pivot Chart Practice
# इन सभी के लिए अलग-अलग Pivot Chart बनाओ।

# Column Chart → Region Wise Sales
# Pie Chart → Category Wise Sales
# Bar Chart → Sales Person Wise Sales
# Line Chart → Date Wise Sales
# Challenge (Interview Level)
# North Region में Electronics की Sales कितनी है?
# Rahul ने Furniture में कितनी Sales की?
# किस Product से सबसे ज्यादा Revenue आया?
# कौन-सा Region सबसे ज्यादा Quantity बेच रहा है?
# किस Sales Person ने Laptop सबसे ज्यादा बेचा?
