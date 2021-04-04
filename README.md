# Backend Test

API creada en Django REST framework, la misma corre en un contenedor Docker, el cual instala Django y las dependencias seleccionadas.

- Base de datos: SQLite3
- Autenticacion: JWT (Simple JWT)

# Instalación
1. Clonar respositorio
2. Crear el contenedor con el comando: "sudo docker-compose build"
3. Correr el contenedor con el comando: "sudo docker-compose up"
4. Generar migraciones con el comando: "sudo docker-compose run --rm django python manage.py makemigrations"
5. Correr migraciones con el comando: "sudo docker-compose run --rm django python manage.py migrate"
6. Importar los fixtures con el comando: "sudo docker-compose run --rm django python manage.py loaddata data"
7. 



La API tiene los siguientes endpoints, los mismos se acceden a traves del BrowsableAPIRenderer, excepto los que requieren POST que hay que ingresar con el Token de JWT a traves de HTTPie. (Los Leads se puedem hacer POST sin JWT ya que está pensado para que sea consumido por un cliente)

/library/ {}
