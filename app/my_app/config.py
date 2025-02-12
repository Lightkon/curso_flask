# Al igual que como hicimos en "hello_world.py" si usamos app.run(debug=True) para iniciar Flask y modo debug
# Este metodo funciona igual, pero es mas profesional.

class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
