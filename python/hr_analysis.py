
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load the employee dataset
df = pd.read_csv("Data/hr_employees.csv")

# Display the first five employee records
print("FIRST 5 EMPLOYEE RECORDS")
print(df.head())

# Display the number of rows and columns
print("\nDATASET SHAPE")
print(df.shape)

# Display all column names
print("\nCOLUMN NAMES")
print(df.columns.tolist())


# Check data quality
print("\nDATA TYPES")
print(df.dtypes)

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATE EMPLOYEE IDs")
print(df["Employee_ID"].duplicated().sum())

print("\nDUPLICATE ROWS")
print(df.duplicated().sum())


# Check unique categories
print("\nGENDER CATEGORIES")
print(df["Gender"].value_counts())

print("\nDEPARTMENT CATEGORIES")
print(df["Department"].value_counts())

print("\nATTRITION CATEGORIES")
print(df["Attrition"].value_counts())


# Check numerical ranges
print("\nNUMERICAL SUMMARY")
print(
    df[
        [
            "Age",
            "Monthly_Income",
            "Years_at_Company",
            "Job_Satisfaction",
        ]
    ].describe()
)


# Department-wise attrition analysis
department_attrition = (
    df.groupby("Department")
    .agg(
        Total_Employees=("Employee_ID", "count"),
        Employees_Left=(
            "Attrition",
            lambda x: (x == "Yes").sum(),
        ),
    )
)

department_attrition["Attrition_Rate"] = (
    department_attrition["Employees_Left"]
    / department_attrition["Total_Employees"]
    * 100
)

print("\nDEPARTMENT-WISE ATTRITION ANALYSIS")
print(department_attrition.round(2))


# Job-role-wise attrition analysis
job_role_attrition = (
    df.groupby("Job_Role")
    .agg(
        Total_Employees=("Employee_ID", "count"),
        Employees_Left=(
            "Attrition",
            lambda x: (x == "Yes").sum(),
        ),
    )
)

job_role_attrition["Attrition_Rate"] = (
    job_role_attrition["Employees_Left"]
    / job_role_attrition["Total_Employees"]
    * 100
)

print("\nJOB-ROLE-WISE ATTRITION ANALYSIS")
print(
    job_role_attrition.sort_values(
        "Attrition_Rate", ascending=False
    ).round(2)
)


# Check the relationship between department and job role
department_role_check = pd.crosstab(
    df["Department"],
    df["Job_Role"],
)

print("\nDEPARTMENT VS JOB ROLE CHECK")
print(department_role_check)


# Job satisfaction-wise attrition analysis
satisfaction_attrition = (
    df.groupby("Job_Satisfaction")
    .agg(
        Total_Employees=("Employee_ID", "count"),
        Employees_Left=(
            "Attrition",
            lambda x: (x == "Yes").sum(),
        ),
    )
)

satisfaction_attrition["Attrition_Rate"] = (
    satisfaction_attrition["Employees_Left"]
    / satisfaction_attrition["Total_Employees"]
    * 100
)

print("\nJOB SATISFACTION-WISE ATTRITION ANALYSIS")
print(satisfaction_attrition.round(2))


# Tenure-wise attrition analysis
tenure_attrition = (
    df.groupby("Years_at_Company")
    .agg(
        Total_Employees=("Employee_ID", "count"),
        Employees_Left=(
            "Attrition",
            lambda x: (x == "Yes").sum(),
        ),
    )
)

tenure_attrition["Attrition_Rate"] = (
    tenure_attrition["Employees_Left"]
    / tenure_attrition["Total_Employees"]
    * 100
)

print("\nTENURE-WISE ATTRITION ANALYSIS")
print(tenure_attrition.round(2))


# Gender-wise attrition analysis
gender_attrition = (
    df.groupby("Gender")
    .agg(
        Total_Employees=("Employee_ID", "count"),
        Employees_Left=(
            "Attrition",
            lambda x: (x == "Yes").sum(),
        ),
    )
)

gender_attrition["Attrition_Rate"] = (
    gender_attrition["Employees_Left"]
    / gender_attrition["Total_Employees"]
    * 100
)

print("\nGENDER-WISE ATTRITION ANALYSIS")
print(gender_attrition.round(2))


# Create age groups
df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 25, 35, 45, 55, 100],
    labels=["Under 25", "25-34", "35-44", "45-54", "55+"],
    right=False,
)

# Age-group-wise attrition analysis
age_attrition = (
    df.groupby("Age_Group", observed=False)
    .agg(
        Total_Employees=("Employee_ID", "count"),
        Employees_Left=(
            "Attrition",
            lambda x: (x == "Yes").sum(),
        ),
    )
)

age_attrition["Attrition_Rate"] = (
    age_attrition["Employees_Left"]
    / age_attrition["Total_Employees"]
    * 100
)

print("\nAGE-GROUP-WISE ATTRITION ANALYSIS")
print(age_attrition.round(2))


# Create monthly income groups
df["Income_Group"] = pd.cut(
    df["Monthly_Income"],
    bins=[0, 40000, 60000, 80000, 100000, float("inf")],
    labels=[
        "Below 40,000",
        "40,000-59,999",
        "60,000-79,999",
        "80,000-99,999",
        "100,000+",
    ],
    right=False,
)

# Income-group-wise attrition analysis
income_attrition = (
    df.groupby("Income_Group", observed=False)
    .agg(
        Total_Employees=("Employee_ID", "count"),
        Employees_Left=(
            "Attrition",
            lambda x: (x == "Yes").sum(),
        ),
    )
)

income_attrition["Attrition_Rate"] = (
    income_attrition["Employees_Left"]
    / income_attrition["Total_Employees"]
    * 100
)

print("\nMONTHLY-INCOME-WISE ATTRITION ANALYSIS")
print(income_attrition.round(2))


# Education-wise attrition analysis
education_attrition = (
    df.groupby("Education")
    .agg(
        Total_Employees=("Employee_ID", "count"),
        Employees_Left=(
            "Attrition",
            lambda x: (x == "Yes").sum(),
        ),
    )
)

education_attrition["Attrition_Rate"] = (
    education_attrition["Employees_Left"]
    / education_attrition["Total_Employees"]
    * 100
)

print("\nEDUCATION-WISE ATTRITION ANALYSIS")
print(education_attrition.round(2))


# Overall HR attrition summary
total_employees = df["Employee_ID"].nunique()

employees_left = (df["Attrition"] == "Yes").sum()
employees_stayed = (df["Attrition"] == "No").sum()

attrition_rate = employees_left / total_employees * 100
retention_rate = employees_stayed / total_employees * 100

hr_summary = pd.DataFrame(
    {
        "Metric": [
            "Total Employees",
            "Employees Left",
            "Employees Stayed",
            "Attrition Rate (%)",
            "Retention Rate (%)",
        ],
        "Value": [
            total_employees,
            employees_left,
            employees_stayed,
            round(attrition_rate, 2),
            round(retention_rate, 2),
        ],
    }
)

print("\nOVERALL HR SUMMARY")
print(hr_summary.to_string(index=False))


# PHASE 2: VISUALIZE EMPLOYEE ATTRITION

# Save images in the project folder, alongside the Data folder
output_folder = Path.cwd()


# Chart 1: Overall employee attrition
categories = ["Stayed", "Left"]
employee_counts = [employees_stayed, employees_left]

plt.figure(figsize=(8, 5))
bars = plt.bar(categories, employee_counts)

plt.title("Employee Attrition Overview")
plt.xlabel("Employee Status")
plt.ylabel("Number of Employees")
plt.bar_label(bars, fmt="%d")
plt.tight_layout()

# Save chart 1 BEFORE displaying it
chart1_path = output_folder / "employee_attrition_overview.png"
plt.savefig(chart1_path, dpi=300, bbox_inches="tight")
print(f"\nChart 1 saved to: {chart1_path.resolve()}")

plt.show()
plt.close()


# Chart 2: Department-wise attrition analysis

# Count employees who left in each department
left_by_department = (
    df[df["Attrition"] == "Yes"]
    .groupby("Department")
    .size()
)

# Count all employees in each department
total_by_department = df.groupby("Department").size()

# Calculate attrition rate as a percentage
department_attrition_rate = (
    left_by_department / total_by_department * 100
).round(2)

print("\nDEPARTMENT-WISE ATTRITION RATE (%)")
print(department_attrition_rate.sort_values(ascending=False))


# Sort attrition rates from highest to lowest
rates = department_attrition_rate.sort_values(ascending=False)

plt.figure(figsize=(9, 5))
bars = plt.bar(rates.index, rates.values, color="steelblue")

plt.bar_label(
    bars,
    labels=[f"{value:.2f}%" for value in rates.values],
    padding=3,
)

plt.title("Employee Attrition Rate by Department")
plt.xlabel("Department")
plt.ylabel("Attrition Rate (%)")
plt.xticks(rotation=45, ha="right")
plt.ylim(0, max(rates.values) + 4)
plt.tight_layout()

# Save chart 2 BEFORE displaying it
chart2_path = output_folder / "department_attrition.png"
plt.savefig(chart2_path, dpi=300, bbox_inches="tight")
print(f"\nChart 2 saved to: {chart2_path.resolve()}")

plt.show()
plt.close()

print("\nBoth charts have been saved successfully.")


# Chart 3: Job-role-wise attrition rate

job_role_rates = (
    job_role_attrition["Attrition_Rate"]
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

bars = plt.barh(
    job_role_rates.index,
    job_role_rates.values,
    color="steelblue"
)

# Show percentages beside the bars
plt.bar_label(
    bars,
    labels=[f"{value:.2f}%" for value in job_role_rates.values],
    padding=3
)

plt.title("Employee Attrition Rate by Job Role")
plt.xlabel("Attrition Rate (%)")
plt.ylabel("Job Role")
plt.gca().invert_yaxis()
plt.xlim(0, max(job_role_rates.values) + 5)
plt.tight_layout()

# Save chart 3
chart3_path = output_folder / "job_role_attrition.png"
plt.savefig(chart3_path, dpi=300, bbox_inches="tight")
print(f"\nChart 3 saved to: {chart3_path.resolve()}")

plt.show()
plt.close()


# Chart 4: Job satisfaction-wise attrition rate

satisfaction_rates = satisfaction_attrition["Attrition_Rate"]

plt.figure(figsize=(8, 5))

bars = plt.bar(
    satisfaction_rates.index.astype(str),
    satisfaction_rates.values,
    color="steelblue"
)

plt.bar_label(
    bars,
    labels=[f"{value:.2f}%" for value in satisfaction_rates.values],
    padding=3
)

plt.title("Employee Attrition Rate by Job Satisfaction")
plt.xlabel("Job Satisfaction Level")
plt.ylabel("Attrition Rate (%)")
plt.ylim(0, max(satisfaction_rates.values) + 5)
plt.tight_layout()

# Save chart 4
chart4_path = output_folder / "satisfaction_attrition.png"
plt.savefig(chart4_path, dpi=300, bbox_inches="tight")
print(f"\nChart 4 saved to: {chart4_path.resolve()}")

plt.show()
plt.close()


# Chart 5: Attrition rate by years at the company

tenure_rates = tenure_attrition["Attrition_Rate"].sort_index()

plt.figure(figsize=(10, 5))

bars = plt.bar(
    tenure_rates.index.astype(str),
    tenure_rates.values,
    color="steelblue"
)

plt.bar_label(
    bars,
    labels=[f"{value:.1f}%" for value in tenure_rates.values],
    padding=3,
    fontsize=8
)

plt.title("Employee Attrition Rate by Years at Company")
plt.xlabel("Years at Company")
plt.ylabel("Attrition Rate (%)")
plt.xticks(rotation=45)
plt.ylim(0, max(tenure_rates.values) + 5)
plt.tight_layout()

# Save chart 5
chart5_path = output_folder / "tenure_attrition.png"
plt.savefig(chart5_path, dpi=300, bbox_inches="tight")
print(f"\nChart 5 saved to: {chart5_path.resolve()}")

plt.show()
plt.close()


# Chart 6: Attrition rate by age group

age_rates = age_attrition["Attrition_Rate"]

plt.figure(figsize=(9, 5))

bars = plt.bar(
    age_rates.index.astype(str),
    age_rates.values,
    color="steelblue"
)

plt.bar_label(
    bars,
    labels=[f"{value:.2f}%" for value in age_rates.values],
    padding=3
)

plt.title("Employee Attrition Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Attrition Rate (%)")
plt.ylim(0, max(age_rates.values) + 5)
plt.tight_layout()

# Save chart 6
chart6_path = output_folder / "age_group_attrition.png"
plt.savefig(chart6_path, dpi=300, bbox_inches="tight")
print(f"\nChart 6 saved to: {chart6_path.resolve()}")

plt.show()
plt.close()


# Chart 7: Attrition rate by monthly income group

income_rates = income_attrition["Attrition_Rate"]

plt.figure(figsize=(10, 5))

bars = plt.bar(
    income_rates.index.astype(str),
    income_rates.values,
    color="steelblue"
)

plt.bar_label(
    bars,
    labels=[f"{value:.2f}%" for value in income_rates.values],
    padding=3
)

plt.title("Employee Attrition Rate by Monthly Income Group")
plt.xlabel("Monthly Income Group")
plt.ylabel("Attrition Rate (%)")
plt.xticks(rotation=20, ha="right")
plt.ylim(0, max(income_rates.values) + 5)
plt.tight_layout()

# Save chart 7
chart7_path = output_folder / "income_group_attrition.png"
plt.savefig(chart7_path, dpi=300, bbox_inches="tight")
print(f"\nChart 7 saved to: {chart7_path.resolve()}")

plt.show()
plt.close()


# Chart 8: Attrition rate by education level

education_rates = education_attrition["Attrition_Rate"]

plt.figure(figsize=(9, 5))

bars = plt.bar(
    education_rates.index.astype(str),
    education_rates.values,
    color="steelblue"
)

plt.bar_label(
    bars,
    labels=[f"{value:.2f}%" for value in education_rates.values],
    padding=3
)

plt.title("Employee Attrition Rate by Education Level")
plt.xlabel("Education Level")
plt.ylabel("Attrition Rate (%)")
plt.ylim(0, max(education_rates.values) + 5)
plt.tight_layout()

# Save chart 8
chart8_path = output_folder / "education_attrition.png"
plt.savefig(chart8_path, dpi=300, bbox_inches="tight")
print(f"\nChart 8 saved to: {chart8_path.resolve()}")

plt.show()
plt.close()


# PHASE 3: EXPORT ANALYSIS RESULTS TO CSV FILES

# Create an output folder for analysis tables
output_folder.mkdir(exist_ok=True)

# Export overall HR summary
hr_summary.to_csv(
    output_folder / "hr_summary.csv",
    index=False
)

# Export department-wise analysis
department_attrition.to_csv(
    output_folder / "department_attrition_analysis.csv"
)

# Export job-role-wise analysis
job_role_attrition.to_csv(
    output_folder / "job_role_attrition_analysis.csv"
)

# Export job satisfaction analysis
satisfaction_attrition.to_csv(
    output_folder / "satisfaction_attrition_analysis.csv"
)

# Export tenure analysis
tenure_attrition.to_csv(
    output_folder / "tenure_attrition_analysis.csv"
)

# Export gender analysis
gender_attrition.to_csv(
    output_folder / "gender_attrition_analysis.csv"
)

# Export age-group analysis
age_attrition.to_csv(
    output_folder / "age_attrition_analysis.csv"
)

# Export monthly-income analysis
income_attrition.to_csv(
    output_folder / "income_attrition_analysis.csv"
)

# Export education analysis
education_attrition.to_csv(
    output_folder / "education_attrition_analysis.csv"
)

print("\nAll analysis tables have been exported successfully.")
