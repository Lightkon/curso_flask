# Los controllers o views en otros frameworks son donde se alojan las rutas
from flask import Blueprint, render_template,  request, redirect, url_for

# Esto es una variable de ruteo, para definir las rutas, el primero es el nombre, el segundo el metodo, el tercero el url de la ruta
taskRoute = Blueprint("index", __name__, url_prefix="/",)  # "/" es la ruta inicial


task_list = ["task1", "task2", "task3"]

@taskRoute.route("/")
def index():
    return render_template("dashboard/task/index.html", tasks=task_list)


@taskRoute.route("/practica")  # "/" es la ruta del index pero dentro de "/tasks" osea /tasks/
def practica():
    name = request.args.get("name", "Desarrollolibre")  # "request" es un atributo de  Flask.
    # "Desarrollolibre" es el mensaje que esta obteniendo render_template y se envia a index.html
    # Si en el url agregamos "/?name=juan" entonces se cambiara el mensaje a "juan"
    # "name" dentro del "get" es la palabra clave para cambiar el mensaje, si fuera "nombre": "/?nombre=juan" seria el comando
    hobbies = ["Videogames", "Puzzles", "Boardgames", "Anime", "Bowling"]
    task = "Pablo no entrego la tarea!"
    return render_template("practica.html", name=name, task=task, hobbies=list(enumerate(hobbies)))

@taskRoute.route("/<int:id>")
def show(id:int):
    return f"Show {id}"

@taskRoute.route("/delete/<int:id>")
def delete(id:int):
    del task_list[id]
    return redirect(url_for("index.index"))

@taskRoute.route("/create", methods=("GET", "POST"))
def create():
    task = request.form.get("task")  # Este dato lo obtiene del formulario en "create.html" el "input" tiene el nombre "task"
    if task:
        task_list.append(task)  # Agrega a la lista todo lo que se ponga en el input del formulario y se proyecta en route("/")
        print(task_list)
        #return redirect("/")  # redirect es un metodo de Flask que te ayuda a redireccionar a otra ruta
        return redirect(url_for("index.index"))  # funciona igual que el anterior pero escribiendo la ruta
        # El primer "index" es el nombre de la ruta origen, el segundo es la ruta index, podria ser practica u otra
    return render_template("dashboard/task/create.html")

@taskRoute.route("/update/<int:id>", methods=("GET", "POST"))
def update(id):
    task = request.form.get("task")
    if task:
        task_list[id] = task  # modifica el valor de la lista que tenga el indice de "id"
        return redirect(url_for("index.index"))
    return render_template("dashboard/task/update.html")