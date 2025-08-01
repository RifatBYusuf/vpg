import streamlit as st
from datetime import datetime, time
import pytz

# Config
st.set_page_config(page_title="VPG Time", page_icon="🌐", layout="wide")
st.markdown("<h1 style='text-align: center;'>🌐 VPG Time Converter</h1>", unsafe_allow_html=True)
st.markdown("##### Convert time between 🇦🇺 Sydney, 🇨🇦 British Columbia, and 🇧🇩 Dhaka")

# Timezones
zones = {
    "🇦🇺 Sydney": "Australia/Sydney",
    "🇨🇦 British Columbia": "Canada/Pacific",
    "🇧🇩 Dhaka": "Asia/Dhaka"
}

# Time input zone
selected_zone_label = st.selectbox("Select the time zone you want to input:", list(zones.keys()))
selected_zone = pytz.timezone(zones[selected_zone_label])

mode = st.radio("Input Method", ["Select from dropdown", "Type manually"])
now_local = datetime.now(selected_zone).time()

if mode == "Select from dropdown":
    col1, col2 = st.columns(2)
    with col1:
        hour = st.selectbox("Hour", range(0, 24), index=now_local.hour)
    with col2:
        minute = st.selectbox("Minute", range(0, 60, 5), index=0)
    input_time = time(hour, minute)
else:
    input_time = st.time_input("Enter Time", value=now_local)

# Localize input time
input_dt = selected_zone.localize(datetime.combine(datetime.now().date(), input_time))

# Convert to all zones
converted_times = {}
for label, tz_name in zones.items():
    tz = pytz.timezone(tz_name)
    converted_times[label] = input_dt.astimezone(tz)

# Output
st.markdown("---")
cols = st.columns(3)
for idx, (label, dt) in enumerate(converted_times.items()):
    with cols[idx]:
        st.markdown(f"### {label}")
        st.success(dt.strftime("%I:%M %p"))
        st.caption(dt.strftime("%A, %d %B %Y"))

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center;'>Made with ❤️ by VPG</p>", unsafe_allow_html=True)
