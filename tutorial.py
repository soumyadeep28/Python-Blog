from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('')




#------- to run the flask application----------
app.run(debug=True)
