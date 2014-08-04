from flask import Flask, render_template, session, redirect, url_for, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form 
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
bootstrap = Bootstrap(app)

# should be in a env variable
app.config['SECRET_KEY'] = 'string hard to guess'

class NameForm(Form):
	name = StringField('What is your name?', validators=[Required()])
	submit = SubmitField('Submit')

# @app.route('/', methods=['GET', 'POST'])
# def index():
# 	name = None
# 	form = NameForm()
# 	if form.validate_on_submit():
# 		name = form.name.data
# 		form.name.data = ''
# 	return render_template('hello.html', form=form, name=name)

@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is None or old_name != form.name.data:
			flash('you\'ve changed your display name')
			flash('done')
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('index'))
	return render_template('hello.html', form=form, name=session.get('name'))

if __name__ == '__main__':
	app.run(debug=True)


