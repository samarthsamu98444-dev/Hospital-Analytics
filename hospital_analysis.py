import pandas as pd
import sqlite3
patients=pd.read_csv(r"C:\Users\samar\OneDrive\Desktop\c language\.vscode\bo.1.txt")
admission=pd.read_csv(r"C:\Users\samar\OneDrive\Desktop\c language\.vscode\bo.2.txt")
conn=sqlite3.connect("hospital.db")
patients.to_sql("patients", conn, if_exists="replace", index=False)

admission.to_sql("admission", conn, if_exists="replace", index=False)
print("the process has been done ")

import matplotlib.pyplot as plt

query="""select department,sum(bill_amount)as revenue
from admission
group by department 
order by revenue desc"""
df=pd.read_sql(query,conn)
plt.plot(df["department"],df["revenue"])
plt.xlabel("department")
plt.ylabel("revenue")
plt.title("revenue based on the department ")
plt.show()


query="""select doctor,sum(bill_amount) as revenue
from admission
group by doctor
order by revenue desc"""
df=pd.read_sql(query,conn)
plt.bar(df["doctor"],df["revenue"])
plt.xlabel("doctor")
plt.ylabel("revenue")
plt.title("revenue by doctor")
plt.show()


query="""select patient_name,city
from patients 
group by patient_name ,city"""
df=pd.read_sql(query,conn)
plt.bar(df["patient_name"],df["city"])
plt.xlabel("patient-name")
plt.ylabel("city")
plt.title("patients by city")
plt.show()


query=""" select bill_amount,admission_date,
sum(bill_amount)over(order by admission_date) as running_revenue
from admission"""
df=pd.read_sql(query,conn)
plt.plot(df["running_revenue"],df["admission_date"])
plt.xlabel("running_revenue")
plt.ylabel("admission_date")
plt.title("running revenue as per date ")
plt.show()

query = """
SELECT disease,
    AVG(julianday(discharge_date) -julianday(admission_date)
    ) AS avg_stay
FROM admission
GROUP BY disease
ORDER BY avg_stay DESC
"""
df = pd.read_sql(query,conn)
plt.bar(df["disease"], df["avg_stay"])
plt.xlabel("Disease")
plt.ylabel("Average Stay (Days)")
plt.title("Average Stay Duration by Disease")
plt.show()