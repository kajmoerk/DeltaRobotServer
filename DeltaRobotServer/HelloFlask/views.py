from datetime import datetime
from flask import render_template, request
from HelloFlask import app, socketio
import Inversekinematics as m
import sys
import eventlet
#from flask_socketio import SocketIO, emit
import socketio
#Startvalues
x_newvalue = 0
y_newvalue = 0
z_newvalue = 0
slide_value = 10
sio = socketio.Server(sync_mode='eventlet')
def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@sio.on('client', namespace='/chat')
def senddata(data):
    socketio.emit('client', 'Hello world', broadcast=True)
    print("i work!", data)


@sio.on('connect')  # global namespace
def handle_connect():
    print('Client connected')

@sio.on('connect', namespace='/chat')
def handle_chat_connect():
    print('Client connected to chat namespace')
    emit('chat message', 'welcome!')

@app.route('/', methods = ['GET', 'POST'])
#@app.route('/home', methods = ['GET', 'POST'])
def home():
    global x_newvalue, y_newvalue, z_newvalue, slide_value
    if 'UP' in request.form:
        x_newvalue = int(request.form['volume']) + x_newvalue
        print(x_newvalue)
    elif 'DOWN' in request.form:
        x_newvalue = x_newvalue - int(request.form['volume']) 
        print(x_newvalue)
    elif 'RIGHT' in request.form:
        y_newvalue = int(request.form['volume']) + y_newvalue
        print(y_newvalue)
    elif 'LEFT' in request.form:
        y_newvalue = y_newvalue - int(request.form['volume'])
        print(y_newvalue)
    elif 'RAISE' in request.form:
        z_newvalue = z_newvalue + int(request.form['volume'])
        print(z_newvalue)
    elif 'LOWER' in request.form:
        z_newvalue = z_newvalue - int(request.form['volume'])
        print(z_newvalue)
    #Save slider position
    if request.form:
        slide_value = request.form['volume']
    #senddata(str(m.getTheta(1,x_newvalue, y_newvalue, z_newvalue)))
    #senddata(str(m.getTheta(2,x_newvalue, y_newvalue, z_newvalue)))
    #senddata(str(m.getTheta(3,x_newvalue, y_newvalue, z_newvalue)))
    return render_template(
        "index.html",
        x_value = x_newvalue,
        y_value = y_newvalue,
        z_value = z_newvalue,
        value = slide_value)

@app.route('/joint1', methods = ['GET', 'POST'])
def sendjoint1():
    return str(m.getTheta(1,x_newvalue, y_newvalue, z_newvalue))
@app.route('/joint2', methods = ['GET', 'POST'])
def sendjoin2():
    return str(m.getTheta(2,x_newvalue, y_newvalue, z_newvalue))
@app.route('/joint3', methods = ['GET', 'POST'])
def sendjoint3():
    return str(m.getTheta(3,x_newvalue, y_newvalue, z_newvalue))