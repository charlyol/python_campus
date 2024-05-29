import os
import sqlite3
from bottle import route, run, redirect, debug, template, request, TEMPLATE_PATH

path_directory = os.path.join(os.getcwd(), '..', 'views')
TEMPLATE_PATH.insert(0, path_directory)

db_path = os.path.abspath('../todo_db/todo.db')


# Redirect the root URL to the todo list
@route('/')
def index():
    redirect('/todo')


# Display the todo list
@route('/todo')
def todo_list():
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Execute SQL query to select open tasks
    c.execute("SELECT id, task, status FROM todo WHERE status LIKE '1'")

    # Fetch all results
    result = c.fetchall()

    # Close the database connection
    conn.close()

    # Return the result formatted using a template
    return template('make_table', rows=result)


# Handle adding a new item to the todo list
@route('/new', method='GET')
def new_item():
    if request.GET.save:
        new = request.GET.task.strip()
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        # Insert the new task into the database
        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new, 1))
        new_id = c.lastrowid

        # Commit the transaction and close the database connection
        conn.commit()
        conn.close()

        # Return a response indicating the new task was successfully inserted
        return ('<p>The new task was inserted into the database, the ID is %s</p>'
                '<form action="/todo"><input type="submit" value="Go to To-Do List" /></form>') % new_id
    else:
        # Return the HTML form for adding a new task
        return template('new_task.tpl')


# Route to handle editing an existing item
@route('/edit/<no:int>', method='GET')
def edit_item(no):
    # If the form is submitted (GET request with 'save' parameter)
    if request.GET.save:
        edit = request.GET.task.strip()
        status = request.GET.status.strip()

        # Determine the status value
        if status == 'open':
            status = 1
        else:
            status = 0

        # Connect to the SQLite database
        conn = sqlite3.connect('../todo_db/todo.db')
        c = conn.cursor()

        # Update the task in the database
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))

        # Commit the transaction and close the database connection
        conn.commit()
        conn.close()

        # Return a response indicating the task was successfully updated
        return ('<p>The item number %s was successfully updated</p>'
                '<form action="/todo"><input type="submit" value="Go to To-Do List" /></form>' % no)
    else:
        # Connect to the SQLite database
        conn = sqlite3.connect('../todo_db/todo.db')
        c = conn.cursor()

        # Select the task that matches the given id
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no),))

        # Fetch the current data of the task
        cur_data = c.fetchone()
        conn.close()

        # Return the template to edit the task
        return template('edit_task', old=cur_data, no=no)


# Route to show an item using a dynamic route with a regular expression
@route('/item<item:re:[0-9]+>')
def show_item(item):
    # Connect to the SQLite database
    conn = sqlite3.connect('../todo_db/todo.db')
    c = conn.cursor()

    # Select the task that matches the given id
    c.execute("SELECT task FROM todo WHERE id LIKE ?", (item,))
    result = c.fetchone()
    conn.close()

    # Check if the result is empty
    if not result:
        return 'This item number does not exist!'
    else:
        return 'Task: %s' % result[0]


# Enable debugging to get detailed error information
debug(True)

# Enable auto-reloading to detect script changes
run(host='localhost', port=8081, reloader=True)
