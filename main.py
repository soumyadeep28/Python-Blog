from flask import Flask, redirect , render_template ,request , session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from flask_mail import Mail  #this is to import mailing feature 
import os , math
from werkzeug.utils  import secure_filename   #to secure files
#defining the application
app = Flask(__name__)

#setting up secret key
app.config['SECRET_KEY'] = "Your_secret_string"


#loading all the data as json file 
with open("config.json" , 'r') as c:

    params = json.load(c)["params"]


#setting up path for file upload 
app.config['UPLOAD_FOLDER'] = params['location']


#----------configure for mailing fitures in gmail
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com' ,
    MAIL_PORT = '465',
    MAIL_USE_SSL = True ,
    MAIL_USER = params['mailuser'] ,
    MAIL_PASSWORD = params['mailpasswd'],
    

)
mail = Mail(app)
#-------- connecting with db------------

local_server = True
if local_server :
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

    
db = SQLAlchemy(app)


#------DB configuration for Contact
#---- db table present in the contact table 'sno' , 'name, 'email' , 'phone' , 'msg' , 'date'

class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.Integer(),unique=True)
    msg = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)


#----- class for post db--------

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80),  nullable=False)
    slug = db.Column(db.String(120), nullable=False)
    content = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)
    img_file = db.Column(db.String(80), nullable=False)



#----------- Routing configuration and the values are passed

@app.route('/')
def home():
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts)/int(params['num_of_post']))
    #[0:params['num_of_post']]
    #Pagination Logic
    page = request.args.get('page')
    if (not str(page).isnumeric() ):
        page = 1
    page = int(page)
    posts = posts[(page-1)*int(params['num_of_post']) : (page-1)*int(params['num_of_post'])+int(params['num_of_post'])]
    if (page==1 ):
        prev = "#"
        next = "/?page="+ str(page+1)

    elif page== last :
        prev = "/?page="+ str(page-1)
        next =  "#"
    else:
        next = "/?page="+ str(page+1)
        prev = "/?page="+ str(page-1)



    #posts = Posts.query.filter_by().all()[0:params['num_of_post']  ]
    return render_template('index.html' , posts= posts , prev=prev , next= next )

@app.route('/dashboard' , methods=["GET" , "POST"])
def dashboard():


    #check if user is already in session or not
    if 'user' in session and session['user'] == params['admin_user'] :
        posts = Posts.query.all()
        return render_template('dashboard.html' ,params = params ,posts = posts )
    #this is for the new login and create the session
    if request.method == "POST":
        user = request.form.get('uname')
        password = request.form.get('pswd')

        if user == params['admin_user']  and password == params['admin_pass'] :
            #set the session variable
            session['user'] = user
            posts = Posts.query.all()
            return render_template('dashboard.html' , params = params  ,posts = posts)
        #go to admin panel
        pass
    else:
        return render_template('login.html' ,params = params )
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact' , methods=['GET' ,'POST'])
def contact():
    ''' Fetched data from form from the contact page'''
    if (request.method == 'POST') :
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        massage = request.form.get('massage')
        entry = Contact(name =name ,phone =phone , email = email , msg = massage , date = datetime.now())
        db.session.add(entry)
        db.session.commit()
        '''
        mail.send_message('New msg from Blog from '  + name , 
                            sender = email , 
                            recipients = [params['mailuser'] ] ,
                            body = massage +'\n Phone number :' + phone 

                            )
        '''

    
    return render_template('contact.html')

@app.route('/post/<string:post_slug>' , methods = ['POST' , 'GET'] )
def post_route(post_slug):
    post = Posts.query.filter_by(slug = post_slug).first()


    return render_template('post.html' , post=post)


@app.route('/edit/<string:sno>' , methods=['POST' ,'GET'] )
def edit(sno):
    if 'user' in session and session['user']== params['admin_user']:
        if request.method == 'POST' :
            box_title = request.form.get('title')
            box_slug = request.form.get('slug')
            box_content = request.form.get('content')
            box_img = request.form.get('img')

            ''' Check serial number is 0 or not if 0 then it is creating new post and 
            if there is any other then it is editing'''
            
            if sno == '0' :
                post = Posts(title = box_title , slug =box_slug ,content = box_content , img_file = box_img , date = datetime.now() )
                print(post)
                db.session.add(post)
                db.session.commit()
                
            else:
                post = Posts.query.filter_by(sno = sno).first()
                post.title = box_title
                post.slug = box_slug
                post.content = box_content
                post.img_file = box_img
                post.date = datetime.now()
                db.session.commit()
                return redirect('/edit/'+ sno )

        post = Posts.query.filter_by(sno = sno).first()
        return render_template('edit.html' , params = params , post = post , sno =sno)

@app.route('/uploader' , methods = ['POST' ,'GET'])
def uploader():
    if 'user' in session and session['user']== params['admin_user']: #to check logged in or not
        if(request.method == 'POST'):
            f =request.files['file1']
            f.save( os.path.join(app.config['UPLOAD_FOLDER'] ,secure_filename(f.filename)))
            return 'Uploaded Successfully'


@app.route('/logout' )
def logout():
    session.pop('user')
    return redirect('/dashboard')


@app.route('/delete/<string:sno>' ,methods= ['GET' , 'POST'] )
def delete(sno):
    if 'user' in session and session['user']== params['admin_user']: #to check logged in or not
        
        post =Posts.query.filter_by(sno = sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')


#------- to run the flask application----------
app.run(debug=True)
