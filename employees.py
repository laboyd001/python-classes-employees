# create a class that contains information about an employee (name, job title, start date) def methods to get/set this info

class Employee:
    """This represents a person who works at a company"""

    def __init__(self, emp_name, title, start_date):
        self.emp_name = emp_name
        self.job_title = title
        self.job_start_date = start_date

    def get_employee_name(self):
        """Returns the name of the employee"""

        return self.emp_name

class Company():
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded

        # consider the concept of aggregation and modify the Company class so that you assign employees to a company:
        self.employees = set()

    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name

    def who_works_here(self):
        """Returns the names of the employees"""

        return self.employees

    # Add the remaining methods to fill the requirements above

# Create a company, and three employees, and then assign the employees to the company:
if __name__ == '__main__':
    # Create the company
    ABC = Company('ABC', '12-1-2018')
    bridgestone = Company('Bridgestone', 'Long time ago')

    # Create some employees
    fred = Employee('Fred', 'Analyst', '1-1-2019')
    sally = Employee('Sally', 'CEO', '12-28-2018')
    joe = Employee('Joe', 'Senior Developer', '1-10-2019')

    # Add the employees into the  aggregate instance of the company:
    ABC.employees.add(fred)
    ABC.employees.add(sally)
    ABC.employees.add(joe)

    print("This is the name of the company:", Company.get_company_name(bridgestone))
   


        