# Los controllers o views en otros frameworks son donde se alojan las rutas
from flask import Blueprint

# Esto es una variable de ruteo, para definir las rutas, el primero es el nombre, el segundo el metodo, el tercero el url de la ruta
taskRoute = Blueprint("index", __name__, url_prefix="/",)  # "/" es la ruta inicial


@taskRoute.route("/")  # "/" es la ruta del index pero dentro de "/tasks" osea /tasks/
def index():
    return "Index"

@taskRoute.route("/<int:id>")
def show(id:int):
    return f"Show {id}"

@taskRoute.route("/delete/<int:id>")
def delete(id:int):
    return f"Delete {id}"

@taskRoute.route("/create", methods=("GET", "POST"))
def create():
    return "create"

@taskRoute.route("/update/<int:id>", methods=("GET", "PUT"))
def update(id):
    return f"Update {id}"