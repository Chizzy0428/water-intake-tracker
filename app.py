import streamlit as st
import pandas as pd
from datetime import datetime, date
from database import init_db, log_intake, get_intake_history
from agent import WaterIntakeAgent
from logger import log_message, log_error

# ----------------------------
# Initialize Database and Agent
# ----------------------------
init_db()
agent = WaterIntakeAgent()

# ----------------------------
# Streamlit Page Config
# ----------------------------
st.set_page_config(page_title="💧 AI Water Tracker", layout="centered")

# Initialize session state
if "tracker_started" not in st.session_state:
    st.session_state.tracker_started = False

# ----------------------------
# Welcome Page
# ----------------------------
if not st.session_state.tracker_started:
    st.title("💧 Welcome to AI Water Tracker")
    st.markdown("""
    Track your daily water intake and get smart hydration insights powered by AI.  
    Stay healthy, stay hydrated!
    """)

    if st.button("🚀 Start Tracking"):
        st.session_state.tracker_started = True
        st.rerun()


# ----------------------------
# Main App Page
# ----------------------------
else:
    st.title("💧 AI Water Tracker")

    # Sidebar navigation
    page = st.sidebar.radio("📋 Menu", ["Log Intake", "View History", "AI Insights", "Reset App"])

    # --------------------------------
    # PAGE 1: Log Intake
    # --------------------------------
    if page == "Log Intake":
        st.header("🚰 Log Your Water Intake")

        user_id = st.text_input("Enter your name or user ID:")
        intake_ml = st.number_input("Enter water amount (ml)", min_value=100, step=50)

        if st.button("Add Intake"):
            try:
                if not user_id:
                    st.warning("Please enter your name or ID.")
                else:
                    log_intake(user_id, intake_ml)
                    log_message(f"User {user_id} logged {intake_ml}ml of water.")
                    st.success(f"✅ {intake_ml} ml logged successfully for {user_id}!")
            except Exception as e:
                log_error(str(e))
                st.error("An error occurred while logging intake.")

        # Display today’s total and progress
        if user_id:
            history = get_intake_history(user_id)
            df = pd.DataFrame(history, columns=["intake_ml", "date"])
            df["date"] = pd.to_datetime(df["date"])

            today_str = date.today().strftime("%Y-%m-%d")
            today_total = df[df["date"].dt.strftime("%Y-%m-%d") == today_str]["intake_ml"].sum()

            goal = 2000  # ml daily goal
            progress = min(today_total / goal, 1.0)
            st.metric("Today's Total", f"{today_total} ml")
            st.progress(progress)

            if today_total < 1000:
                st.info("💧 Keep going! You're doing great.")
            elif today_total < goal:
                st.success("👏 Almost there! A few more sips to reach your goal.")
            else:
                st.balloons()
                st.success("🎉 You reached your daily goal! Stay hydrated!")

    # --------------------------------
    # PAGE 2: View History
    # --------------------------------
    elif page == "View History":
        st.header("📊 Water Intake History")

        user_id = st.text_input("Enter your user ID to view history:")
        if user_id:
            history = get_intake_history(user_id)
            if history:
                df = pd.DataFrame(history, columns=["intake_ml", "date"])
                df["date"] = pd.to_datetime(df["date"])
                df["day"] = df["date"].dt.date

                # Daily summary
                daily_summary = df.groupby("day")["intake_ml"].sum().reset_index()

                st.subheader("📅 Daily Summary")
                st.line_chart(daily_summary.set_index("day")["intake_ml"])
                st.dataframe(df)
            else:
                st.info("No history found for this user.")

    # --------------------------------
    # PAGE 3: AI Insights
    # --------------------------------
    elif page == "AI Insights":
        st.header("🤖 AI Hydration Insights")

        user_id = st.text_input("Enter your user ID:")
        if user_id and st.button("Analyze Hydration"):
            try:
                history = get_intake_history(user_id)
                if not history:
                    st.warning("No intake history available for this user.")
                else:
                    df = pd.DataFrame(history, columns=["intake_ml", "date"])
                    df["date"] = pd.to_datetime(df["date"])
                    today_str = date.today().strftime("%Y-%m-%d")
                    today_total = df[df["date"].dt.strftime("%Y-%m-%d") == today_str]["intake_ml"].sum()

                    st.write("Analyzing your water intake using AI... ⏳")
                    analysis = agent.analyze_intake(today_total)
                    st.success("💡 AI Insight:")
                    st.write(analysis)

                    log_message(f"AI analyzed intake for {user_id}: {today_total}ml")
            except Exception as e:
                log_error(str(e))
                st.error("Failed to generate AI insights.")

    # --------------------------------
    # PAGE 4: Reset
    # --------------------------------
    elif page == "Reset App":
        if st.button("🔄 Reset App"):
            st.session_state.tracker_started = False
            st.success("App reset. Restarting...")
            st.rerun()

