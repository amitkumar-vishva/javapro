# SELECT-WEHERE
# GROUP BY
# HAVING
# JOIN
# WINDOW FUNCTION
# CTE

# -----------------------------------------------------------------------------
#     hamare pass me kon kon se department hai
# -----------------------------------------------------------------------------
# command :-

            # select Department from employee group by Department;


# -----------------------------------------------------------------------------
#     hame dekhna hai ki hamre kis department me kitne empoyee hai
# -----------------------------------------------------------------------------
# command :-

            # select Department, count(*) from employee group by Department;

# -----------------------------------------------------------------------------
#    hame dekhna hai ki kis department ke andar kitni salary hai(total)
# -----------------------------------------------------------------------------
# command :-

            # select Department, sum(Salary) from employee group by Department;

# -----------------------------------------------------------------------------
#     agar ham total salary ka averge dekha ho to 
# -----------------------------------------------------------------------------
# command :-

            # select Department, avg(Salary) from employee group by Department;

# -----------------------------------------------------------------------------
#     agar ham dekhna chte hai ki kis employee, department, ki salary high hai
# -----------------------------------------------------------------------------
# command :-

            # SELECT Name, Department, Salary
            # FROM Employee
            # WHERE Salary = (
            #     SELECT MAX(Salary)
            #     FROM Employee
            #     WHERE Department = 'IT'
            # );

# or

# SELECT Name, Department, Salary
# FROM Employee
# WHERE Department = 'HR'
#   AND Salary = (
#     SELECT MIN(Salary)
#     FROM Employee
#     WHERE Department = 'HR'
# );

# -----------------------------------------------------------------------------
#    agar kisi department ke all employee dekhne ho jese HR,IT etc
# -----------------------------------------------------------------------------
# command :-

            # select * from employee where Department = 'HR';

# ------------------------------------------------------------------------------
#         GROUP BY
# ------------------------------------------------------------------------------

# Basic GROUP BY Questions (1–20)


#----> Har department mein kitne employees hain?

    # SELECT DEPARTMENT, COUNT(*) FROM EMPLOYEE GROUP BY DEPARTMENT;

#----> Har city mein kitne employees hain?

    # SELECT CITY, COUNT(*) FROM EMPLOYEE GROUP BY CITY;

#----> Har department ki average salary nikalo.

    # SELECT DEPARTMENT, AVG(SALARY) FROM EMPLOYEE GROUP BY DEPARTMENT;

#----> Har department ka total salary nikalo.

    # SELECT DEPARTMENT, SUM(SALARY) FROM EMPLOYEE GROUP BY DEPARTMENT;

#----> Har department ki maximum salary nikalo.

    # SELECT * FROM EMPLOYEE AS E WHERE SALARY=(SELECT MAX(SALARY) FROM EMPLOYEE WHERE DEPARTMENT = E.DEPARTMENT);

#----> Har department ki minimum salary nikalo.

    # SELECT DEPARTMENT, MIN(SALARY) FROM EMPLOYEE GROUP BY DEPARTMENT;
    # SELECT * FROM EMPLOYEE AS E WHERE SALARY=(SELECT MIN(SALARY) FROM EMPLOYEE WHERE DEPARTMENT = E.DEPARTMENT);


#----> Har city ki average salary nikalo.

    # SELECT CITY, COUNT(*) FROM EMPLOYEE GROUP BY CITY;
    # SELECT CITY, AVG(SALARY) FROM EMPLOYEE GROUP BY CITY;

#----> Har city ka total salary expense nikalo.

    # SELECT CITY, SUM(SALARY) FROM EMPLOYEE GROUP BY CITY;

#----> Har age group mein employees ki count nikalo.

    # SELECT AGE, COUNT(*) AS TOTAL_EMPLOYEES FROM EMPLOYEE GROUP BY AGE;

# Har gender ke employees ki count nikalo.
# Har designation mein employees count karo.
# Har joining year mein kitne employees join hue?
# Har month mein kitni sales hui?
# Har product category ki total sales nikalo.
# Har product ka total quantity sold nikalo.
# Har customer ki total purchase nikalo.
# Har payment method ka usage count nikalo.
# Har order status ka count nikalo.
# Har region ki sales calculate karo.
# Har brand ke products count karo.


# Intermediate GROUP BY Questions (21–40)


# Department wise highest salary employee find karo.
# City wise highest salary find karo.
# City wise lowest salary find karo.
# Department wise average age nikalo.
# Department wise maximum experience nikalo.
# Employee wise total sales nikalo.
# Customer wise order count nikalo.
# Product wise average rating nikalo.
# Category wise average price nikalo.
# Month wise revenue nikalo.
# Year wise total sales nikalo.
# Employee wise performance calculate karo.
# Manager wise employee count nikalo.
# Location wise customer count nikalo.
# Category wise profit calculate karo.
# Department wise bonus total nikalo.
# City wise employee salary comparison karo.
# Product wise total orders nikalo.
# Customer wise average order value nikalo.
# Salesperson wise total revenue nikalo.
# Advanced GROUP BY Questions (41–50)
# Sabse zyada revenue wali category find karo.
# Sabse zyada employees wala department find karo.
# Highest average salary wala department find karo.
# Lowest performing sales region find karo.
# Most profitable product category find karo.
# Most active customer find karo.
# Highest selling product find karo.
# Highest revenue month find karo.
# Employee performance report banao.
# Monthly sales summary report banao.
























































































# Level 1: Basic Practice
# Q1. पूरे Employee table में कितने employees हैं?
# Expected columns:

# Count

# Q2. सभी employees की Total Salary निकालो।
# Q3. सभी employees की Average Salary निकालो।
# Q4. सबसे ज्यादा Salary और सबसे कम Salary निकालो।
# Level 2: GROUP BY Practice
# Q5. हर Department में कितने employees हैं?
# Output ऐसा चाहिए:

# Department	Count
# HR	?
# IT	?
# Sales	?
# Finance	?

# Q6. हर Department की Total Salary निकालो।
# Q7. हर Department की Average Salary निकालो।
# Q8. हर Department की Highest Salary निकालो।
# Q9. हर Department की Lowest Salary निकालो।
# Level 3: City Based Practice
# Q10. हर City में कितने employees हैं?
# Q11. हर City की Average Salary निकालो।
# Q12. Delhi city में कितने employees हैं?
# Q13. Noida city में सबसे ज्यादा salary किसकी है?
# Level 4: WHERE + GROUP BY
# Q14. सिर्फ HR department की Total Salary निकालो।
# Hint:

# WHERE Department = 'HR'

# Q15. सिर्फ IT department की Average Salary निकालो।
# Q16. Sales department में सबसे कम Salary किसकी है?
# Level 5: Subquery Practice
# Q17. HR department में सबसे ज्यादा salary वाले employee का नाम निकालो।
# Output:

# Name	Department	Salary
# ?	HR	?

# Q18. IT department में सबसे कम salary वाले employee का नाम निकालो।
# Q19. Finance department की Average Salary से ज्यादा salary वाले employees निकालो।
# Q20. पूरे company में सबसे ज्यादा salary वाले employee की जानकारी निकालो।
# Bonus Interview Questions 🔥
# Q21. हर Department में कितने employees की salary 30000 से ज्यादा है?
# Q22. ऐसे Department दिखाओ जिनमें 5 से ज्यादा employees हैं।
# (Hint: HAVING लगेगा)

# Q23. ऐसे Department दिखाओ जिनकी total salary 200000 से ज्यादा है।