from app import db, ToDo

first_todo = ToDo(todo_text = "learn flask")
db.session.add(first_todo)
db.session.commit()