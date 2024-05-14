###############################################################################
## Sprint 3: Database Integration
## Feature 2: Persist To-Do List
## User Story 2: Load To-Do List
###############################################################################
import os
from flask import Flask, render_template, request, redirect, url_for, g
from database import db, Todo

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))   # Get the directory of the this file
todo_file = os.path.join(basedir, 'todo_list.txt')     # Create the path to the to-do list file using the directory
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'todos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.before_request
def load_data_to_g():
    todos = Todo.query.all()
    g.todos = todos 
    g.todo = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
sdfdsfsdfslol;sdfsd

sdlfksdfsdfk