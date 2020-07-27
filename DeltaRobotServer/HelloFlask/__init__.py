import eventlet
eventlet.monkey_patch(thread=True)
from flask import Flask
from flask_socketio import SocketIO, emit
app = Flask(__name__)
app.config['SECRET KEY'] = '0931'
socketio = SocketIO(app)
from datetime import datetime
from flask import render_template, request
from HelloFlask import app, socketio
import Inversekinematics as m
import sys
import math
import numpy
import time
#from flask_socketio import SocketIO, emit
import socketio
from threading import Thread
#Startvalues
x_newvalue = 0
y_newvalue = 0
z_newvalue = 120
slide_value = 10
sio = socketio.Server(async_mode='eventlet')

@sio.on('connect')  # global namespace
def handle_connect(sid, environ):
    print('Client connected')

@sio.on('connect', namespace='/')
def handle_chat_connect(sid, data):
    print('Client connected to joint1 namespace')

def emitData(x_value, y_value, z_value, time):
    #Computing the pulse for each joint:
    data1 = 1.94 * m.getTheta(1,x_value, y_value, z_value) + 110
    data2 = 1.94 * m.getTheta(2,x_value, y_value, z_value) + 110
    data3 = 1.94 * m.getTheta(3,x_value, y_value, z_value) + 110
    #Emitting the computed pulses:
    sio.emit('joint1', data1, namespace='/')
    eventlet.sleep(0)
    sio.emit('joint2', data2, namespace='/')
    eventlet.sleep(0)
    sio.emit('joint3', data3, namespace='/')
    eventlet.sleep(0)
    print("joint angel_1 = " + str(data1))
    print("joint angel_2 = " + str(data2))
    print("joint angel_3 = " + str(data3))
    eventlet.sleep(time)

#Function for moving in a circle
def circleEmit():
    global x_newvalue, y_newvalue, z_newvalue, slide_value
    for x in numpy.arange(0, 2*math.pi, 0.3):
        x_newvalue = 0+40*math.cos(x)
        y_newvalue = 0+40*math.sin(x)
        z_newvalue = 120
        emitData(x_newvalue, y_newvalue, z_newvalue, 0)

#Function for moving in a square
def squareEmit():
    global x_newvalue, y_newvalue, z_newvalue, slide_value
    z_newvalue = 120
    x_newvalue = -40
    y_newvalue = -40
    for x in range(0,2):
        x_newvalue = x_newvalue *-1
        emitData(x_newvalue, y_newvalue, z_newvalue, 0.3)
        for y in range(0,1):
            y_newvalue = y_newvalue *-1
            emitData(x_newvalue, y_newvalue, z_newvalue, 0.3)
    x_newvalue = 40
    emitData(x_newvalue, y_newvalue, z_newvalue, 0.3)

@app.route('/', methods = ['GET', 'POST'])
def home():
    global x_newvalue, y_newvalue, z_newvalue, slide_value
    if 'RIGHT' in request.form:
        x_newvalue = x_newvalue - int(request.form['volume'])
        print(x_newvalue)
    elif 'LEFT' in request.form:
        x_newvalue = int(request.form['volume']) + x_newvalue 
        print(x_newvalue)
    elif 'UP' in request.form:
        y_newvalue = int(request.form['volume']) + y_newvalue
        print(y_newvalue)
    elif 'DOWN' in request.form:
        y_newvalue = y_newvalue - int(request.form['volume'])
        print(y_newvalue)
    elif 'RAISE' in request.form:
        z_newvalue = z_newvalue + int(request.form['volume'])
        print(z_newvalue)
    elif 'LOWER' in request.form:
        z_newvalue = z_newvalue - int(request.form['volume'])
        print(z_newvalue)
    elif 'HOME' in request.form:
        x_newvalue = 0
        y_newvalue = 0
        z_newvalue = 120

    #Save slider position
    if request.form:
        slide_value = request.form['volume']

    #New dictionary for storing joint values
    d={}
    #Storing the joint values in the dictioary
    for y in range (1,4):
        d["data{0}".format(y)] = 1.94 * m.getTheta(y,x_newvalue, y_newvalue, z_newvalue) + 110
        print("thetavalue_" + str(y)+" = " + str(d["data{0}".format(y)]) )

    jointset = ['joint1', 'joint2', 'joint3']

    #Check if the joint values is below the degress limit
    for num, name in zip(range(1,4), jointset):
        if d["data{0}".format(num)] < 460 and d["data{0}".format(num)] > 110 :
            #Emit the event and data to the client
            sio.emit(name, d["data{0}".format(num)])
            eventlet.sleep(0)
            print("joint angel_1 = " + str(d["data{0}".format(num)]) )

    #Update webpage
    return render_template(
        "index.html",
        x_value = x_newvalue,
        y_value = y_newvalue,
        z_value = z_newvalue,
        value = slide_value)

@app.route('/modes', methods = ['GET', 'POST'])
def modes():
    if 'CIRCLE' in request.form:
        #Running the function in a new thread to prevent the webpage from being blocked.
        thread = Thread(target = circleEmit)
        thread.daemon = True
        thread.start()
    if 'SQUARE' in request.form:
        thread = Thread(target = squareEmit)
        thread.daemon = True
        thread.start()
        #squareEmit()
    return render_template(
        "modes.html")
