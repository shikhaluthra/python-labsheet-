import numpy as np

marks = np.array([
    [80, 75, 90, 85],
    [70, 65, 80, 75],
    [90, 88, 92, 95],
    [60, 72, 68, 70],
    [85, 80, 78, 88]
])

student_averages = np.mean(marks, axis=1)
subject_averages = np.mean(marks, axis=0)

print("Marks:")
print(marks)
print("Each student's average:", student_averages)
print("Each subject's average:", subject_averages)
