from django.urls import path
from .views import (
    index,
    test,
    # Estudiantes
    crear_estudiante,
    lista_estudiantes,
    # Socios
    crear_socio,
    lista_socios,
    # Instructores
    crear_instructor,
    lista_instructores,
    # Clases
    crear_clase,
    lista_clases
)

urlpatterns = [
    path("", index, name="index"),
    path("test/", test , name="test"),

    # ==========================
    # Estudiantes
    # ==========================
    path("estudiantes/nuevo/", crear_estudiante, name="estudiante_form"),
    path("estudiantes/", lista_estudiantes, name="estudiante_list"),

    # ==========================
    # Socios
    # ==========================
    path("socios/nuevo/", crear_socio, name="socio_form"),
    path("socios/", lista_socios, name="socio_list"),

    # ==========================
    # Instructores
    # ==========================
    path("instructores/nuevo/", crear_instructor, name="instructor_form"),
    path("instructores/", lista_instructores, name="instructor_list"),

    # ==========================
    # Clases
    # ==========================
    path("clases/nuevo/", crear_clase, name="clase_form"),
    path("clases/", lista_clases, name="clase_list"),
]
