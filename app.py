from flask import Flask,render_template,request,redirect,url_for
import mongoengine
import os
from mongoengine import *
APP_ROOT= os.path.dirname(os.path.abspath(__file__))
print(APP_ROOT)
static= os.path.join(APP_ROOT,"static")
print(static)
images_folder = os.path.join(static, 'image')
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

        for image in request.files.getlist("img"):
            image_name = image.filename
            image_dir = os.path.join(images_folder, image_name)
            image.save(image_dir)
            print(image_dir)

        namex=request.form["name"]
        desx=request.form["des"]
        imgx='/static/image/'+image_name
        print(imgx)
        linkx=request.form["link"]

        game=Game(name=namex, img=imgx ,des=desx,link=linkx)

        game.save()
        return redirect(url_for("hobby"))
@app.route("/deletegame/<id>")
def delete(id):
    delete_obj=Game.objects().with_id(id)
    if delete_obj is None:
        return "wrong id"
    else:
        old_img = os.path.join(APP_ROOT+delete_obj.img)
        print (old_img)
        os.remove(old_img)
        delete_obj.delete()
        return redirect(url_for("hobby"))

@app.route("/updategame/<id>",methods=["GET","POST"])
def updating(id):
    game = Game.objects().with_id(id)
    if request.method=="GET":
        return render_template("updating.html",object=game)

    elif request.method=="POST":
        for image in request.files.getlist("img"):

            image_name = image.filename
            image_dir = os.path.join(images_folder, image_name)
            print(image_dir)


        if request.form["name"] is not "":
            game.update(set__name=request.form["name"])
        if request.form["des"] is not "":
            game.update(set__des=request.form["des"])
        if image_name is not "":
            old_img = os.path.join(APP_ROOT + game.img)
            os.remove(old_img)
            image.save(image_dir)
            game.update(set__img=('/static/image/'+image_name))

        if request.form["link"] is not "":
            game.update(set__link=request.form["link"])
        return redirect(url_for("hobby"))

if __name__ == '__main__':
    app.run()