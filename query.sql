SELECT * FROM patients;
SELECT* FROM admission;

SELECT count(*)as total_patients
FROM admission;
SELECT disease,count(*)as total_deci
FROM admission
group by disease
order by total_deci DESC
;

SELECT doctor,bill_amount
FROM admission
group by doctor
order by bill_amount DESC;

SELECT city,count(*)as total_patients
FROM patients
GROUP by city 
order by total_patients DESC
;

SELECT p.patient_name, a.disease
FROM patients p join admission a 
on p.patient_id=a.patient_id
group by p.patient_name,a.disease;
 
SELECT patient_id ,
count(*) as patients
FROM admission
group by patient_id
having count(*)>1
order by patients DESC; 




SELECT  p.patient_name , a.bill_amount
FROM patients p 
JOIN admission a on p.patient_id=a.patient_id
group by patient_name
ORDER by bill_amount DESC;

SELECT doctor,bill_amount,
rank()over(PARTITION by doctor order by bill_amount DESC)as s 
FROM admission 
order by bill_amount DESC;

SELECT p.patient_name,a.bill_amount,
sum(a.bill_amount)over (order by  a.admission_id) as s 
FROM admission a join patients p on p.patient_id=a.patient_id;

SELECT round(avg(julianday(discharge_date)-julianday(admission_date)),0)||'days 'as avg_stay
FROM admission;

SELECT disease,round(avg(julianday(discharge_date)-julianday(admission_date)))as avg_stay
FROM admission
GROUP by disease
ORDER by avg_stay DESC;

SELECT disease,sum(bill_amount) as revenue,
rank()over( order by sum(bill_amount) DESC)as disease_rank  
FROM admission
GROUP by disease ;

SELECT p.patient_name,sum(a.bill_amount)as revenue,
rank()over (ORDER by sum(a.bill_amount)desc)as patient_rank
FROM admission a  join patients p on a.patient_id=p.patient_id
GROUP by p.patient_name;

SELECT admission_date,bill_amount,
sum(bill_amount)over(ORDER by admission_date DESC) as running_revenue
FROM admission;
