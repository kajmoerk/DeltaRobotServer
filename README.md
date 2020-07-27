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
## References:
Computations are based on inverse kinematics from:
R.L. Williams II, “The Delta Parallel Robot: Kinematics Solutions”, Internet Publication,
www.ohio.edu/people/williar4/html/pdf/DeltaKin.pdf, January 2016.
