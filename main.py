from flask import request, redirect, render_template, session, flash, Flask

app = Flask(__name__)
app.config['DEBUG'] = True 

# first, need app route for / as that is what loads when we run localhost:5000

# GET is when page just loads, user doesn't do anything
@app.route("/", methods=['GET']) #forgot to define a function 
def indexGet(): #TIME TO TEST!!!
    return render_template("index.html")

# needs to be global
theDict = {}
@app.route("/", methods=['POST'])
def indexPost():
    usertext = request.form['userText']
    # maybe i don't need a loop at all
    thecount = usertext.count("the")
    theDict[usertext] = thecount
    return redirect("/results")
# go here
@app.route("/results", methods=['GET'])
def results():
    return render_template("results.html", theDict=theDict) 
app.run()