from app import db, Todo

# first_todo = Todo(todo_text="learn flask")
# db.session.add(first_todo)
# db.session.commit()

all_todos = Todo.query.all()
print(all_todos)