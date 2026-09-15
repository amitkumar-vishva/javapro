# ---------------------------------------------------------------------------------
#     difference between SQL and NoSQL databases
# ---------------------------------------------------------------------------------
# SQL
# “SQL databases mein data tables ke form mein store hota hai, jisme rows aur columns hote hain. 
# Iska schema predefined hota hai aur ye structured data aur data ke beech relationships ke liye use hota hai.
# like - Banking systems, ERP systems, and applications requiring complex queries
# and transactions
#  Examples hain MySQL aur PostgreSQL, oracle,sql server.”

# NoSQL
# “NoSQL databases mein data flexible formats jaise documents, key-value pairs ya graphs mein store hota hai.
#  Ye tab useful hote hain jab data ka structure frequently change hota hai ya high scalability chahiye hoti hai.
#  MongoDB iska common example hai.”
# like - social media platorms, iot data storage, real-time analytics, and big data applications
# Example - MongoDB, cassandra, Redis, couchbase

# Main Difference
# “Main difference ye hai ki SQL fixed schema aur structured tables use karta hai,
#  jabki NoSQL flexible data models use karta hai aur large applications ke liye generally zyada scalable hota hai.”

# ---------------------------------------------------------------------------------
#     IS operator
# ---------------------------------------------------------------------------------
# use reacord ko show karo jis ki value null hai

# SELECT *
# FROM students
# WHERE phone IS NULL;

# ---------------------------------------------------------------------------------
#     IS NOT operator
# ---------------------------------------------------------------------------------
# use reacord ko show karo jis ki value null nahi hai

# SELECT *
# FROM students
# WHERE phone IS NOT NULL;

# ---------------------------------------------------------------------------------
#     limit operator
# ---------------------------------------------------------------------------------
# kitna record chiye ye utna hee record nikal kar dega

# SELECT *
# FROM students
# LIMIT 5;

# ---------------------------------------------------------------------------------
#     UNION
# ---------------------------------------------------------------------------------
#  UNION = 2 tables ko jodo + duplicate hatao

# Example - 
# SELECT name FROM students_2025
# UNION
# SELECT name FROM students_2026;


# ---------------------------------------------------------------------------------
#     UNION ALL
# ---------------------------------------------------------------------------------
#  UNION ALL = 2 tables ko jodo + duplicate bhi rakho

# Example - 
# SELECT name FROM students_2025
# UNION ALL
# SELECT name FROM students_2026;

# ---------------------------------------------------------------------------------
#     INTERSET
# ---------------------------------------------------------------------------------
# dono table me comman data nikal kar deta hai

# Example - 
# SELECT name FROM students_2025
# INTERSECT
# SELECT name FROM students_2026;


