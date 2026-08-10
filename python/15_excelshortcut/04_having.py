# having ka use group by ke sath me grouping ke baad me filter karne ke liye hota hai

# ------------------------------------------------------------------------
#         HAVING
# ------------------------------------------------------------------------
# MODULE 3: HAVING – 30 SQL Practice Questions


# HAVING ka use GROUP BY ke baad filter lagane ke liye hota hai.

# Basic HAVING Questions (1–10)

#----> Un departments ko find karo jahan employees ki count 10 se zyada hai.

    # SELECT DEPARTMENT, COUNT(*) FROM EMPLOYEE GROUP BY DEPARTMENT HAVING COUNT(*)>5;

#----> Un cities ko find karo jahan employees ki count 50 se zyada hai.

    # SELECT CITY, COUNT(*) FROM EMPLOYEE GROUP BY CITY HAVING COUNT(*)>5;

#----> Un departments ko find karo jahan average salary 50000 se zyada hai.

    # SELECT DEPARTMENT, AVG(SALARY) AS AVG_SALARY FROM EMPLOYEE GROUP BY DEPARTMENT HAVING AVG(SALARY)>50000;

#----> Un cities ko find karo jahan average salary 40000 se zyada hai.

    # SELECT CITY, AVG(SALARY) AS AVG_SALARY FROM EMPLOYEE GROUP BY CITY HAVING AVG(SALARY)>40000;

# Un products ko find karo jinki total sales 1 lakh se zyada hai.
# Un categories ko find karo jinka total revenue 5 lakh se zyada hai.
# Un customers ko find karo jinhone 5 se zyada orders kiye hain.
# Un employees ko find karo jinki total sales 50000 se zyada hai.
# Un months ko find karo jahan sales 10 lakh se zyada hai.
# Un departments ko find karo jahan maximum salary 1 lakh se zyada hai.

# Intermediate HAVING Questions (11–20)

# Department wise average salary nikal kar sirf wo departments dikhao jahan average salary 70000 se zyada hai.
# City wise employee count nikalo aur sirf wo cities dikhao jahan 100 employees se zyada hain.
# Product wise sales calculate karo aur sirf top selling products dikhao.
# Category wise profit nikalo aur sirf profitable categories dikhao.
# Customer wise total purchase nikalo aur sirf high value customers dikhao.
# Salesperson wise sales nikalo aur jinki sales target se zyada hai unhe dikhao.
# Department wise average age nikalo aur sirf wo departments dikhao jahan average age 30 se zyada hai.
# Region wise revenue calculate karo aur sirf bade regions dikhao.
# Brand wise product count nikalo aur sirf wo brands dikhao jinke products 20 se zyada hain.
# Payment method wise transaction count nikalo aur sirf popular methods dikhao.

# Advanced HAVING Questions (21–30)

# Wo departments find karo jahan employees ki average salary company average salary se zyada hai.
# Wo customers find karo jinka total spending average customer spending se zyada hai.
# Wo products find karo jinka total sales amount average product sales se zyada hai.
# Wo cities find karo jahan highest number of customers hain.
# Wo categories find karo jahan total profit maximum hai.
# Wo employees find karo jinki total sales 5 lakh se zyada hai.
# Wo months find karo jahan revenue pichle month se zyada hai.
# Wo departments find karo jahan salary expense 50 lakh se zyada hai.
# Wo stores find karo jahan average order value 5000 se zyada hai.
# Ek report banao jisme sirf high-performing departments dikhein.
