from pynput import keyboard
import time
import threading

running = True

global data2send
data2send = ""

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        while running:
            self.send_data()
            time.sleep(2)
    def send_data(self):
        print("sended: " + data2send)
        #Send data to server hier


thread1 = myThread(1, "Thread-1", 1)
thread1.setDaemon(True)
thread1.start()                 #Start Networt Sending Thread


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        data2send = "hallo"
        print(data2send)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
