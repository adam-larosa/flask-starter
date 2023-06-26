from config import app

from models import Cat

@app.route( '/' )
def rootroute():
    return "meow\n"

if __name__ == '__main__':
    app.run( port = 5555, debug = True )