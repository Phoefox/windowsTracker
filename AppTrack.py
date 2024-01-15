import pygetwindow as gw
import datetime
import time
import pandas as pd
from pathlib import Path

SIGNAL = None

def track():    
    while SIGNAL != 'Exit':
        if SIGNAL == 'Halt':
            print('Halt!')
        if wait_for_signal():
            break
        print('Running >>')
        filename = str(datetime.datetime.now()).replace(' ', '_').replace(':', '-')
        pth = Path('D:/Marek/New_programming/Study/AppTrack/records/'+ filename + '.csv')
        save_df().to_csv(pth, index=False)
      

def save_df():
    global SIGNAL
    df = pd.DataFrame()
    for i in range(60):
        df = pd.concat([df, record_activity()], ignore_index=True)
        if SIGNAL in ('Halt', 'Exit'):
            return df
    return df


def record_activity():
    global SIGNAL
    data = []
    for i in range(60):
        data.append({'time': datetime.datetime.now(), 'window': gw.getActiveWindowTitle()})
        time.sleep(1)
        if SIGNAL in ('Halt', 'Exit'):
            return pd.DataFrame(data)
    return pd.DataFrame(data)
    


def wait_for_signal():
    global SIGNAL
    while SIGNAL == 'Halt':
        time.sleep(0.5)
    if SIGNAL == 'Exit':
        return True



if __name__ =='__main__':
    track()

