class person(object):
    def __init__(self, name, age):  # takes input for name and age, can take input for
        # height and birthday, but those are set in the setter
        assert type(name) is str  # Checks that any input values are of the right type
        self.name = name
        assert type(age) is int  # throws error if condition is not true
        self.age = age

    def heightSetter(self, heightIn):  # has a setter for height to set without using height in the initializer,
        # generally good practice, but not necessary for basic cases in python, can be helpful for variable naming
        # differences or changing/accessing specific parts of each instance
        assert type(heightIn) is height  # assert statement throws error if type of heightIn is not height
        self.height = heightIn

    def birthdaySetter(self, birthday):  # makes a setter for birthday to set without using birthday in the initializer
        assert type(birthday) is date  # assert throw error if condition is not try
        self.birthday = birthday

    def heightGetter(self):  # gets the height out specifically, can be access in python with instance.height, but that
        # isn't a very safe way to do it in other languages and can get messy in python if variable names are different or
        # you're returning a user created data type
        if self.height is not None:
            return self.height
        else:
            raise ValueError("Height not set")

    def birthdayGetter(self):
        if self.birthday is not None:
            return self.birthday
        else:
            raise ValueError("Birthday not set")

    def lastNameGetter(self):  # getters can also be used to return specific things, ex: only the last name from a name
        names = self.name.split(" ")
        return names[-1]


class binghamtonPerson(person):
    idNumber = 0  # this is a class variable, it does not depend on the instance (can always be set the same,

    # increments in this case, but no input to the instance makes a difference to what this is

    def __init__(self, name, age):
        person.__init__(self, name, age)  # . searches through operator to find method, calls
        # __init__ method from person
        self.ID = binghamtonPerson.idNumber
        binghamtonPerson.idNumber += 1

    def __lt__(self,
               otherBinghamtonPerson):  # remap the greater than/less than operators to check ID number between two
        # binghamton people instead of default which which would throw error
        return self.idNumber < otherBinghamtonPerson.idNumber

    def __gt__(self, otherBinghamtonPerson):
        return self.idNumber > otherBinghamtonPerson.idNumber

    def say(self, msg):  # prints the students name followed by what they said
        return self.lastNameGetter() + ' says: ' + str(msg)


class student(binghamtonPerson):  # applies the property of being a student to any students (underGrad/Grad/Transfer),
    # makes is Student function run much easier
    pass


class underGrad(student):
    def __init__(self, name, age, graduationYear):
        binghamtonPerson.__init__(self, name, age)  # creates the undergrad as a student which is a
        # binghamtonPerson, which is a person, which is an object
        assert type(graduationYear) is int
        self.graduationYear = graduationYear  # assigns the new property that wasn't set in the binghamtonPerson part
        # of __init__

    def say(self, msg):
        return binghamtonPerson.say(self, 'Dude, ' + msg)  # calls the binghamtonPerson version of say with the rest as
        # the input to that


class gradStudent(student):  # implement to see how being a student causes differences between underGrad/grad/transfer
    def __init__(self, name, age, degreeType):
        binghamtonPerson.__init__(self, name, age)
        assert type(degreeType) is str
        self.degree = degreeType

    def say(self, msg):
        return self.degree + ' ' + binghamtonPerson.say(self, msg)


class transferStudent(student):
    def __init__(self, name, age, fromWhere):
        binghamtonPerson.__init__(self, name, age)
        assert type(fromWhere) is str
        self.previousSchool = fromWhere

    def say(self, msg):
        return underGrad.say(self, 'at ' + self.previousSchool + ' we say ' + msg)


class professor(binghamtonPerson):
    def __init__(self, name, age, department):
        binghamtonPerson.__init__(self, name, age)
        self.department = department

    def say(self, msg):
        new = 'In ' + str(self.department) + ' courses, we say '
        return binghamtonPerson.say(self, new + msg)

    def lecture(self, topic):  # calls it's own method for say to pass arguments into that which in turn calls
        # binghamtonPerson's method for stay with another concatonation to the string being passed
        return self.say('it is obvious that ' + topic)


def isStudent(person):
    """
    Function to check whether or not the person is any type of student
    setting all types of students as students with the pass class above makes this function much easier to run by
    only having to check one thing
    ex without student:
    #return isinstance(person, underGrad) or isinstance(person, gradStudent) or isinstance(person,transferStudent)
    """
    return isinstance(person, student)


class grades(object):
    def __init__(self):  # creates empty gradeBook
        self.students = []  # list of students
        self.grades = {}  # dictionary to associate ID with grades
        self.isSorted = True  # sorted by default since there is nothing in it

    def addStudent(self, student):
        if not isStudent(student):  # throws error if the input is not a student
            raise TypeError('Must add object of type student to addStudent')
        if student in self.students:  # Throws error if student is already in the list
            raise ValueError('Duplicate Student')
        self.students.append(student)
        self.grades[student.ID] = []  # makes new dict entry for student
        # in most languages, and in some cases in python you should use a getter instead of just accessing student.ID, but in this case it is safe to access with just the . instead of writing a getter method
        self.isSorted = False  # since input is unsorted, adding a new student will unsort the gradebook

    def addGrade(self, student, grade):
        assert (type(grade) is int) or (type(grade) is float)
        try:
            self.grades[student.ID].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')

    def getGrades(self, student):
        try:
            return self.grades[student.ID][:]  # [:] on the end makes a copy of the grades to avoid accidentally changing
        except KeyError:
            raise ValueError('Student not in grade book')

    def allStudentGetter(self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.students: #uses a generator instead of returning a copy of this list to avoid over using memory.
            yield s.ID # yield returns the value shown and stops the program until __next__ method is called
                    # in this case, yield will only return one student at a time, waiting for whatever calls the
                    # studentGetter to request another student

    def gradeReportMethod(self):
        #does the exact same thing as grade report function, but called in class instead of as function
        # just used to show different ways to call the same thing in classes
        report = []
        for id in self.allStudentGetter(): #allStudentGetter returns the student ID
            total = 0.0
            numGrades = 0
            for g in self.grades[id]:
                total += g
                numGrades += 1
            try:
                average = total / numGrades
                report.append(self.students[len(report)].name + "'s mean grade is " + str(average))
            except ZeroDivisionError:
                report.append(self.students[len(report)].name + " has no grades")
        return "\n".join(report)

def gradeReportFunction(course):
    #does the exact same thing as gradeReportMethod, but can be called as a function instead
    #just used to show different ways to call the same thing in classes
    report = []
    for s in course.allStudentGetter():
        total = 0.0
        numGrades = 0
        for g in course.grades[s]:
            total += g
            numGrades += 1
        try:
            average = total / numGrades
            report.append(self.students[len(report)].name + "'s mean grade is " + str(average))
        except ZeroDivisionError:
            report.append(self.students[len(report)].name + " has no grades")
    return '\n'.join(report)

nathan = underGrad('Nathan Frank', 22, 2019)
brandi = binghamtonPerson('Brandi', 22)
foreman = professor('Dennis Foreman', 100, 'CS 311')
doc = gradStudent('Joe', 25, 'PHD')
ralph = transferStudent('Ralph', 20, 'RIT')

myGrades = grades()
myGrades.addStudent(doc)
myGrades.addStudent(ralph)
myGrades.addStudent(nathan)
myGrades.addGrade(nathan, 100)
myGrades.addGrade(nathan, 95)
myGrades.addGrade(doc, 75)
myGrades.addGrade(doc, 70)
myGrades.addGrade(doc, 75)
myGrades.addGrade(nathan, 80)
myGrades.addGrade(nathan, 95)
myGrades.getGrades(nathan)
myGrades.addGrade(doc, 90)
myGrades.addGrade(doc, 80)
myGrades.addGrade(nathan, 90)
myGrades.addGrade(ralph, 45)
myGrades.addGrade(ralph, 75)
myGrades.addGrade(ralph, 100)
myGrades.addGrade(ralph, 59)
myGrades.addGrade(ralph, 47)
myGrades.addGrade(ralph, 100)
myGrades.addGrade(ralph, 0)
myGrades.addGrade(ralph, 50)
myGrades.addGrade(ralph, 89)
myGrades.addGrade(ralph, 67)


# moving out of the way for now
class height(object):  # create data type to store height
    def __init__(self, feet, inches):
        if type(feet) is not int:
            raise TypeError("Please input your height in feet as an integer")
        if (type(inches) is not int) and (type(inches) is not float):
            raise TypeError("Please input your height in inches as a number")
        self.feet = feet
        self.inches = inches

    def __str__(self):  # replaces the normal string method in python
        return str(self.feet) + "'" + str(self.inches) + '"'

    def heightInInches(self):
        return (12 * self.feet) + self.inches


class date(object):  # create data type for date, does not require a year
    def __init__(self, month, day, year=None):
        if type(day) is not int or type(month) is not int:  # or type(year) is not int:
            raise TypeError("Day and month must both be of type int")
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        if self.year is None:
            return str(self.month) + '/' + str(self.day)
        return str(self.month) + '/' + str(self.day) + '/' + str(self.year)
