# back_analisis_datos
En este repositorio está el código correspondiente a la conexión a una base de datos en MySQL donde se realiza la inserció y consulta a la misma arrojando como resultado 7 endpoints para ser consumidas.


## Requisitos para el proyecto

Para poder ejecutar correctamente el proyecto es necesario tener instalado `Python`,
ademas de un servidor de bases de datos como **[MySQL](https://dev.mysql.com/downloads/workbench/)** o `MariaDB`.

## Clonando del proyecto

Primero debe clonar este repositorio usando el comando:

```
$ git clone https://github.com/wetb/back_analisis_datos.git
```

## Instalando el proyecto

Si desea trabajar sobre un entorno virtual de Python puede dar [clic aqui](https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/)
para seguir un tutorial para instalar un entorno virtual en el sistema operativo que desee.

Realice la instalación de las librerias necesarias para la ejecución del proyecto usando el comando

```
$ pip install -r requirements.txt
```

Edite la configuración de usuario y contraseña de `MySQL` para la conexion de la base de datos en el archivo `\myproject\myproject\settings.py`

**NOTA:** debe crear previamente una base de datos para el proyecto y agregar el nombre a la configuración en el campo "[database_name]".

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '[database_name]',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Una vez cambiada la información para la conexión a la base de datos y las librerias necesarias esten instaladas, debe realizar lo siguiente para la migración
de las tablas a la base de datos creada previamente en **MySQL**.

```
$ python manage.py makemigrations
$ python manage.py migrate
```

Para realizar la inserción de los datos, edite la configuración de usuario y contraseña de la base de datos para la conexion con **MySQL**
en el script `myproject\utils.py`:

```
'mysql+pymysql://[user]:[password]@127.0.0.1/[database_name]'
```

Ejecutando el script en una consola con el siguiente comando se realizará la inserción de los datos en **MySQL**:

```
$ python data_management.py
```

Finalmente, para ejecutar el servidor de **Django** se debe usar el siguiente comando en una consola:

```
$ python manage.py runserver
```

## Funcionamiento del proyecto

- Para ingresar a la API en el navegador ingrese el siguiente link <http://127.0.0.1:8000/api/>

- Para hacer una peticion GET a cada una de las preguntas del dashboard:

```
GET http://127.0.0.1:8000/api/aplicacion1_boyaca/
GET http://127.0.0.1:8000/api/matriculas_municipio/
GET http://127.0.0.1:8000/api/genero_matricula/
GET http://127.0.0.1:8000/api/jornada_matricula/
GET http://127.0.0.1:8000/api/ie_matricula/
GET http://127.0.0.1:8000/api/grado_matricula/
GET http://127.0.0.1:8000/api/ie_metod/
```