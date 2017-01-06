from flask import Flask,render_template,request
import mongoengine
from mongoengine import *
app = Flask(__name__)
#mongodb://<dbuser>:<dbpassword>@ds133358.mlab.com:33358/flask
host = "ds133358.mlab.com"
port = 33358
db_name = "flask"
user_name = "admin"
password = "admin"
mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

class Game(Document):
    name= StringField()
    des= StringField()
    img= StringField()
    link= StringField()

@app.route('/')
def hello_world():
    return render_template("intro.html")
@app.route("/game")
def hobby():
    return render_template("game.html",game_list=Game.objects)
@app.route("/addgame", methods=["GET","POST"])
def adding():
    if request.method=="GET":
        return render_template("adding.html")
    elif request.method=="POST":
        namex=request.form["name"]
        desx=request.form["des"]
        imgx=request.form["img"]
        linkx=request.form["link"]
        game=Game(name=namex, img=imgx ,des=desx,link=linkx)
        game.save()
        return "thank for your add"
@app.route("/deletegame/<id>")
def delete(id):
    delete_obj=Game.objects().with_id(id)
    if delete_obj is None:
        return "wrong id"
    else:
        delete_obj.delete()
        return "delete success"

@app.route("/updategame/<id>",methods=["GET","POST"])
def updating(id):
    game = Game.objects().with_id(id)
    if request.method=="GET":
        return render_template("updating.html",object=game)
    elif request.method=="POST":
        if request.form["name"] is not "":
            game.update(set__name=request.form["name"])
        if request.form["des"] is not "":
            game.update(set__des=request.form["des"])
        if request.form["img"] is not "":
            game.update(set__img=request.form["img"])
        if request.form["link"] is not "":
            game.update(set__link=request.form["link"])
        return "updated succesful"

if __name__ == '__main__':
    app.run()