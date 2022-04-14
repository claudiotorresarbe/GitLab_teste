from config import *
from flask import *

bp_cadastroform = Blueprint("bp_cadastroform",__name__,template_folder="templates")

@bp_cadastroform.route("/cadastroform",methods=["GET","POST"])
def cadastroform():

   #check if logged
   #if "id" in session:
      #return redirect('/')

   data = []

   #get
   if request.method == 'GET':
      action = request.args.get('action')
      id = request.args.get('id')
   
      #is None, info, edit or delete?
      if action not in(None,'info','edit','delete'):
         return redirect('/cadastro')
      
      #if id is not exists or parameters error
      if id != None:
         data = db.sql(f'select email,status,count(*) from example where id = {id}')[0]
         if data[2] == 0:
            return redirect('/cadastro')
      elif action == None and id == None:
         pass
      else:
         return redirect('/cadastro')

   #post
   if request.method == 'POST':

      #variables method get
      action = request.args.get('action')
      id = request.args.get('id')
      
      while True:
         
         #method
         if action in(None,'info','edit'):
            email = request.form['email']
            status = request.form['status']
            data = [email,int(status)]

         #if delete data
         if action == 'delete':
            result = db.delete('example',f'id={id}')
            return redirect('/cadastro')

         #check values
         if len(email) == 0 or int(status) == -1:
            flash('danger','Preencha os campo!')
            break
         
         #if new data
         if action == None:
            result = db.insert('example','email,status',f'"{email}",{status}')
            flash('success','Cadastro realizado com sucesso!')
            data = []
            break

         #if edit data
         if action == 'edit':
            result = db.update('example',f'email="{email}",status={status}',f'id={id}')
            flash('success','Cadastro alterado com sucesso!')
            break
   
   return render_template("cadastroform/index.html",data=data)
    
    