# ------------------------------------------------------------------------------
#         JOIN
# ------------------------------------------------------------------------------
#----> 1. Ye kya hai?
# JOIN = 2 ya zyada tables ka jodta hai

#----> 2. Ye kyun hai?
# Data alag-alag tables me hota hai. JOIN ka use kar ke information ek saath milti hai.

#----> 3. Ye kaise kaam karta hai?
# Common column ke basis par tables ko match karta hai:

# SELECT *
# FROM students
# JOIN courses
# ON students.course_id = courses.id;

# or

# SELECT *
# FROM students AS S
# JOIN courses AS C
# ON S.course_id = C.courses.id;

#----> 4. Main Types
# JOIN
#  ├── INNER JOIN  → sirf matching data
#  ├── LEFT JOIN   → left table ka sab data
#  ├── RIGHT JOIN  → right table ka sab data
#  └── FULL JOIN   → dono tables ka sab data


# Note :- Full table matlab left join + right join our es ko add karne ke liye (union) ka use hota hai
# Note :- UNION :- union duplicate ko remove karta hai
# Note :- UNION ALL :- ye sab kuch deta hai

# Key Point :-

# SELECT → kya dikhana hai
# FROM   → pehli table
# JOIN   → dusri table
# ON     → dono ko kis column se jodna hai






# 🟢 INNER JOIN — Questions 1–25
# --------------------------------------------------------------------
# INNER JOIN = dono tables me matching data

# Customer name aur payment amount dikhao.
# SELECT C.FIRST_NAME,P.AMOUNT FROM CUSTOMER AS C INNER JOIN PAYMENT AS P ON C.CUSTOMER_ID = P.CUSTOMER_ID;
# Customer ID aur payment ID dikhao.
# SELECT C.CUSTOMER_ID,P.CUSTOMER_ID FROM CUSTOMER AS C INNER JOIN PAYMENT AS P ON C.CUSTOMER_ID = P.CUSTOMER_ID;
# Har customer ki payment details find karo.
# SELECT C.CUSTOMER_ID,C.FIRST_NAME,C.LAST_NAME,P.AMOUNT,P.MODE,P.PAYMENT_DATE FROM CUSTOMER AS C INNER JOIN PAYMENT AS P ON C.CUSTOMER_ID = P.CUSTOMER_ID;
# Customer aur payment details combine karo.
# Customer name aur payment amount dikhao.
# Customer name aur payment date dikhao.
# SELECT C.FIRST_NAME,C.LAST_NAME,P.PAYMENT_DATE FROM CUSTOMER AS C INNER JOIN PAYMENT AS P ON C.CUSTOMER_ID = P.CUSTOMER_ID;
# Customer first name aur payment status dikhao.
# SELECT C.FIRST_NAME,C.LAST_NAME,P.MODE FROM CUSTOMER AS C INNER JOIN PAYMENT AS P ON C.CUSTOMER_ID = P.CUSTOMER_ID;

# Customer ID aur payment amount dikhao.
# SELECT C.CUSTOMER_ID,P.AMOUNT FROM CUSTOMER AS C INNER JOIN PAYMENT AS P ON C.CUSTOMER_ID = P.CUSTOMER_ID;

# Customer last name aur payment date dikhao.
# SELECT C.LAST_NAME,P.PAYMENT_DATE FROM CUSTOMER AS C INNER JOIN PAYMENT AS P ON C.CUSTOMER_ID = P.CUSTOMER_ID;

# Customer name aur payment method dikhao.
# Customer aur payment transaction details join karo.
# Customer name aur transaction ID dikhao.
# Customer name aur payment type dikhao.
# Customer name aur payment details dikhao.
# Payment ID ke saath customer name dikhao.
# Customer name aur payment currency dikhao.
# Customer name aur payment reference number dikhao.
# Customer aur payment status join karke dikhao.
# Customer name aur payment time dikhao.
# Customer ID aur payment status dikhao.
# Customer details aur payment amount combine karo.
# Customer name aur transaction details dikhao.
# Customer aur payment method details combine karo.
# Customer name aur payment confirmation dikhao.
# Customer ki complete payment information dikhao.

# 🔵 LEFT JOIN — Questions 26–50
# --------------------------------------------------------------------
# LEFT JOIN = Left table ka pura data + matching payment data

# Saare customers dikhao, chahe payment hui ho ya nahi.
# SELECT * FROM CUSTOMER AS C LEFT JOIN PAYMENT AS P ON C.CUSTOMER_ID = P.CUSTOMER_ID;

# Wo customers find karo jinhone payment nahi ki.
# SELECT C.CUSTOMER_ID, C.FIRST_NAME, C.LAST_NAME FROM CUSTOMER AS C LEFT JOIN PAYMENT AS P ON C.CUSTOMER_ID = P.CUSTOMER_ID WHERE P.CUSTOMER_ID IS null;

# Saare customers ke saath unki payment details dikhao.
# Saare customers ke saath payment amount dikhao.
# Saare customers ke saath payment status dikhao.
# Saare customers ke saath payment date dikhao.
# Saare customers ke saath payment method dikhao.
# Saare customers ke saath transaction ID dikhao.
# Saare customers ke saath payment reference dikhao.
# Saare customers ki payment history dikhao.
# Un customers ko find karo jinki payment missing hai.
# Saare customers aur unki payment information dikhao.
# Saare customers ke saath total payment information dikhao.
# Saare customers ke saath payment confirmation dikhao.
# Saare customers aur unka payment status dikhao.
# Saare customers ke saath latest payment details dikhao.
# Saare customers ke saath payment method dikhao.
# Saare customers ka payment record dikhao.
# Saare customers ke saath transaction details dikhao.
# Saare customers aur unki payment date dikhao.
# Saare customers ke saath payment amount dikhao.
# Saare customers aur unke payment IDs dikhao.
# Saare customers ke saath successful/failed payment status dikhao.
# Saare customers ka payment summary dikhao.
# Saare customers ke saath complete payment details dikhao.

# 🟣 RIGHT JOIN — Questions 51–60
# --------------------------------------------------------------------
# RIGHT JOIN = Right table ka pura data + matching customer data

# Saari payments dikhao aur unke customers.
# Saare payment transactions dikhao aur customer details.
# Saare payment IDs dikhao aur customer names.
# Saare payment amounts dikhao aur customer names.
# Saari payment dates dikhao aur customer details.
# Saare payment methods dikhao aur customers.
# Saare payment statuses dikhao aur customer names.
# Saare transaction IDs dikhao aur customer information.
# Saari payment history dikhao aur customer details.
# Saari payments dikhao, chahe customer match ho ya nahi.

# 🟠 SELF JOIN — Questions 61–70
# --------------------------------------------------------------------
# ⚠️ Important: Self JOIN ke liye Customer table me koi relationship hona chahiye, jaise referrer_id, parent_customer_id etc.

# Customer aur uske referrer ka naam dikhao.
# Aise customers find karo jinka referrer same ho.
# Har customer ke saath uske referred customer ki details dikhao.
# Customer referral hierarchy report banao.
# Same city wale customers ki pairs find karo.
# Same payment amount wale customers find karo.
# Aise customers find karo jinki payment kisi aur customer ke equal hai.
# Customer aur referring customer relationship dikhao.
# Har referrer ke under kitne customers hain find karo.
# Customer referral ka complete structure banao.

# 🟡 CROSS JOIN — Questions 71–80
# --------------------------------------------------------------------
# CROSS JOIN = Har customer × Har payment

# Saare customers aur saare payment methods ka combination banao.
# Saare customers aur saare payment statuses ka combination dikhao.
# Saare customers aur saare payment types ka combination banao.
# Saare customers aur available payment methods combine karo.
# Saare customers aur payment dates ka combination banao.
# Saare customers aur transaction types ka combination banao.
# Saare customers aur currencies ka combination banao.
# Saare customers aur payment statuses ka possible combination banao.
# Saare customers aur payment methods ka planning table banao.
# Saare customers aur payment options ka complete combination banao.

# 🔴 Multiple Table JOIN — Questions 81–90
# --------------------------------------------------------------------
# Yahan Customer + Payment + ek third table rakhenge.

# Customer + Payment + Order ki complete report banao.
# Customer + Payment + Address report banao.
# Customer + Payment + Order details dikhao.
# Customer + Payment + Product details dikhao.
# Customer + Payment + Order + Product report banao.
# Customer + Payment + Address + Order history dikhao.
# Customer + Payment + Product + Category details dikhao.
# Customer + Payment + Order + Product ki sales report banao.
# Customer + Payment + Address + Order + Product complete report banao.
# Customer + Payment + Order + Product + Category dashboard banao.

# 🔥 Real Company Interview — Questions 91–100
# --------------------------------------------------------------------
# Un customers ko find karo jinhone kabhi payment nahi ki.
# Un customers ko find karo jinki payment missing hai.
# Har customer ka total payment amount nikalo.
# Har customer ki average payment nikalo.
# Top 5 customers by total payment find karo.
# Har customer ki highest payment find karo.
# Monthly payment report customer details ke saath banao.
# Aise customers find karo jinka payment record missing hai.
# Customer ka total spending / lifetime payment value nikalo.
# Complete customer-payment dashboard ke liye customer aur payment data combine karo.
































# INNER JOIN Questions (1–25)
# ------------------------------------------
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
# ------------------------------------------
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
# ------------------------------------------
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
# ------------------------------------------
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
# -----------------------------------------------------
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
