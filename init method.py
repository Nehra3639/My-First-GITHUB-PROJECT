class employee():
    pass
    def __init__(self, fname, lname, pay):
         self.fname = fname
         self.lname = lname
         self.pay = pay
         self.email = fname + "." + lname + "@gmail.com"
     
     
emp1 = employee("Kapil", "nehra", "50000")
emp2 = employee("Akshansh", "nehra",  "65000")
     
print(emp1.fname)
print(emp2.fname)
print(emp1.lname)
print(emp2.lname)
print(emp1.email)
print(emp2.email)
print(emp1.pay)
print(emp2.pay)
 