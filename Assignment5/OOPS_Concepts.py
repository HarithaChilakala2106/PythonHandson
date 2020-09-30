class RestaurantStaff:
    def __init__(self, name, phone, email, address, salary):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.salary = salary

    def __str__(self):
        return f"Staff Name :{self.name} Phone: {self.phone}  Email : {self.email}  Address :{self.address}  Salary : {self.salary}"


# Chef is a child class which extends RestaurantStaff
class Chef(RestaurantStaff):
    def __init__(self, name, phone, email, address, salary, cuisine_expertise):
        super().__init__(name, phone, email, address, salary)
        self.cuisine_expertise = cuisine_expertise

    def __str__(self):
        return f"Chef : {super(Chef, self).__str__()} {self.cuisine_expertise}"

    @staticmethod
    def prepare_menu():
        print("processed staff payroll")

    @staticmethod
    def take_dish_name():
        print("Took Dish name")


# RestaurantManager is a child class which extends RestaurantStaff
class RestaurantManager(RestaurantStaff):
    def __init__(self, name, phone, email, address, salary, employeescnt):
        super().__init__(name, phone, email, address, salary)
        self.employeescnt = employeescnt

    def __str__(self):
        return f"RestaurantManager : {super(RestaurantManager, self).__str__()} Employeescnt : {self.employeescnt}"

    @staticmethod
    def staff_payroll():
        print("processed staff payroll")

    @staticmethod
    def calculate_billing():
        print("Billing details calculated")

    @staticmethod
    def provide_bill():
        print("Bill has been given")


# Server is a child class which extends RestaurantStaff
class Server(RestaurantStaff):
    def __init__(self, name, phone, email, address, salary, assignedtables):
        super().__init__(name, phone, email, address, salary)
        self.assignedtables = assignedtables

    def __str__(self):
        return f"Server : {super(Server, self).__str__()} assignedtables : {self.assignedtables}"

    @staticmethod
    def fulfill_book_table_request():
        print("Table request has been served")

    @staticmethod
    def take_customer_order():
        print("Took order from customer")

    @staticmethod
    def send_order_to_kitchen():
        print("ordersent to kitchen")


# Custome is a class
class Customer:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Customer Name :{self.name} Phone: {self.phone}  Email : {self.email}"

    def send_book_table_request(self):
        print("Sent request for table booking", self.name)

    @staticmethod
    def give_order():
        print("Order placed")

    @staticmethod
    def ask_bill():
        print("Requested for bill")


if __name__ == '__main__':
    staff = RestaurantStaff("Haritha", 12376543, "haritha@gmail.com", "Munich", 6000)
    # print(staff.__str__())

    staff.name = "Harika"
    print(staff)

    chef = Chef("Kanth", 123566544, "Kanth@gmail.com", "Munich", 4000, "[panner,roti,salad,juice]")
    print(chef.__str__())
    chef.take_dish_name()
    chef.prepare_menu()

    mgr = RestaurantManager("Jitendra", 8777687654, "Jitendra@gmail.com", "Munich", 4000, 30)
    print(mgr.__str__())
    mgr.staff_payroll()
    mgr.calculate_billing()
    mgr.provide_bill()

    server = Server("Naveen", 123566544, "Naveenh@gmail.com", "Munich", 2000, "[1,4,5]")
    print(server.__str__())
    server.fulfill_book_table_request()
    server.take_customer_order()
    server.send_order_to_kitchen()

    customer = Customer("Amoolya", 345687655, "amoolya@gmail.com")
    print(customer.__str__())
    customer.send_book_table_request()
    customer.give_order()
