
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug, static_file
global comments


def html_comments():
	global comments
	text = '<ul>'
	for i in range(0,len(comments)):
		text += '<li class="message">'+comments[i]+'</li>'
	text += '</ul>'
	return text

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

