"""Chi-square tests: is attrition different across groups, or could it be chance?
Run from the project root:  python python/significance_tests.py
"""
import pandas as pd
from scipy.stats import chi2_contingency

df = pd.read_csv("Data/hr_employees.csv")

print("Chi-square test of Attrition against each group")
for col in ["Department", "Job_Satisfaction", "Gender", "Education"]:
    p = chi2_contingency(pd.crosstab(df[col], df["Attrition"]))[1]
    print(f"{col:<18} p = {p:.3f}")

# Post-hoc check: HR versus all other departments
is_hr = df["Department"] == "HR"
p_hr = chi2_contingency(pd.crosstab(is_hr, df["Attrition"]))[1]
print(f"\nHR vs other departments (chosen after seeing results): p = {p_hr:.3f}")
