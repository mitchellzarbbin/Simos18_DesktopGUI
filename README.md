# Simos18_DesktopGUI

This repository contains the code for a desktop application that provides a graphical user interface (GUI) for interacting with the Simos18 automotive system. The application is built using the Tkinter library in Python.

## Files

### ui/ui.py

This file contains the implementation of the UI class and the ConnectionGUI class. The UI class initializes the main window of the application and sets its properties. The ConnectionGUI class represents the interface manager section of the application and handles the creation of dropdown menus and buttons for selecting and connecting to the available interfaces.

### func/J2534_Interfaces.py

This file contains the implementation of the GetJ2534Interfaces function. This function retrieves the available interfaces from the Windows registry. It uses the winreg module to access the registry keys and retrieve the necessary information about the interfaces.

### main.py

This file is the entry point of the application. It creates instances of the UI and ConnectionGUI classes and starts the main event loop of the application.

### More to Come!
