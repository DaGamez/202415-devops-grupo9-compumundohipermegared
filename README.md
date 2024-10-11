``` bash
/
│
├── app/
│   ├── __init__.py        # Inicialización del paquete Flask
│   ├── models.py          # Definición de modelos (SQLAlchemy)
│   ├── routes.py          # Definición de rutas (endpoints RESTful)
│   └── utils.py           # Funciones auxiliares (ej. manejo de JWT, validaciones)
│
├── application.py         # Script principal para correr la aplicación
├── Dockerfile             # Dockerfile para empaquetar la app en un contenedor
├── requirements.txt       # Dependencias de la aplicación
├── .ebextensions/         # Configuraciones adicionales para Elastic Beanstalk
│   └── flask.config        # Configuración personalizada para Elastic Beanstalk
├── .gitignore             # Archivos y directorios a ignorar por git
└── README.md              # Instrucciones y documentación del proyecto

```


Descripción de los archivos y carpetas:
- **/app/**: Contiene la lógica de la aplicación Flask, incluyendo modelos, rutas, y utilidades.
- **application.py**: Archivo principal de la aplicación que define la lógica para Flask.
- **Dockerfile**: Definición de la imagen Docker para empaquetar y desplegar la aplicación en AWS.
- **requirements.txt**: Las dependencias necesarias para correr la aplicación.
- **runtime.txt**: Define la versión de Python que se usará en Elastic Beanstalk.
- **.ebextensions/**: Contiene archivos de configuración para ajustar el entorno en Elastic Beanstalk.
- **README.md**: Instrucciones y detalles del proyecto.

Esta estructura está pensada para facilitar el despliegue en Elastic Beanstalk, además de organizar adecuadamente el código.


## Despliegue de aplicación manual

- Comprimir en un zip: /app application.py requirements.txt .ebextensions
- Cargar e implementar en Elastic Beanstalk
- Configurar variables de entorno en Elastic Beanstalk


## Ejecutar local

### Iniciar todos los servicios
``` bash
 cd scripts
 chmod +x local.sh
 ./local.sh

```

### Iniciar unicamente base de datos
``` bash
 cd scripts
 chmod +x db.sh
 ./db.sh

```

### Ejecutar unicamente aplicación

``` bash
 docker build -t blacklist_app .
 docker run -d -p 5000:5000 --name flask_app blacklist_app

```

