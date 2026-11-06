
import streamlit as st
import random

st.set_page_config(
    page_title="CyberSafe | Cybersecurity Awareness",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #f4f7fb;
}
.stButton>button {
    background-color: #1565C0;
    color: white;
    border-radius: 8px;
}
h1, h2, h3 {
    color: #123456;
}
</style>
""", unsafe_allow_html=True)

st.title("🛡️ CyberSafe")
st.subheader("Cybersecurity Awareness & Online Safety")
st.write(
    "Learn about cyberattacks, understand online threats, "
    "and discover how to protect yourself in the digital world."
)

menu = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Types of Cyber Attacks",
        "How to Stay Safe",
        "Security Best Practices",
        "Cybersecurity Quiz",
        "About"
    ]
)

if menu == "Home":
    st.header("Welcome to CyberSafe")

    st.write("""
    Cybersecurity is the practice of protecting computers,
    mobile devices, networks, and personal information
    from unauthorized access and digital attacks.

    Cyber threats can affect individuals, businesses,
    educational institutions, and governments.
    """)

    col1, col2, col3 = st.columns(3)

    col1.metric("Main Goal", "Protection")
    col2.metric("Key Focus", "Awareness")
    col3.metric("Priority", "Online Safety")

    st.info(
        "Remember: Awareness is your first line of defense "
        "against cyberattacks."
    )

    st.subheader("What will you learn?")
    st.markdown("""
    - Understand common cyberattacks.
    - Recognize suspicious emails and websites.
    - Create strong passwords.
    - Protect personal information.
    - Browse the internet safely.
    """)

elif menu == "Types of Cyber Attacks":
    st.header("Common Types of Cyber Attacks")

    attacks = {
        "Phishing": """
        Phishing is a fraudulent attempt to steal sensitive
        information through fake emails, messages, or websites.

        **Example:** An email pretending to come from your bank
        asks you to verify your account through a suspicious link.

        **Prevention:** Verify the sender and avoid suspicious links.
        """,

        "Malware": """
        Malware is malicious software designed to damage,
        disrupt, or gain unauthorized access to devices.

        **Examples:** Viruses, worms, trojans, and spyware.

        **Prevention:** Use trusted software and keep security
        updates enabled.
        """,

        "Ransomware": """
        Ransomware is malicious software that locks or encrypts
        files and demands payment for their recovery.

        **Prevention:** Maintain offline backups and update
        your operating system.
        """,

        "Password Attacks": """
        Attackers may attempt to obtain passwords through
        stolen credentials, guessing, or automated attempts.

        **Prevention:** Use unique passwords and enable
        multi-factor authentication.
        """,

        "Denial of Service (DoS)": """
        A denial-of-service attack attempts to make a website
        or online service unavailable by overwhelming it
        with traffic or requests.

        **Prevention:** Organizations can use traffic filtering,
        monitoring, and appropriate protection services.
        """,

        "Social Engineering": """
        Social engineering manipulates people into revealing
        confidential information or performing unsafe actions.

        **Prevention:** Verify unusual requests before sharing
        information or transferring money.
        """
    }

    for name, description in attacks.items():
        with st.expander(name):
            st.write(description)

elif menu == "How to Stay Safe":
    st.header("How to Protect Yourself Online")

    safety_tips = [
        "Use strong and unique passwords.",
        "Enable multi-factor authentication.",
        "Never click unknown or suspicious links.",
        "Avoid downloading files from untrusted sources.",
        "Keep your operating system and applications updated.",
        "Use trusted antivirus and security tools.",
        "Avoid sharing sensitive personal information.",
        "Use secure Wi-Fi networks.",
        "Back up important data regularly.",
        "Check website addresses before entering information."
    ]

    for i, tip in enumerate(safety_tips, 1):
        st.success(f"{i}. {tip}")

elif menu == "Security Best Practices":
    st.header("Essential Cybersecurity Practices")

    st.subheader("Password Security")
    st.write("""
    - Create long, unique passwords.
    - Use a reputable password manager.
    - Never reuse important passwords.
    - Enable multi-factor authentication.
    """)

    st.subheader("Email Security")
    st.write("""
    - Check the sender's email address.
    - Be careful with unexpected attachments.
    - Avoid clicking suspicious links.
    - Report suspicious emails.
    """)

    st.subheader("Device Security")
    st.write("""
    - Install software updates.
    - Use device screen locks.
    - Enable firewall protection.
    - Install applications from trusted sources.
    """)

    st.subheader("Data Protection")
    st.write("""
    - Back up important files.
    - Encrypt sensitive information.
    - Limit access to personal data.
    - Avoid using public computers for sensitive accounts.
    """)

elif menu == "Cybersecurity Quiz":
    st.header("🧠 Test Your Cybersecurity Knowledge")

    questions = [
        {
            "question": "What is phishing?",
            "options": [
                "A type of computer hardware",
                "A fraudulent attempt to steal information",
                "A programming language",
                "A backup method"
            ],
            "answer": "A fraudulent attempt to steal information"
        },
        {
            "question": "Which password practice is safest?",
            "options": [
                "Using your birth date",
                "Using the same password everywhere",
                "Using unique and strong passwords",
                "Sharing passwords with friends"
            ],
            "answer": "Using unique and strong passwords"
        },
        {
            "question": "What does MFA stand for?",
            "options": [
                "Multi-Factor Authentication",
                "Main Firewall Access",
                "Multiple File Application",
                "Managed File Account"
            ],
            "answer": "Multi-Factor Authentication"
        },
        {
            "question": "What is ransomware?",
            "options": [
                "A backup application",
                "Software that demands payment after restricting access to data",
                "A secure browser",
                "An operating system"
            ],
            "answer": "Software that demands payment after restricting access to data"
        },
        {
            "question": "What should you do with a suspicious email?",
            "options": [
                "Open every attachment",
                "Click every link",
                "Verify the sender and report it",
                "Forward it to everyone"
            ],
            "answer": "Verify the sender and report it"
        }
    ]

    if "quiz_submitted" not in st.session_state:
        st.session_state.quiz_submitted = False

    with st.form("cyber_quiz"):
        answers = []

        for i, q in enumerate(questions):
            st.write(f"**Q{i+1}. {q['question']}**")
            answer = st.radio(
                "Choose your answer:",
                q["options"],
                key=f"question_{i}"
            )
            answers.append(answer)

        submitted = st.form_submit_button("Submit Quiz")

    if submitted:
        score = sum(
            answers[i] == questions[i]["answer"]
            for i in range(len(questions))
        )

        st.subheader(f"Your Score: {score}/{len(questions)}")

        if score == len(questions):
            st.success("Excellent! You have strong cybersecurity awareness.")
        elif score >= 3:
            st.info("Good work! Keep learning about cybersecurity.")
        else:
            st.warning("Keep studying and try again!")

        for i, q in enumerate(questions):
            if answers[i] == q["answer"]:
                st.success(f"Q{i+1}: Correct")
            else:
                st.error(
                    f"Q{i+1}: Incorrect. Correct answer: {q['answer']}"
                )

elif menu == "About":
    st.header("About CyberSafe")

    st.write("""
    CyberSafe is an educational cybersecurity awareness
    application developed to help beginners understand
    common digital threats and learn how to protect
    their personal information.

    **Application Objectives:**

    - Increase cybersecurity awareness.
    - Educate users about common cyber threats.
    - Promote responsible internet usage.
    - Encourage safe digital habits.

    **Technology:** Python and Streamlit

    **Purpose:** Educational and awareness only.
    """)

st.sidebar.divider()
st.sidebar.caption("CyberSafe | Stay Aware. Stay Secure. 🛡️")
