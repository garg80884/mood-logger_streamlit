import streamlit as st
import pandas as pd
from datetime import datetime
import os
import joblib
import matplotlib.pyplot as plt
import plotly.express as px

# -----------------------------
# Authentication Setup
# -----------------------------
USERS_FILE = "users.csv"
LOG_FILE = "mood_log.csv"

if not os.path.exists(USERS_FILE):
    pd.DataFrame(columns=["username", "password"]).to_csv(USERS_FILE, index=False)

if not os.path.exists(LOG_FILE):
    pd.DataFrame(columns=["timestamp", "username", "text", "mood"]).to_csv(LOG_FILE, index=False)

def load_users():
    return pd.read_csv(USERS_FILE)

def save_user(username, password):
    users = load_users()
    users.loc[len(users)] = [username, password]
    users.to_csv(USERS_FILE, index=False)

def authenticate_user(username, password):
    users = load_users()
    if username in users["username"].values:
        return users[users["username"] == username]["password"].iloc[0] == password
    return False

# -----------------------------
# Mood Tips
# -----------------------------
mood_tips = {
    "joy": "😊 Keep spreading joy! Share your happiness with others.",
    "anger": "😠 Try to breathe deeply and take a moment to calm down.",
    "sadness": "😢 It’s okay to feel sad. Talk to someone or rest a bit.",
    "neutral": "😐 A balanced state. Maybe explore a hobby!",
    "disappointment": "😔 Don’t worry. Learn and grow from the moment.",
    "admiration": "👏 Acknowledge the positive! Celebrate it.",
    "approval": "👍 Keep up the good choices!",
    "realization": "💡 Use your new insight for growth.",
    "remorse": "🙏 Everyone makes mistakes. What can you learn from it?",
    "embarrassment": "😳 It happens! Laugh it off and move forward."
}

# -----------------------------
# Model and Vectorizer
# -----------------------------
model = joblib.load("model/saved_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

def predict_mood(text):
    X_vect = vectorizer.transform([text])
    return model.predict(X_vect)[0]

def save_log(username, text, mood):
    timestamp = datetime.now()
    entry = pd.DataFrame([[timestamp, username, text, mood]], columns=["timestamp", "username", "text", "mood"])
    log_df = pd.read_csv(LOG_FILE)
    log_df = pd.concat([log_df, entry], ignore_index=True)
    log_df.to_csv(LOG_FILE, index=False)

def load_user_logs(username):
    df = pd.read_csv(LOG_FILE, parse_dates=["timestamp"])
    return df[df["username"] == username]

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="🧠 Mood Logger", layout="centered")
st.markdown("<h1 style='text-align:center;color:#4B7BEC;'>🧠 Mood Logger</h1>", unsafe_allow_html=True)
st.markdown("### Track your emotions and get personalized mood tips.")

# -----------------------------
# Auth Interface
# -----------------------------
if "user" not in st.session_state:
    auth_mode = st.sidebar.radio("Login / Signup", ["Login", "Signup"])
    st.markdown(
            "<div style='background:#e8f0fe; padding:10px; border-radius:8px;'>"
            "<strong>Try it now:</strong> <code>Username:</code> demo | <code>Password:</code> demo"
            "</div>",
            unsafe_allow_html=True
        )
    if auth_mode == "Login":
        st.subheader("🔐 Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if authenticate_user(username, password):
                st.session_state.user = username
                st.success(f"Welcome, {username}!")
                st.rerun()
            else:
                st.error("Invalid credentials.")

    elif auth_mode == "Signup":
        st.subheader("📝 Create an Account")
        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")
        if st.button("Sign Up"):
            save_user(new_user, new_pass)
            st.success("Account created. You can now log in.")
else:
    username = st.session_state.user
    menu = st.sidebar.selectbox("📂 Menu", ["Log Mood", "Mood Dashboard", "Logout"])

    if menu == "Logout":
        st.session_state.clear()
        st.success("Logged out.")
        st.rerun()

    elif menu == "Log Mood":
        st.subheader(f"💬 How are you feeling, {username}?")
        user_input = st.text_area("Describe your thoughts or feelings:", height=150)
        if st.button("Analyze & Save"):
            if user_input.strip():
                mood = predict_mood(user_input)
                save_log(username, user_input, mood)
                st.success(f"Mood detected: **{mood.upper()}**")
                st.info(f"💡 Tip: {mood_tips.get(mood, 'Stay mindful!')}")
            else:
                st.warning("Please write something to analyze.")

    elif menu == "Mood Dashboard":
        st.subheader("📊 Your Mood Dashboard")
        data = load_user_logs(username)

        if data.empty:
            st.info("You haven’t logged any moods yet.")
        else:
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("#### Mood Distribution")
                fig, ax = plt.subplots()
                data["mood"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
                ax.axis("equal")
                st.pyplot(fig)

            with col2:
                st.markdown("#### Mood Over Time")
                fig = px.scatter(data, x="timestamp", y="mood", color="mood", title="Mood Entries Timeline")
                fig.update_layout(height=400, xaxis_title="Time", yaxis_title="Mood")
                st.plotly_chart(fig, use_container_width=True)

            st.markdown("#### 🗒️ Recent Entries")
            st.dataframe(data.sort_values(by="timestamp", ascending=False).head(10))

    st.markdown("---")
    st.markdown("<small>Made with ❤️ using GoEmotions + Streamlit</small>", unsafe_allow_html=True)
