from flask import Flask , render_template ,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from flask_mail import Mail  #this is to import mailing feature 

#defining the application
app = Flask(__name__)


#loading all the data as json file 
with open("config.json" , 'r') as c:

    params = json.load(c)["params"]

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
    posts = Posts.query.filter_by().all()[0:params['num_of_post']]
    return render_template('index.html' , posts= posts)

@app.route('/dashboard')
def dashboard():
    return render_template('login.html' )
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




#------- to run the flask application----------
app.run(debug=True)
