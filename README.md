
#Bypass AntiVm Techniques (Working...)

###How To Use It?
1- This command should run in your vm.
  - python eagle.py
2- Your vm will be restarted automatically. After restarting your vm, you should close your vm and this command should run in your host machine.
  - python eagle.py -c "Your Vm's .vmx file path"
3- This command should run in your vm.
  - python eagle.py -v

###Requirements
import wmi
  - https://pypi.python.org/pypi/WMI/
import pywin32
  - https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/

###Bypass Anti VirtualMachine Techniques (Working on)

When cuckoo_detection.exe what is in https://github.com/AlicanAkyol/sems is run in Vmware, result is shown below(Win7 - 64 bit):
![alt tag](https://github.com/AlicanAkyol/sems/blob/master/vmware_normal.png)

If eagle what will be uploaded here is run in Vmware, cuckoo_detection's result is show below(Win7 - 64 bit):
![alt tag](https://github.com/AlicanAkyol/eagle/blob/master/VmwareEagle.png)

###Bypass Anti VirtualBox Techniques (In progress)

###Bypass Anti Cuckoo Sandbox Techniques (In progress)
