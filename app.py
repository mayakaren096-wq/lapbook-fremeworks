# Realizado por Fhany Mendez y Karen Maya - Grupo: 305 - Frameworks

from flask import Flask, render_template

app = Flask(__name__)

# Estructura de datos con la información solicitada tratada mediante Jinja
TEMAS_LAPBOOK = [
    {
        "id": "html",
        "titulo": "HTML",
        "subtitulo": "Lenguaje de Marcado",
        "color_tag": "tag-html",
        "definicion": "HTML (HyperText Markup Language) es el código que se utiliza para estructurar y desplegar una página web y sus contenidos.",
        "puntos_clave": [
            "Usa etiquetas como <h1>, <p>, <div>, <span>.",
            "Define la estructura semántica de los documentos web.",
            "Estándar actual: HTML5."
        ],
        "codigo_ejemplo": "<!DOCTYPE html>\n<html>\n  <head><title>Mi Web</title></head>\n  <body>\n    <h1>Hola Mundo</h1>\n  </body>\n</html>"
    },
    {
        "id": "css",
        "titulo": "CSS",
        "subtitulo": "Hojas de Estilo",
        "color_tag": "tag-css",
        "definicion": "CSS (Cascading Style Sheets) es el lenguaje que usamos para estilizar un documento HTML y controlar su aspecto visual.",
        "puntos_clave": [
            "Permite aplicar colores, fuentes, márgenes y diseño adaptativo (Responsive).",
            "Usa selectores, propiedades y valores.",
            "Soporta Flexbox y CSS Grid para diagramaciones complejas."
        ],
        "codigo_ejemplo": "body {\n  background-color: #f3e5f5;\n  font-family: 'Poppins', sans-serif;\n  color: #4a4a4a;\n}"
    },
    {
        "id": "javascript",
        "titulo": "JavaScript",
        "subtitulo": "Lenguaje de Programación",
        "color_tag": "tag-js",
        "definicion": "JavaScript es un lenguaje de programación dinámico que permite agregar interactividad, animaciones y lógica del lado del cliente.",
        "puntos_clave": [
            "Manipula el DOM (Document Object Model) en tiempo real.",
            "Maneja eventos de usuario como clics, desplazamientos y datos de formularios.",
            "Permite realizar peticiones asíncronas (Fetch API / AJAX)."
        ],
        "codigo_ejemplo": "document.getElementById('btn').addEventListener('click', () => {\n  alert('¡Lapbook interactiva!');\n});"
    },
    {
        "id": "jinja",
        "titulo": "Jinja",
        "subtitulo": "Motor de Plantillas",
        "color_tag": "tag-jinja",
        "definicion": "Jinja es un motor de plantillas extensible y rápido para Python, comúnmente utilizado dentro de frameworks como Flask.",
        "puntos_clave": [
            "Permite insertar datos dinámicos en archivos HTML.",
            "Utiliza sintaxis de delimitadores: {{ variable }} y {% estructura %}.",
            "Admite herencia de plantillas y bucles de renderizado."
        ],
        "codigo_ejemplo": "{% for item in temas %}\n  <h3>{{ item.titulo }}</h3>\n  <p>{{ item.definicion }}</p>\n{% endfor %}"
    },
    {
        "id": "sql",
        "titulo": "SQL",
        "subtitulo": "Base de Datos",
        "color_tag": "tag-sql",
        "definicion": "SQL (Structured Query Language) es el lenguaje estándar para gestionar y manipular bases de datos relacionales.",
        "puntos_clave": [
            "Permite consultar, insertar, actualizar y eliminar registros (CRUD).",
            "Garantiza la integridad de los datos mediante llaves primarias y foráneas.",
            "Utilizado en motores como SQLite, PostgreSQL y MySQL."
        ],
        "codigo_ejemplo": "SELECT id, nombre, calificacion \nFROM alumnos \nWHERE grupo = '305';"
    }
]

@app.route('/')
def index():
    # Se pasan los datos a la plantilla HTML renderizada por Jinja
    return render_template('index.html', temas=TEMAS_LAPBOOK)

if __name__ == '__main__':
    app.run(debug=True)