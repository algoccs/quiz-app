# 📝 Quiz App - Flask Project

Este es un proyecto de aplicación de cuestionarios (Quiz) desarrollado en Python utilizando el framework **Flask**. El proyecto está estructurado siguiendo las buenas prácticas de la industria, utilizando un entorno virtual aislado para gestionar las dependencias de forma segura sin alterar el sistema operativo.

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
