from flask import Flask, render_template, request
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"

todos = ["learn flask", "doa  thing"]

class ToDoForm(FlaskForm):
    todo = StringField("ToDo")
    submit = SubmitField("Add todo")

@app.route("/", methods=["GET", "POST"])
def index():
    if 'todo' in request.form:
        todos.append(request.form['todo'])
    return render_template('index.html', todos = todos, template_form = ToDoForm())
