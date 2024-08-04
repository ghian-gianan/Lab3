def __eq__(self, other):
    """Return if equal or not"""
    if (self.name == other.name):
        return "Equal"
    else:
        return "Not Equal"
    
def __li__(self, other):
    """Returns if less than or not"""
    if (self.name < other.name):
        return "Less Than"
    else:
        return "Not Less Than"
    
def __gt__(self, other):
    if self.name > other.name:
        return "Greater Than"
    elif self.name == other.name:
        return "Both are Equal"
    else:
        return "Not Greater Than nor Equal"
    
def main():
    """A simple test."""
    student = Student("StudentBoy", 5)
    
    for i in range(1, 6):
        student.setScore(i, 100)
    print(student)
    
    student2 = Student("StudentGirl", 5)
    
    for i in range(1, 6):
        student2.setScore(i, 100)
        
        print(student2)
        print("\n")
        print("-------COMPARISON-------")
        print(student==student2)
        print(student<student2)
        print(student2<student)
        print(student>student2)
        print("\n")