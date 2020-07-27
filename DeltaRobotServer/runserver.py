import eventlet
import os
from HelloFlask import app, socketio, sio   # Imports the code from HelloFlask/__init__.py
#from flask_socketio import SocketIO, emit
import subprocess
import socketio
#from clienthandler import chitchat
#from multiprocessing import Process

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')

    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    app = socketio.WSGIApp(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
    #app.run(HOST, PORT)
    #socketio.run(app, HOST, PORT)
    #app.run(debug=True, host='0.0.0.0')
    #socketio.run(app, debug=True, host='0.0.0.0')