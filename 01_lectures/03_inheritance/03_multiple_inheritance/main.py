from project.employee import Employee
from project.person import Person
from project.teacher import Teacher

p = Person()
t = Teacher()
e = Employee()

print(p.sleep())
print(t.teach())
print(e.get_fired())
