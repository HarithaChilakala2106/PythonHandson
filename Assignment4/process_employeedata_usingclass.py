from decimal import Decimal


def get_avg_salary(employees):
    averagesal = 0.0
    if len(employees) > 0:
        averagesal = sum(float(e.sal) for e in employees) / len(employees)
    return averagesal


# For each department, who is the employee with the salary closest to the average salary of that department (position)?
def get_emp_sal_iscls_with_avgsal_ofdept(employees):
    emplstbypos = {}  # to hold departmentwise employees list
    emp_avg_sal_grpbypos = {}  # to hold department wise average sal
    emp_avg_cls_sal_byposition = {}  # to hold employees whoses salary is closest to departmentwise avg sal
    for pos in set(e.position for e in employees):
        emplstbypos[pos] = list(e for e in employees if e.position == pos)
        # add the salaries of employees in each dept and divide with total no.of employees in correspondig dept
        # round the average to 2 decimals
        emp_avg_sal_grpbypos[pos] = round((sum(float(e.sal) for e in employees if e.position == pos) / len(
            list(e for e in employees if e.position == pos))), 2)
    # print(emp_avg_sal_grpbypos)
    # iterate over the employees in each dept
    for empllst in emplstbypos.values():
        closesal = 0
        listofsal = {}
        for emp in empllst:
            listofsal[emp.name] = emp.sal  # store the departmentwise salaries into a list
        # find the difference between departmentwise avg salary and each emp salray
        # now find the salary with min difference i.e closest salary with avgsal
        closesal = min(listofsal.values(), key=lambda x: abs(float(x) - emp_avg_sal_grpbypos[emp.position]))
        emp = list(emp for emp in empllst if emp.sal == closesal)

        # print(listofsal)
        # print(closesal)
        for e in emp:
            emp_avg_cls_sal_byposition[e.position + "_" + str(emp_avg_sal_grpbypos[e.position])] = e.__str__()
    return emp_avg_cls_sal_byposition


class Employee:
    def __init__(self, e):
        self.name = e[0]
        self.age = e[1]
        self.gender = e[2]
        self.sal = e[3]
        self.position = e[4]

    def __str__(self):
        return self.name + " " + self.age + " " + self.gender + " " + self.sal + " " + self.position


def read_employees():
    f = open('Employees.txt', 'r')
    employeeslist = f.readlines()
    emprecs = []
    if len(employeeslist) >= 0:
        for emp in list(tuple(employee.strip().split(" ") for employee in employeeslist)):
            emprecs.append(Employee(emp))
    else:
        print("No data found about employees")
    return emprecs


if __name__ == '__main__':
    emprecords = read_employees()
    print("***************The Emplyees data ************")
    for emp in emprecords:
        print(emp.__str__())
    print("***************The Emplyees data ************")
    print("1. Average Salary of employees : {:.2f}".format(get_avg_salary(emprecords)))
    print("10. For each department, employee with the salary closest to the average salary of that department: ")
    print(get_emp_sal_iscls_with_avgsal_ofdept(emprecords))
