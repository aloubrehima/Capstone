from dataclasses import dataclass

@dataclass  # Define the dataclass
class Student:
    name: str
    school_id: str
    gpa: float # new filed for gpa

def main():
    alex = Student('Alex', 'zd3860gz', 4.0)
    print(alex.name)  # Print the name of the student
    print(alex.school_id)  # Print the school ID of the student
    print(alex.gpa)  # Print the GPA of the student
    print(alex)


jack = Student('Jack', '7683778', 3.9)
print(jack)

abdallah = Student('Abdallah', 'jkd87df', 2.5)
print(abdallah)




if __name__ == "__main__":
    main()

