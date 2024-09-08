import winreg

def GetJ2534Interfaces():
    """
    Retrieves the available interfaces from the Windows registry.

    Parameters:
    None

    Returns:
    A list of available interfaces.
    """
    interfaces = []
    try:
        BaseKey = winreg.OpenKeyEx(
            winreg.HKEY_LOCAL_MACHINE, r"Software\\PassThruSupport.04.04\\"
        )
    except:
        print("No J2534 DLLs found in HKLM PassThruSupport. Continuing anyway.")
        return interfaces

    for i in range(winreg.QueryInfoKey(BaseKey)[0]):
        try:
            DeviceKey = winreg.OpenKeyEx(BaseKey, winreg.EnumKey(BaseKey, i))
            Name = winreg.QueryValueEx(DeviceKey, "Name")[0]
            FunctionLibrary = winreg.QueryValueEx(DeviceKey, "FunctionLibrary")[0]
            interfaces.append((Name, "J2534_" + FunctionLibrary))
        except:
            print("Found a J2534 interface, but could not enumerate the registry entry. Continuing.")
    return interfaces



