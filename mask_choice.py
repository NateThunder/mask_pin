import os
import msvcrt

def mask_pin(message="Pin: ", length=None, confirm=False):
    def clear_console():
        os.system("cls" if os.name == "nt" else "clear")

    digits = []

    while True:
        clear_console()
        print(f"{message}{'*' * len(digits)}", flush=True, end="")

        key = msvcrt.getch()

        if key in (b'\x00', b'\xe0'):
            msvcrt.getch()
            continue

        try:
            char = key.decode()
        except UnicodeDecodeError:
            continue

        if char == "\r":  # Enter key
            if length is None or len(digits) == length:
                break
            else:
                continue  # Don't allow Enter if length not yet met
        elif char == "\x08":  # Backspace
            if digits:
                digits.pop()
        elif char.isdigit():
            if length is None or len(digits) < length and confirm == True:
                digits.append(char)
                if len(digits) == length:
                    break
            elif length is None or len(digits) < length and confirm == False:
                digits.append(char)
                

    clear_console()
    print(f"{message}{'*' * len(digits)}", flush=True)

    return int("".join(digits)) if digits else None

# EXAMPLES:

# Fixed length PIN:
# pin_result = mask_pin(4, 'Pin: ')

# Infinite length PIN until Enter:
pin_result = mask_pin('Pin: ',4, True)

if pin_result is not None:
    print(f"Your PIN is: {pin_result}")
else:
    print("No PIN entered.")
