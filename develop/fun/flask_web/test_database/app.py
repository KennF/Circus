import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)

manager = Manager(app)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class NameForm(Form):
    name = StringField(label='What\'s your name?', validators=[ Required() ])
    submit = SubmitField(label='Submit')

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    
    def __repr__(self):
        return '<User %r>' % self.username

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')
    
    def __repr__(self):
        return '<Role %r>' % self.name
@app.route('/', )

if __name__ == '__main__':
    manager.run()
