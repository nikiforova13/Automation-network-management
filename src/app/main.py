from flask import Flask, render_template
from routers import router

# from flask_restx import Api, namespace

app = Flask(__name__)

# swagger = Api(router, '0.1.0', 'It apps', doc='/docs')
# swagger.add_namespace(ns)
app.register_blueprint(router, url_prefix="/configurations")


# swagger.add_namespace(router)

@app.get('/')
def main():
    return render_template('main.html')

@app.get('/contact')
def contact():
    return render_template('info.html')


if __name__ == "__main__":
    app.run(debug=True)
