from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__,
            template_folder="../client/templates",
            static_folder="../client/static")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


def create_app(test_config=None):

    @app.route('/', methods=['POST', 'GET'])
    def index():
        if request.method == 'POST':
            task_content = request.form['content']
            new_task = Todo(content=task_content)

            try:
                db.session.add(new_task)
                db.session.commit()
                return redirect('/')
            except:
                return task_content

        else:
            tasks = Todo.query.order_by(Todo.date_created).all()
            return render_template('index.html', tasks=tasks)

    @app.route('/delete/<int:id>')
    def delete(id):
        task_to_delete = Todo.query.get_or_404(id)

        try:
            db.session.delete(task_to_delete)
            db.session.commit()
            return redirect('/')
        except:
            return 'Problem deleting task'

    @app.route('/update/<int:id>', methods=['Get', 'POST'])
    def update(id):
        task = Todo.query.get_or_404(id)

        if request.method == 'POST':
            task.content = request.form['content']

            try:
                db.session.commit()
                return redirect('/')
            except:
                return 'Cannnot update task'
        else:
            return render_template('update.html', task=task)

    return app