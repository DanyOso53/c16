from flask import Flask, render_template

appw = Flask(__name__)

@appw.route("/")
def parte1() :
    return("1era página")


@appw.route("/index")
def partei() :
    name = "Daniel"
    return render_template("index.html", indice_variable= name)

appw.run()
