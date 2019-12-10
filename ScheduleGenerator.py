"""
    Schedule Generator
    author : Josue Rojas Vega
    since : 9-12-2019
    objective: generate all the posibilities to create my schedules, 
                detecting all the collides, and too practice a little bit of Python
"""

days = ["L", "K", "M", "J", "V", "S"]
headers = ["Codigo", "Nombre", "Profesor", "Creditos"]

def writeFile(filename, data):
    pass

def courseCollide(course1, course2):
    return True

def menu():
    print("---Generador de Horarios---")
    print("0. Mostrar cursos          ")
    print("1. Agregar curso           ")
    print("2. Eliminar curso          ")
    print("3. Reset                   ")
    print("4. Generar horarios (excel)")
    print("5. Salir                   ")
    print("---------------------------")

def createCourse():
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
    courses_list = []
    schedules_list = []
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