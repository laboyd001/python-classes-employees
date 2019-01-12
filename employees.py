# create a class that contains information about an employee (name, job title, start date) def methods to get/set this info

class Employee(object):
    """This represents a person who works at a company"""

    def __init__(self, emp_name, title, start_date):

        self.emp_name = emp_name
        self.job_title = title
        self.job_start_date = start_date

    def __str__(self):
        """Returns the name of the employee"""

        return f"{self.emp_name}"

class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded

        # consider the concept of aggregation and modify the Company class so that you assign employees to a company:
        self._employees = list()

    def get_company_name(self):
        """Returns the name of the company"""
        return self.company_name

    @property
    def employees(self):
        """lists all the employees in the company
        Builds a dict with company (key) and list of employees (value)
        Example:
        {
            "Apple": ['steve jobs', 'steve woz', 'somebody else']
        }
        """
        # create empty dict
        companies_and_emps = dict()
        # get name of company
        company = self.get_company_name()
        # loop over employee list
        for emp in self._employees:
            try:
                # add employees as value for company key
                companies_and_emps[company].append(emp.emp_name)
            except KeyError:
                # create new key value pair with company as key and empty list as value
                companies_and_emps[company] = list()
                # add employee as value for company key
                companies_and_emps[company].append(emp.emp_name)

        # print(companies_and_emp)
        return companies_and_emps

    @employees.setter
    def employees(self, emp):
        """This method adds an employee to list of employees
        
        Arguments:
            emp {Employee} -- Employee obj
        """
        self._employees.append(emp)

    def __str__(self):
        return f"{self.company_name}"

class Industry(object):
    """This represents an industry"""

    def __init__(self, name):
        self.name = name
        self.companies = dict()

    def add_company_to_industry(self, company_obj):

        """add company obj to industry
        
        Arguments:
            company_object {Company} -- Represents a company and includes a list of its employees
        """

        try:
            # try to add company (value) to industry (key)
            self.companies[company_obj.company_name].append(company_obj)
        except KeyError:
            # if key doesn't exist, create new key value pair
            self.companies[company_obj.company_name]= list()
            # add company (value) to industry (key)
            self.companies[company_obj.company_name].append(company_obj)
    
    def list_industries(self):
        """Method to list industries and related companies
        """

        # create empty dictionary
        ind = dict()
        # loop over companies in industry
        for c in self.companies:
            try:
                # add company to industry(key)
                ind[self.name].append(c)
            except KeyError:
                # create new key value pair with industry as key and an empty as value
                ind[self.name] = list()
                # add company to industry(key)
                ind[self.name].append(c)
        print(ind)

    def __str__(self):
        return f"{self.name}"

    # Add the remaining methods to fill the requirements above

# Create a company, and three employees, and then assign the employees to the company:
# if __name__ == '__main__':
# Create the company
ABC = Company('ABC', '12-1-2018')
bridgestone = Company('Bridgestone', 'Long time ago')

# Create some employees
fred = Employee('Fred', 'Analyst', '1-1-2019')
sally = Employee('Sally', 'CEO', '12-28-2018')
joe = Employee('Joe', 'Senior Developer', '1-10-2019')

melissa = Employee('Melissa', 'Manager Sales Analytics', '1-1-2001')
katie = Employee('Katie', 'Analyst', '1-12-2013')
gwen = Employee('Gwen', 'Coordinator', '1-30-2012')

# Add the employees into the  aggregate instance of the company:
ABC.employees = fred
ABC.employees = sally
ABC.employees = joe

bridgestone.employees = melissa
bridgestone.employees = katie
bridgestone.employees = gwen

print("This is the name of the first company:", Company.get_company_name(ABC))
print("\nThis is the name of the second company:", Company.get_company_name(bridgestone))
print("\nHere's the name of the first company and employess:\n",ABC.employees)
print("\nHere's the name of the second company and employess:\n",bridgestone.employees)

# create an industry instance
tires = Industry('Tires')
sales = Industry('Sales')

# add company to industry
tires.add_company_to_industry(bridgestone)
sales.add_company_to_industry(ABC)

print("\nFirst Industry:")
tires.list_industries()
print("\nSecond Industry:")
sales.list_industries()


   


        