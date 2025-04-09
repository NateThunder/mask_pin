# 🔒 Masked PIN Entry (Windows Console)

This Python script allows users to enter a 4-digit PIN with masked input (using asterisks `*`) in a Windows command-line interface. It captures each keystroke without displaying the actual digit entered, providing basic input privacy.

---

## 📦 Features

- Accepts a fixed-length PIN (e.g., 4 digits)
- Displays asterisks `*` as you type
- Hides actual key input using `msvcrt`
- Clears the screen between inputs for extra privacy

---

## 🧑‍💻 Requirements

- Windows OS  
- Python 3.x

> The script uses the `msvcrt` module, which is **Windows-only**.

---

## 🚀 Usage

### Run the script:

```bash
python pin_mask.py
```

### Example Output:
```
Enter your 4-digit pin: *
Enter your 4-digit pin: **
Enter your 4-digit pin: ***
Enter your 4-digit pin: ****
1234
```


## 🧠 How It Works

- Uses `msvcrt.getch()` to read one character at a time from the console without echoing.
- `os.system("cls")` clears the screen after each character.
- Collected digits are joined and converted to an integer at the end.

---

## 🔐 Security Note

This is a **basic demo** of PIN masking for educational or simple CLI use. It’s not secure for production authentication systems:
- Input is only masked visually, not encrypted.
- `os.system("cls")` may cause screen flickering.

---

## 🛠️ Customization

To change the PIN length:
```python
mask_pin(6)  # for a 6-digit PIN
```


---

## 📁 File Structure

```
pin_mask.py     # Contains the mask_pin function
README.md       # You're reading it!
```

---

## 📜 License

MIT License
