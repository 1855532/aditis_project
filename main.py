from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

#connects default URL to a function
@app.route('/')
def home():
    #Flask import uses Jinga to render HTML
    return render_template("home.html")

@app.route('/aboutus/')
def journal():
    #Flask import uses Jinga to render HTML
    return render_template("aboutus.html")

@app.route('/aboutus/aditi/')
def aditi():
    #Flask import uses Jinga to render HTML
    return render_template("aboutus.html", name = "Aditi", grade = "11th grade", about = "Hello! I am Aditi and I am a Junior at Del Norte. I love animals, travel, and science. This is my first year in Mr. M's class and I am learning so much about Python and html files! I look forward to learning more about computers and programming.", contributions = "Contribution to the Flask Portfolio project: I created the about us page and formatted it. Along with Carter, I created a Navbar and added all the links. I also formatted the home page and added all the links to the projects, repl.its and resources.")

@app.route('/aboutus/carter/')
def carter():
    #Flask import uses Jinga to render HTML
    return render_template("aboutus.html")

@app.route('/aboutus/isai/')
def isai():
    #Flask import uses Jinga to render HTML
    return render_template("aboutus.html")

@app.route('/aboutus/mustafa/')
def mustafa():
    #Flask import uses Jinga to render HTML
    return render_template("aboutus.html")

@app.route('/aboutus/sophie/')
def sophie():
    #Flask import uses Jinga to render HTML
    return render_template("aboutus.html")

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='3000', host='0.0.0.0')
