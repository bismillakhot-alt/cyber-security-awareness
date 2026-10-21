# 🛡️ CyberShield – Cybersecurity Awareness Website

A simple, beginner-friendly **Cybersecurity Awareness Website** built with **Python** and **Streamlit**.  
Everything runs from a single `app.py` file — no database, no extra files, no complex setup.

---

## 📸 Features

| Section | Description |
|---|---|
| 📖 Introduction | Beginner-friendly explanation of what cybersecurity is |
| ⚠️ Common Threats | Phishing, Malware, Hacking, Online Fraud, Weak Passwords, Public Wi-Fi risks |
| ✅ Safety Tips | 8 practical tips to stay safe online |
| 🔐 Password Checker | Live strength meter with score, colour bar, and improvement suggestions |
| 🧠 Quiz | 5 multiple-choice questions with instant score and per-question review |

---

## 🛠️ Tech Stack

- **Language:** Python 3.7+
- **Framework:** [Streamlit](https://streamlit.io/)
- **Libraries used:** `streamlit`, `re` (built-in)

---

## 🚀 Getting Started

### 1. Clone or Download the project

```bash
git clone https://github.com/your-username/cybershield.git
cd cybershield
```

Or simply download `app.py` and place it in a folder.

### 2. Install Streamlit

```bash
pip install streamlit
```

> **Note:** Python 3.7 or higher is required. You can check your version with `python --version`.

### 3. Run the App

```bash
streamlit run app.py
```

### 4. Open in Browser

Streamlit will automatically open your default browser at:

```
http://localhost:8501
```

---

## 📁 Project Structure

```
cybershield/
├── app.py              ← The entire website (single file)
├── README.md           ← This file
└── Project_Report.md   ← Detailed project report
```

---

## 🔐 Password Strength Checker

The checker evaluates passwords against **6 criteria**:

| Criteria | Points |
|---|---|
| At least 8 characters | +1 |
| At least 12 characters | +1 |
| Contains an uppercase letter (A–Z) | +1 |
| Contains a lowercase letter (a–z) | +1 |
| Contains a number (0–9) | +1 |
| Contains a special character (!@#$…) | +1 |

- **0–2 points** → 🔴 Weak  
- **3–4 points** → 🟡 Medium  
- **5–6 points** → 🟢 Strong  

> No passwords are stored or sent anywhere. Everything runs locally in your browser.

---

## 🧠 Quiz Questions

1. What does "phishing" mean in cybersecurity?
2. Which of the following is the strongest password?
3. What does "2FA" stand for?
4. What should you look for in a URL to know it is secure?
5. Which action helps protect your device from malware?

---

## 🎨 Design

- Dark theme (`#0d1117` background — similar to GitHub dark mode)
- Blue accent headings (`#58a6ff`)
- Green tip cards, blue threat cards
- Clean, readable layout with a centered single-column design

---

## 📋 Requirements

Create a `requirements.txt` file with the following content if you want to share the project:

```
streamlit>=1.28.0
```

Install it with:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add more quiz questions
- Add new cyber threat categories
- Improve the UI/styling
- Add a dark/light mode toggle

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

Built with ❤️ using Python & Streamlit.  
🛡️ *Stay safe. Stay informed.*
