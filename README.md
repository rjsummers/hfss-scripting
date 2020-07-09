This repository (will) contain useful scripts to use with Ansys HFSS. The
primary goal right now is to write scripts that will automatically send
(email or SMS) notifications to oneself when HFSS has finished running
analysis on a model.

analyze_design.py will open up the specified project, analyze the specified
design, and export the results in an s2p file. It can be executed in windows
powershell as below:a
```powershell
& "C:\Program Files\AnsysEM\AnsysEM19.4\Win64\ansysedt.exe" -RunScriptAndExit analyze_design.py
```

The python script `run_hfss.py` will run the above powershell command,
then send a notification via. email after HFSS has exited.
