class Student:
    def __init__(self , name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Ім'я: {self.name} "
              f"\nРік: {self.age}")
student = Student("Захар" , 15)
student.info()