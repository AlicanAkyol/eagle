
#Bypass AntiVm Techniques (Working...)

###How To Use It?

  - When your vm is closed, run below command in your host machine. <br />-> python eagle.py -c "Your Vm's .vmx file path"
  - Start your vm and run below command in your vm. <br />-> python eagle.py
  - After restart your vm, run below command in your vm. <br />-> python eagle.py -v
  - 
**IMPORTANT:** windows 7

###Requirements
  - import wmi <br />-> https://pypi.python.org/pypi/WMI/
  - import pywin32 <br />-> https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/

###Bypass Anti VirtualMachine Techniques (Working on)

When cuckoo_detection.exe what is in https://github.com/AlicanAkyol/sems is run in Vmware, result is shown below(Win7 - 64 bit):<br />
![alt tag](https://github.com/AlicanAkyol/sems/blob/master/vmware_normal.png)

When eagle is run in Vmware, result is show below(Win7 - 64 bit):<br />
![alt tag](https://github.com/AlicanAkyol/eagle/blob/master/VmwareEagle.png)

###Bypass Anti VirtualBox Techniques (In progress)

###Bypass Anti Cuckoo Sandbox Techniques (In progress)
