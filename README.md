### About Port-Scanner

A port scanner is a software tool designed to scan a network or host for open ports. It works by sending packets to the target device and analyzing the response to determine which ports are open, closed, or filtered. Port scanning can be used for legitimate purposes, but it is also commonly used by hackers to identify vulnerable systems.

### Features of the Code

The code creates a GUI-based port scanner application using the tkinter library.
The application takes input from the user for the host IP address and the port number to be scanned.
It uses the socket library to create a TCP connection with the specified host and port.
The scan is performed with a timeout of 2 seconds to prevent the scanner from getting stuck on unresponsive ports.
The application checks the result of the scan and displays a message indicating whether the port is open or closed.

### Modules Used

Socket - This module provides a low-level interface for network communication via sockets. It enables the creation of network sockets that can be used for sending and receiving data over a network.
<br><br>
Tkinter - This module is a standard Python library for creating graphical user interfaces (GUIs). It provides a set of tools and widgets for building windows, menus, buttons, and other GUI elements.
