import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import folium
from streamlit_folium import st_folium
from streamlit_autorefresh import st_autorefresh
# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="IoT Vehicle Tracking",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================
# CUSTOM CSS
# =====================================
st.markdown("""
<style>

.main{
background:#0f172a;
}

[data-testid="stSidebar"]{
background:#111827;
}

.dashboard-card{
background:rgba(255,255,255,0.05);
backdrop-filter:blur(10px);
padding:20px;
border-radius:20px;
box-shadow:0px 4px 30px rgba(0,255,255,0.1);
margin-bottom:20px;
}

.title-text{
text-align:center;
font-size:42px;
font-weight:bold;
color:#00FFFF;
animation:glow 2s infinite alternate;
}

@keyframes glow{

from{
text-shadow:0 0 10px #00FFFF;
}

to{
text-shadow:0 0 30px #00FFFF;
}

}

.online{
height:15px;
width:15px;
background:#00ff00;
border-radius:50%;
display:inline-block;
animation:pulse 1s infinite;
}

.alert{
height:15px;
width:15px;
background:red;
border-radius:50%;
display:inline-block;
animation:pulse 1s infinite;
}

@keyframes pulse{

0%{
transform:scale(1);
}

50%{
transform:scale(1.4);
}

100%{
transform:scale(1);
}

}

.big-metric{

font-size:28px;
font-weight:bold;
text-align:center;

}

</style>
""",
unsafe_allow_html=True)

# =====================================
# HEADER
# =====================================

st.markdown(
"""
<div class="title-text">
🚗 Smart Fleet Monitoring System
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<center>

<span class="online"></span>

SYSTEM ONLINE

</center>
""",
unsafe_allow_html=True
)

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("⚙ Control Panel")

refresh_rate = st.sidebar.slider(
    "Refresh Rate (Seconds)",
    1,
    10,
    3
)

selected_vehicle = st.sidebar.selectbox(
    "Select Vehicle",
    [
        "All Vehicles",
        "VH001",
        "VH002",
        "VH003"
    ]
)

theme = st.sidebar.radio(
    "Dashboard Theme",
    [
        "Dark",
        "Light"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success(
    "System Online"
)

st.sidebar.info(
    f"Refresh : {refresh_rate}s"
)

# =====================================
# LOAD DATA
# =====================================

try:

    df = pd.read_csv(
        "data/vehicle_log.csv"
    )

except:

    st.warning(
        "No Vehicle Data Found"
    )

    st.stop()
# =====================================
# SAFE DATA PREPARATION
# =====================================

required_columns = {
    "Latitude": 31.3260,
    "Longitude": 75.5762,
    "Speed": 0,
    "Fuel": 0,
    "Engine": False,
    "Locked": False,
    "Status": "SAFE",
    "Alert": "No Alert"
}

for col, default in required_columns.items():

    if col not in df.columns:

        df[col] = default

if len(df) == 0:

    st.warning("No data available")

    st.stop()

latest = df.iloc[-1]

latest_lat = float(latest["Latitude"])

latest_lon = float(latest["Longitude"])

current_fuel = float(latest["Fuel"])

latest_speed = float(latest["Speed"])

latest_engine = bool(latest["Engine"])

latest_locked = bool(latest["Locked"])
# =====================================
# BASIC FILTERING
# =====================================

if selected_vehicle != "All Vehicles":

    if "VehicleID" in df.columns:

        df = df[
            df["VehicleID"]
            ==
            selected_vehicle
        ]

# =====================================
# KPI CALCULATIONS
# =====================================

total_records = len(df)

avg_speed = 0

if "Speed" in df.columns:

    avg_speed = round(
        df["Speed"].mean(),
        2
    )

max_speed = 0

if "Speed" in df.columns:

    max_speed = round(
        df["Speed"].max(),
        2
    )

theft_count = 0

if "Status" in df.columns:

    theft_count = len(
        df[
            df["Status"]
            ==
            "THEFT"
        ]
    )

# =====================================
# KPI ROW
# =====================================

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.metric(
        "📊 Records",
        total_records
    )

with c2:

    st.metric(
        "🚀 Avg Speed",
        avg_speed
    )

with c3:

    st.metric(
        "⚡ Max Speed",
        max_speed
    )

with c4:

    st.metric(
        "🚨 Theft Alerts",
        theft_count
    )

st.markdown("---")
st.markdown("""
<div class="dashboard-card">

<h3>📡 System Status</h3>

✅ GPS Active

✅ Fleet Connected

✅ Database Connected

✅ Dashboard Online

</div>
""",
unsafe_allow_html=True)
# =====================================
# VEHICLE STATUS SECTION
# =====================================

st.subheader(
    "🚗 Fleet Status"
)

latest = df.iloc[-1]

col1,col2,col3 = st.columns(3)

with col1:

    st.markdown(
        """
        ### Engine Status
        """
    )
    if "Engine" in df.columns:
        if latest["Engine"]:
            st.success("🟢 Running")
        else:
            st.error("🔴 OFF")
    else:
            st.warning("Engine Data Not Available")



with col2:

    st.markdown(
        """
        ### Lock Status
        """
    )
    if "Locked" in df.columns:
        if latest["Locked"]:
            st.error("🔒 Locked")
        else:
            st.success("🔓 Unlocked")
    else:
            st.warning("Lock Data Not Available")
with col3:

    st.markdown(
        """
        ### Fuel Level
        """
    )
    if "Fuel" in df.columns:
        st.info(
        f"{latest['Fuel']} L"
    )
    else:
        st.warning(
        "Fuel Data Not Available"
    )
st.markdown("---")
st.markdown("---")

st.subheader(
"🚗 Live Fleet Vehicles"
)

v1,v2,v3 = st.columns(3)

with v1:

    st.markdown(
    """
    <div class="dashboard-card">

    <h3>VH001</h3>

    GPS Active

    Fuel Monitoring

    Theft Protection

    </div>
    """,
    unsafe_allow_html=True
    )

with v2:

    st.markdown(
    """
    <div class="dashboard-card">

    <h3>VH002</h3>

    GPS Active

    Route Tracking

    Theft Protection

    </div>
    """,
    unsafe_allow_html=True
    )

with v3:

    st.markdown(
    """
    <div class="dashboard-card">

    <h3>VH003</h3>

    GPS Active

    Security Enabled

    Live Monitoring

    </div>
    """,
    unsafe_allow_html=True
    )
# =====================================
# LIVE DATA TABLE
# =====================================

st.subheader(
    "📋 Latest Vehicle Logs"
)

st.dataframe(
    df.tail(20),
    use_container_width=True
)

st.markdown("---")

# =====================================
# SPEED CHART
# =====================================

st.subheader(
    "📈 Speed Analytics"
)

if "Speed" in df.columns:

    fig = px.line(
        df,
        y="Speed",
        title="Vehicle Speed"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
# =====================================
# LIVE GPS MAP
# =====================================

st.markdown("---")

st.subheader("🗺️ Live Vehicle Location Map")

if (
    "Latitude" in df.columns and
    "Longitude" in df.columns
):

    latest_lat = float(
        df.iloc[-1]["Latitude"]
    )

    latest_lon = float(
        df.iloc[-1]["Longitude"]
    )

    vehicle_map = folium.Map(
        location=[
            latest_lat,
            latest_lon
        ],
        zoom_start=15
    )

    # Current Vehicle Marker

    folium.Marker(

        [latest_lat, latest_lon],

        popup="Current Vehicle",

        tooltip="Vehicle Location",

        icon=folium.Icon(
            color="green",
            icon="car"
        )

    ).add_to(vehicle_map)

    st_folium(
        vehicle_map,
        width=1200,
        height=500
    )
# =====================================
# ROUTE VISUALIZATION
# =====================================

st.markdown("---")

st.subheader(
    "🛣️ Vehicle Route History"
)

route_map = folium.Map(

    location=[
        latest_lat,
        latest_lon
    ],

    zoom_start=14
)

coordinates = []

for _, row in df.iterrows():

    coordinates.append([

        row["Latitude"],
        row["Longitude"]

    ])

if len(coordinates) > 1:

    folium.PolyLine(

        coordinates,

        weight=5,

        tooltip="Vehicle Route"

    ).add_to(route_map)

    folium.Marker(

        coordinates[0],

        popup="Start Location",

        icon=folium.Icon(
            color="blue"
        )

    ).add_to(route_map)

    folium.Marker(

        coordinates[-1],

        popup="Current Location",

        icon=folium.Icon(
            color="green"
        )

    ).add_to(route_map)

st_folium(

    route_map,

    width=1200,

    height=500
)
# =====================================
# GEOFENCE MAP
# =====================================

st.markdown("---")

st.subheader(
    "🛡️ Geofence Security Zone"
)

SAFE_LAT = 31.3260
SAFE_LON = 75.5762

SAFE_RADIUS = 500

geo_map = folium.Map(

    location=[
        SAFE_LAT,
        SAFE_LON
    ],

    zoom_start=15
)

folium.Circle(

    location=[
        SAFE_LAT,
        SAFE_LON
    ],

    radius=SAFE_RADIUS,

    popup="Safe Zone",

    fill=True

).add_to(geo_map)

folium.Marker(

    [SAFE_LAT, SAFE_LON],

    popup="Base Location",

    icon=folium.Icon(
        color="blue"
    )

).add_to(geo_map)

folium.Marker(

    [latest_lat, latest_lon],

    popup="Vehicle",

    icon=folium.Icon(
        color="green"
    )

).add_to(geo_map)

st_folium(

    geo_map,

    width=1200,

    height=500
)
# =====================================
# THEFT ALERT LOCATIONS
# =====================================

st.markdown("---")

st.subheader(
    "🚨 Theft Alert Locations"
)

theft_df = df[

    df["Status"] == "THEFT"

]

if len(theft_df) > 0:

    theft_map = folium.Map(

        location=[
            latest_lat,
            latest_lon
        ],

        zoom_start=13
    )

    for _, row in theft_df.iterrows():

        folium.Marker(

            [
                row["Latitude"],
                row["Longitude"]
            ],

            popup=row["Alert"],

            icon=folium.Icon(
                color="red"
            )

        ).add_to(theft_map)

    st_folium(

        theft_map,

        width=1200,

        height=500
    )

else:

    st.success(
        "No Theft Events Detected"
    )
st.markdown("---")

st.subheader(
"🛡 Security Center"
)

if theft_count > 0:

    st.error(
    f"{theft_count} Security Alerts Detected"
    )

else:

    st.success(
    "No Security Threats Found"
    )

st.progress(
max(
0,
100 - theft_count*10
)/100
)
# =====================================
# GOOGLE MAPS LINK
# =====================================

st.markdown("---")

st.subheader(
    "📍 Open In Google Maps"
)

maps_url = (

    f"https://www.google.com/maps?q="
    f"{latest_lat},{latest_lon}"

)

st.markdown(

    f"""
    [🌍 Open Vehicle Location]({maps_url})
    """
)
# =====================================
# FUEL ANALYTICS
# =====================================

st.markdown("---")

st.subheader("⛽ Fuel Analytics")

if "Fuel" in df.columns:

    col1, col2, col3 = st.columns(3)

    current_fuel = round(
        df["Fuel"].iloc[-1], 2
    )

    avg_fuel = round(
        df["Fuel"].mean(), 2
    )

    fuel_used = round(
        df["Fuel"].iloc[0]
        -
        df["Fuel"].iloc[-1],
        2
    )

    with col1:
        st.metric(
            "Current Fuel",
            f"{current_fuel} L"
        )

    with col2:
        st.metric(
            "Average Fuel",
            f"{avg_fuel} L"
        )

    with col3:
        st.metric(
            "Fuel Consumed",
            f"{fuel_used} L"
        )

    fuel_chart = px.line(
        df,
        y="Fuel",
        title="Fuel Consumption Trend"
    )

    st.plotly_chart(
        fuel_chart,
        use_container_width=True
    )
# =====================================
# VEHICLE HEALTH
# =====================================

st.markdown("---")

st.subheader("🩺 Vehicle Health Monitor")

health_score = 100

if current_fuel < 10:
    health_score -= 20

if max_speed > 100:
    health_score -= 15

if theft_count > 0:
    health_score -= 10

st.progress(
    health_score / 100
)

st.success(
    f"Vehicle Health Score: {health_score}%"
)
fleet_health = max(
0,
100 - theft_count*5
)

st.markdown(
f"""
<div class="dashboard-card">

<h2>
Fleet Health Score
</h2>

<div class="big-metric">
{fleet_health}%
</div>

</div>
""",
unsafe_allow_html=True
)
# =====================================
# SPEED DISTRIBUTION
# =====================================

st.markdown("---")

st.subheader(
    "🚀 Speed Distribution"
)

if "Speed" in df.columns:

    hist = px.histogram(
        df,
        x="Speed",
        nbins=20,
        title="Vehicle Speed Distribution"
    )

    st.plotly_chart(
        hist,
        use_container_width=True
    )
# =====================================
# SPEED TREND
# =====================================

st.markdown("---")

st.subheader(
    "📈 Speed Trend Analysis"
)

speed_fig = px.area(
    df,
    y="Speed",
    title="Speed Over Time"
)

st.plotly_chart(
    speed_fig,
    use_container_width=True
)
# =====================================
# THEFT ANALYTICS
# =====================================

st.markdown("---")

st.subheader(
    "🚨 Theft Analytics"
)

safe_count = len(
    df[
        df["Status"] == "SAFE"
    ]
)

theft_count = len(
    df[
        df["Status"] == "THEFT"
    ]
)

pie_data = {

    "Status": [
        "SAFE",
        "THEFT"
    ],

    "Count": [
        safe_count,
        theft_count
    ]
}

pie_df = pd.DataFrame(
    pie_data
)

pie_chart = px.pie(
    pie_df,
    values="Count",
    names="Status",
    title="Security Status Distribution"
)

st.plotly_chart(
    pie_chart,
    use_container_width=True
)
# =====================================
# ALERT ANALYTICS
# =====================================

st.markdown("---")

st.subheader(
    "📢 Alert Analytics"
)

if "Alert" in df.columns:

    alert_counts = (
        df["Alert"]
        .value_counts()
        .reset_index()
    )

    alert_counts.columns = [
        "Alert",
        "Count"
    ]

    alert_chart = px.bar(
        alert_counts,
        x="Alert",
        y="Count",
        title="Alert Frequency"
    )

    st.plotly_chart(
        alert_chart,
        use_container_width=True
    )
# =====================================
# FLEET PERFORMANCE
# =====================================

st.markdown("---")

st.subheader(
    "🏆 Fleet Performance KPIs"
)

k1,k2,k3,k4 = st.columns(4)

with k1:
    st.metric(
        "Records",
        len(df)
    )

with k2:
    st.metric(
        "Avg Speed",
        round(
            df["Speed"].mean(),
            2
        )
    )

with k3:
    st.metric(
        "Max Speed",
        round(
            df["Speed"].max(),
            2
        )
    )

with k4:
    st.metric(
        "Theft Events",
        theft_count
    )
# =====================================
# ROUTE STATISTICS
# =====================================

st.markdown("---")

st.subheader(
    "🛣 Route Statistics"
)

total_points = len(df)

st.info(
    f"GPS Points Collected: "
    f"{total_points}"
)

st.success(
    f"Latest Coordinates: "
    f"{latest_lat}, {latest_lon}"
)
# =====================================
# FLEET COMMAND CENTER
# =====================================

st.markdown("---")

st.subheader("🎮 Fleet Command Center")

control_col1, control_col2, control_col3 = st.columns(3)

with control_col1:

    if st.button(
        "🔒 Lock Vehicle"
    ):

        st.error(
            "Vehicle Locked"
        )

with control_col2:

    if st.button(
        "🔓 Unlock Vehicle"
    ):

        st.success(
            "Vehicle Unlocked"
        )

with control_col3:

    if st.button(
        "🚨 Emergency Stop"
    ):

        st.warning(
            "Emergency Stop Activated"
        )
# =====================================
# ENGINE CONTROL
# =====================================

st.markdown("---")

st.subheader("⚙ Engine Control")

engine_col1, engine_col2 = st.columns(2)

with engine_col1:

    if st.button(
        "🟢 Start Engine"
    ):

        st.success(
            "Engine Started"
        )

with engine_col2:

    if st.button(
        "🔴 Stop Engine"
    ):

        st.error(
            "Engine Stopped"
        )
# =====================================
# VEHICLE SELECTOR
# =====================================

st.markdown("---")

st.subheader(
    "🚗 Vehicle Selector"
)

vehicle_selected = st.selectbox(

    "Choose Vehicle",

    [
        "VH001",
        "VH002",
        "VH003"
    ]
)

st.info(
    f"Selected Vehicle : "
    f"{vehicle_selected}"
)
# =====================================
# EXPORT CSV
# =====================================

st.markdown("---")

st.subheader(
    "📥 Export Vehicle Data"
)

csv_file = df.to_csv(
    index=False
)

st.download_button(

    label="Download CSV",

    data=csv_file,

    file_name=
    "vehicle_log.csv",

    mime="text/csv"
)
# =====================================
# PDF REPORT
# =====================================

st.markdown("---")

st.subheader(
    "📄 Generate Report"
)

if st.button(
    "Generate PDF Report"
):

    st.success(
        "PDF Generation Requested"
    )

    st.info(
        "Run generate_report.py"
    )
# =====================================
# LIVE FLEET SUMMARY
# =====================================

st.markdown("---")

st.subheader(
    "📡 Fleet Summary"
)

summary_col1, summary_col2, summary_col3 = st.columns(3)

with summary_col1:

    st.metric(
        "Vehicles Online",
        3
    )

with summary_col2:

    st.metric(
        "Active Alerts",
        theft_count
    )

with summary_col3:

    st.metric(
        "Total GPS Points",
        len(df)
    )
# =====================================
# ACTIVITY FEED
# =====================================

st.markdown("---")

st.subheader(
    "📜 Recent Activity"
)

activity_df = df.tail(10)

for _, row in activity_df.iterrows():

    st.write(

        f"""
        🚗 Vehicle Update

        Speed: {row['Speed']} km/h

        Fuel: {row['Fuel']} L

        Status: {row['Status']}
        """
    )
# =====================================
# AUTO REFRESH
# =====================================

st_autorefresh(

    interval=3000,

    key="fleet_refresh"
)
# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.caption(
    f"Last Updated : "
    f"{datetime.now()}"
)
st.markdown("---")

st.markdown(
"""
<center>

🚀 Developed Using

Python • Streamlit • IoT • GPS • Analytics

<br>

© 2026 Smart Vehicle Tracking System

</center>
""",
unsafe_allow_html=True
)