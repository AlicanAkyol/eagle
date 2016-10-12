# -*- coding: cp1254 -*-
from _winreg import *
import os
import sys
import argparse
import wmi
import win32serviceutil                                         
import subprocess
import ctypes
import random, string
import platform

# r"SYSTEM\\CurrentControlSet\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000"

KEY1 = "HARDWARE\\DEVICEMAP\\Scsi\\"
KEY2 = "\\Target Id 0\\Logical Unit Id 0"
BACKWARD_SLASH = "\\"
conf_arr = [ 'isolation.tools.getPtrLocation.disable = "TRUE"', 
'isolation.tools.setPtrLocation.disable = "TRUE"', 
'isolation.tools.setVersion.disable = "TRUE"', 
'isolation.tools.getVersion.disable = "TRUE"', 
'monitor_control.disable_directexec = "TRUE"', 
'monitor_control.disable_chksimd = "TRUE"', 
'monitor_control.disable_ntreloc = "TRUE"', 
'monitor_control.disable_selfmod = "TRUE"', 
'monitor_control.disable_reloc = "TRUE"', 
'monitor_control.disable_btinout = "TRUE"', 
'monitor_control.disable_btmemspace = "TRUE"', 
'monitor_control.disable_btpriv = "TRUE"', 
'monitor_control.disable_btseg = "TRUE"' 
]

global_list = []
xp = False

def modifyValue( arrr ):

	try:
		aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
		aKey = OpenKey(aReg, arrr[0], 0, KEY_ALL_ACCESS)
		try:
			# asubkey_name = EnumKey(aKey,i)
			# asubkey = OpenKey(aKey,asubkey_name)
			val = QueryValueEx(aKey, arrr[1])
			for j in range (len(arrr)):
				if j > 1:
					try:
						if arrr[j].upper() in val[0].upper():
							SetValueEx(aKey, arrr[1], 0, REG_SZ, "NVIDIA")
					except Exception, err:
						try:
							for k in range(len(val[0])):
								if arrr[j].upper() in val[0][k].upper():
									SetValueEx(aKey, arrr[1], 0, REG_SZ, "NVIDIA")
						except Exception, err:
							pass
			
		except Exception,err:
			pass
				
		CloseKey(aKey)
		CloseKey(aReg)
		
	except Exception, err:
		pass



def checkAndDeleteKey( vmRegKeys ):  ## unused

	try:
		aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
		aKey = OpenKey(aReg, vmRegKeys, 0, KEY_ALL_ACCESS)
		if aKey:

			try:
				print vmRegKeys
				DeleteValue( aKey, "LocalizedString" )

			except Exception,err:
				pass

			CloseKey(aKey)
			CloseKey(aReg)
                        
	except Exception,err:
                pass

def traverse( key, reg_list):

        try:
                hReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
		hKey = OpenKey(hReg, key, 0, KEY_ALL_ACCESS)
                #hKey = _winreg.OpenKey(root, key);
                try:
                        i = 0
                        while True:
                                strFullSubKey = ""
                                strSubKey = ""
                                try:
                                        strSubKey = EnumKey(hKey, i)
                                        print strSubKey
                                        strFullSubKey = key + "\\" + strSubKey;
                                except WindowsError:
                                        hKey.Close();
                                        return;
                                traverse( key, global_list);
                                print strSubKey
                                global_list.append(key);
                                i += 1
                                
                except  WindowsError,err:
                        pass
                hKey.Close();                

        except:
                pass


 
def regDeleteKey( key ):

        try:        
                #traverse( key, global_list);
                #print global_list
                #for item in global_list:
                        #hReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
                        #hKey = OpenKey(hReg, item, 0, KEY_ALL_ACCESS)

                        #try:
                                #DeleteKey(hKey, item);
                        #except:
                        #       pass

                        #hKey.Close();
                hReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
                hKey = OpenKey(hReg, key, 0, KEY_ALL_ACCESS)
                DeleteKey(hReg, key);
                hKey.Close();
                

        except Exception, err:
                print err
                print key
                pass


def keyList():

	vmRegKeys = [
	"SOFTWARE\\Clients\\StartMenuInternet\\VMWAREHOSTOPEN.EXE",
	"SOFTWARE\\VMware, Inc.\\VMware Tools",
	"SOFTWARE\\Microsoft\\ESENT\\Process\\vmtoolsd",
	"SYSTEM\\CurrentControlSet\\Enum\\IDE\\CdRomNECVMWar_VMware_SATA_CD01_______________1.00____",
	"SYSTEM\\CurrentControlSet\\Enum\\IDE\\CdRomNECVMWar_VMware_IDE_CDR10_______________1.00____",
	"SYSTEM\\CurrentControlSet\\Enum\\SCSI\\Disk&Ven_VMware_&Prod_VMware_Virtual_S&Rev_1.0",
	"SYSTEM\\CurrentControlSet\\Enum\\SCSI\\Disk&Ven_VMware_&Prod_VMware_Virtual_S",
	"SYSTEM\\CurrentControlSet\\Control\\CriticalDeviceDatabase\\root#vmwvmcihostdev",
	"SYSTEM\\CurrentControlSet\\Control\\VirtualDeviceDrivers",
	"SYSTEM\\CurrentControlSet\\Services\\IRIS5",
	"SOFTWARE\\eEye Digital Security",
	"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Wireshark",
	"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\wireshark.exe",
	"SOFTWARE\\ZxSniffer.exe",
	"SOFTWARE\\Cygwin",
	"SOFTWARE\\B Labs\\Bopup Observer",
	"AppEvents\\Schemes\\Apps\\Bopup Observer",
	"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Win Sniffer_is1",
	"SOFTWARE\\Win Sniffer"
        ]
	
	for reg in vmRegKeys:
                try:
                        regDeleteKey( reg )
                except Exception,err:
                        pass

        
def valueList():

	arr = [ [ "SYSTEM\\CurrentControlSet\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000", 
	"DriverDesc", 
	"vmware svga ii", 
	"vmware svga 3d", 
	"vmware vmscsi controller" ], 
	[ "SYSTEM\\CurrentControlSet\\Control\\Class\\{4D36E96F-E325-11CE-BFC1-08002BE10318}\\0000", 
	"InfSection", 
	"vmmouse" ], 
	[ "SYSTEM\\CurrentControlSet\\Control\\Video\\{4BEF3D64-1F2B-4026-9EE4-B6D8CD9FEA1B}\\0000", 
	"Device Description", 
	"vmware svga ii" ], 
	[ "SYSTEM\\CurrentControlSet\\Control\\Video\\{3A8088C5-4419-4572-801C-A10BA858952F}\\0000", 
	"Device Description", 
	"vmware svga 3d" ], 	
	[ "SYSTEM\\CurrentControlSet\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000", 
	"HardwareInformation.AdapterString", 
	"VMware SVGA 3D" ], 
	[ "SYSTEM\\CurrentControlSet\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000", 
	"HardwareInformation.ChipType", 
	"VMware Virtual SVGA 3D Graphics Adapter" ], 	
	[ "SYSTEM\\CurrentControlSet\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000", 
	"InfSection", 
	"VM3D_AMD64" ], 
	[ "SYSTEM\\CurrentControlSet\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000", 
	"InstalledDisplayDrivers", 
	"vm3dum64", 
	"vm3dum", 
	"vm3dgl64",	
	"vm3dgl" ], 
	[ "SYSTEM\\CurrentControlSet\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000", 
	"OpenGLDriverName", 
	"vm3dgl64.dll" ], 
	[ "SYSTEM\\CurrentControlSet\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000", 
	"OpenGLDriverNameWow", 
	"vm3dgl.dll" ], 
	[ "SYSTEM\\CurrentControlSet\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000", 
	"ProviderName", 
	"VMware, Inc." ],
	[ "SYSTEM\\CurrentControlSet\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000", 
	"UserModeDriverName", 
	"vm3dum64.dll" ],
	[ "SYSTEM\\CurrentControlSet\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000", 
	"UserModeDriverNameWow", 
	"vm3dum.dll" ],
	[ "SYSTEM\\CurrentControlSet\\Control\\Class\\{4D36E96F-E325-11CE-BFC1-08002BE10318}\\0000", 
	"DriverDesc", 
	"VMware Pointing Device" ],
	[ "SYSTEM\\CurrentControlSet\\Control\\Class\\{4D36E96F-E325-11CE-BFC1-08002BE10318}\\0000", 
	"ProviderName", 
	"VMware, Inc." ],
	[ "SYSTEM\\CurrentControlSet\\Control\\Class\\{4D36E96F-E325-11CE-BFC1-08002BE10318}\\0001", 
	"DriverDesc", 
	"VMware USB Pointing Device" ],
	[ "SYSTEM\\CurrentControlSet\\Control\\Class\\{4D36E96F-E325-11CE-BFC1-08002BE10318}\\0000", 
	"InfSection", 
	"VMUsbMouse" ],
	[ "SYSTEM\\CurrentControlSet\\Control\\Class\\{4D36E96F-E325-11CE-BFC1-08002BE10318}\\0000", 
	"ProviderName", 
	"VMware, Inc." ]
	]
	
	arr_val1 = [ "Scsi Port 0", "Scsi Port 1", "Scsi Port 2", "Scsi Port 3", "Scsi Port 4" ];
	arr_val2 = [ "Scsi Bus 0", "Scsi Bus 1", "Scsi Bus 2", "Scsi Bus 3", "Scsi Bus 4", "Scsi Bus 5", "Scsi Bus 6" ];
	
	for j in range(len(arr_val1)):
		for k in range(len(arr_val2)):
			first_value = KEY1 + arr_val1[j] + BACKWARD_SLASH + arr_val2[k] + KEY2
			arr_port = [ [first_value, 
			"Identifier", 
			"vmware"] 
			]
			modifyValue(arr_port[0])
				
	for i in range(len(arr)):
		modifyValue( arr[i] )

def stopAndDeleteServices( service_name ): ## working on...

        try:
                for i in range( len( service_name ) ):
                        try:
                                win32serviceutil.StopService( service_name[i] )
                        except:
                                pass
                        
        except Exception,err:
                pass

        try:
                for i in range( len( service_name ) ):
                        try:
                                delete_service_command = "sc delete " + service_name[i]
                                subprocess.call(delete_service_command, shell=True)
                        except:
                                pass

        except Exception,err:
                pass

        try:
                vmFiles()
                
        except Exception, err:
                pass


def servicesList(): ## working on...

        services = [ "vmhgfs", "VMMEMCTL", "vmmouse", "vmrawdsk",
				 "VMTools", "vmusbmouse", "vmvss", "vmscsi",
				 "VMware Physical Disk Helper Service",
				 "vmxnet", "vmx_svga", "vmbus", "VMBusHID", "vmci" ]
	
        stopAndDeleteServices ( services )

def randomword( length ):

        return ''.join(random.choice(string.lowercase) for i in range(length))

def vmFiles():
        #"C:\Windows\System32\drivers\\vmmouse.sys",
        files = [
		"C:\WINDOWS\System32\\vm3dgl64.dll",
		"C:\WINDOWS\System32\\vm3dgl.dll",
		"C:\WINDOWS\System32\\vm3dum64.dll",
		"C:\WINDOWS\System32\\vm3dum.dll",
		"C:\WINDOWS\System32\VmbuxCoinstaller.dll",
		"C:\WINDOWS\System32\\vmGuestLib.dll",
		"C:\WINDOWS\System32\\vmGuestLibJava.dll",
		"C:\WINDOWS\System32\\vmhgfs.dll",
		"C:\WINDOWS\System32\\vmicsvc.exe",
		"C:\WINDOWS\System32\\vmwogl32.dll",
		"C:\WINDOWS\System32\\vmmreg32.dll",
		"C:\WINDOWS\System32\\vmx_fb.dll",
		"C:\WINDOWS\System32\\vmx_mode.dll",
                "C:\WINDOWS\System32\\vmhgfs.dll",
		"C:\WINDOWS\System32\VMUpgradeAtShutdownWXP.dll",
		"C:\Windows\System32\drivers\\vmhgfs.sys",
                "C:\Windows\System32\drivers\\VMMEMCTL.sys",
                "C:\Windows\System32\drivers\\vmrawdsk.sys",
                "C:\Windows\System32\drivers\VMTools.sys",
                "C:\Windows\System32\drivers\\vmusbmouse.sys",
                "C:\Windows\System32\drivers\\vmvss.sys",
                "C:\Windows\System32\drivers\\vmscsi.sys",
                "C:\Windows\System32\drivers\VMware Physical Disk Helper Service.sys",
                "C:\Windows\System32\drivers\\vmxnet.sys",
                "C:\Windows\System32\drivers\\vmx_svga.sys",
                "C:\Windows\System32\drivers\\vmbus.sys",		
                "C:\Windows\System32\drivers\\VMBusHID.sys",
                "C:\Windows\System32\drivers\\vmci.sys" 
	]

        files2 = [
		"C:\WINDOWS\SysWOW64\\vm3dgl64.dll",
		"C:\WINDOWS\SysWOW64\\vm3dgl.dll",
		"C:\WINDOWS\SysWOW64\\vm3dum64.dll",
		"C:\WINDOWS\SysWOW64\\vm3dum.dll",
		"C:\WINDOWS\SysWOW64\VmbuxCoinstaller.dll",
		"C:\WINDOWS\SysWOW64\\vmGuestLib.dll",
		"C:\WINDOWS\SysWOW64\\vmGuestLibJava.dll",
		"C:\WINDOWS\SysWOW64\\vmhgfs.dll",
		"C:\WINDOWS\SysWOW64\\vmicsvc.exe",
		"C:\WINDOWS\SysWOW64\\vmwogl32.dll",
		"C:\WINDOWS\SysWOW64\\vmmreg32.dll",
		"C:\WINDOWS\SysWOW64\\vmx_fb.dll",
		"C:\WINDOWS\SysWOW64\\vmx_mode.dll",
                "C:\WINDOWS\SysWOW64\\vmhgfs.dll",
		"C:\WINDOWS\SysWOW64\VMUpgradeAtShutdownWXP.dll",
		"C:\Windows\SysWOW64\drivers\\vmhgfs.sys",
                "C:\Windows\SysWOW64\drivers\\VMMEMCTL.sys",
                "C:\Windows\SysWOW64\drivers\\vmrawdsk.sys",
                "C:\Windows\SysWOW64\drivers\VMTools.sys",
                "C:\Windows\SysWOW64\drivers\\vmusbmouse.sys",
                "C:\Windows\SysWOW64\drivers\\vmvss.sys",
                "C:\Windows\SysWOW64\drivers\\vmscsi.sys",
                "C:\Windows\SysWOW64\drivers\VMware Physical Disk Helper Service.sys",
                "C:\Windows\SysWOW64\drivers\\vmxnet.sys",
                "C:\Windows\SysWOW64\drivers\\vmx_svga.sys",
                "C:\Windows\SysWOW64\drivers\\vmbus.sys",		
                "C:\Windows\SysWOW64\drivers\\VMBusHID.sys",
                "C:\Windows\SysWOW64\drivers\\vmci.sys" 
	]

        for i in range( len( files ) ):
                
                try:
                       os.remove( files[i] )
                        
                except Exception, err:
                        pass

        for i in range( len( files2 ) ):
                
                try:
                       os.remove( files2[i] )
                        
                except Exception, err:
                        pass

        if xp == False:
                uninstallVmTools()

def rename_files ( fileName, files ):

        try:
                fileName = files.split("\\")
                if "dll" in fileName[len(fileName) - 1]:
                        newFile = randomword( 15 ) + ".dll"
                        files = files.replace(fileName[len(fileName) - 1], newFile)
                else:
                        newFile = randomword( 15 ) + ".sys"
                        files = files.replace(fileName[len(fileName) - 1], newFile)
                
                newFileName = ""
                for j in range(len(fileName)):
                        if j == 0:
                                newFileName = fileName[j]
                        else:
                                newFileName += "\\" + fileName[j]
                                                
                os.rename( newFileName, files )
        except:
                pass
        
def uninstallVmTools ():

        try:
                uninstall_vmtools_command = "wmic product where name='VMware Tools' call uninstall"
                subprocess.call(uninstall_vmtools_command, shell=True)
        except:
                pass

def addValuesToConf ( path ):
	
	try:
		with open(path, "a") as myfile:
                        for i in range ( len (conf_arr) ):
                                myfile.write("\n" + conf_arr[i])
                                
	except Exception, err:
		print err
	

def start ():

        valueList()
        keyList()
        servicesList()
	finish()

def finish ():

        print "Completed..."
        
def disableWow64 ():

        try:
                k32 = ctypes.windll.kernel32
                wow64 = ctypes.c_long( 0 )
                k32.Wow64DisableWow64FsRedirection( ctypes.byref(wow64) )
                start()
                k32.Wow64EnableWow64FsRedirection( wow64 )
        except:
                pass
        
def main ():

        usage = "Usage: use --help for further information"
	description = "Bypass AntiVM Technics"
        parser = argparse.ArgumentParser(description = description, usage = usage)
	parser.add_argument('-c', '--config', dest = 'config', action = 'store', help = 'It should be called in your host. Your vm must be off. Config file is your .vmx file. Example: python eagle.py -c C:\Users\user\vm\myvm.vmx')
	parser.add_argument('-v', '--value', dest = 'valueList', action = 'store_true', help = 'Modify Registry Values, It should be called after the vm is restarted. Except XP!', default = False)
	parser.add_argument('-u', '--uninstallvmtools', dest = 'vmtools', action = 'store_true', help = 'Uninstall VmTools. It should be called firstly for XP!', default = False)
	parser.add_argument('-x', '--XP', dest = 'xp', action = 'store_true', help = 'Run except uninstallvmtools. It should be called after uninstallVmtools for XP!', default = False)
	args = parser.parse_args()

        if args.valueList:
                valueList()

        if args.vmtools:
                uninstallVmTools()
                
        if args.xp:
                xp = True
                start()

        if args.config != None:
                addValuesToConf ( args.config )

        elif "64" in platform.uname()[4]:
                disableWow64()
                
        else:
                start()
                
                
if __name__ == "__main__":
        
        main()
