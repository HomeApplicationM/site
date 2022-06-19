from flask import Flask
app = Flask(__name__)

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "<h1 style='color:blue'>Bisous <3 <3 <3 <3 <3 <3</h1>"

    return app

if __name__ == "__main__":
    create_app().run(host='0.0.0.0')
