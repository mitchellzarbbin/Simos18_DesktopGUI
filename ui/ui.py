from tkinter import *

from func.J2534_Interfaces import *

class UI:
    def __init__(self):
        """
        Initializes the UI class.

        Parameters:
        None

        Returns:
        None
        """
        self.root = Tk()
        self.root.title("neBuLa - Simos18 Desktop Application")
        self.root.geometry("360x120")
        self.root.config(bg="white")

class ConnectionGUI:
    def __init__(self, root):
        """
        Initializes the UI class.
        Parameters:
        - root: The root Tkinter object.
        Returns:
        None
        """
        self.root = root
        self.frame = LabelFrame(root, text="Interface Manager", padx=5, pady=5, bg="white")
        self.label_interface = Label(self.frame, text="Avaliable Interface(s)", bg="white", width=18, anchor=W)
        self.label_STMIN = Label(self.frame, text="STMIN", bg="white", width=15, anchor=W)

        self.STMINOptionMenu()
        self.InterfaceOptionMenu()

        self.btn_interfacerefresh = Button(self.frame, text="Refresh", width=10, command=self.InterfaceOptionMenu)
        self.btn_getecu = Button(self.frame, text="Get ECU", width=10, state="disabled")

        self.padx = 20
        self.pady = 5

        self.publish()

    def publish(self):
        """
        Publishes the frame, labels, dropdowns, and buttons to the GUI grid.
        Parameters:
        - None
        Returns:
        - None
        """
        self.frame.grid(row=0, column=0, rowspan=3, columnspan=3, padx=5, pady=5)
        self.label_interface.grid(column=1, row=2)
        self.label_STMIN.grid(column=1, row=3)

        self.drop_STMIN.grid(column=2, row=3, padx=self.padx, pady=self.pady)
        self.drop_Interfaces.grid(column=2, row=2, padx=self.padx)

        self.btn_interfacerefresh.grid(column=3, row=2)
        self.btn_getecu.grid(column=3, row=3)

    def InterfaceOptionMenu(self):
        """
        Creates an option menu for selecting an interface.
        Returns:
            None
        """
        self.drop_Interfaces = StringVar()
        self.drop_Interfaces.set("Select Interface")

        self.drop_Interfaces = StringVar()
        self.drop_Interfaces.set("Select Interface")
        interfaces = GetJ2534Interfaces()
        self.drop_Interfaces = OptionMenu(self.frame, self.drop_Interfaces, interfaces, *interfaces)

    def STMINOptionMenu(self):
        """
        Creates the dropdown menu for the available STMIN values.
        Parameters:
        - None
        Returns:
        - None
        """
        self.drop_STMIN = StringVar()
        self.drop_STMIN.set("Select STMIN")
        self.drop_STMIN = OptionMenu(self.frame, self.drop_STMIN, "35000")


if __name__ == "__main__":
    UI()
    ConnectionGUI()