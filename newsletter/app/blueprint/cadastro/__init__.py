from config import *
from flask import *

bp_cadastro = Blueprint("bp_cadastro",__name__,template_folder="templates")

@bp_cadastro.route("/cadastro",methods=["GET","POST"])
def cadastro():

   #check if logged
   #if "id" in session:
      #return redirect('/')

   #rows per page
   row = 10

   #get
   if request.method != 'POST':
      search = request.args.get('search')
      page = request.args.get('page')
      #flash('danger','Preencha o campo!')

   #prepare value of search 
   if search:
      where = 'where id||email like "%'+search+'%"'
   else:
      where = ''

   #if page is null
   if page is None:
      page = 0

   #page actual
   page = int(page) * (0 if page == 0 else row)

   #prepare query to search
   qry = f"select id, email, case when status = 0 then 'I' else 'A' end from example {where} order by id asc limit {row+1} offset {page}"

   #search
   data = db.sql(qry)

   #tratament of result
   if not isinstance(data,list):
      data = ''

   return render_template("cadastro/index.html",data=data,row=row)
        