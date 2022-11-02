class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        gpa_characters = set("1234567890-.")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname) and name_characters.issuperset(major)):
            raise ValueError
        if not isinstance(gpa, float) or (gpa < 0.0) or (gpa > 4.0):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)


if __name__ == '__main__':
    student1 = Student('Heinrichs', 'Alex', 'CIS', 4.0)
    student2 = Student('Heimlik', 'Ahlix', 'CIS', 3.0)
    print(student1)
    print(student2)
