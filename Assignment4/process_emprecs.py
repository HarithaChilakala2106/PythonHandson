def read_employees():
    f = open('Employees.txt', 'r')
    employeeslist = f.readlines()
    emprecs = []
    if len(employeeslist) >= 0:
        emprecs = list(tuple(emp.strip().split(" ") for emp in employeeslist))
    else:
        print("No data found about employees")
    return emprecs


# What is the average salary in the company?
def get_avg_salary(employees):
    averagesal = 0.0
    if len(employees) > 0:
        averagesal = sum(float(e[3]) for e in employees) / len(employees)
    return averagesal


# What is the name of the oldest employee? What about the youngest?
def find_young_and_old_emp(employees, value=None):
    # reverse = True for descending order
    employees = sorted(employees, key=lambda x: x[1])
    if value == "YOUNG":
        return employees[0]
    else:
        return employees[len(employees) - 1]


# COUNT employess based on different condition
# How many employees are occupying the MNG position? -- By Position
# What is the Male/Female proportion in the company? -- By Gender
# How many employees are there for each of the following age groups: 18-25, 26-35, 36-48, 49-60, 61+? -- By age group
# How many employees are there for each department (position)?
def count_employess(data, filterparamvalue=None, paramposition=None):
    if filterparamvalue == "POSITION":
        empcntbyposition = {}
        for position in set(e[4] for e in data):
            empcntbyposition[position] = len(tuple(e for e in data if e[paramposition] == position))
        return empcntbyposition
    elif filterparamvalue == "M" or filterparamvalue == "F":
        return len(tuple(e for e in data if e[paramposition] == filterparamvalue)) / len(data) * 100
    elif filterparamvalue == "AGEGROUP":
        agegroups = [(18, 25), (26, 35), (36, 48), (49, 60), (61,)]
        empcntbyagegrp = {}
        for agegroup in agegroups:
            if len(agegroup) != 1:
                empcntbyagegrp[agegroup] = len(
                    tuple(e for e in data if int(e[paramposition]) in range(agegroup[0], int(agegroup[1]) + 1)))
            else:
                empcntbyagegrp[agegroup] = len(tuple(
                    e for e in data if int(e[paramposition]) >= agegroup[0]))
        return empcntbyagegrp


# Which department (position) requires the most budget (in terms of salary)?
def get_max_budget_dept(data):
    empbudget = {}
    maxdept = ""
    for position in set(e[4] for e in data):
        empbudget[position] = sum(float(e[3]) for e in data if e[4] == position)
    return max(empbudget, key=lambda p: p[1])


# What is the average between the best and worst salary for each department (position)?
def get_avg_bestandworst_sal_by_position(data):
    empsalavg = {}
    for position in set(e[4] for e in data):
        lst = sorted(list(e[3] for e in data if e[4] == position))
        length = len(lst)
        if length == 0:
            empsalavg[position] = 0
        elif length == 1:
            empsalavg[position] = lst[0]
        else:
            empsalavg[position] = (float(lst[0]) + float(lst[1])) / 2

    return empsalavg


def get_emp_whose_sal_isclosest(data):
    listofemp = sorted(tuple((e[0], e[3]) for e in data), key=lambda x: x[1])
    # print(listofemp)
    # print(tuple(zip(listofemp, listofemp[1:])))
    saldiff = list(abs(float(t[0][1]) - float(t[1][1])) for t in tuple(zip(listofemp, listofemp[1:])))
    # print(listofsal)
    ind = saldiff.index(min(saldiff))
    return listofemp[ind], listofemp[ind + 1]


if __name__ == '__main__':
    emprecords = read_employees()
    if len(emprecords) > 0:
        print("Average Salary of employees {:.2f} ".format(get_avg_salary(emprecords)))
        youngemp = find_young_and_old_emp(emprecords, "YOUNG")
        print("Youngest Employee is : {} and Age is: {} years".format(youngemp[0], youngemp[1]))
        oldemp = find_young_and_old_emp(emprecords, "OLD")
        print("Oldest Employee is : {} and Age is: {} years".format(oldemp[0], oldemp[1]))
        cntempbypos = count_employess(emprecords, "POSITION", 4)
        print("No.Of emplyees who are grouped by position {}".format(cntempbypos))
        print("No.Of emplyees who are {} by position is {}".format("MNG", list(cntempbypos[key] for key in cntempbypos.keys() if key == "MNG")[0]))
        print("No.of emplyees who are {} is {} %".format("M", count_employess(emprecords, "M", 2)))
        print("No.of emplyees who are {} is {} %".format("F", count_employess(emprecords, "F", 2)))
        print("Employees grouped by age {agegroup(min, max): count} :", count_employess(emprecords, "AGEGROUP", 1))
        print("Maximum budget required by {} department".format(get_max_budget_dept(emprecords)))
        print("Avergae of best and worst salary average {}".format(get_avg_bestandworst_sal_by_position(emprecords)))
        print("{} and {} are the employess whose salary is closest".format(get_emp_whose_sal_isclosest(emprecords)[0],
                                                                           get_emp_whose_sal_isclosest(emprecords)[1]))
