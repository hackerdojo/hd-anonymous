from google.appengine.api import mail
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util, template

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render('main.html', locals()))
    
    def post(self):
        message = self.request.get('body')
        if message:
            mail.send_mail(
                sender="Anonymous <no-reply@hackerdojo-anonymous.appspotmail.com>",
                to="Staff <staff@hackerdojo.com>",
                subject="An anonymous tip has been submitted",
                body='%s\n\n---\n%s' % (message, self.request.remote_addr))
            thankyou = True
            self.response.out.write(template.render('main.html', locals()))
        else:
            self.redirect("/")

def main():
    application = webapp.WSGIApplication([('/', MainHandler)],debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
