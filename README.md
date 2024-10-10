# 202415-devops-compumundohipermegared

## Estructura de Carpetas

```
microservice_project/
│
├── app/
│   ├── __init__.py                # Inicialización del paquete app, configuraciones globales
│   ├── config.py                  # Configuraciones del proyecto (desarrollo, producción, etc.)
│   ├── models/                    # Modelos de la base de datos (SQLAlchemy)
│   │   ├── __init__.py            # Inicialización del paquete de modelos
│   │   └── blacklist.py           # Modelo de la lista negra
│   ├── resources/                 # Controladores (endpoints REST)
│   │   ├── __init__.py            # Inicialización del paquete de recursos
│   │   └── blacklist.py           # Lógica para agregar/verificar emails en la lista negra
│   ├── schemas/                   # Definiciones de esquemas (serialización/deserialización)
│   │   ├── __init__.py            # Inicialización del paquete de esquemas
│   │   └── blacklist.py           # Esquema de serialización de datos de la lista negra
│   ├── services/                  # Lógica de negocio y servicios internos
│   │   ├── __init__.py            # Inicialización del paquete de servicios
│   │   └── blacklist_service.py   # Lógica del servicio de la lista negra
│   ├── utils/                     # Funciones de utilidad (ej. validaciones, manejo de tokens JWT)
│   │   ├── __init__.py            # Inicialización del paquete de utilidades
│   │   └── jwt_helper.py          # Manejo de JWT (creación, validación, etc.)
│   ├── extensions/                # Extensiones de Flask (JWT, SQLAlchemy, etc.)
│   │   ├── __init__.py            # Inicialización del paquete de extensiones
│   │   └── jwt.py                 # Configuración de JWT en Flask
│   ├── tests/                     # Pruebas unitarias e integrales del proyecto
│   │   ├── __init__.py            # Inicialización del paquete de pruebas
│   │   ├── test_blacklist.py      # Pruebas para la lista negra
│   ├── main.py                    # Punto de entrada principal de la aplicación
│
├── migrations/                    # Migraciones de la base de datos (utilizando Flask-Migrate)
│   └── README                      # Información sobre cómo usar las migraciones
│
├── .env                           # Variables de entorno (configuraciones locales)
├── .gitignore                     # Archivos y carpetas a ignorar en git
├── Dockerfile                     # Configuración de Docker para la aplicación
├── Pipfile                        # Gestión de dependencias del proyecto con pipenv
├── Pipfile.lock                   # Archivo de bloqueo de dependencias (generado por pipenv)
├── README.md                      # Descripción del proyecto, instrucciones de instalación y uso
├── postman_collection.json        # Colección de Postman para probar la API
├── Makefile                       # Comandos útiles de automatización (ej. test, lint, build)
└── requirements.txt               # Alternativa para gestionar dependencias (opcional)

```