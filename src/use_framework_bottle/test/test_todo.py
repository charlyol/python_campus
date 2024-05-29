from use_framework_bottle.app import controlers
from webtest import TestApp
import pytest
import os
import sqlite3

db_path = os.path.abspath('../app/todo_db/todo.db')


@pytest.fixture
def test_app():
    return TestApp(controlers)


# Fixture pour configurer une base de données de test
@pytest.fixture
def setup_db():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(
        '''CREATE TABLE IF NOT EXISTS todo (id INTEGER PRIMARY KEY, task TEXT NOT NULL, status INTEGER NOT NULL)''')
    c.execute("INSERT INTO todo (task, status) VALUES ('Test task 1', 1)")
    c.execute("INSERT INTO todo (task, status) VALUES ('Test task 2', 1)")
    conn.commit()
    conn.close()
    yield
    # Tear down
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("DROP TABLE todo")
    conn.commit()
    conn.close()


def test_index_redirect(test_app):
    response = test_app.get('/')
    assert response.status_int == 302
    assert response.headers['Location'] == 'http://localhost/todo'


def test_todo_list(test_app, setup_db):
    response = test_app.get('/todo')
    assert response.status_int == 200
    assert 'Test task 1' in response.text
    assert 'Test task 2' in response.text


def test_add_new_item(test_app, setup_db):
    response = test_app.get('/new', params={'save': 'save', 'task': 'New test task'})
    assert response.status_int == 200
    assert 'The new task was inserted into the database' in response.text

    response = test_app.get('/todo')
    assert 'New test task' in response.text


def test_edit_item(test_app, setup_db):
    response = test_app.get('/edit/1')
    assert response.status_int == 200
    assert 'Test task 1' in response.text

    response = test_app.get('/edit/1', params={'save': 'save', 'task': 'Updated test task', 'status': 'open'})
    assert response.status_int == 200
    assert 'The item number 1 was successfully updated' in response.text

    response = test_app.get('/todo')
    assert 'Updated test task' in response.text
