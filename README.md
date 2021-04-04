# Jaimovich Andrés: Backend Test

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
7. Crear superusuario con el comando: "sudo docker-compose run --rm django python manage.py createsuperuser"


La API tiene los siguientes endpoints, los mismos se acceden a traves del BrowsableAPIRenderer, excepto cuando se requiere POST que hay que ingresar con el Token de JWT a traves de HTTPie. (Los Leads se pueden hacer POST sin JWT ya que está pensado para que sea consumido por un cliente)

En caso de pedir un POST en library, book o author. Primero se deberá generar el token de JWT en el endpoint /token/, ahi se debe ingresar los datos del usuario y JWT va a devolver 2 codigos; 'access' y 'refresh'. En caso de que se realice la consulta dentro de los 30 minutos despues de crear el token se deberá volver a ingresar el codigo de 'refresh' en el endpoint /token/refresh/, este proporcionará un nuevo codigo 'access'.

Guia de endpóints del API
- /library/ (POST)
- /library/{id} (GET, PUT, DELETE)
- /library/{id}/books/{id} (GET)
- /book/ (GET, POST)
- /book/{id} (GET, PUT)
- /book/?title=&author=&libraries= (GET) {Busqueda por campos}
- /book/?search= (GET) {Busqueda general}
- /author/ (POST)
- /author/{id} (GET)
- /lead/ (POST)

Como caracteristica especial al crearse el Lead, una vez validados los datos se hace una "emulacion" de envio de email a traves de la consola.
Se habilitó el cache de Django.
