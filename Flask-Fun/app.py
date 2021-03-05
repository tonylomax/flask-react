from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "sqlite:///tonys_cupboard.db"  # path to database and its name
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo_text = db.Column(db.String(100), index=True)


# class blogs(db.Model):
#     id = db.Column(
#         db.Integer, primary_key=True
#     )  # primary key column, automatically generated IDs
#     author = db.Column(db.String(80), index=True, unique=True)  # book title
#     blogs = db.Column(db.String(80), index=True, unique=True)  # book title

db.create_all()


def __repr__(self):
    return "{} in: {},{}".format(self.author, self.content)


class ToDoForm(FlaskForm):
    todo = StringField("ToDo")
    submit = SubmitField("Add todo")


@app.route("/", methods=["GET", "POST"])
def index():
    # myBlogs = blogs.query.all()
    # print("my blogs",  myBlogs)
    if "todo" in request.form:
        db.session.add(Todo(todo_text=request.form["todo"]))
        db.session.commit()
    return render_template(
        "index.html", todos=Todo.query.all(), template_form=ToDoForm()
    )
