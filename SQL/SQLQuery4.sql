USE HR_Analytics;
GO

-- STEP 1: Display the first 10 employee records to inspect the data.
SELECT TOP 10 *
FROM dbo.hr_employees;

-- STEP 2: Count all employee records.
SELECT COUNT(*) AS Total_Employees
FROM dbo.hr_employees;

-- STEP 3: Count employees who left the company (Attrition = 1).
SELECT COUNT(*) AS Employees_Left
FROM dbo.hr_employees
WHERE Attrition = 1;

-- STEP 4: Count employees who stayed with the company (Attrition = 0).
SELECT COUNT(*) AS Employees_Stayed
FROM dbo.hr_employees
WHERE Attrition = 0;

-- STEP 5: Count employees in each department, from largest to smallest.
SELECT
    Department,
    COUNT(*) AS Total_Employees
FROM dbo.hr_employees
GROUP BY Department
ORDER BY Total_Employees DESC;

-- STEP 6: Count employees who left in each department.
SELECT
    Department,
    COUNT(*) AS Employees_Left
FROM dbo.hr_employees
WHERE Attrition = 1
GROUP BY Department
ORDER BY Employees_Left DESC;

-- STEP 7: Calculate the attrition rate for each department.
-- Attrition rate = employees who left / total employees * 100.
SELECT
    Department,
    COUNT(*) AS Total_Employees,
    SUM(CAST(Attrition AS INT)) AS Employees_Left,
    CAST(
        SUM(CAST(Attrition AS FLOAT)) * 100 / COUNT(*)
        AS DECIMAL(5,2)
    ) AS Attrition_Rate
FROM dbo.hr_employees
GROUP BY Department
ORDER BY Attrition_Rate DESC;

-- STEP 8: Compare employee attrition rates by gender.
SELECT
    Gender,
    COUNT(*) AS Total_Employees,
    SUM(CAST(Attrition AS INT)) AS Employees_Left,
    CAST(
        AVG(CAST(Attrition AS FLOAT)) * 100
        AS DECIMAL(5,2)
    ) AS Attrition_Rate
FROM dbo.hr_employees
GROUP BY Gender
ORDER BY Attrition_Rate DESC;

-- STEP 9: Compare attrition rates for each job satisfaction level.
SELECT
    Job_Satisfaction,
    COUNT(*) AS Total_Employees,
    SUM(CAST(Attrition AS INT)) AS Employees_Left,
    CAST(
        AVG(CAST(Attrition AS FLOAT)) * 100
        AS DECIMAL(5,2)
    ) AS Attrition_Rate
FROM dbo.hr_employees
GROUP BY Job_Satisfaction
ORDER BY Job_Satisfaction;

-- STEP 10: Compare attrition rates by years at the company.
SELECT
    Years_at_Company,
    COUNT(*) AS Total_Employees,
    SUM(CAST(Attrition AS INT)) AS Employees_Left,
    CAST(
        AVG(CAST(Attrition AS FLOAT)) * 100
        AS DECIMAL(5,2)
    ) AS Attrition_Rate
FROM dbo.hr_employees
GROUP BY Years_at_Company
ORDER BY Years_at_Company;

-- STEP 11: Compare attrition rates by education level.
SELECT
    Education,
    COUNT(*) AS Total_Employees,
    SUM(CAST(Attrition AS INT)) AS Employees_Left,
    CAST(
        AVG(CAST(Attrition AS FLOAT)) * 100
        AS DECIMAL(5,2)
    ) AS Attrition_Rate
FROM dbo.hr_employees
GROUP BY Education
ORDER BY Attrition_Rate DESC;

-- STEP 12: Group employees into age bands and calculate attrition rates.
-- CASE assigns each employee to an age group.
SELECT
    CASE
        WHEN Age < 25 THEN 'Under 25'
        WHEN Age < 35 THEN '25-34'
        WHEN Age < 45 THEN '35-44'
        WHEN Age < 55 THEN '45-54'
        ELSE '55+'
    END AS Age_Group,
    COUNT(*) AS Total_Employees,
    SUM(CAST(Attrition AS INT)) AS Employees_Left,
    CAST(
        AVG(CAST(Attrition AS FLOAT)) * 100
        AS DECIMAL(5,2)
    ) AS Attrition_Rate
FROM dbo.hr_employees
GROUP BY
    CASE
        WHEN Age < 25 THEN 'Under 25'
        WHEN Age < 35 THEN '25-34'
        WHEN Age < 45 THEN '35-44'
        WHEN Age < 55 THEN '45-54'
        ELSE '55+'
    END
ORDER BY Age_Group;

-- STEP 13: Group employees into monthly-income bands and calculate attrition.
SELECT
    CASE
        WHEN Monthly_Income < 40000 THEN 'Below 40k'
        WHEN Monthly_Income < 60000 THEN '40k-59k'
        WHEN Monthly_Income < 80000 THEN '60k-79k'
        WHEN Monthly_Income < 100000 THEN '80k-99k'
        ELSE '100k+'
    END AS Income_Group,
    COUNT(*) AS Total_Employees,
    SUM(CAST(Attrition AS INT)) AS Employees_Left,
    CAST(
        AVG(CAST(Attrition AS FLOAT)) * 100
        AS DECIMAL(5,2)
    ) AS Attrition_Rate
FROM dbo.hr_employees
GROUP BY
    CASE
        WHEN Monthly_Income < 40000 THEN 'Below 40k'
        WHEN Monthly_Income < 60000 THEN '40k-59k'
        WHEN Monthly_Income < 80000 THEN '60k-79k'
        WHEN Monthly_Income < 100000 THEN '80k-99k'
        ELSE '100k+'
    END
ORDER BY Income_Group;

-- STEP 14: Calculate average monthly income for each department.
SELECT
    Department,
    AVG(Monthly_Income) AS Average_Monthly_Income
FROM dbo.hr_employees
GROUP BY Department
ORDER BY Average_Monthly_Income DESC;

-- STEP 15: Calculate average employee age for each department.
SELECT
    Department,
    AVG(Age) AS Average_Age
FROM dbo.hr_employees
GROUP BY Department
ORDER BY Average_Age DESC;

-- STEP 16: Display the 10 employees with the highest monthly income.
SELECT TOP 10
    Employee_ID,
    Department,
    Job_Role,
    Monthly_Income
FROM dbo.hr_employees
ORDER BY Monthly_Income DESC;

-- STEP 17: Display employees whose job satisfaction level is 1.
SELECT
    Employee_ID,
    Department,
    Job_Role,
    Job_Satisfaction,
    Attrition
FROM dbo.hr_employees
WHERE Job_Satisfaction = 1;

-- STEP 18: Calculate the overall company attrition rate.
SELECT
    COUNT(*) AS Total_Employees,
    SUM(CAST(Attrition AS INT)) AS Employees_Left,
    CAST(
        AVG(CAST(Attrition AS FLOAT)) * 100
        AS DECIMAL(5,2)
    ) AS Attrition_Rate
FROM dbo.hr_employees;

-- STEP 19: Compare attrition rates by job role.
SELECT
    Job_Role,
    COUNT(*) AS Total_Employees,
    SUM(CAST(Attrition AS INT)) AS Employees_Left,
    CAST(
        AVG(CAST(Attrition AS FLOAT)) * 100
        AS DECIMAL(5,2)
    ) AS Attrition_Rate
FROM dbo.hr_employees
GROUP BY Job_Role
ORDER BY Attrition_Rate DESC;

-- STEP 20: Calculate average years at the company for each department.
SELECT
    Department,
    AVG(Years_at_Company) AS Average_Years
FROM dbo.hr_employees
GROUP BY Department
ORDER BY Average_Years DESC;

-- STEP 21: List employees who have worked at the company for less than 2 years.
SELECT
    Employee_ID,
    Department,
    Years_at_Company,
    Attrition
FROM dbo.hr_employees
WHERE Years_at_Company < 2
ORDER BY Years_at_Company;

-- STEP 22: List employees with job satisfaction level 4 who left the company.
SELECT
    Employee_ID,
    Department,
    Job_Satisfaction,
    Years_at_Company
FROM dbo.hr_employees
WHERE Job_Satisfaction = 4
AND Attrition = 1;

-- STEP 23: Find departments with more than 150 employee departures.
SELECT
    Department,
    COUNT(*) AS Employees_Left
FROM dbo.hr_employees
WHERE Attrition = 1
GROUP BY Department
HAVING COUNT(*) > 150;

-- STEP 24: Find departments with more than 800 employees in total.
SELECT
    Department,
    COUNT(*) AS Total_Employees
FROM dbo.hr_employees
GROUP BY Department
HAVING COUNT(*) > 800
ORDER BY Total_Employees DESC;

-- STEP 25: Find the department with the highest attrition rate.
SELECT TOP 1
    Department,
    COUNT(*) AS Total_Employees,
    SUM(CAST(Attrition AS INT)) AS Employees_Left,
    CAST(
        AVG(CAST(Attrition AS FLOAT)) * 100
        AS DECIMAL(5,2)
    ) AS Attrition_Rate
FROM dbo.hr_employees
GROUP BY Department
ORDER BY Attrition_Rate DESC;

-- STEP 26: Find the department with the lowest attrition rate.
SELECT TOP 1
    Department,
    COUNT(*) AS Total_Employees,
    SUM(CAST(Attrition AS INT)) AS Employees_Left,
    CAST(
        AVG(CAST(Attrition AS FLOAT)) * 100
        AS DECIMAL(5,2)
    ) AS Attrition_Rate
FROM dbo.hr_employees
GROUP BY Department
ORDER BY Attrition_Rate ASC;


-- STEP 27: Calculate the overall retention rate.
-- Retention rate = employees who stayed / total employees * 100.
SELECT
    COUNT(*) AS Total_Employees,
    COUNT(*) - SUM(CAST(Attrition AS INT)) AS Employees_Stayed,
    CAST(
        (COUNT(*) - SUM(CAST(Attrition AS FLOAT)))
        * 100.0 / COUNT(*)
        AS DECIMAL(5,2)
    ) AS Retention_Rate
FROM dbo.hr_employees;

-- STEP 28: Count employees at each job satisfaction level.
SELECT
    Job_Satisfaction,
    COUNT(*) AS Total_Employees
FROM dbo.hr_employees
GROUP BY Job_Satisfaction
ORDER BY Job_Satisfaction;

-- STEP 29: Find departments with more than 140 employee departures.
SELECT
    Department,
    COUNT(*) AS Employees_Left
FROM dbo.hr_employees
WHERE Attrition = 1
GROUP BY Department
HAVING COUNT(*) > 140;

-- STEP 30: Compare average monthly income for employees who left and stayed.
-- Attrition = 1 means left; Attrition = 0 means stayed.
SELECT
    Attrition,
    COUNT(*) AS Total_Employees,
    AVG(Monthly_Income) AS Average_Monthly_Income
FROM dbo.hr_employees
GROUP BY Attrition;

-- STEP 31: Compare attrition by gender within each department.
SELECT
    Department,
    Gender,
    COUNT(*) AS Total_Employees,
    SUM(CAST(Attrition AS INT)) AS Employees_Left,
    CAST(
        AVG(CAST(Attrition AS FLOAT)) * 100
        AS DECIMAL(5,2)
    ) AS Attrition_Rate
FROM dbo.hr_employees
GROUP BY Department, Gender
ORDER BY Department, Gender;

-- STEP 32: Compare average years of service for employees who left and stayed.
SELECT
    Attrition,
    COUNT(*) AS Total_Employees,
    AVG(Years_at_Company) AS Average_Years
FROM dbo.hr_employees
GROUP BY Attrition;

-- STEP 33: Compare attrition by gender and job satisfaction level.
SELECT
    Gender,
    Job_Satisfaction,
    COUNT(*) AS Total_Employees,
    SUM(CAST(Attrition AS INT)) AS Employees_Left,
    CAST(
        AVG(CAST(Attrition AS FLOAT)) * 100
        AS DECIMAL(5,2)
    ) AS Attrition_Rate
FROM dbo.hr_employees
GROUP BY Gender, Job_Satisfaction
ORDER BY Job_Satisfaction, Gender;

-- STEP 34: Calculate attrition among employees earning more than 80,000.
SELECT
    COUNT(*) AS Total_Employees,
    SUM(CAST(Attrition AS INT)) AS Employees_Left,
    CAST(
        AVG(CAST(Attrition AS FLOAT)) * 100
        AS DECIMAL(5,2)
    ) AS Attrition_Rate
FROM dbo.hr_employees
WHERE Monthly_Income > 80000;

-- STEP 35: Count employees and departures by department for employees
-- whose job satisfaction level is 1 or 2.
SELECT
    Department,
    COUNT(*) AS Total_Employees,
    SUM(CAST(Attrition AS INT)) AS Employees_Left
FROM dbo.hr_employees
WHERE Job_Satisfaction <= 2
GROUP BY Department
ORDER BY Employees_Left DESC;

-- STEP 36: Compare total rows with the number of unique employee IDs.
SELECT
    COUNT(*) AS Total_Rows,
    COUNT(DISTINCT Employee_ID) AS Unique_Employees
FROM dbo.hr_employees;

-- STEP 37: Count missing values in five important columns.
-- Each CASE returns 1 when the column is NULL, otherwise 0.
SELECT
    SUM(CASE WHEN Employee_ID IS NULL THEN 1 ELSE 0 END) AS Missing_ID,
    SUM(CASE WHEN Age IS NULL THEN 1 ELSE 0 END) AS Missing_Age,
    SUM(CASE WHEN Department IS NULL THEN 1 ELSE 0 END) AS Missing_Department,
    SUM(CASE WHEN Monthly_Income IS NULL THEN 1 ELSE 0 END) AS Missing_Income,
    SUM(CASE WHEN Attrition IS NULL THEN 1 ELSE 0 END) AS Missing_Attrition
FROM dbo.hr_employees;

-- STEP 38: Find employee IDs that appear more than once.
-- No returned rows means there are no duplicate IDs.
SELECT
    Employee_ID,
    COUNT(*) AS ID_Count
FROM dbo.hr_employees
GROUP BY Employee_ID
HAVING COUNT(*) > 1;

-- STEP 39: Count employees for each Attrition value.
-- Expected values: 0 (stayed) and 1 (left).
SELECT
    Attrition,
    COUNT(*) AS Total_Employees
FROM dbo.hr_employees
GROUP BY Attrition;

-- STEP 40: Final HR summary with total employees, departures, retained employees,
-- attrition rate, and retention rate in one result row.
SELECT
    COUNT(*) AS Total_Employees,
    SUM(CAST(Attrition AS INT)) AS Employees_Left,
    COUNT(*) - SUM(CAST(Attrition AS INT)) AS Employees_Stayed,
    CAST(
        AVG(CAST(Attrition AS FLOAT)) * 100
        AS DECIMAL(5,2)
    ) AS Attrition_Rate,
    CAST(
        (1 - AVG(CAST(Attrition AS FLOAT))) * 100
        AS DECIMAL(5,2)
    ) AS Retention_Rate
FROM dbo.hr_employees;
