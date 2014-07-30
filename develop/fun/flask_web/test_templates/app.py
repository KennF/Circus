from datetime import datetime
from flask import Flask, request, current_app, redirect, url_for, render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
	# print current_app.name
	# print dir(current_app)
	# user_agent = request.headers.get('User-Agent')
	# ret = 'hello world' + '<br/>'
	# ret += 'Your browser\'s User Agent is ' + user_agent + '<br/>'
	# # for k in dir(current_app):
	# # 	ret += '%s' % k + '<br/>'
	# # for k,v in current_app.url_map.items():
	# # 	ret += '%s: %s' % (k,v) + '<br/>'
	# return 
    return render_template('title.html', current_time=datetime.utcnow())

@app.route('/bad')
def error_400():
	return '<h1>Bad Request</h1>', 400

@app.errorhandler(404) 
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500) 
def internal_error(e):
    return render_template('500.html'), 404

@app.route('/redirect')
def redirect_to():
	return redirect(url_for('index'))

@app.route('/user/<name>/')
def user(name):
	return render_template('user.html', name=name, check_safe='<h1>safe</h1>', check_unsafe='<h1>unsafe</h1>',
        comments=['comment1', 'comment2'])
@app.route('/users/<name>/')
def users(name):
    return render_template('users.html', name=name)

# @app.before_request
def before():
	print '======= before request ========'

if __name__ == '__main__':
	manager.run()

