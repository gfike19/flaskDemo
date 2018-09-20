from flask import request, redirect, render_template, session, flash, Flask

app = Flask(__name__)
app.config['DEBUG'] = True 

# first, need app route for / as that is what loads when we run localhost:5000

# GET is when page just loads, user doesn't do anything
@app.route("/", methods=['GET']) #forgot to define a function 
def indexGet(): #TIME TO TEST!!!
    return render_template("index.html")

@app.route("/", methods=['POST'])
def indexPost():
    usertext = request.form['userText']

    # maybe break usertext into a list and then check that?
    alist = []
    thecount = usertext.count("the")

    return render_template("index.html", thecount=thecount) #TEST NUMBAH 8(??)!!
app.run()