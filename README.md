# 🔒 Masked PIN Entry (Windows Console)

This project provides secure-feeling, visually masked PIN entry tools for the Windows command line using Python. As users type their PIN, digits are replaced with asterisks (`*`) to prevent shoulder-surfing. The system handles input in real-time without echoing typed characters.

---

## 📦 Features

- 🔢 Accepts digit-only input (`0-9`)
- ✨ Masking with asterisks (`*`) during typing
- ⬅️ Supports backspace for correction
- ⌨️ Ignores arrow keys and other non-numeric input
- 🧼 Clears screen between keystrokes for better visual privacy
- ⚙️ Multiple modes: fixed-length, infinite-length, and confirmation

---

## 🧑‍💻 Requirements

- **Windows OS**
- **Python 3.x**

> Uses the `msvcrt` module, which is **only available on Windows**.

---

## 🚀 Usage

Each file offers a different variation of the masked input function:

### `mask_pin.py`  
**Use Case:** Fixed-length PIN  
```python
mask_pin(length=4, message="Enter PIN: ")
```

### `mask_pin_infinate.py`  
**Use Case:** Infinite-length PIN until Enter is pressed  
```python
mask_pin(message="Enter PIN: ")
```

### `mask_choice.py`  
**Use Case:** Optional confirmation and flexible-length support  
```python
mask_pin(message="Enter PIN: ", length=4, confirm=True)
```

---

## 🧠 How It Works

- `msvcrt.getch()` reads individual keypresses without echoing them.
- Non-numeric and special keys are ignored.
- Backspace (`\x08`) removes the last digit.
- `os.system("cls")` clears the screen after each keystroke.
- Input is visually masked with asterisks (`*`), but the actual digits are stored in memory.

---

## 📁 File Overview

```
mask_pin.py           # Basic fixed-length masked PIN entry
mask_pin_infinate.py  # Infinite-length masked PIN entry
mask_choice.py        # Flexible version with optional confirmation
README.md             # Documentation (this file)
```

---

## 🔐 Security Note

⚠️ These scripts are for **educational/demo purposes** only.

- Input is only masked visually; no encryption is involved.
- Console clearing may behave differently across terminal emulators.
