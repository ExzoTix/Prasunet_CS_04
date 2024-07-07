from pynput import keyboard

# log file name [location: in the same folder]
log_file = 'keylog.txt'

def on_press(key):
    try:
        with open(log_file, 'a') as f:
            f.write(f'{key.char}')
    except AttributeError:
        if key == keyboard.Key.space:
            with open(log_file, 'a') as f:
                f.write(' ')
        else:
            with open(log_file, 'a') as f:
                f.write(f'[{key}]')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def main():
    # User Consent is essential
    print("""This program will record and log your keystrokes.
Do you agree to proceed?
""")
    consent = input("If Yes press Y, If No press N")
    
    if consent == 'Y':
        print("Keylogging started. Press ESC to stop.")
        # Keylogging
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
        print("""Keylogging stopped.
Keystrokes are saved as keylog.txt in the same folder where this Program file is saved.
""")
    else:
        print("Keylogging cancelled. No keystrokes will be logged.")

if __name__ == "__main__":
    main()
