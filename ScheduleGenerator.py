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

# Constants?
days = ["L", "K", "M", "J", "V", "S"]
headers = ["Codigo", "Nombre", "Profesor", "Creditos"]

def writeFile(filename, data):
    pass

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
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Codigo  : "+course[0])
    print("Nombre  : "+course[1])
    print("Profesor: "+course[2])
    print("Creditos: "+course[3])
    print("Horario :")
    for day in course[4]:
        print(day[0], end="") #initial letter
        print(day[1][0], end="") #start hour
        print(day[1][1]) #final hour
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<")

def menu():
    # Menu
    print("---Generador de Horarios---")
    print("0. Mostrar cursos          ")
    print("1. Agregar curso           ")
    print("2. Eliminar curso          ")
    print("3. Reset                   ")
    print("4. Generar horarios (.csv) ")
    print("5. Salir                   ")
    print("---------------------------")

def createCourse():
# [Code, Name, Teacher, Credits, [[Day, [startHour, finalHour]], [Day, [startHour, finalHour]] ]]
# ['IC-2001', 'Estructuras de Datos', 'XXXXXXXXXXXXX', '4', [['M', ['09:30', '11:20']], ['V', ['9:30', '11:20']]]]
    global headers, days
    course = []
    for header in headers:
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

def run():
#main (menu to add, remove courses and generate the schedules)
    courses_list = []
    schedule = []
    while (True):
        option = int(input("Ingrese una de las opciones"))
        if option == 1:
            courses_list.append(createCourse())
        elif (option == 2):
            pass
        elif (option == 3):
            pass
        elif (option == 4):
            pass
        else:
            return

if __name__ == "__main__":
    run()