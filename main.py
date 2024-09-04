from ui.ui import UI, ConnectionGUI

RootMaster = UI()

ConnectionMaster = ConnectionGUI(RootMaster.root)

RootMaster.root.mainloop()