from my_app import app


if __name__ == "__main__":  # Corre flask sin necesidad de hacerlo desde la terminal
    app.run()
    # app.run(debug=True)  # Con esta configuracion entramos en modo debug y cada ves que hagamos cambios y guardamos,
    # se reflejan los cambios