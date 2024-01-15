This script is OS_Windows specific!

WindowsTracker recognizes which window is selected and saves this information into a .csv file. This information can be later analyzed to better understand your behaviour on PC. You can see how much time you dedicate to different tasks so you can adjust your schedule to be more effective.

Example record:

time,window
2024-01-08 21:01:52.773523,Translate Google - Google Chrome
2024-01-08 21:01:53.774018,Translate Google - Google Chrome
2024-01-08 21:01:54.775450,Translate Google - Google Chrome
2024-01-08 21:01:55.776658,Wikipedia - Google Chrome
2024-01-08 21:01:56.777660,Multiprocessing - Wikipedia - Google Chrome
2024-01-08 21:01:57.778662,Multiprocessing - Wikipedia - Google Chrome
...

The "AppTrack.py" is the main script that can run on its own. It will record the selected window once per second and save this information once per hour into .csv file. 

"executor.py" is used to control the "AppTrack.py" while it is running - halt, run, or exit the program. It displays at the taskbar (downright corner of your screen) as a small "T" icon.
