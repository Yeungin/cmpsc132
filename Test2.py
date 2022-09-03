# LAB2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement

import random
from re import X

class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''
    def __init__(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        # initiallzing attributes
        self.cid = cid
        self.cname = cname
        self.credits = credits


    def __str__(self):
        # YOUR CODE STARTS HERE
        return "{}({}): {}".format(self.cid, self.credits, self.cname) #printing the course info

    __repr__ = __str__

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        if isinstance(other, Course): #checking if two courses are the same
            if self.cid == other.cid:
                return True
            else:
                return False
        else: 
            return False


class Catalog:
    ''' 
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> C.courseOfferings
        {'CMPSC132': (CMPSC132(3): Programming in Python II, 400), 'CMPSC360': (CMPSC360(3): Discrete Mathematics, 200)}
        >>> C.removeCourse('CMPSC360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC132': (CMPSC132(3): Programming in Python II, 400)}
        >>> isinstance(C.courseOfferings['CMPSC132'][0], Course)
        True
    '''

    def __init__(self):
        # YOUR CODE STARTS HERE
        self.courseOfferings = {} #initiallizing the .courseOfferings dict

    def addCourse(self, cid, cname, credits, capacity):
        # YOUR CODE STARTS HERE
        if cid not in self.courseOfferings: #check if the course is already in the dict, if not, add it
            self.courseOfferings[cid] = Course(cid, cname, credits), capacity
            return f"Course added successfully"
        else:
            return f"Course added already"

    def removeCourse(self, cid): #check if the course is in the dict, if so, remove it
        if cid in self.courseOfferings:
            del self.courseOfferings[cid]
            return f"Course removed successfully"
        else:
            return f"Course not found"

class Semester:
    '''
        >>> cmpsc131 = Course('CMPSC131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> semester = Semester(1)
        >>> semester
        No courses
        >>> semester.addCourse(cmpsc132)
        >>> isinstance(semester.courses['CMPSC132'], Course)
        True
        >>> semester.addCourse(math230)
        >>> semester
        CMPSC132, MATH 230
        >>> semester.isFullTime
        False
        >>> semester.totalCredits
        7
        >>> semester.addCourse(phys213)
        >>> semester.addCourse(econ102)
        >>> semester.addCourse(econ102)
        'Course already added'
        >>> semester.addCourse(phil119)
        >>> semester.isFullTime
        True
        >>> semester.dropCourse(phil119)
        >>> semester.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> semester.totalCredits
        16
        >>> semester.dropCourse(cmpsc131)
        'No such course'
        >>> semester.courses
        {'CMPSC132': CMPSC132(3): Programming in Python II, 'MATH 230': MATH 230(4): Calculus, 'PHYS 213': PHYS 213(2): General Physics, 'ECON 102': ECON 102(3): Intro to Economics, 'JAPNS 001': JAPNS 001(4): Japanese I}
    '''

    def __init__(self, sem_num):
        # --- YOUR CODE STARTS HERE
        self.sem_num = sem_num #initializing attributes
        self.courses = {}



    def __str__(self):
        # YOUR CODE STARTS HERE
        str = "" #probably not the best way to format the list of courses, but it works
        for key in self.courses:
            if bool(str) == False:
                str += self.courses[key].cid
            else:
                str += ", " + self.courses[key].cid
        if bool(self.courses) == True:
            return f"{str}"
        else:
            return f"No courses"

    __repr__ = __str__

    def addCourse(self, course):
        # YOUR CODE STARTS HERE
        if course.cid not in self.courses: #checking if the course is in the dict, if not, add it
            self.courses[course.cid] = course
        else: 
            return f"Course already added"

    def dropCourse(self, course):
        # YOUR CODE STARTS HERE
        if course.cid in self.courses: #checking if the course is in the dict, if so, remove it
            del self.courses[course.cid]
        else:
            return f"No such course"

    @property
    def totalCredits(self):
        # YOUR CODE STARTS HERE
        cred = 0
        for key in self.courses: #calculate the amount of credits when called by itterating through each dict entry and adding the credit values
            cred += self.courses[key].credits
        return cred

    @property
    def isFullTime(self):
        # YOUR CODE STARTS 
        if self.totalCredits >= 12: #if the student currently has 12 or more credits, they are a fulltime
            return True
        else:
            return False

class Loan:
    '''
        >>> import random
        >>> random.seed(2)  # Setting seed to a fixed value, so you can predict what numbers the random module will generate
        >>> first_loan = Loan(4000)
        >>> first_loan
        Balance: $4000
        >>> first_loan.loan_id
        17412
        >>> second_loan = Loan(6000)
        >>> second_loan.amount
        6000
        >>> second_loan.loan_id
        22004
        >>> third_loan = Loan(1000)
        >>> third_loan.loan_id
        21124
    '''
    

    def __init__(self, amount):
        # YOUR CODE STARTS HERE
        self.loan_id = self.__getloanID
        self.amount = amount



    def __str__(self):
        # YOUR CODE STARTS HERE
        return "Balance: ${}".format(self.amount)

    __repr__ = __str__


    @property
    def __getloanID(self):
        loanID = random.randint(10000, 99999)
        return loanID

class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''

    def __init__(self, name, ssn):
        # YOUR CODE STARTS HERE
        self.name = name
        self._ssn = ssn

    def __str__(self):
        # YOUR CODE STARTS HERE
        ssn_4 = self._ssn[-4:]
        return "Person({}, ***-**-{})".format(self.name, ssn_4)

    __repr__ = __str__

    def get_ssn(self):
        # YOUR CODE STARTS HERE
        return f"{self._ssn}"

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        if isinstance(other, Person):
            if self._ssn == other._ssn:
                return True
        return False

class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> st1 = s1.createStudent(p)
        >>> isinstance(st1, Student)
        True
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC360', C, 1)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC132}
    '''
    def __init__(self, name, ssn, supervisor=None):
        # YOUR CODE STARTS HERE
        self.supervisor = supervisor
        
        super().__init__(name,ssn)


    def __str__(self):
        # YOUR CODE STARTS HERE
        return "Staff({}, {})".format(self.name, self.id)

    __repr__ = __str__


    @property
    def id(self):
        # YOUR CODE STARTS HERE
        id = "905"
        full_name = self.name.split()
        for word in full_name: #getting initials
            id = id + word[:1].lower()
        id = id + self._ssn[-4:]
        return id

    @property   
    def getSupervisor(self):
        # YOUR CODE STARTS HERE
        if self.supervisor == None:
            pass
        else:
            return self.supervisor

    def setSupervisor(self, new_supervisor):
        # YOUR CODE STARTS HERE
        if isinstance(new_supervisor, Staff):
            self.supervisor = new_supervisor
            return f"Completed!"

    def applyHold(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.holds = True
            return f"Completed!"
        

    def removeHold(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.holds = False
            return f"Completed!"

    def unenrollStudent(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.active = False
            return f"Completed!"

    def createStudent(self, person):
        # YOUR CODE STARTS HERE
        self.student = Student(person.name, person._ssn, "Freshman")
        return self.student

class Student(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC311', C, 1)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132, CMPSC360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC132', C, 1)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC360')
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC360')
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: No courses}
        >>> s1.enrollCourse('CMPSC360', C, 2)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
    '''
    def __init__(self, name, ssn, year):
        random.seed(1)
        # YOUR CODE STARTS HERE
        super().__init__(name, ssn)
        self.year = year
        self.semesters = {}
        self.holds = False
        self.active = True
        self.account = None

    def __str__(self):
        # YOUR CODE STARTS HERE
        return "Student({}, {}, {})".format(self.name, self.id, self.year)

    __repr__ = __str__
    
    def __createStudentAccount(self):
        # YOUR CODE STARTS HERE
        if self.active == True:
            self.account = StudentAccount(self)
            


    @property
    def id(self):
        # YOUR CODE STARTS HERE
        id = ""
        full_name = self.name.split()
        for word in full_name: #getting initials
            id = id + word[:1].lower()
        id = id + self._ssn[-4:]
        return id

    def registerSemester(self):
        # YOUR CODE STARTS HERE
        if (self.holds == False) and (self.active == True):
            sem_num = len(self.semesters) + 1
            sem = Semester(sem_num)
            self.semesters[sem.sem_num] = sem
            
            if sem_num == 1 or sem_num == 2:
                self.year == "Freshman"
            if sem_num == 3 or sem_num == 4:
                self.year == "Sophmore"
            if sem_num == 5 or sem_num == 6:
                self.year == "Junior"
            if sem_num > 6:
                self.year == "Senior"
        else:
            return f"Unsuccessful operation"
        pass


    def enrollCourse(self, cid, catalog, semester):
        if (self.holds == True) or (self.active == False):
            return "Unsuccessful operation"
        if cid not in catalog.courseOfferings:
            return "Course not found"
        if cid in self.semesters[semester].courses:
            return "Course already enrolled"
        course = catalog.courseOfferings[cid]
        self.semesters[semester].courses[cid] = course
        #credits = course[0].credits
        #self.account.chargeAccount(credits*1000)
        return "Course added successfully"


    def dropCourse(self, cid):
        # YOUR CODE STARTS HERE
        if (self.holds == False) and (self.active == True):
            if cid in self.semesters[len(self.semesters)]:
                self.semesters[self.sem_num].remove(cid)
                #refund half of the money
                #self.account.makePayment(self.semesters[self.sem_num].courses*500)
                return "Course dropped successfully"
            else:
                return "Course not found"
        else:
            return "Unsuccessful operation"


    def getLoan(self, amount):
        # YOUR CODE STARTS HERE
        if self.active == True:
            if self.sem.isFullTime == True:
                self.loan = Loan(amount)
                self.account.makePayment(amount)
            else:
                return "Not full-time"
        else:
            return "Unsuccessful operation"

if __name__=='__main__':
    import doctest
    #doctest.testmod()
    doctest.run_docstring_examples(Staff, globals(), name='HW22',verbose=True)