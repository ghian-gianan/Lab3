def main():
    """A simple test."""
    student = []
    
    student = Student("Justine", 5)
    for i in range(1, 6):
        student.setScore(i, 100):
    studentList.append(student)
    
    student1 = Student("Mon", 8)
    for i in range(1, 9):
        student1.setScore (i, 100)
    studentList.append(student)
    
    student2 = Student("Darren", 5)
    for i in range(1, 6):
        student2.setScore(i, 100)
    studentList.append(student2)
    
    random.shuffle(studentList)
    
    print("Shuffled list of Student: ")
    
    for i in studentList:
        print(i.__str__())
        
    print("\nSorted list of Student: ")
    
    studentList.sort(key = lambda x:x.name)
    
    for i in studentList:
        print(i.__str__())
        
if __name__ = "__main__":
    main()