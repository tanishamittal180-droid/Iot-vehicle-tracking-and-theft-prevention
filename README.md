# 🚗 IoT Vehicle Tracking & Theft Prevention System

## 📌 Project Overview

The IoT Vehicle Tracking & Theft Prevention System is a smart vehicle monitoring solution developed using Python, Streamlit, GPS simulation, Geofencing, Analytics, and Security Monitoring techniques.

The system continuously tracks vehicle movement, monitors speed and fuel consumption, detects theft attempts, stores vehicle history, and visualizes data through an interactive Streamlit dashboard.

This project simulates a real-world IoT-based vehicle security and fleet management platform.

---

# 🎯 Objectives

- Track vehicle location in real time
- Monitor speed and fuel usage
- Detect unauthorized vehicle movement
- Implement geofence-based security
- Generate theft alerts
- Store vehicle history logs
- Visualize vehicle data using maps and analytics
- Generate vehicle performance reports

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Dashboard

- Streamlit

## Data Processing

- Pandas
- NumPy

## Visualization

- Plotly
- Folium
- Streamlit-Folium

## Reporting

- ReportLab

## Database

- CSV File Storage

---

# 📂 Project Structure

```text
IoT-Vehicle-Tracking-Theft-Prevention-System

│
├── data
│   ├── vehicle_log.csv
│   └── config.json
│
├── python_simulation
│   ├── gps_simulator.py
│   ├── vehicle_controller.py
│   ├── geofence.py
│   ├── theft_detector.py
│   ├── alert_manager.py
│   ├── analytics.py
│   ├── fuel_analytics.py
│   ├── route_tracker.py
│   ├── cloud_simulator.py
│   └── report_generator.py
│
├── outputs
│   └── Vehicle_Report.pdf
│
├── main.py
├── dashboard.py
├── generate_report.py
├── requirements.txt
└── README.md
```

---

# ⚙️ System Workflow

```text
GPS Simulator
       ↓
Vehicle Controller
       ↓
Geofence Security
       ↓
Theft Detection Engine
       ↓
Vehicle Logger
       ↓
CSV Database
       ↓
Analytics Engine
       ↓
Streamlit Dashboard
       ↓
PDF Report Generation
```

---

# 🚀 Features

## Vehicle Tracking

- Real-time GPS simulation
- Latitude and longitude tracking
- Vehicle route monitoring

## Vehicle Monitoring

- Speed monitoring
- Fuel monitoring
- Engine status monitoring
- Lock status monitoring

## Security Features

- Geofence security
- Theft detection
- Vehicle movement monitoring
- Alert generation

## Analytics

- Speed analysis
- Fuel consumption analysis
- Theft statistics
- Vehicle health score
- Fleet performance monitoring

## Visualization

- Interactive maps
- Route visualization
- Geofence visualization
- Theft alert mapping
- Dashboard KPIs

## Reporting

- Vehicle history logs
- PDF report generation
- Performance statistics

---

# 🔐 Theft Detection Logic

The system identifies suspicious activity using the following conditions:

## Condition 1

Locked vehicle is moving.

```text
Vehicle Locked
+
Speed > 5 km/h
=
Theft Alert
```

## Condition 2

Vehicle exits geofence area.

```text
Outside Safe Zone
=
Theft Alert
```

---

# 🗺️ Geofence Security

A secure zone is created around a predefined location.

If the vehicle remains inside the zone:

```text
SAFE
```

If the vehicle leaves the zone:

```text
THEFT ALERT
```

---

# 📊 Dashboard Features

The Streamlit dashboard provides:

### Live Monitoring

- Vehicle status
- Fuel level
- Speed
- Theft alerts

### Maps

- Live GPS map
- Route history
- Geofence map
- Theft locations

### Analytics

- Fuel analytics
- Speed analytics
- Theft analytics
- Alert analytics
- Vehicle health monitoring

### Fleet Monitoring

- Fleet summary
- Vehicle cards
- Fleet KPIs
- Activity feed

---

# 📈 Analytics Generated

## Speed Analytics

- Average speed
- Maximum speed
- Speed trend analysis
- Speed distribution

## Fuel Analytics

- Current fuel level
- Fuel consumption
- Fuel trend analysis

## Security Analytics

- Theft events
- Alert statistics
- Security score

---

# 📄 PDF Reports

The system automatically generates vehicle reports containing:

- Vehicle statistics
- Average speed
- Maximum speed
- Fuel information
- Theft alerts
- Performance summary

---

# ▶️ Installation

## Step 1

Clone the repository.

```bash
git clone https://github.com/yourusername/vehicle-tracking-system.git
```

## Step 2

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

## Generate Vehicle Data

```bash
python main.py
```

This will continuously generate simulated vehicle data.

---

## Launch Dashboard

```bash
streamlit run dashboard.py
```

---

## Generate PDF Report

```bash
python generate_report.py
```

---

# 📷 Dashboard Modules

### Module 1

Vehicle Status Monitoring

### Module 2

Live GPS Tracking

### Module 3

Route Tracking

### Module 4

Geofence Monitoring

### Module 5

Theft Detection

### Module 6

Fuel Analytics

### Module 7

Speed Analytics

### Module 8

Fleet Monitoring

### Module 9

PDF Reporting

---

# 🌍 Real-World Applications

- Vehicle Security Systems
- Fleet Management
- Logistics Tracking
- Delivery Vehicle Monitoring
- Smart Transportation Systems
- Vehicle Theft Prevention
- Smart City Transportation

---
# screenshots
<img width="1366" height="768" alt="Screenshot 2026-06-13 125521" src="https://github.com/user-attachments/assets/53fbbc3e-3b4b-42d0-bd7c-c2ae26dc7b59" />
<img width="1366" height="768" alt="Screenshot 2026-06-13 125543" src="https://github.com/user-attachments/assets/94fe08e5-aecc-4cea-91d0-1280e622cc75" />
<img width="1366" height="768" alt="Screenshot 2026-06-13 125722" src="https://github.com/user-attachments/assets/58021488-226b-4987-9aff-9e7c81d63813" />
<img width="1366" height="768" alt="Screenshot 2026-06-13 125743" src="https://github.com/user-attachments/assets/fade0147-362d-4128-bbd3-90dba0fd9e02" />
<img width="1366" height="768" alt="Screenshot 2026-06-13 125826" src="https://github.com/user-attachments/assets/6b0d9730-65f2-4050-93e1-c0e0bcc31dce" />
<img width="1366" height="768" alt="Screenshot 2026-06-13 125841" src="https://github.com/user-attachments/assets/a439a620-07ed-4a51-942d-b70fff3608e4" />
<img width="1366" height="768" alt="Screenshot 2026-06-13 125856" src="https://github.com/user-attachments/assets/bb9617d0-b1aa-49f4-a97d-dbeea670a910" />
<img width="1366" height="768" alt="Screenshot 2026-06-13 125947" src="https://github.com/user-attachments/assets/e133215b-76a0-4e03-8c81-b33d4a79575f" />
<img width="1366" height="768" alt="Screenshot 2026-06-13 125959" src="https://github.com/user-attachments/assets/5fe4c684-740f-4a60-93a4-0cf28b67951f" />


# 🔮 Future Enhancements

- ESP32 Integration
- Real GPS Module Integration
- Firebase Cloud Database
- MQTT Communication
- Telegram Alert Bot
- Email Notifications
- AI Theft Prediction
- Face Recognition Authentication
- RFID-Based Vehicle Access
- Camera-Based Security Monitoring

---

# 🎓 Learning Outcomes

Through this project, the following concepts are demonstrated:

- Internet of Things (IoT)
- Vehicle Tracking Systems
- Geofencing
- Security Monitoring
- Data Analytics
- Streamlit Dashboard Development
- Data Visualization
- Report Generation
- Fleet Management Concepts

---

# 📌 Conclusion

The IoT Vehicle Tracking & Theft Prevention System is a comprehensive simulation of a smart vehicle monitoring platform. The system successfully demonstrates vehicle tracking, geofence security, theft detection, analytics, route visualization, and reporting using Python and Streamlit. It serves as a strong foundation for developing a real-world IoT-enabled vehicle security and fleet management solution.

---

## 👩‍💻 Developer

Tanisha Mittal

B.Tech Electronics and Communication Engineering (ECE)

Python | IoT | Machine Learning | Data Analytics | Streamlit Development

---
