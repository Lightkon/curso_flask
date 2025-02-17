from flask import Flask

from my_app.tasks.controllers import taskRoute  # Importa la ruta de los modulos (carpetas .py)

from my_app.config import DevConfig

app = Flask(__name__) # , template_folder="/templates" se puede poner junto con __name__ para nombrar a la carpeta de html's
#app.config.from_object(DevConfig)  # Esto es lo mismo que decir "app.debug = True"

app.register_blueprint(taskRoute)  # Registra los modulos

app.config.from_object(DevConfig)  # Activa el modo debug
