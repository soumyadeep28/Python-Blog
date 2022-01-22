from flask import Flask , render_template ,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


#-------- connecting with db------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/squarecube'
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



#----------- Routing configuration and the values are passed

@app.route('/')
def home():
    return render_template('index.html')

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

    
    return render_template('contact.html')

@app.route('/post' )
def post():

    return render_template('post.html')




#------- to run the flask application----------
app.run(debug=True)
