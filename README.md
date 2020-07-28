# DeltaRobotServer
A flask/python server for controlling delta robots trough Socket.IO's emits and events.
The DeltaRobotServer works with the DeltaController: https://github.com/kajmoerk/DeltaController.git or any websockets that support Socket.IO
![Image Software Architecture](https://github.com/kajmoerk/DeltaRobotServer/blob/master/Images/Software_Architecture.jpeg)
## Freatures:
* C++ library for converting cartesian coordinates to joint degrees and pulse.
* Local hosted server with Html/Css/Javascript as frontend and Python/C++ as backend.  
* Test pattern - Circle.
* Test pattern - Square.
## Todo:
* Teach linear point to point.
* Teach circular point to point.
* Trajectory planning
## Test and edit in Visual Studio:
Clone the repository and open the "DeltaRobotServer.sln". A new Python enviroment will have to be created and dependencies needs to be installed.
Edit the Inversekinematics.cpp in the Inversekinematics folder, if needed. 
## Test and edit without Visual Studio:
Clone the repository and run "setup.py", to install dependencies and then run "runserver.py" to start the server.
The Inversekinematics folder can be ignored, instead the Inversekinematics.cpp in DeltarobotServer/DeltarobotServer/HelloFlask/src/ should be edited, if needed.
## References:
Computations are based on inverse kinematics from:
R.L. Williams II, “The Delta Parallel Robot: Kinematics Solutions”, Internet Publication,
www.ohio.edu/people/williar4/html/pdf/DeltaKin.pdf, January 2016.
