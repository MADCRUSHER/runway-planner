import streamlit as st
from datetime import time

st.set_page_config(page_title="Runway Planner", layout="centered")

# ---------------- SESSION STATE INIT ----------------
if "generated" not in st.session_state:
    st.session_state.generated = False

# ---------------- HEADER ----------------
st.title("✈️ Runway Planner")
st.caption("A constraint-based daily planner for lab-heavy schedules")

st.divider()

# ---------------- DAILY INPUTS ----------------
st.subheader("📥 Daily Setup")

college_start = st.time_input(
    "College Start Time",
    value=time(8, 0)
)

college_end = st.time_input(
    "College End Time",
    value=time(17, 30)
)

energy = st.selectbox(
    "Energy Level",
    ["Low", "Normal", "High"]
)

if st.button("🚀 Generate My Day"):
    st.session_state.generated = True

st.divider()

# ---------------- GENERATED PLAN ----------------
if st.session_state.generated:
    st.subheader("📅 Today’s Plan")

    st.write(f"🧑‍🎓 **College:** {college_start.strftime('%H:%M')} – {college_end.strftime('%H:%M')}")
    st.write("✈️ **Career:** 90 mins (after college)")
    st.write("🏋️ **Exercise:** 60 mins (flexible)")
    st.write("🍽️ **Dinner:** 7:00 – 8:00 PM")
    st.write("🎮 **Valorant:** Up to 2 matches")
    st.write("📖 **Journal:** 10:30 – 11:00 PM")

    st.divider()

    # ---------------- COMPLETION SYSTEM ----------------
    st.subheader("✅ Completion Check")

    exercise_done = st.checkbox("Exercise Completed", key="exercise")
    career_done = st.checkbox("Career Work Completed", key="career")

    if exercise_done and career_done:
        st.success("🎮 Valorant Unlocked — Enjoy guilt-free!")
    else:
        st.warning("🔒 Valorant Locked — Finish Exercise + Career")
