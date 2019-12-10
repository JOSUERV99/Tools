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

def run():
    print("Hello World!", end="\t")

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

if __name__ == "__main__":
    createCourse()