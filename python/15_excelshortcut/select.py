# ----------------------------------------------------------------------
# SQL SELECT Practice Sheet (100 Questions)
# ----------------------------------------------------------------------
                        
# Employees table ki sari rows dikhao.

#------> SELECT * FROM EMPLOYEE;

# Sirf employee_name column dikhao.

#------> SELECT NAME FROM EMPLOYEE;

# employee_name aur salary dikhao.

#------> SELECT NAME,SALARY FROM EMPLOYEE;

# Department column ki unique values dikhao.
    # DISTNCT :- ES KI HELP SE HAM UNIQUE VALUE FIND KAR SAKTE HAI
#------> SELECT DISTINCT DEPARTMENT FROM EMPLOYEE;

# Top 5 rows dikhao.

# ------> SELECT * FROM EMPLOYEE LIMIT 5;

# Name aur Age dikhao.

#-------> SELECT NAME, AGE FROM EMPLOYEE;

# Employee ID aur Name dikhao.

#-------> SELECT EMPID, NAME FROM EMPLOYEE;

# Department aur Salary dikhao.

#------> SELECT DEPARTMENT, SALARY FROM EMPLOYEE;

# Hire Date dikhao.
# Gender dikhao.
# Email dikhao.
# Phone Number dikhao.
# Name aur Email dikhao.
# Name aur City dikhao.
# Name, Department aur Salary dikhao.

# -------------------------------------------------------
#       Level 2 – WHERE (21–40)
# ---------------------------------------------------------

# Salary 50000 se zyada ho.

#-----> SELECT * FROM EMPLOYEE WHERE SALARY>=50000;

# Salary 30000 se kam ho

#-----> SELECT * FROM EMPLOYEE WHERE SALARY<=30000;

# Department = IT.

#-----> SELECT * FROM EMPLOYEE WHERE DEPARTMENT = 'IT';

# City = Delhi.

#-----> SELECT * FROM EMPLOYEE WHERE CITY = 'DELHI';

# Age = 25.

#-----> SELECT * FROM EMPLOYEE WHERE AGE = 25;


# Salary >= 60000.
# Salary <= 40000.
# Employee ID = 10.
# Name = Rahul.

#----> SELECT * FROM EMPLOYEE WHERE NAME = 'RAHUL';

# Bonus > 5000.
# Department HR ho.
# City Mumbai ho.
# Experience > 5 years.
# Age < 30.
# Salary = 45000.
# Joining year 2024 ho.
# Manager ID = 5.
# Status Active ho.
# Gender Female ho.