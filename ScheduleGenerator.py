#####################################################################################
"""                                                                                 #            
#    Schedule Generator                                                             #    
#    author : Josue Rojas Vega                                                      #
#    since : 9-12-2019                                                              #
#    objective: generate all the posibilities to create my schedules,               #
#                detecting all the collides                                         #
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
    def __dict__(self):
        return {"name":self.name, "code":self.code, "teacher":self.teacher, "credits":self.credits, "sessions": { x for x in self.sessions }}
    
    def courseCollide(self, otherCourse):
        def getHour(hourWithFormat): # 13:00 for example
            return int(hourWithFormat[:2])*10 + int(hourWithFormat[3:])
        for i in range(len(self.sessions)):
            for j in range(len(otherCourse.sessions)):
                if getHour(self.sessions[i].startHour) in \
                range(getHour(otherCourse.sessions[j].startHour),  getHour(otherCourse.sessions[j].finalHour)):
                    return True
        return False

class Session:
    def __init__(self, day, startHour, finalHour):
        self.day = day
        self.startHour = startHour
        self.finalHour = finalHour
    def __dict__(self):
        return {str(self.day): { "startHour":self.startHour, "finalHour":self.finalHour}}

class Generator:
    def __init__(self, coursesOptions):
        self.coursesOptions = coursesOptions

# [Code, Name, Teacher, Credits, [[Day, [startHour, finalHour]], [Day, [startHour, finalHour]] ]]
session1 = Session("K", "13:00", "14:50")
session2 = Session("J", "13:00", "14:50")
course = Course("IC2001", "Data Structures", "Fulano Mengano", 3, [session1, session2])
print(course.__dict__())
