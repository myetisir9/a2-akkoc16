
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug, static_file
from hashlib import sha256

def create_hash(password):
    #Function taken from: https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()

password_hash = '51447d39ee4c9a8b7f54b58d8d4dd3eab587969dc3229eb51191fa3a4eaaa1df'

def htmlify(title,text):
    page = """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <title>%s</title>
            </head>
            <body>
            %s
            </body>
        </html>

    """ % (title,text)
    return page

def index():
   return static_file('index.html', root='./BIL101 A1')

@route('/comment')
def comment():
	return '''
            <form action="/comments" method="post">
                Comment: <input name="comment" type="text" value="" /></br>
                Password: <input name="passwordd" type="password" value="" />
                <input value="Click me" type="submit" />
            </form>
        '''
commentlist = []




def static_file_callback(filename):
	return static_file(filename, root='./BIL101 A1')

route('/', 'GET', index)
route('/<filename:path>', 'GET', static_file_callback)

#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()

