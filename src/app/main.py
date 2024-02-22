from flask import Flask
from routers import router

# from flask_restx import Api, namespace

app = Flask(__name__)

# swagger = Api(router, '0.1.0', 'It apps', doc='/docs')
# swagger.add_namespace(ns)
app.register_blueprint(router, url_prefix="/configurations")
# swagger.add_namespace(router)


if __name__ == "__main__":
    app.run(debug=True)
