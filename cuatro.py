alumnos = int(input("cuantos alumnos va a ingresar?"))
calificaciones = int(input("cuantas calificaciones van a ser por alumno?"))
calificacion = 0
sumatoria_alumno = 0
promedio_alunno=0
sumatoria_grupo = 0
promedio_grupo = 0
calificaciones_totales = 0

for i in range(alumnos+1):
    print(f"ingresando calificaciones del alumno {i+1}")
    for x in range(calificaciones +1):
        calificacion = int(input("ingrese el valor de la calificacion"))
        sumatoria_alumno= calificacion + sumatoria_alumno
    promedio_alunno = sumatoria_alumno / calificaciones
    print(f"promedio del alumno {i+1} es igual a: {promedio_alunno}")
    sumatoria_grupo = promedio_alunno + sumatoria_grupo 
promedio_grupo= sumatoria_grupo / alumnos
calificaciones_totales = alumnos * calificaciones
print(f"promedio del grupo es: {promedio_grupo} cantidad de calificaciones del grupo es {calificaciones_totales}")


