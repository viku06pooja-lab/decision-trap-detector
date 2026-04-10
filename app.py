import streamlit as st
import time

# Page setup
st.set_page_config(page_title="Decision Trap Detector", layout="centered")

# Title
st.title("⚠️ Decision Trap Detector")
st.markdown("### 🧠 Smart Behavior Analysis System")
st.divider()

st.info("🔍 Use Case: Messaging, Emails, Financial Decisions")
st.caption("🌍 Based on common behavioral patterns in human decision-making")

st.write("This system detects impulsive decisions and provides structured guidance.")

# Input
user_input = st.text_area("Type your message:")

# Button
analyze = st.button("Analyze Decision")

# Session state
if "cooldown" not in st.session_state:
    st.session_state.cooldown = False

# Keywords
emotional_words = ["tensed", "angry", "frustrated", "sad", "panic", "stress"]
major_decisions = ["career", "job", "marriage", "politics", "investment", "business"]
study_keywords = ["study", "exam", "read", "prepare", "assignment"]
life_keywords = ["love", "relationship", "trust", "friend", "breakup", "commit"]

# MAIN LOGIC
if analyze:

    if user_input.strip() == "":
        st.warning("Please type something first!")

    else:
        risk = 0
        is_emotional = False
        is_major = False
        is_study = False
        is_life = False

        text = user_input.lower()

        # Emotion detection
        for word in emotional_words:
            if word in text:
                risk += 30
                is_emotional = True
                break

        # Major decision
        for word in major_decisions:
            if word in text:
                is_major = True
                break

        # Study
        for word in study_keywords:
            if word in text:
                is_study = True
                break

        # Life decisions
        for word in life_keywords:
            if word in text:
                is_life = True
                break

        # Other logic
        if len(user_input) > 50:
            risk += 20
        if user_input.isupper():
            risk += 30
        if "!!!" in user_input:
            risk += 30
        if len(user_input.split()) < 3:
            risk += 20

        # Output
        st.subheader("📊 Decision Risk Analysis")
        st.progress(min(risk, 100) / 100)

        # Result
        if risk < 30:
            st.success("✅ Low Risk – Calm decision")

        elif risk < 60:
            st.warning("⚠️ Medium Risk – Think again")

            if is_emotional:
                st.write("💬 You may be under stress. Talk to someone you trust before deciding.")
            else:
                st.write("💬 Take a moment to think before acting.")

        else:
            st.error("🚨 High Risk – Impulsive decision detected!")
            st.write("👉 Suggestion: Wait before acting.")

        # Confidence
        st.write(f"🧠 Decision Confidence Score: {100 - risk}%")

        # Emotion tag
        st.write(f"🧠 Detected State: {'Emotional / Stressed' if is_emotional else 'Normal'}")

        # Explanation
        st.subheader("🧠 Why this decision is risky:")

        reasons = []
        if is_emotional:
            reasons.append("Emotional stress detected")
        if user_input.isupper():
            reasons.append("ALL CAPS indicates emotional intensity")
        if "!!!" in user_input:
            reasons.append("Urgency detected from punctuation")
        if len(user_input.split()) < 3:
            reasons.append("Very short message suggests impulsiveness")
        if len(user_input) > 50:
            reasons.append("Long message may indicate rushed thinking")

        for r in reasons:
            st.write("•", r) if reasons else st.write("• Calm behavior detected")

        # Final insight
        st.subheader("🧾 Final Insight")

        if risk < 30:
            st.write("This appears to be a well-thought-out decision.")
        elif risk < 60:
            st.write("This decision may need reconsideration.")
        else:
            st.write("This is likely an impulsive decision. Pause before acting.")

        # Major decision layer
        if is_major:
            st.warning("⚠️ This is a major life decision. Plan carefully and consult others.")

        # Study layer
        if is_study:
            st.subheader("📚 Study Recommendation")
            if risk >= 60:
                st.write("Take a short break, then study with focus.")
            else:
                st.write("Good time to study. Try 25-minute focus sessions.")
            st.write("💡 Tip: Pomodoro technique (25 min study + 5 min break).")

        # Life decision layer
        if is_life:
            st.subheader("❤️ Personal Decision Guidance")
            if risk >= 60:
                st.write("You may be emotional. Take time before deciding.")
            else:
                st.write("Consider trust, values, and long-term impact.")
            st.write("💡 Talk to someone you trust before deciding.")

        # 🌍 Universal decision guidance
        if any(q in text for q in ["should i", "do i", "is it good to"]):
            st.subheader("🌍 Decision Guidance")

            st.write("🧠 Summary:")
            st.write("This is a decision requiring balanced thinking.")

            st.write("📌 Consider:")
            st.write("• Long-term impact")
            st.write("• Emotional vs logical thinking")
            st.write("• Risks vs benefits")
            st.write("• Personal values")

            if risk >= 60:
                st.write("⚠️ You may be deciding emotionally. Pause.")
            else:
                st.write("Take time to evaluate outcomes.")

            st.write("🤝 Talk to a trusted person before deciding.")

        # Cooldown trigger
        if risk >= 60:
            st.session_state.cooldown = True

# Cooldown
if st.session_state.cooldown:
    st.subheader("⏳ Cooldown Recommendation")

    if st.button("Start Cooldown Timer"):
        countdown = st.empty()
        for i in range(5, 0, -1):
            countdown.write(f"⏳ Waiting... {i}")
            time.sleep(1)

        countdown.write("✅ Now reconsider calmly.")
        st.session_state.cooldown = False