from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
@app.route("/for")
def for_demo():
    return render_template("for.html", names=["phuc","trang","minh","thanh"])

food_list=[{
    "name":"bun dau",
    "desc":"30k-mam tom thom lung",
    "img":"http://7monngonmoingay.com/wp-content/uploads/2014/11/cach-lam-bun-dau-mam-tom-ha-noi-ngon-tuyet-cu-meo-9.jpg"
    },
    {
    "name":"thit cho",
    "desc":"aaa",
    "img":"http://media.suckhoenhi.vn/files/thanhhao.nguyen/2015/10/21/an-thit-cho-co-beo-khong-suckhoenhivn2-1049.jpg"
    },
    ]

@app.route('/hello')
def hello_world():
    return 'Hello '
@app.route("/food")
def food():
    return render_template("food_blog.html",food_list=food_list)
@app.route("/user/<user_name>")
def user(user_name):
    return "hello" + user_name

@app.route("/number/<int:x>")
def number(x):
    return"number{0}".format(x)

@app.route("/sum/<int:a>/<int:y>")
def sum(a,y):
    return "sum{0}+{1}={2}".format(a,y,a+y)
@app.route("/google")
def google():
    return redirect("http://google.com")
@app.route("/hi")
def hi():
    return redirect(url_for("hello_world"))
@app.route("/sum-1-2")
def sum_1_2():
    return redirect(url_for("sum",a=1,y=2))

@app.route("/render")
def ex():
    return render_template("render_example.html",
                           name="Phuc",
                           age=11,
                           city="hn")
@app.route("/render2")
def ex2():
    person_value={
        "name":"thanh",
        "age":19,
        "city":"hanoi"
    }
    return render_template("last one.html",person=person_value)

if __name__ == '__main__':
    app.run()
