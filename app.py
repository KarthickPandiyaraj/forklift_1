from flask import Flask, render_template

app = Flask(__name__)

#Create custom error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Create internal server error page
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

@app.route('/')
def index():
    return "Hai"



if __name__ == '__main__':
    app.run(debug=True)