def read_employees():
    f = open('Employees.txt', 'r')
    employeeslist = f.readlines()
    emprecs = []
    if len(employeeslist) >= 0:
        for emp in employeeslist:
            emp = tuple(emp.strip().split(" "))
            emprecs.append(emp)
    else:
        print("No data found about employees")
    return emprecs


def get_avg_salary(employees):
    if len(employees) > 0:
        averagesal = sum(float(e[3]) for e in employees) / len(employees)
        print("{:.2f}".format(averagesal))


def get_employee_data(data, criteria, filterparamvalue=None, paramposition=None):
    if len(data) > 0:
        if criteria == "AVGSAL":
            averagesal = sum(float(e[paramposition]) for e in data) / len(data)
            print("Average Salary of employees {:.2f} ".format(averagesal))
        elif criteria == "AGE":
            # reverse = True for descending order
            employees = sorted(data, key=lambda x: x[1])
            if filterparamvalue == "YOUNG":
                print("Youngest Employee is : {} and Age is: {} years".format(employees[0][0], employees[0][1]))
            elif filterparamvalue == "OLD":
                print("Oldest Employee is : {} and Age is: {} years".format(employees[len(employees) - 1][0],
                                                                            employees[len(employees) - 1][1]))
        elif criteria == "COUNT":
            if filterparamvalue == "MNG":
                print("Total emplyees who are {} is {}".format(filterparamvalue, len(
                    tuple(e for e in data if e[paramposition] == filterparamvalue))))
            elif filterparamvalue == "M" or filterparamvalue == "F":
                print("Total emplyees who are {} is {} %".format(filterparamvalue, len(
                    tuple(e for e in data if e[paramposition] == filterparamvalue)) / len(data) * 100))
            elif type(filterparamvalue) == list:
                print("Employees grouped by age")
                for agegroup in filterparamvalue:
                    if len(agegroup) == 1:
                        print("      No.of emplyees whose age is {} are {}".format(str(agegroup[0])+'+', len(
                            tuple(e for e in data if int(e[paramposition]) >= agegroup[0]))))
                    else:
                        print("      No.of emplyees whose age is {} are {}".format(agegroup, len(tuple(
                            e for e in data if int(e[paramposition]) in range(agegroup[0], int(agegroup[1]) + 1)))))


if __name__ == '__main__':
    emprecords = read_employees()
    get_employee_data(emprecords, "AVGSAL", None, 3)
    get_employee_data(emprecords, "AGE", "YOUNG")
    get_employee_data(emprecords, "AGE", "OLD")
    get_employee_data(emprecords, "COUNT", "MNG", 4)
    get_employee_data(emprecords, "COUNT", "M", 2)
    get_employee_data(emprecords, "COUNT", "F", 2)
    get_employee_data(emprecords, "COUNT", [(18, 25), (26, 35), (36, 48), (49, 60), (61,)], 1)
