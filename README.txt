WindowsTracker recognizes which window is selected and saves this information into a .csv file. This information can be later analyzed to better understand your behaviour on PC. You can see how much time you dedicate to different tasks so you can adjust your schedule to be more effective.
This script is OS_Windows specific!


The "AppTrack.py" is the main script that can run on its own. It will record the selected window once per second and save this information once per hour into .csv file. 
"executor.py" is used to control the "AppTrack.py" while it is running - halt, run, or exit the program. It displays at the taskbar (downright corner of your screen) as a small "T" icon.
