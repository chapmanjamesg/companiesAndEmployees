import datetime

class Employee:
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title
        self.start_date = datetime.date.today()



class Company:
    def __init__(self, name, address, ind_type):
        self.name = name
        self.address = address
        self.ind_type = ind_type
        self.employee = list()

    def report(self):
        print(f"{self.name} is in the {self.ind_type} industry and has the following employees")
        for i in self.employee:
            print(f"* {i.name}")

    
# Employees
terry = Employee("Terry", "dog walker")
stan = Employee("Stan", "fourth grader")
particle_man = Employee("Particle Man", "superhero")
person_man = Employee("Person Man", "punchline")
triangle_man = Employee("Triangle Man", "triangle")

# Companies
cruise_line_entertainment = Company("Cruise Line Entertainment", "33 3rd street", "TV studio")
particle_company = Company("The Particle Company", "44 4th blvd", "energy")

# Hiring process

cruise_line_entertainment.employee.append(terry)
cruise_line_entertainment.employee.append(stan)
particle_company.employee.append(particle_man)
particle_company.employee.append(person_man)
particle_company.employee.append(triangle_man)

cruise_line_entertainment.report()
particle_company.report()