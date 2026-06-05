# 🧠 Quiz App — Sistema de Cuestionarios Dinámicos

¡Bienvenido al repositorio de **Quiz App**! Esta es una aplicación web *full-stack* robusta, interactiva y de enfoque educativo diseñada para servir como una herramienta pedagógica en el aula. A través de este proyecto, los estudiantes pueden asimilar conceptos fundamentales del desarrollo de software moderno: la **arquitectura cliente-servidor**, la gestión y diseño de **bases de datos relacionales con SQL/SQLite**, y el renderizado dinámico en el servidor mediante el **sistema de plantillas Jinja2 con Flask**.

---

## 🚀 Arquitectura y Características Principales

El proyecto implementa una arquitectura modular bien definida para separar las responsabilidades del frontend, el backend y la persistencia de datos:

### 🌐 Backend y Servidor Web (`app.py`)
* **Controlador Central:** Gestiona el ciclo de vida de las peticiones HTTP (`GET` y `POST`).
* **Enrutamiento Dinámico:** Define las rutas principales de la aplicación web:
  * ` / `: Pantalla de bienvenida e inicio del cuestionario.
  * `/test`: Renderizado dinámico de preguntas y captura de respuestas en tiempo real.
  * `/results`: Procesamiento y visualización del puntaje final obtenido por el usuario.
* **Inyección de Contexto:** Extrae la información desde la capa de persistencia y la expone de manera segura al motor de plantillas.

### 💾 Persistencia y Base de Datos SQL (`database.py`)
* **Motor Integrado:** Utiliza **SQLite**, eliminando la necesidad de configurar servidores de base de datos complejos y permitiendo un almacenamiento local ligero en un único archivo.
* **Modelo de Datos Eficiente:** Tablas estructuradas de forma relacional para almacenar de manera independiente las preguntas, las opciones de respuesta y las claves de corrección.
* **Consultas SQL Puras:** Diseñado didácticamente con sentencias SQL nativas (`CREATE TABLE`, `INSERT INTO`, `SELECT`) para que los alumnos dominen la sintaxis estándar del lenguaje.

### 🎨 Frontend Basado en Plantillas (`templates/` & `static/`)
* **Herencia de Plantillas (Jinja2):** Se utiliza `base.html` como la plantilla maestra que define la estructura global (HTML5, metadatos, barra de navegación y pie de página). Las vistas secundarias heredan este esqueleto mediante bloques de contenido dinámico:
  * `test.html`: Estructura adaptativa para desplegar secuencialmente el banco de preguntas.
  * `results.html`: Tarjeta de puntuación final con retroalimentación inmediata.
* **Aislamiento de Estilos y Comportamiento:** Los estilos responsivos se unifican en `static/css/style.css`.

---

## 📂 Estructura del Proyecto

La disposición de los archivos sigue estrictamente las convenciones de diseño de aplicaciones Flask:

```text
quiz-app/
│
├── templates/               # Capa de Vistas: Plantillas HTML dinámicas (Jinja2)
│   ├── base.html            # Layout maestro (Esqueleto base de la interfaz)
│   ├── test.html            # Contenedor dinámico del cuestionario
│   └── results.html         # Pantalla modular de resultados y feedback
│
├── static/                  # Capa de Recursos Estáticos
│   ├── css/
│   │   └── style.css        # Hoja de estilos general y componentes responsivos
│
├── app.py                   # Capa de Control: Servidor Flask y lógica de negocio
├── database.py              # Capa de Modelo: Inicialización, semillas y consultas SQL
│
└── README.md                # Documentación oficial del proyecto
```

---

## 🛠️ Tecnologías Utilizadas

| Componente | Tecnología | Descripción |
| :--- | :--- | :--- |
| **Backend** | Python 3.x / Flask | Servidor web ágil, microframework de enrutamiento. |
| **Base de Datos** | SQL / SQLite3 | Persistencia relacional local mediante consultas estructuradas. |
| **Vistas** | HTML5 / Jinja2 | Renderizado dinámico y modular por herencia de bloques. |
| **Diseño** | CSS3 Moderno | Interfaz limpia, responsiva y adaptable a dispositivos móviles. |

---


## 🚀 Guía de Configuración y Despliegue

Sigue estos pasos detallados para preparar tu entorno de desarrollo, gestionar las librerías y asegurar que el proyecto sea transportable.

### Paso 1: Crear el archivo de dependencias (`requirements.txt`)
Para registrar de forma exacta qué librerías necesita este proyecto para funcionar (como Flask), ejecutamos:

```bash
pip freeze > requirements.txt
```
*   **`pip`**: Invoca al instalador de paquetes de Python local de tu entorno.
*   **`freeze`**: Le pide a pip que genere una lista de todas las librerías instaladas actualmente y sus versiones exactas.
*   **`>`**: Operador de redirección que toma la lista generada y la escribe dentro de un archivo, borrando el contenido previo si el archivo ya existía.
*   **`requirements.txt`**: El nombre estándar del archivo de texto donde se guarda la "receta" de dependencias del proyecto.

### Paso 2: Configurar la exclusión de Git (`.gitignore`)
La carpeta del entorno virtual (`venv/`) contiene miles de archivos específicos de tu sistema operativo que no deben subirse a GitHub. Para ignorarla automáticamente, ejecutamos:

```bash
echo "venv/" > .gitignore
```
*   **`echo`**: Comando que imprime en la terminal el texto que se le introduce a continuación.
*   **`"venv/"`**: El texto exacto que queremos guardar. La barra diagonal `/` indica a Git que debe ignorar la carpeta completa y todo su contenido.
*   **`>`**: Redirige el texto del comando `echo` hacia el archivo en lugar de mostrarlo en la pantalla.
*   **`.gitignore`**: Archivo oculto especial que lee Git para saber qué archivos o carpetas debe excluir del repositorio.

---


## 🛠️ Cómo Replicar este Proyecto en otra Computadora

Si descargas este proyecto en una computadora nueva o un compañero de equipo quiere ejecutarlo, no tendrá la carpeta `venv/` (ya que fue ignorada). Deberá seguir estos tres comandos detallados en su terminal:

### 1. Crear un nuevo entorno virtual
```bash
python3 -m venv venv
```
*   **`python3`**: Llama al intérprete de Python versión 3 del sistema operativo.
*   **`-m`**: Flag de *módulo*. Permite ejecutar una herramienta interna de Python como si fuera un programa autónomo.
*   **`venv` (primero)**: El nombre del módulo oficial de Python para crear entornos aislados.
*   **`venv` (segundo)**: El nombre de la carpeta física que se creará en el disco duro para guardar el entorno.

### 2. Activar el entorno virtual
```bash
source venv/bin/activate
```
*   **`source`**: Comando de Linux/Bash que lee y ejecuta las instrucciones de un archivo directamente en la sesión actual de la terminal.
*   **`venv/bin/activate`**: La ruta del script que modifica temporalmente las variables de entorno de la terminal, desviando los comandos `python` y `pip` hacia la carpeta local del proyecto.

### 3. Instalar todas las dependencias juntas
```bash
pip install -r requirements.txt
```
*   **`pip`**: Llama al gestor de paquetes de Python (ahora apuntando de forma segura al entorno activo).
*   **`install`**: La instrucción para descargar e instalar librerías desde el repositorio oficial de Python (PyPI).
*   **`-r`**: Flag de *requirements*. Le avisa a pip que no va a instalar una sola librería, sino que debe leer una lista desde un archivo de texto.
*   **`requirements.txt`**: El archivo que contiene la lista de librerías y versiones que creamos en el Paso 1.

---


## 🔄 Flujo de Trabajo Diario

Cada vez que regreses a trabajar en este proyecto en el futuro, el orden correcto de comandos es:

1. **Abrir la terminal** en la carpeta raíz del proyecto.
2. **Activar el entorno**: `source venv/bin/activate` (Verás el indicador `(venv)` al inicio de la línea de comandos).
3. **Ejecutar la aplicación**: `python app.py` (o el nombre de tu archivo principal).
4. **Salir del entorno** (opcional): Al terminar de programar, puedes escribir `deactivate` para volver al Python global de tu sistema.

---


## 📝 Guía Metodológica y Ejercicios para Clase

Este proyecto está meticulosamente diseñado para guiar clases prácticas de programación. Aquí se proponen tres laboratorios de aprendizaje:

> 💡 **Laboratorio 1: El Poder de SQL (`database.py`)**
> 
> Pide a los alumnos que exploren el archivo de la base de datos. Como ejercicio, deben **modificar las sentencias de inserción** para añadir un nuevo bloque de preguntas sobre un tema diferente y verificar cómo impacta en las tablas relacionales empleando sentencias `SELECT`.

> 💡 **Laboratorio 2: Ciclo de Petición HTTP (`app.py`)**
> 
> Analizar cómo viajan los datos desde el cliente hacia el servidor. Los estudiantes pueden **rastrear el método `POST`** implementado al enviar el cuestionario, entendiendo cómo Flask recibe los parámetros, calcula el puntaje y redirige de manera segura al endpoint de resultados.

> 💡 **Laboratorio 3: Modularización de Vistas (`templates/`)**
> 
> Estudiar la herencia de plantillas Jinja2. Desafía a los estudiantes a **modificar la barra de navegación en `base.html`** para observar cómo el cambio se propaga instantáneamente en `quiz.html` y `results.html` sin tocar una sola línea de código en esas páginas secundarias.
---

## 📄 Licencia

Este proyecto está bajo la protección de la Licencia MIT. Eres libre de usarlo, modificarlo y distribuirlo con fines educativos en el aula.

