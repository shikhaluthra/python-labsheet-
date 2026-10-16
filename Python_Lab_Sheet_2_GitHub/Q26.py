# Python Libraries and Applications - Lab Sheet 2
# Q26

import pandas as pd

data = {
    "RollNo": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Rohan", "Kavya", "Arjun", "Simran"],
    "Department": ["BCA", "BCA", "MCA", "BCA", "MCA", "MCA", "BCA", "MCA"],
    "Age": [20, 21, 22, 20, 23, 22, 21, 24],
    "Marks": [85, 92, 67, 78, 88, 95, 55, 73]
}
df = pd.DataFrame(data)

# Solution
def get_grade(marks):
    if marks >= 90: return "A+"
    elif marks >= 80: return "A"
    elif marks >= 70: return "B"
    elif marks >= 60: return "C"
    else: return "D"
df["Grade"] = df["Marks"].apply(get_grade)
print(df)
