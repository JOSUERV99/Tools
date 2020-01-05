#####################################################################################
"""                                                                                 #            
#    Schedule Generator                                                             #    
#    author : Josue Rojas Vega                                                      #
#    since : 9-12-2019                                                              #
#    objective: generate all the posibilities to create my schedules,               #
#                detecting all the collides and save the data in json file          #
"""                                                                                 #        
#####################################################################################

#Libraries
import os, time, json
from random import randint 

class Course:
    def __init__(self, code, name, teacher, credits, sessions={}):
        self.name = name
        self.code = code
        self.teacher = teacher
        self.credits = credits
        self.sessions = sessions
        self.__dict__ = {"name":self.name, "code":self.code, "teacher":self.teacher, "credits":self.credits, "sessions": self.dictHours()}   
    def collide(self, otherCourse):
        def getHour(hourWithFormat): # 13:00 for example
            return int(hourWithFormat[:2])*100 + int(hourWithFormat[3:])
        for i in self.sessions:
            for j in otherCourse.sessions:
                if i == j:
                    hourStart = getHour(self.sessions[i]["startHour"])
                    hourFinal = getHour(self.sessions[i]["finalHour"])
                    otherHourStart = getHour(otherCourse.sessions[j]["startHour"])
                    otherHourFinal = getHour(otherCourse.sessions[j]["finalHour"])
                    if hourStart in range(otherHourStart, otherHourFinal) or hourFinal in range(otherHourStart, otherHourFinal) :
                        print(hourStart, "-> r({},{})".format(otherHourStart, otherHourFinal), "\n", hourFinal , "-> r({},{})".format(otherHourStart, otherHourFinal))
                        return True
        return False
    def dictHours(self):
        dictionary = {}
        for d in self.sessions:
            dictionary.update(d.__dict__)
        return dictionary
    def saveJson(self):
        with open('{}.json'.format("{}_{}".format(self.code, self.name)), 'w') as file:
            json.dump(self.__dict__, file)

class Session:
    def __init__(self, day, startHour, finalHour):
        self.day = day
        self.startHour = startHour
        self.finalHour = finalHour
        self.__dict__ = {str(self.day): {"startHour":self.startHour, "finalHour":self.finalHour}}

class Generator:
    def __init__(self, coursesOptions={}):
        self.coursesOptions = coursesOptions
    def addCourse(self, course):
        if course not in self.coursesOptions:
            self.coursesOptions[course.name] = course
        else:
            self.coursesOptions[course.name] += course
    def generateDict(self):
        _dict = {}
        for keyCourse in self.coursesOptions:
            _dict[keyCourse] = {}
            for course in _dict[keyCourse]:
                _dict[keyCourse].update(course.__dict__)
        return _dict
    def saveJson(self):
        with open('{}.json'.format("courses"), 'w') as file:
            json.dump(self.generateDict(), file)

# [Code, Name, Teacher, Credits, [[Day, [startHour, finalHour]], [Day, [startHour, finalHour]] ]]
session1A = Session("K", "13:00", "14:50")
session2A = Session("J", "13:00", "14:50")
session1B = Session("K", "13:00", "15:55")
session2B = Session("J", "16:00", "16:50")

courseA = Course("IC2001", "Data Structures", "Fulano Mengano", 3, [session1A, session2A])
courseB = Course("IC2001", "Data Structures", "Fulano Mengano", 3, [session1B, session2B])

gen = Generator()
gen.addCourse(courseA)
gen.addCourse(courseB)
print(courseA.collide(courseB))