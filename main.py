import webapp2
import os
import logging
import jinja2

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render({'title': 'HOME'}))

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/about.html')
        self.response.write(template.render({'title': 'ABOUT'}))

class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
        self.response.write(template.render({'title': 'CONTACT'}))

class OriginHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/TheOrigin.html')
        self.response.write(template.render({'title': 'The Origin'}))

class MLHHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/MLH.html')
        self.response.write(template.render({'title': 'Michigan Legal Help'}))

class EASportsHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/EASports.html')
        self.response.write(template.render({'title': 'EA Sports'}))

class EAXfinityHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/EAXfinity.html')
        self.response.write(template.render({'title': 'EA Xfinity'}))

class FitBarkHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/FitBark.html')
        self.response.write(template.render({'title': 'FitBark'}))

app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/about.html', AboutHandler),
    ('/contact.html', ContactHandler),
    ('/TheOrigin.html', OriginHandler),
    ('/MLH.html', MLHHandler),
    ('/EASports.html', EASportsHandler),
    ('/EAXfinity.html', EAXfinityHandler),
    ('/FitBark.html', FitBarkHandler),
], debug=True)
