"""    
@objective Normalizing courses data from u-page                                                                                                                                                       
@author Josue Rojas Vega                                                      
@since 9-12-2019                                                              
"""                                                                                       
import os, time, json
from random import randint 
import EnrollmentBot as bot

class Course:
    def __init__(self, code, group, name, teacher, credits, sessions={}):
        self.name = name
        self.group = group
        self.code = code
        self.teacher = teacher
        self.credits = credits
        self.sessions = sessions
        self.__dict__ = {"name":self.name, "group":self.group, "code":self.code, "teacher":self.teacher, "credits":self.credits, "sessions": self.dictHours()}   
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
    def __init__(self, coursesOptions=[]):
        self.coursesOptions = coursesOptions
    def dataToScrapy(data):
        pass
    def addCourse(self, course):
        if course not in self.coursesOptions:
            self.coursesOptions.append(course)
    def dictCourses(self):
        dictionary = {}
        for course in self.coursesOptions:
            tagGroup = "G{}".format(course.group)
            tagCourse = course.name
            if tagCourse not in dictionary:
                dictionary[tagCourse] = {tagGroup: course.__dict__}
            else:
                dictionary[tagCourse].update({tagGroup: course.__dict__})
        return dictionary
    def saveJson(self):
        with open('{}.json'.format("courses"), 'w') as file:
            json.dump(self.dictCourses(), file)

# [Code, Name, Teacher, Credits, [[Day, [startHour, finalHour]], [Day, [startHour, finalHour]] ]]
# session1A = Session("K", "13:00", "14:50")
# session2A = Session("J", "13:00", "14:50")
# session1B = Session("K", "13:00", "15:55")
# session2B = Session("J", "16:00", "16:50")
# courseA = Course("IC2001", 3, "Data Structures", "Fulano Mengano", 3, [session1A, session2A])
# courseB = Course("IC2001", 4, "Data Structures", "Fulano Mengano", 3, [session1B, session2B])
# gen = Generator()
# gen.addCourse(courseA)
# gen.addCourse(courseB)
# print(gen.dictCourses())
# gen.saveJson()
#print(courseA.collide(courseB))

