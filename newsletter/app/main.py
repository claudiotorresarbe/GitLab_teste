from config import *
from flask import *

from blueprint.cadastro import bp_cadastro
from blueprint.cadastroform import bp_cadastroform
from blueprint.home import bp_home

app = Flask(__name__)
app.secret_key = ".!Fl4sk"

app.register_blueprint(bp_cadastro)
app.register_blueprint(bp_cadastroform)
app.register_blueprint(bp_home)

@app.errorhandler(404)
def error(e):
   return redirect("/")

if __name__ == "__main__":
   CreateAll()
   app.run(host="0.0.0.0",port=3000,debug=True)
    