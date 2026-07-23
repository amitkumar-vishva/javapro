# -----------------------------------------------------------------
#     Select query
# -----------------------------------------------------------------
# # SELECT * FROM table;
#   Puri table dekhna
#   -- Query level: Basic SELECT (poora data fetch)

# # SELECT col1, col2 FROM table;
#   Sirf specific columns dekhna
#   -- Query level: Basic SELECT (selected columns tak)

# # SELECT DISTINCT city FROM table;
#   Duplicate values hata kar unique values dekhna
#   -- Query level: SELECT + Unique filtering

# # SELECT COUNT(*) FROM table;
#   Total rows count karna
#   -- Query level: Aggregate function (row counting)

# # SELECT COUNT(DISTINCT city) FROM table;
#   Unique values count karna
#   -- Query level: Aggregate + DISTINCT

# # SELECT WHERE;
#   Condition ke hisaab se data filter karna
#   -- Query level: Row filtering (individual rows tak)

# # SELECT ORDER BY;
#   Data ko sort karna
#   -- Query level: Result ordering tak

# # SELECT LIMIT;
#   Top N rows dekhna
#   -- Query level: Output rows ko restrict karna

# # SELECT AS;
#   Column ka temporary naam dena
#   -- Query level: Column display change karna

# # SELECT IN;
#   Ek se zyada values match karna
#   -- Query level: Multiple condition filtering

# # SELECT NOT IN;
#   Kuch values ko exclude karna
#   -- Query level: Negative filtering

# # SELECT BETWEEN;
#   Range ke andar ka data lena
#   -- Query level: Range filtering

# # SELECT LIKE;
#   Pattern search karna
#   -- Query level: Text matching

# # SELECT IS NULL;
#   Null values dhoondhna
#   -- Query level: Missing data filtering

# # SELECT IS NOT NULL;
#   Non-null values dhoondhna
#   -- Query level: Existing data filtering

# # SELECT AND;
#   Multiple conditions lagana
#   -- Query level: Multiple filters combine karna

# # SELECT OR;
#   Kisi bhi condition ke match hone par data lena
#   -- Query level: Alternative conditions

# # SELECT NOT;
#   Condition ko ulta karna
#   -- Query level: Reverse filtering

# # SELECT CASE WHEN;
#   Conditional output banana
#   -- Query level: Data transformation

# # SELECT IF() (MySQL);
#   Simple conditional logic
#   -- Query level: Small condition handling

# # SELECT CONCAT();
#   Text ko jodna
#   -- Query level: String manipulation

# # SELECT UPPER();
#   Capital letters mein convert karna
#   -- Query level: Text formatting

# # SELECT LOWER();
#   Small letters mein convert karna
#   -- Query level: Text formatting

# # SELECT LENGTH();
#   Text ki length nikalna
#   -- Query level: String calculation

# # SELECT SUBSTRING();
#   Text ka hissa nikalna
#   -- Query level: String extraction

# # SELECT ROUND();
#   Decimal round karna
#   -- Query level: Numeric formatting

# # SELECT CEIL();
#   Upar ki taraf round karna
#   -- Query level: Numeric calculation

# # SELECT FLOOR();
#   Neeche ki taraf round karna
#   -- Query level: Numeric calculation

# # SELECT AVG();
#   Average nikalna
#   -- Query level: Aggregate calculation

# # SELECT SUM();
#   Total nikalna
#   -- Query level: Aggregate calculation

# # SELECT MIN();
#   Minimum value
#   -- Query level: Aggregate calculation

# # SELECT MAX();
#   Maximum value
#   -- Query level: Aggregate calculation

# # SELECT GROUP BY;
#   Same values ko group karna
#   -- Query level: Data grouping

# # SELECT HAVING;
#   Grouped data ko filter karna
#   -- Query level: Group filtering (GROUP BY ke baad)

# # SELECT INNER JOIN;
#   Dono tables ka matching data
#   -- Query level: Multiple tables se data lena

# # SELECT LEFT JOIN;
#   Left table ka saara data + matching right data
#   -- Query level: Table relationship handling

# # SELECT RIGHT JOIN;
#   Right table ka saara data + matching left data
#   -- Query level: Table relationship handling

# # SELECT CROSS JOIN;
#   Har row ko har row se combine karna
#   -- Query level: Cartesian product

# # SELECT UNION;
#   Do queries ka result combine karna
#   -- Query level: Multiple result sets merge

# # SELECT UNION ALL;
#   Combine karna duplicates ke saath
#   -- Query level: Result merge with duplicates

# # SELECT Subquery;
#   Ek query ke andar doosri query
#   -- Query level: Nested query logic

# # SELECT EXISTS;
#   Check karna ki data exist karta hai ya nahi
#   -- Query level: Existence checking

# # SELECT Window Functions;
#   Ranking, running total, partitions
#   -- Query level: Advanced analytics

# # SELECT ROW_NUMBER();
#   Har row ko unique rank dena
#   -- Query level: Row-wise ranking

# # SELECT RANK();
#   Rank dena (ties ke saath)
#   -- Query level: Ranking with gaps

# # SELECT DENSE_RANK();
#   Rank dena (without gaps)
#   -- Query level: Continuous ranking

# # SELECT LAG();
#   Previous row ki value dekhna
#   -- Query level: Previous record comparison

# # SELECT LEAD();
#   Next row ki value dekhna
#   -- Query level: Future record comparison




# ----------------------------------------------------------------------
# SQL SELECT Practice Sheet (100 Questions)
# ----------------------------------------------------------------------
# Level 1 – Basic SELECT (1–20)
                        
# Employees table ki sari rows dikhao.
# Sirf employee_name column dikhao.
# employee_name aur salary dikhao.
# Department column ki unique values dikhao.
# Top 5 rows dikhao.
# Top 10 rows dikhao.
# Salary column ka naam Employee_Salary dikhao.
# City column ka naam Location dikhao.
# Name aur Age dikhao.
# Employee ID aur Name dikhao.
# Table ke sabhi columns dikhao.
# Department aur Salary dikhao.
# Salary aur Bonus dikhao.
# Hire Date dikhao.
# Gender dikhao.
# Email dikhao.
# Phone Number dikhao.
# Name aur Email dikhao.
# Name aur City dikhao.
# Name, Department aur Salary dikhao.

# Level 2 – WHERE (21–40)

# Salary 50000 se zyada ho.
# Salary 30000 se kam ho.
# Department = IT.
# City = Delhi.
# Age = 25.
# Salary >= 60000.
# Salary <= 40000.
# Employee ID = 10.
# Name = Rahul.
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
# Project = AI ho.

# Level 3 – AND / OR / NOT (41–55)

# IT department aur salary 50000 se zyada.
# Delhi aur age 30.
# HR ya Finance.
# Salary >50000 ya Bonus >10000.
# NOT IT department.
# NOT Delhi city.
# Female aur Delhi.
# Male ya HR.
# Salary >40000 aur Experience >3.
# Bonus >5000 aur Department Sales.
# Salary <30000 ya City Jaipur.
# Active aur Salary >60000.
# Age 25 aur Gender Male.
# NOT HR aur Salary >50000.
# Delhi ya Mumbai.

# Level 4 – ORDER BY (56–65)

# Salary ascending.
# Salary descending.
# Name A–Z.
# Name Z–A.
# Age ascending.
# Age descending.
# Joining Date latest first.
# Bonus highest first.
# Department alphabetical.
# City alphabetical.

# Level 5 – DISTINCT (66–70)

# Unique departments.
# Unique cities.
# Unique designations.
# Unique genders.
# Unique managers.

# Level 6 – LIKE (71–80)

# Name A se start ho.
# Name R se start ho.
# Name a par end ho.
# Name me "an" ho.
# Email gmail ho.
# Phone 98 se start ho.
# City me "pur" ho.
# Name ki second letter a ho.
# Name 5 letters ka ho.
# Email company.com par end ho.
# Level 7 – IN / BETWEEN (81–90)
# Department IT, HR, Finance.
# City Delhi ya Noida.
# Salary 30000–50000.
# Age 20–30.
# Bonus 5000–10000.
# Department NOT IN Sales.
# Salary NOT BETWEEN 20000–40000.
# City IN Jaipur, Agra.
# Experience 2–5 years.
# Employee ID 1–20.

# Level 8 – NULL (91–95)

# Email NULL ho.
# Phone NULL ho.
# Manager NULL ho.
# Bonus NULL na ho.
# Address NULL na ho.
# Level 9 – Functions (96–100)
# Total employees count karo.
# Average salary nikalo.
# Highest salary dikhao.
# Lowest salary dikhao.
# Total salary dikhao.















# ✅ GROUP BY → 50 Questions
# ✅ HAVING → 30 Questions
# ✅ JOINS → 100 Questions
# ✅ Subqueries → 50 Questions
# ✅ Window Functions → 100 Questions


# Basic GROUP BY Questions (1–20)
# Har department mein kitne employees hain?
# Har city mein kitne employees hain?
# Har department ki average salary nikalo.
# Har department ka total salary expense nikalo.
# Har department ki maximum salary nikalo.
# Har department ki minimum salary nikalo.
# Har city ki average salary nikalo.
# Har city ka total salary expense nikalo.
# Har age group mein employees ki count nikalo.
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














# MODULE 3: HAVING – 30 SQL Practice Questions


# HAVING ka use GROUP BY ke baad filter lagane ke liye hota hai.
# Assume tables:

# employees
# emp_id	name	department	city	salary

# sales
# sale_id	product	category	customer_id	amount

# Basic HAVING Questions (1–10)


# Un departments ko find karo jahan employees ki count 10 se zyada hai.
# Un cities ko find karo jahan employees ki count 50 se zyada hai.
# Un departments ko find karo jahan average salary 50000 se zyada hai.
# Un cities ko find karo jahan average salary 40000 se zyada hai.
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












# INNER JOIN Questions (1–25)
# INNER JOIN = Dono tables mein matching data dikhana

# Employees aur departments ko join karke employee name aur department name dikhao.
# Employee name aur department ID dikhao.
# Har employee ka department find karo.
# Customer aur order details combine karo.
# Customer name aur order amount dikhao.
# Product aur sales table ko join karo.
# Employee aur salary table join karo.
# Employee name aur salary amount dikhao.
# Customer name aur order date dikhao.
# Department wise employee details dikhao.
# Employee aur manager details join karo.
# Student aur course details combine karo.
# Employee name aur project name dikhao.
# Customer aur payment details dikhao.
# Order ID ke saath customer name dikhao.
# Product name aur category name dikhao.
# Salesperson aur sales details join karo.
# Employee aur attendance details join karo.
# Customer aur address details combine karo.
# Employee aur location details dikhao.
# Orders aur products ko join karo.
# Employee aur bonus details dikhao.
# Department aur location details combine karo.
# Customer aur feedback details join karo.
# Invoice aur customer information combine karo.
# LEFT JOIN Questions (26–50)
# LEFT JOIN = Left table ka pura data + matching right data

# Saare employees dikhao, chahe department assign ho ya nahi.
# Saare customers dikhao jinhone order kiya ya nahi.
# Wo customers find karo jinhone kabhi order nahi kiya.
# Wo employees find karo jinka department missing hai.
# Saare products dikhao chahe sale hui ho ya nahi.
# Saare departments dikhao chahe employee ho ya nahi.
# Saare students dikhao chahe course assigned ho ya nahi.
# Saare suppliers dikhao chahe unke orders ho ya nahi.
# Saare customers ke saath unki total orders information dikhao.
# Saare employees ke saath project details dikhao.
# Saare products ke saath sales details dikhao.
# Saare departments ke employee count dikhao.
# Saare cities ke customers dikhao.
# Saare managers ke under employees dikhao.
# Saare orders ke saath customer information dikhao.
# Saare employees ki salary details dikhao.
# Saare customers ka payment status dikhao.
# Saare products ka inventory status dikhao.
# Saare categories ke products dikhao.
# Saare stores ka sales data dikhao.
# Saare employees ka attendance record dikhao.
# Saare users ka login data dikhao.
# Saare departments ka average salary dikhao.
# Saare customers ka purchase history dikhao.
# Saare vendors ka transaction data dikhao.
# RIGHT JOIN Questions (51–60)
# Saare departments dikhao aur unke employees.
# Saare products dikhao aur unki sales.
# Saare categories dikhao aur products.
# Saare customers dikhao aur orders.
# Saare projects dikhao aur employees.
# Saare managers dikhao aur team members.
# Saare locations dikhao aur employees.
# Saare suppliers dikhao aur products.
# Saare courses dikhao aur students.
# Saare payment methods dikhao aur transactions.
# SELF JOIN Questions (61–70)
# SELF JOIN = Jab ek hi table ko khud se join karte hain.
# Example: Employee aur uska Manager same employees table mein ho.

# Employee name aur uske manager ka naam dikhao.
# Aise employees find karo jinka manager same department mein hai.
# Har employee ke saath uske senior employee ki details dikhao.
# Employee hierarchy report banao.
# Same salary wale employees find karo.
# Same department mein kaam karne wale employees ki pairs dikhao.
# Aise employees find karo jinki salary kisi aur employee ke barabar hai.
# Employee aur reporting manager relationship dikhao.
# Har manager ke under kitne employees hain find karo.
# Employee hierarchy ka complete structure banao.
# CROSS JOIN Questions (71–80)
# CROSS JOIN = Har row ko dusri table ki har row ke saath combine karta hai.

# Saare products aur saare colors ka combination banao.
# Saare employees aur saare departments ka combination dikhao.
# Saare months aur saare products ka sales planning table banao.
# Saare cities aur saare products ka combination banao.
# Saare customers aur available offers combine karo.
# Saare employees aur available shifts combine karo.
# Saare courses aur batches ka combination banao.
# Saare stores aur products ka combination banao.
# Saare dates aur products ka calendar banao.
# Saare departments aur locations ka possible combination banao.
# Multiple Table JOIN Questions (81–90)
# Multiple JOIN = 3 ya zyada tables ko connect karna.

# Customer + Orders + Products ki complete sales report banao.
# Employee + Department + Salary report banao.
# Product + Category + Sales report banao.
# Customer + Order + Payment details dikhao.
# Employee + Department + Location details dikhao.
# Salesperson + Product + Revenue report banao.
# Customer + Address + Order history dikhao.
# Employee + Project + Manager report banao.
# Product + Inventory + Supplier report banao.
# Department + Employee + Performance report banao.
# Real Company Interview JOIN Questions (91–100)
# Un customers ko find karo jinhone kabhi order nahi kiya.
# Un products ko find karo jo kabhi sell nahi hue.
# Har customer ka total purchase amount nikalo.
# Har employee ka department aur average department salary dikhao.
# Top 5 customers by total spending find karo.
# Har department mein highest salary employee find karo.
# Monthly sales report banao customer details ke saath.
# Aise employees find karo jinka salary record missing hai.
# Customer lifetime value report banao.
# Complete company dashboard ke liye employee, sales aur department data combine karo.







# Basic Subquery Questions (1–15)
# Company ki average salary se zyada salary wale employees find karo.
# Sabse zyada salary wale employee ka naam find karo.
# Sabse kam salary wale employee ka naam find karo.
# Second highest salary find karo.
# Average salary se kam salary wale employees dikhao.
# IT department ke employees ki salary compare karo.
# Highest salary wale department ko find karo.
# Highest selling product find karo.
# Average sales se zyada sales wale products find karo.
# Maximum order amount wala customer find karo.
# Minimum order amount wala customer find karo.
# Total sales average se zyada wale customers find karo.
# Highest revenue category find karo.
# Average age se zyada age wale employees find karo.
# Company ke highest paid employees find karo.
# Intermediate Subquery Questions (16–35)
# Har department ka highest salary employee find karo.
# Har department ki average salary se zyada salary wale employees find karo.
# Un employees ko find karo jo company ke average experience se zyada experience rakhte hain.
# Highest salary department ke saare employees dikhao.
# Lowest salary department ke saare employees dikhao.
# Aise customers find karo jinka purchase average customer purchase se zyada hai.
# Aise products find karo jinki sales average product sales se zyada hai.
# Second highest sales amount find karo.
# Third highest salary find karo.
# Top 5 highest salary employees find karo using subquery.
# Aise departments find karo jahan employee count average department count se zyada hai.
# Highest revenue month find karo.
# Aise customers find karo jinhone sabse zyada orders kiye.
# Aise employees find karo jinki salary maximum salary ke 80% se zyada hai.
# Highest performing salesperson find karo.
# Aise products find karo jo average price se mehange hain.
# Aise cities find karo jahan employee count average city count se zyada hai.
# Highest profit category find karo.
# Average order value se zyada orders find karo.
# Aise employees find karo jinka salary apne department average se zyada hai.
# EXISTS / NOT EXISTS Questions (36–45)
# EXISTS = Check karta hai data exist karta hai ya nahi.

# Aise customers find karo jinhone kam se kam ek order kiya hai.
# Aise customers find karo jinhone kabhi order nahi kiya.
# Aise products find karo jinki sales available hai.
# Aise products find karo jo kabhi sell nahi hue.
# Aise employees find karo jinka attendance record hai.
# Aise employees find karo jinka project assigned nahi hai.
# Aise departments find karo jahan employees available hain.
# Aise departments find karo jahan koi employee nahi hai.
# Aise customers find karo jinka payment record hai.
# Aise suppliers find karo jinhone delivery ki hai.
# Advanced Subquery Questions (46–50)
# Department wise second highest salary find karo.
# Har category ka highest selling product find karo.
# Har city ka highest salary employee find karo.
# Customer ke first aur last order ka comparison karo.
# Ek complete employee performance report banao using subqueries.














# MODULE 6: WINDOW FUNCTIONS – 100 SQL Practice Questions
# Window Functions = Data ko group kiye bina usi table ke andar ranking, comparison aur calculations karna.

# Common Window Functions:

# ROW_NUMBER() → Har row ko unique number dena
# RANK() → Ranking dena (same value par same rank)
# DENSE_RANK() → Ranking dena (gap ke bina)
# PARTITION BY → Group banana bina rows ko hide kiye
# LAG() → Pichli row ki value dekhna
# LEAD() → Agli row ki value dekhna
# Running Total → Dheere-dheere total calculate karna
# Assume tables:

# employees
# emp_id	name	department	salary

# sales
# sale_id	product	category	amount	sale_date

# ROW_NUMBER() Questions (1–20)
# Sabhi employees ko salary ke basis par row number do.
# Department ke andar employees ko salary ke basis par row number do.
# Har department ka highest salary employee find karo.
# Har department ka top 3 salary employee find karo.
# Sales transactions ko date ke according number do.
# Har customer ke orders ko order date ke according number do.
# Har category ke products ko ranking number do.
# Employees ko joining date ke according number do.
# Har city ke customers ko number assign karo.
# Latest order per customer find karo.
# First order per customer find karo.
# Duplicate records identify karo.
# Duplicate employees find karo.
# Har department ka first employee find karo.
# Har department ka last employee find karo.
# Monthly sales ko sequence number do.
# Products ko sales amount ke basis par number do.
# Customer transactions ko sequence mein arrange karo.
# Employee history report banao.
# Top performing employees identify karo.
# RANK() Questions (21–35)
# Employees ko salary ranking do.
# Department wise salary ranking do.
# Salesperson ko sales ke basis par rank karo.
# Products ko revenue ke basis par rank karo.
# Customers ko spending ke basis par rank karo.
# Highest selling product rank karo.
# Highest paid employee rank karo.
# Department mein top salary employees find karo.
# Cities ko revenue ke basis par rank karo.
# Categories ko profit ke basis par rank karo.
# Monthly sales ranking banao.
# Yearly revenue ranking banao.
# Employee performance ranking banao.
# Customer value ranking banao.
# Store performance ranking banao.
# DENSE_RANK() Questions (36–50)
# Employees ko salary ke basis par dense rank do.
# Same salary wale employees ko same rank do.
# Third highest salary find karo.
# Fifth highest salary find karo.
# Department wise third highest salary find karo.
# Top 3 products by revenue find karo.
# Top 5 customers by purchase find karo.
# Top performing departments find karo.
# Highest revenue months find karo.
# Salary bands create karo.
# Product category ranking banao.
# Sales region ranking banao.
# Employee growth ranking banao.
# Customer loyalty ranking banao.
# Business performance ranking banao.
# PARTITION BY Questions (51–65)
# Department wise salary rank banao.
# City wise employee ranking banao.
# Category wise product ranking banao.
# Customer wise order ranking banao.
# Region wise sales ranking banao.
# Har department ka average salary dikhao.
# Har department ke employee ke saath department average salary dikhao.
# Har category ke saath category total sales dikhao.
# Har customer ke saath total purchase dikhao.
# Har month ke saath yearly sales total dikhao.
# Department salary comparison report banao.
# Employee vs department average comparison karo.
# Product vs category sales comparison karo.
# Customer vs city average spending comparison karo.
# Region performance report banao.
# LAG() Questions (66–75)
# Employee ki previous salary dikhao.
# Monthly sales ko previous month se compare karo.
# Customer ka previous order amount dikhao.
# Product price change identify karo.
# Salary increment calculate karo.
# Previous year's revenue compare karo.
# Previous transaction amount dikhao.
# Employee promotion analysis karo.
# Monthly growth percentage calculate karo.
# Sales decline identify karo.
# LEAD() Questions (76–85)
# Employee ki next salary dikhao.
# Customer ka next order date dikhao.
# Next month sales compare karo.
# Product ka next price dikhao.
# Future sales prediction report banao.
# Next transaction amount dikhao.
# Employee career progression analyze karo.
# Customer buying pattern analyze karo.
# Next purchase gap calculate karo.
# Future revenue trend analyze karo.
# Running Total / Moving Average Questions (86–100)
# Daily running sales total nikalo.
# Monthly running revenue nikalo.
# Customer lifetime spending calculate karo.
# Employee cumulative performance calculate karo.
# Product cumulative sales calculate karo.
# 7 days moving average sales nikalo.
# Monthly average sales trend nikalo.
# Running customer count calculate karo.
# Running profit calculate karo.
# Year-to-date sales nikalo.
# Quarter-wise running revenue nikalo.
# Sales growth percentage calculate karo.
# Employee yearly performance trend banao.
# Complete sales analytics report banao.
# Complete company dashboard ke liye window functions use karo.




