import pandas as pd

data = pd.read_csv("data.csv")

salaryMean = data["salary"].mean()

employeeAge = data[data["age"] > 30]

print(f"Средняя зарплата сотрудников: {salaryMean}")
print(f"Сотрудники старше 30 лет:\n{employeeAge}")
