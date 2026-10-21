import streamlit as st
import re

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CyberShield – Cybersecurity Awareness",
    page_icon="🛡️",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Overall background */
    .stApp { background-color: #0d1117; color: #e6edf3; }

    /* Section cards */
    .card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 20px 24px;
        margin-bottom: 20px;
    }

    /* Threat badges */
    .threat-badge {
        display: inline-block;
        background-color: #1f2937;
        border-left: 4px solid #3b82f6;
        border-radius: 6px;
        padding: 10px 16px;
        margin: 8px 0;
        width: 100%;
    }

    /* Tip items */
    .tip-item {
        background-color: #1f2937;
        border-left: 4px solid #22c55e;
        border-radius: 6px;
        padding: 10px 16px;
        margin: 8px 0;
    }

    /* Strength bars */
    .strength-weak   { color: #ef4444; font-weight: bold; }
    .strength-medium { color: #f59e0b; font-weight: bold; }
    .strength-strong { color: #22c55e; font-weight: bold; }

    h1, h2, h3 { color: #58a6ff; }
    hr { border-color: #30363d; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("## 🛡️ CyberShield")
st.markdown("### Cybersecurity Awareness")
st.markdown("---")

# ══════════════════════════════════════════════════════════════════════════════
# 1 ▸ INTRODUCTION
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("## 📖 What is Cybersecurity?")
st.markdown("""
<div class="card">
<b>Cybersecurity</b> is the practice of protecting computers, networks, programs, and data
from digital attacks, unauthorized access, damage, or theft.<br><br>
In today's connected world, almost everything is online — banking, shopping, communication,
and even health records. This makes it essential for everyone — not just IT professionals —
to understand basic cyber hygiene and stay safe online.
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# 2 ▸ COMMON CYBER THREATS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("## ⚠️ Common Cyber Threats")

threats = [
    ("🎣 Phishing",
     "Fake emails or websites trick you into revealing passwords, credit card numbers, "
     "or other sensitive information. Always verify the sender before clicking any link."),
    ("🦠 Malware",
     "Malicious software (viruses, ransomware, spyware) that infects your device to steal "
     "data or cause damage. Avoid downloading files from unknown sources."),
    ("💻 Hacking",
     "Unauthorized access to systems or networks to steal data, disrupt services, or plant "
     "backdoors. Keep software up to date to patch security vulnerabilities."),
    ("💳 Online Fraud",
     "Scammers pose as banks, sellers, or officials to steal money or personal information. "
     "If an offer looks too good to be true, it probably is."),
    ("🔓 Weak Passwords",
     "Short or obvious passwords are cracked in seconds using automated tools. "
     "Use long, unique passwords and a password manager."),
    ("📶 Public Wi-Fi Risks",
     "Unsecured public networks allow attackers to intercept your data. "
     "Use a VPN when connecting to public Wi-Fi."),
]

for title, desc in threats:
    st.markdown(f"""
    <div class="threat-badge">
        <b>{title}</b><br>
        <span style="color:#8b949e;">{desc}</span>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# 3 ▸ SAFETY TIPS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("## ✅ Basic Safety Tips")

tips = [
    "🔑 Use passwords with 12+ characters — mix uppercase, lowercase, numbers, and symbols.",
    "🔄 Never reuse the same password across different websites.",
    "📲 Enable Two-Factor Authentication (2FA) wherever possible.",
    "🔗 Check for 'https://' before entering personal info on any website.",
    "💾 Keep your OS, browser, and apps updated to fix security bugs.",
    "📧 Do not click suspicious links or download unexpected email attachments.",
    "🔒 Lock your devices when not in use and set strong PINs.",
    "📦 Back up important data regularly to an external drive or cloud.",
]

for tip in tips:
    st.markdown(f'<div class="tip-item">{tip}</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# 4 ▸ PASSWORD STRENGTH CHECKER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("---")
st.markdown("## 🔐 Password Strength Checker")
st.markdown("Type a password below to see how strong it is (nothing is stored or sent).")

password = st.text_input("Enter a password to check:", type="password", key="pwd_input")

def check_password_strength(pwd):
    """Return (score 0-5, label, list of missing criteria)."""
    score = 0
    missing = []

    if len(pwd) >= 8:
        score += 1
    else:
        missing.append("At least 8 characters")

    if len(pwd) >= 12:
        score += 1
    else:
        missing.append("At least 12 characters (recommended)")

    if re.search(r"[A-Z]", pwd):
        score += 1
    else:
        missing.append("An uppercase letter (A–Z)")

    if re.search(r"[a-z]", pwd):
        score += 1
    else:
        missing.append("A lowercase letter (a–z)")

    if re.search(r"\d", pwd):
        score += 1
    else:
        missing.append("A number (0–9)")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-]", pwd):
        score += 1
    else:
        missing.append("A special character (!@#$…)")

    if score <= 2:
        label = "Weak"
    elif score <= 4:
        label = "Medium"
    else:
        label = "Strong"

    return score, label, missing

if password:
    score, label, missing = check_password_strength(password)

    # Colour the label
    css_class = {"Weak": "strength-weak", "Medium": "strength-medium", "Strong": "strength-strong"}[label]
    bar_color  = {"Weak": "#ef4444",       "Medium": "#f59e0b",         "Strong": "#22c55e"}[label]
    bar_pct    = int((score / 6) * 100)

    st.markdown(f"""
    <div class="card">
        <b>Strength:</b> <span class="{css_class}">{label}</span>
        &nbsp;({score}/6 criteria met)<br><br>
        <div style="background:#30363d;border-radius:6px;height:12px;width:100%;">
            <div style="background:{bar_color};width:{bar_pct}%;height:12px;border-radius:6px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if missing:
        st.markdown("**To improve your password, add:**")
        for m in missing:
            st.markdown(f"- {m}")
    else:
        st.success("🎉 Excellent! Your password meets all criteria.")

# ══════════════════════════════════════════════════════════════════════════════
# 5 ▸ CYBERSECURITY QUIZ
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("---")
st.markdown("## 🧠 Cybersecurity Quiz")
st.markdown("Test your knowledge! Select an answer for each question and click **Submit Quiz**.")

# Quiz data: (question, [options], correct_index)
QUIZ = [
    (
        "1. What does 'phishing' mean in cybersecurity?",
        ["Catching fish using the internet",
         "A fake attempt to steal sensitive information via email/website",
         "A type of antivirus software",
         "Encrypting your files for safety"],
        1,
    ),
    (
        "2. Which of the following is the STRONGEST password?",
        ["password123", "john1990", "T!9kR#2mLq@7", "mydog"],
        2,
    ),
    (
        "3. What does '2FA' stand for?",
        ["Two-Factor Authentication", "Two File Access",
         "Twice Fast Application", "Two Firewall Access"],
        0,
    ),
    (
        "4. What should you look for in a URL to know it is secure?",
        ["http://", "ftp://", "https://", "www."],
        2,
    ),
    (
        "5. Which action helps protect your device from malware?",
        ["Sharing your password with friends",
         "Keeping your software and OS updated",
         "Using public Wi-Fi without a VPN",
         "Clicking all email links to check them"],
        1,
    ),
]

# Store answers in session state
if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = [None] * len(QUIZ)
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

with st.form("quiz_form"):
    for i, (question, options, _correct) in enumerate(QUIZ):
        st.markdown(f"**{question}**")
        choice = st.radio(
            label=question,
            options=options,
            index=st.session_state.quiz_answers[i] if st.session_state.quiz_answers[i] is not None else 0,
            key=f"q{i}",
            label_visibility="collapsed",
        )
        st.session_state.quiz_answers[i] = options.index(choice)
        st.markdown("")  # small spacer

    submitted = st.form_submit_button("✅ Submit Quiz", use_container_width=True)

if submitted:
    score = sum(
        1 for i, (_q, _opts, correct) in enumerate(QUIZ)
        if st.session_state.quiz_answers[i] == correct
    )
    total = len(QUIZ)
    pct   = int((score / total) * 100)

    if pct == 100:
        emoji, msg = "🏆", "Perfect score! You're a cybersecurity pro!"
    elif pct >= 60:
        emoji, msg = "👍", "Good job! Review the topics you missed."
    else:
        emoji, msg = "📚", "Keep learning — cybersecurity is worth mastering!"

    st.markdown(f"""
    <div class="card" style="text-align:center;">
        <h2>{emoji} You scored {score} / {total} ({pct}%)</h2>
        <p style="color:#8b949e;">{msg}</p>
    </div>
    """, unsafe_allow_html=True)

    # Show correct / incorrect per question
    st.markdown("### Review")
    for i, (question, options, correct) in enumerate(QUIZ):
        user_ans = st.session_state.quiz_answers[i]
        if user_ans == correct:
            st.success(f"✔ Q{i+1}: Correct! — {options[correct]}")
        else:
            st.error(f"✘ Q{i+1}: Your answer: **{options[user_ans]}** | Correct: **{options[correct]}**")

# ══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("---")
st.markdown(
    "<p style='text-align:center;color:#8b949e;font-size:13px;'>"
    "🛡️ CyberShield – Cybersecurity Awareness &nbsp;|&nbsp; "
    "Stay safe. Stay informed.</p>",
    unsafe_allow_html=True,
)
