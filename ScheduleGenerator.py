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
import os
from random import randint
import time 

# Constants?
days = ["L", "K", "M", "J", "V", "S"]
some_headers = ["Codigo", "Nombre", "Profesor", "Creditos"]
schedules_generated = []
courses_list = []
id_count = 0

def writeFile(filename, data):
    #data is a list of schedules->(list of courses)
    file = open(filename, "w")
    file.write("-----------------------------------------------")
    file.write("\tSchedules generated: \n")
    file.write("-----------------------------------------------")
    for schedule in data:
        # iterating into the schedules
        file.write(schedule[0]) #shedule id
        file.write(schedule[1]) #credits for schedule
        for course in schedule[2]:
            #iterating into the courses
            file.write(course_to_string(course))
        file.write("-----------------------------------------------")
    file.close()

def courseCollide(startHour, finalHour, otherStartHour, otherFinalHour):
# (1200, 1350, 1300, 14:50) collide X
    return otherStartHour in range(otherStartHour, otherFinalHour+1) \
        or otherFinalHour in range(otherStartHour, otherFinalHour+1)

def getDaysPerCourse(course):
# [ "L", "M" ]
    return [ day[0] for day in course[4] ]

def getRealHour(hour):
# 12:00 -> 1200 (for verify range later)
    return int(hour[:2])*100 + int(hour[3:])

def rightHour(hour):
# Format: 00:00 -> 23:59
    return len(hour) == 5 and int(hour[:2]) in range(0, 24) \
        and int(hour[3:]) in range(0, 60)

def course_to_string(course):
    # ["Codigo", "Nombre", "Profesor", "Creditos"]
    string = ">>>>>>>>>>>>>>>>>>>>>>>>>>>\n";
    string += "Codigo  : "+course[0]+"\n"
    string += "Nombre  : "+course[1]+"\n"
    string += "Profesor: "+course[2]+"\n"
    string += "Creditos: "+str(course[3])+"\n"
    string += "Horario :\n"
    for day in course[4]:
        string += day[0] #initial letter
        string += day[1][0] #start hour
        string += day[1][1] + "\n" #final hour
    string += "<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
    print(string)
    return string

def showCourses():
    global courses_list
    if (len(courses_list) != 0 ):
        print("Mostrando cursos: ")
        for course in courses_list:
            print(course_to_string(course))
        input("")
    else:
        print("No hay cursos a mostrar")

def menu():
    # Menu
    print("---Generador de Horarios---")
    print("0. Mostrar cursos          ")
    print("1. Agregar curso           ")
    print("2. Eliminar curso          ")
    print("3. Generar Horarios        ")
    print("4. Generar archivo  (.txt) ")
    print("5. Salir                   ")
    print("---------------------------")

def getDay(day, startHour, finalHour):
    return [day, startHour, finalHour]

def getCourse(code, name, teacher, credits, days):
    return [code, name, teacher, credits, days]

def createCourse():
# [Code, Name, Teacher, Credits, [[Day, [startHour, finalHour]], [Day, [startHour, finalHour]] ]]
# ['IC-2001', 'Estructuras de Datos', 'XXXXXXXXXXXXX', '4', [['M', ['09:30', '11:20']], ['V', ['9:30', '11:20']]]]
    global some_headers, days
    course = []
    for header in some_headers:
        course += [input(header + " :")]
    schedule_course = []
    day_amount= int(input("Cantidad de Dias:"))
    for i in range(day_amount):
        day = []
        day.append(input("Elige el {0} dia: {1} \n ->".format(str(i+1),days)))
        hour = []
        hour.append(input("Hora inicial: "))
        hour.append(input("Hora final: "))
        day.append(hour)
        schedule_course.append(day)       
    course.append(schedule_course)
    print(course)
    return course

def getCreditsPerShedule(courses):
    # the sum of the credits for each course
    return sum( [(int(course[3]) for course in courses)] )

def getSchedule(scheduleId, courses):
    # Schedule Id, credits, [.....
    # [Code, Name, Teacher, Credits, [[Day, [startHour, finalHour]], [Day, [startHour, finalHour]] ]]
    # ...]
    return [scheduleId, getCreditsPerShedule(courses), courses]

def contains_course(code, courses):
    codes = set( course[0] for course in courses )
    return code in codes

def haveAllTheCourses(next_shedule):
    global courses_list
    codes =  set( course[0] for course in courses_list )
    for course in next_shedule:
        if not course[0] in codes:
            return False
    return True

def generateSchedules():
    #generate all the posibilities with all the courses given
    global id_count, schedules_generated, courses_list
    chances = pow(len(courses_list), len(courses_list)) 
    while (chances != 0):
        new_schedule = []
        counter = 0
        while not haveAllTheCourses(new_schedule) and new_schedule not in schedules_generated:
            new_course = courses_list[randint(0, len(courses_list))]
            if ( new_course not in new_schedule ):
                for course in new_schedule:
                    if courseCollide(new_course, course):
                        continue
            if (counter == 100):
                break
            counter+=1
        chances-=1

def run():
#main (menu to add, remove courses and generate the schedules)
    global courses_list, schedules_generated
    
    while (True):
        opcion = 0
        menu()
        try:
            option = int(input("*"*40+"\nIngrese una de las opciones: -> "))
        except ValueError:
            continue
        if option == 1:
            course = createCourse()
            if course != None:
                courses_list.append(course)
        elif (option == 4):
            filename = input("Ingresa el nombre del archivo a crear: ")
            writeFile(filename, courses_list)
        elif (option == 3):
            print("Generacion de los horarios...")
            time.sleep(2)
            generateSchedules()
            time.sleep(2)
            print("Terminado.")
            time.sleep(1)
            os.system("clear")
        elif (option == 2 or option == 1):
            print("Que tratas de hacer?")
        elif (option == 0):
            showCourses()
        else:
            return
        time.sleep(2)
        os.system("cls")

if __name__ == "__main__":
    run()