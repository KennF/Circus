import cgi
import datetime
import urllib
import webapp2
import jinja2
import os

from google.appengine.ext import db
from google.appengine.api import users

form = """
    <form method="post" action="testform">
        <input name="q">
        <input type="submit" value="submit">
    </form>
    """

         

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["content-type"] = "text/html"
        self.response.out.write(form)

class TestHandler(webapp2.RequestHandler):
    def post(self):
        # q = self.request.get('q')
        # self.response.out.write(q)
        self.response.headers["content-type"] = "text/plain"
        self.response.out.write(self.request)

app = webapp2.WSGIApplication([('/', MainPage),
                                ('/testform', TestHandler)],
                              debug=True)