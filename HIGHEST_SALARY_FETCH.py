employee={
    "TANISHQ":{"AGE":19,"SALARY":10000},
    "SHUBHAM":{"AGE":20,"SALARY":20000},
    "DEV":{"AGE":21,"SALARY":15000}
}
emply_name=" "
max_sal=0
for i in employee:
    if employee[i]["SALARY"]>max_sal:
        max_sal=employee[i]["SALARY"]
        emply_name=i
print("The employee with the highest salary is:" + emply_name + " with a salary of " + str(max_sal))