# comision-78130
Repositorio de la comisión 78130 Python Flex
comision-78130_TP3_Calarame --> https://github.com/caldatjp/comision-78130_TP3_Calarame.git
ultimo modificado --> 19/10/25 9.45 hs

-------------------- crear repositorio Git
En GitHub, crear repositorio, agregar nombre y descripcion, luego readme on, publico, ignore file = Phyton
https://github.com/caldatjp/TuPrimeraPagina_Calarame.git
crear carpeta del proyecto
sobre la misma abrir git bash
y escribir got clone https://github.com/caldatjp/TuPrimeraPagina_Calarame.git .
abrir visual studio code desde esa ubicacion

-------------------- crear entorno virtual
desde vsc, escribir en proyecto: python -m venv entorno_virtual
Importante: si tira error, activar la directiva de seguridad desde powershell como administrador
	Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
activar entorno: entorno_virtual/Scripts/activate
en el file gitignore, agregar al final entorno_virtual
pip freeze > requirements.txt
-------------------- instalacion django
instalar django --> pip install django
para verificar instalacion y version ejecutar : django-admin --version
-------------------- instalar base de datos sqllite viewer
buscar en extensiones --> SQLLite Viewer --> instalar
-------------------- levantar servidor
ejecutar en la raiz del proyecto comando --> python manage.py runserver
verificar en http://127.0.0.1:8000/

-------------------- creacion de proyecto y apps
django-admin startproject proyecto_coder .
django-admin startapp coder
ir a proyecto_coder, file settings, agregar "coder" en seccion "Installed Apps"
crear en app coder, el file urls.py
crear en app coder, la carpeta template, y dentro de esta carpeta coder
crear en template/coder --> file index.html
setear en urls.py de proyecto_coder --> urlpatterns

--------------------- levantar estructuras de base de datos 
una vez creada la estructura de tabla
ejecutar
python manage.py makemigrations
python manage.py migrate

-----------*************** ESTRUCTURA 

SOCIOS
	socio_id
	socio_nombre
	socio_apellido
	socio_docnro
	socio_fecnacimiento
	socio_fecalta
	socio_fecbaja
INSTRUCTORES
	inst_id
	inst_nombre
	inst_apellido
	inst_sexo
	inst_especialidad
	inst_turno
CLASES
	clase_id
	clase_nombre
	clase_especialidad
	clase_horario
	clase_cupo