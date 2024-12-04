
# 🔐 Password Strength & Leak Checker 🚀

This Python script helps you **analyze password security** by checking its strength and detecting if it exists in leaked databases like **RockYou**. Perfect for cybersecurity enthusiasts and password analysis! 🛡️

---

## 🌟 Features
- ✅ Detects passwords in leaked databases (e.g., **RockYou**).
- ✅ Evaluates password strength based on:
  - **Length**
  - **Complexity** (Uppercase, Lowercase, Numbers, Special Characters)
  - **Avoidance of common patterns**.
- ✅ Supports multiple system configurations (BlackArch, Kali, etc.).
- ✅ Provides detailed feedback on password security.

---

## ⚡ How It Works
1. 📂 Detects and loads **RockYou wordlists** from your system.
2. 🔍 Compares your password against leaked databases.
3. 📊 Scores your password's strength:
   - **Strong** 🟢 (Score ≥ 8)
   - **Moderate** 🟡 (Score 5-7)
   - **Weak** 🔴 (Score < 5)

---

## 🚀 Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/Akilash-A/password_security_check.git
   ```
2. Navigate to the directory:
   ```bash
   cd password_security_check
   ```
3. Run the script:
   ```bash
   python password_security_check.py
   ```
4. Enter your password when prompted.

---

## 📸 Preview
```text
Enter your password: ********
Password strength: Strong Password 💪
```
or
```text
Password is from a leaked database: /usr/share/wordlists/rockyou.txt 🚨
```

---

## 🛠️ Requirements
- Python 3.x
- Access to RockYou or similar password wordlists (optional but recommended).

---

## 🌍 Contribute
Feel free to **fork**, **create issues**, or **submit pull requests** to improve this tool! 🙌

---

## 📜 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

### 🧑‍💻 Created by [Akilash A](https://github.com/Akilash-A) 💡
