"""Student Academic Performance Analysis using Pandas and Matplotlib."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "students.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

SUBJECTS = ["Python Marks", "DBMS Marks", "AI Marks"]

def load_and_clean_data(path: Path) -> pd.DataFrame:
    """Load the CSV and perform basic cleaning and validation."""
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    required = [
        "Student ID", "Student Name", "Gender", "Department", "Attendance",
        "Study Hours", "Assignment Marks", "Internal Assessment Marks",
        "Python Marks", "DBMS Marks", "AI Marks", "Final Exam Marks",
    ]
    missing = [column for column in required if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns in {path.name}: {missing}")

    df = df.drop_duplicates(subset=["Student ID"])
    numeric = [
        "Attendance", "Study Hours", "Assignment Marks",
        "Internal Assessment Marks", "Python Marks", "DBMS Marks",
        "AI Marks", "Final Exam Marks",
    ]
    for column in numeric:
        df[column] = pd.to_numeric(df[column], errors="coerce")
        df[column] = df[column].fillna(df[column].median())

    df["Student Name"] = df["Student Name"].fillna("Unknown").astype(str).str.strip()
    df["Department"] = df["Department"].fillna("Unknown").astype(str).str.strip()
    df["Gender"] = df["Gender"].fillna("Unknown").astype(str).str.strip()
    df["Attendance"] = df["Attendance"].clip(0, 100)
    return df

def analyze_data(df: pd.DataFrame) -> pd.DataFrame:
    """Add average marks and performance labels."""
    df = df.copy()
    df["Average Subject Marks"] = df[SUBJECTS].mean(axis=1).round(2)
    df["Performance"] = pd.cut(
        df["Average Subject Marks"],
        bins=[-float("inf"), 39.99, 59.99, 79.99, float("inf")],
        labels=["Low", "Average", "Good", "Excellent"],
    )
    return df

def make_charts(df: pd.DataFrame) -> None:
    """Save charts illustrating the main questions in the lab sheet."""
    # Subject-wise performance
    df[SUBJECTS].mean().plot(kind="bar", rot=0)
    plt.title("Average Marks by Subject")
    plt.ylabel("Average Marks")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "subject_wise_performance.png", dpi=150)
    plt.close()

    # Department-wise performance
    df.groupby("Department")["Average Subject Marks"].mean().sort_values().plot(kind="bar")
    plt.title("Average Performance by Department")
    plt.ylabel("Average Subject Marks")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "department_wise_performance.png", dpi=150)
    plt.close()

    # Attendance pattern
    df["Attendance"].plot(kind="hist", bins=10, edgecolor="black")
    plt.title("Student Attendance Distribution")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "attendance_distribution.png", dpi=150)
    plt.close()

    # Study hours vs marks
    plt.scatter(df["Study Hours"], df["Average Subject Marks"])
    plt.title("Study Hours vs Average Subject Marks")
    plt.xlabel("Study Hours per Day")
    plt.ylabel("Average Subject Marks")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "study_hours_vs_marks.png", dpi=150)
    plt.close()

    # Attendance vs marks
    plt.scatter(df["Attendance"], df["Average Subject Marks"])
    plt.title("Attendance vs Average Subject Marks")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Average Subject Marks")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "attendance_vs_marks.png", dpi=150)
    plt.close()

def main() -> None:
    df = load_and_clean_data(DATA_FILE)
    analyzed = analyze_data(df)

    high = analyzed.nlargest(5, "Average Subject Marks")
    low = analyzed.nsmallest(5, "Average Subject Marks")
    department = analyzed.groupby("Department", as_index=False)["Average Subject Marks"].mean()
    subject = analyzed[SUBJECTS].mean().rename_axis("Subject").reset_index(name="Average Marks")

    analyzed.to_csv(OUTPUT_DIR / "analyzed_students.csv", index=False)
    high.to_csv(OUTPUT_DIR / "top_performers.csv", index=False)
    low.to_csv(OUTPUT_DIR / "low_performers.csv", index=False)
    department.to_csv(OUTPUT_DIR / "department_summary.csv", index=False)
    subject.to_csv(OUTPUT_DIR / "subject_summary.csv", index=False)
    make_charts(analyzed)

    print("\\n=== Student Academic Performance Analysis ===")
    print(f"Students analyzed: {len(analyzed)}")
    print("\\nTop performers:")
    print(high[["Student ID", "Student Name", "Department", "Average Subject Marks"]].to_string(index=False))
    print("\\nStudents needing support:")
    print(low[["Student ID", "Student Name", "Department", "Average Subject Marks"]].to_string(index=False))
    print("\\nSubject-wise averages:")
    print(subject.to_string(index=False))
    print("\\nDepartment-wise averages:")
    print(department.to_string(index=False))
    print(f"\\nReports and charts saved in: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
