#!usr/bin/env python
#coding:utf-8

from flask import Flask, url_for, request, render_template,flash, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form, TextField, SubmitField, required, ValidationError
from datetime import datetime


DEBUG = True
SECRET_KEY = '\xb3|\x0cYxxM\xd7P\x16\xc3\x9f.\x16\xbe\xd0x\xdaQA\x8c\xc5\x9b}'
SQLALCHEMY_DATABASE_URI = 'sqlite:///todo.sqlite'

app = Flask(__name__)
app.config.from_object(__name__)

db = SQLAlchemy(app)
db.init_app(app)

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255), nullable=False)
	posted_on = db.Column(db.Date, default = datetime.utcnow)
	status = db.Column(db.Boolean(), default=False)

	def __init__(self, *args, **kwargs):
		super(Todo, self).__init__(*args, **kwargs)

	def __repr__(self):
		return "<Todo '%s'>" % self.title

	def store_to_db(self):
		db.session.add(self)
		db.session.commit()

	def delete_todo(self):
		db.session.delete(self)
		db.session.commit()

class TodoForm(Form):
	title = TextField(u'内容', validators=[required(message=u'任务内容')])


@app.route('/', methods=['GET', 'POST'])
def index():
	todo = Todo.query.order_by('-id')
	form = TodoForm(request.form)
	if request.method == 'POST' and form.validate_on_submit():
		t = Todo(title=form.title.data)
		try:
			t.store_to_db()
			print 'done'
			flash(u'添加成功')
			return redirect(request.args.get('next') or url_for('index'))
		except:
			flash(u'存储失败')
	return render_template('index.html', todo=todo, form=form)

@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
	todo = Todo.query.filter_by(id=id).first()
	form = TodoForm(title=todo.title)
	if request.method == 'POST' and form.validate_on_submit():
		Todo.query.filter_by(id=id).update({Todo.title: request.form('title')})
		db.session.commit()
		flash(u'记录编辑成功')
		return redirect(url_for('index'))
	return render_template('edit.html', todo=todo, form=form)

def tdel(id):
	todo = Todo.query.filter_by(id=id).first()
	if todo:
		todo.delete_todo()
	flash(u'记录删除成功')
	return redirect(url_for('index'))

@app.route('/<int:id>/done')
def done(id):
	todo = Todo.query.filter_by(id=id).first()
	if todo:
		Todo.query.filter_by(id=id).update({Todo.status:True})
		db.session.commit()
		flash(u'任务完成')

	return redirect(url_for('index'))

@app.route('/<int:id>/redo')
def redo(id):
	todo = Todo.query.filter_by(id=id).first()
	if todo:
		Todo.query.filter_by(id=id).update({Todo.status:False})
		db.session.commit()
		flash(u'记录重置成功')

	return 	redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_404.html'), 404




@app.route('/hello')
def hello():
	return 'Hello world'

if __name__ == '__main__':
	app.run()


