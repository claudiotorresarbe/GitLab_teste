from config import *
from flask import *

bp_home = Blueprint("bp_home",__name__,template_folder="templates")

@bp_home.route("/",methods=["GET","POST"])
def home():

   #check if logged
   #if "id" in session:
      #return redirect('/')

   #post
   #if request.method == 'POST':
      #email = request.form['email']
      #flash('danger','Preencha o campo!')

   return redirect("/cadastro")
    