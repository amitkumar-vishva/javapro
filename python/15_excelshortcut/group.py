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



# ------- PRACTICS QUESTION -----------
# -------------------------------------------------------------------------------
# Q1. पूरे Employee table में कितने employees हैं?
# -------------------------------------------------------------------------------
    # select count(*) from employee;

# -------------------------------------------------------------------------------
# Q2. सभी employees की Total Salary निकालो।
# -------------------------------------------------------------------------------






















































































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