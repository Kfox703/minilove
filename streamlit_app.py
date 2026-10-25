import streamlit as st
import datetime
st.set_page_config(page_title="MINI BABYLOVE", page_icon="❤️", layout="centered")
ANNIVERSARY = datetime.datetime(2021, 4, 18, 0, 0, 0)
# print("\n"*4) LIVE DATABASING (Session State) print("\n"*4)
if "tummy" not in st.session_state:
    st.session_state.tummy = "Full and happy"
if "emotion" not in st.session_state:
    st.session_state.emotion = "Neutral and cozy"
if "social_battery" not in st.session_state:
    st.session_state.social_battery = 55
if "custom_message" not in st.session_state:
    st.session_state.custom_message = "I love you my sweet baby!<3"
now = datetime.datetime.now()
delta = now - ANNIVERSARY
years = delta.days // 365
remaining_days_after_years = delta.days % 365
months = remaining_days_after_years // 30
remaining_days = remaining_days_after_years % 30
remaining_days = delta.days % 365
seconds = delta.seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60
rem_seconds = seconds % 60
# --- HIS LIVE DISPLAY VIEW ---
st.title("MINI BABYLOVE 🐻‍❄️")
st.subheader("We've Been Together For ⏱:")
st.info(f"**{years}** Years, **{months}** Months,**{remaining_days}** Days, **{hours}h {minutes}m {rem_seconds}s**")

st.divider()

# st.subheader("⁒" Current Status")
st.markdown(f"🤢 **Tummy:** {st.session_state.tummy}")
st.markdown(f"🎭 **Mood:** {st.session_state.emotion}")
st.markdown(f"🔋 **Social Battery: {st.session_state.social_battery}%**")
st.progress(st.session_state.social_battery / 100)

st.divider()

st.subheader("Letters to my Love💌")
st.chat_message("user", avatar="❤️").write(st.session_state.custom_message)

st.divider()

# --- PASSWORD PROTECTED ADMIN PANEL ---
with st.expander("⚙️ Missus Control Only! No Boyz Allowed."):
    # Type your secret password here (Change "my_secret_password" to whatever you want!)
    password = st.text_input("Enter Admin Password", type="password")

    if password == "041821<3":
        st.success("Access Granted! Update your stats:")
        new_tummy = st.text_input("How is your tummy?", value=st.session_state.tummy)
        new_emotion = st.text_input("What is your current mood?", value=st.session_state.emotion)
        new_battery = st.slider("Social Battery Level", 0, 100, int(st.session_state.social_battery))
        new_message = st.text_area("Update your message:", value=st.session_state.custom_message)

        if st.button("Publish Live Updates ✨"):
            st.session_state.tummy = new_tummy
            st.session_state.emotion = new_emotion
            st.session_state.social_battery = new_battery
            st.session_state.custom_message = new_message
            st.toast("Status updated successfully!", icon="✅")
            st.rerun()
    elif password != "041821<3":
        st.error("Incorrect password! Hands off, my man bichacha! (ง•o•)ง")
st.fragment(run_every="1s")
primaryColor = "#ff2a2a"          # Signature Nothing OS Red accents
backgroundColor = "#000000"       # Deep AMOLED black battery-saving background
secondaryBackgroundColor = "#161616" # Dark gray for clean panel cards
textColor = "#ffffff"             # Crisp white typography
font = "monospace"                # Clean, retro tech typography