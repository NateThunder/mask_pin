# 🔒 Masked PIN Entry (Windows Console)

This Python script provides a secure-feeling, visually masked PIN entry system in the Windows command-line interface. As the user types, digits are replaced by asterisks (`*`) and input is handled without displaying the actual characters. It supports backspace and ignores non-numeric and special keys for a cleaner experience.

---

## 📦 Features

- Input masking using asterisks
- Supports backspace for correction
- Skips special/arrow keys and ignores non-numeric input
- Clears the screen between keystrokes for visual privacy
- Uses `msvcrt` for low-level, non-echoed key reading

---

## 🧑‍💻 Requirements

- **Windows OS**  
- **Python 3.x**

> Uses the `msvcrt` module, which is only available on Windows systems.

---

## 🚀 Usage

### Run the script:

```bash
python pin_mask.py
```

You’ll be prompted to enter a PIN like this:

```
Pin: *
Pin: **
Pin: ***
Pin: ****
```

If you press backspace, it will remove the last entered digit. Press Enter to submit once you're done.

---

## 🧠 How It Works

- `msvcrt.getch()` reads single keypresses without showing them.
- Only numeric characters are accepted (`0-9`).
- Backspace (`\x08`) lets users correct input.
- Arrow keys and other special keys are ignored.
- `os.system("cls")` clears the console after each input to refresh the prompt.

---

## 🛠️ Customization

To change the length of the required PIN or prompt message, modify the `mask_pin()` function call:

```python
mask_pin(6, "Enter 6-digit code: ")  # For 6 digits
```

You can also change the message to match your use case.

---

## 📁 File Structure

```
pin_mask.py     # Contains the mask_pin function and logic
README.md       # You're reading it!
```

---

## 🔐 Security Note

⚠️ This script is intended for **educational and CLI-demo purposes only**.

- The masking is only visual — data is not encrypted or securely stored.
- Clearing the screen with `os.system("cls")` can be disruptive and inconsistent on some terminals.

---

## 📜 License

MIT License
```

---

Let me know if you’d like a ZIP file version with this `README.md` and your Python script inside, or if you want sections added like contributing guidelines or credits.