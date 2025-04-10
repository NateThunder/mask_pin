import os
import msvcrt

def mask_pin(length, message):
    def clear_console():
        os.system("cls" if os.name == "nt" else "clear")

    digits = []

    while len(digits) < length:
        clear_console()
        print(f"{message}{'*' * len(digits)}", flush=True, end="")

        key = msvcrt.getch()

        # Check special keys (e.g., arrow keys produce two-byte sequences)
        if key in (b'\x00', b'\xe0'):
            msvcrt.getch()  # Skip the next byte for special keys
            continue

        try:
            char = key.decode()
        except UnicodeDecodeError:
            continue  # Ignore undecodable bytes

        if char == "\r":  # Enter key
            break
        elif char == "\x08":  # Backspace key (ASCII code for backspace)
            if digits:
                digits.pop()
        elif char.isdigit():  # Only allow digits
            digits.append(char)

    clear_console()
    print(f"{message}{'*' * len(digits)}", flush=True)
    
    if digits:
        pin = int("".join(digits))
        return pin
    else:
        return None

# pin_result = mask_pin(4, 'Pin: ')
# if pin_result is not None:
#     print(f"Your PIN is: {pin_result}")
# else:
#     print("No PIN entered.")