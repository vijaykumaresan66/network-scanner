Yes. I checked your **actual `main.py`** and the risk logic you uploaded, so this README is based on what your project really implements—not the generic version above.

Your application includes network discovery, device comparison, risk scoring, CSV export, network topology, port scanning, auto-refresh, search/filtering, and login/dashboard flow.  

# 🔐 Advanced Network Scanner

A Python-based cybersecurity tool for **network discovery, device monitoring, risk assessment, port scanning, and network topology visualization**.

The project provides a graphical dashboard that discovers devices on the local network, tracks newly detected and offline devices, calculates a basic security risk level, and allows scan results to be exported as CSV.

---

## 📌 Project Overview

The **Advanced Network Scanner** is designed as a practical cybersecurity and network-security project for understanding how network reconnaissance and device monitoring work.

The application provides a dashboard containing:

* Number of detected devices
* Newly detected devices
* Offline devices
* Last scan time
* Device search/filtering
* Device status
* Risk level
* Network topology
* Port scanning
* CSV export

The application uses a Tkinter-based graphical interface and separates scanning, networking, monitoring, exporting, topology, port scanning, threat analysis, and login functionality into modules. 

---

## 🚀 Key Features

### 🔍 1. Network Discovery

The scanner identifies devices available on the local network.

The application obtains the local network and passes it to the network scanning module to discover devices. 

---

### 📊 2. Security Dashboard

The dashboard displays:

| Metric        | Description                                             |
| ------------- | ------------------------------------------------------- |
| **Devices**   | Number of currently detected devices                    |
| **New**       | Newly detected devices                                  |
| **Offline**   | Devices detected previously but not currently available |
| **Last Scan** | Time of the most recent scan                            |

These values are updated after each scan.  

---

### 🖥️ 3. Device Information

Detected devices are displayed in a table containing:

* IP Address
* MAC Address
* Hostname
* Vendor
* Status
* Risk

The application dynamically inserts the discovered device information into the dashboard. 

---

### 🔎 4. Device Search

The dashboard includes a search field that allows the user to filter discovered devices.

Search results are updated while typing. 

---

### 🛡️ 5. Risk Assessment

The scanner calculates a basic risk score for each discovered device.

The current risk engine checks for commonly associated higher-risk ports:

| Port | Service |
| ---: | ------- |
|   21 | FTP     |
|   23 | Telnet  |
|  445 | SMB     |
| 3389 | RDP     |
| 5900 | VNC     |

Each matching port increases the risk score. An unknown vendor also adds to the score.  

Risk levels are categorized as:

* 🟢 **Low**
* 🟡 **Medium**
* 🔴 **High**

The score thresholds are implemented directly in the threat-analysis module. 

---

### 🔌 6. Port Scanner

A user can select a device from the dashboard and run a port scan against its IP address.

The application displays the discovered open ports in a result dialog. 

---

### 🌐 7. Network Topology

The application includes a **NETWORK TOPOLOGY** feature that passes the currently discovered devices to the topology module for visualization. 

---

### 📁 8. CSV Export

Scan results can be exported to a CSV file for further analysis or documentation.

The application checks whether scan data exists before performing the export. 

---

### 🔄 9. Automatic Scanning

The scanner supports automatic refresh.

After starting the application, the automatic refresh mechanism periodically checks whether a scan is running and starts a new scan when required. 

The application schedules this automatic refresh after startup. 

---

### ⚡ 10. Multithreaded Scanning

Network scanning is executed using a background thread so that the graphical interface can continue operating while the scan is running.

The project uses Python's `threading` module and prevents multiple scans from running simultaneously.  

---

### 🔐 11. Login System

The application starts through a login module. After successful authentication, the login window is closed and the main scanner dashboard is launched. 

---

## 🏗️ Project Architecture

```text
Advanced-Network-Scanner/
│
├── main.py
│
├── modules/
│   ├── scanner.py
│   ├── network.py
│   ├── monitor.py
│   ├── export.py
│   ├── topology.py
│   ├── portscanner.py
│   ├── threat.py
│   └── login.py
│
├── screenshots/
│   └── scanner.png
│
├── requirements.txt
└── README.md
```

---

## 🧩 Module Responsibilities

| Module           | Purpose                                                    |
| ---------------- | ---------------------------------------------------------- |
| `main.py`        | Main GUI, dashboard, scan workflow and application control |
| `scanner.py`     | Network device discovery                                   |
| `network.py`     | Determines the local network                               |
| `monitor.py`     | Compares previous and current device states                |
| `export.py`      | Exports scan results                                       |
| `topology.py`    | Displays network topology                                  |
| `portscanner.py` | Performs port scanning                                     |
| `threat.py`      | Calculates device risk                                     |
| `login.py`       | Handles application login                                  |

The main application imports and connects these modules into a single workflow. 

---

## 🛠️ Technologies Used

* **Python**
* **Tkinter**
* **Python Threading**
* **Network Scanning**
* **TCP/IP Networking**
* **Port Scanning**
* **CSV Data Export**
* **Network Topology Visualization**
* **Basic Risk Analysis**

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/advanced-network-scanner.git
```

### 2. Open the Project

```bash
cd advanced-network-scanner
```

### 3. Install Dependencies

```bash
py -m pip install -r requirements.txt
```

---

## ▶️ Run the Application

On Windows:

```bash
py main.py
```

The application starts with the login interface. After successful login, the network scanner dashboard is displayed. 

---

## 🔄 Application Workflow

```text
             ┌───────────────┐
             │     Login     │
             └───────┬───────┘
                     ↓
             ┌───────────────┐
             │   Dashboard   │
             └───────┬───────┘
                     ↓
             ┌───────────────┐
             │ Local Network │
             │   Detection   │
             └───────┬───────┘
                     ↓
             ┌───────────────┐
             │    Network    │
             │    Scanning   │
             └───────┬───────┘
                     ↓
             ┌───────────────┐
             │ Device Results│
             └───────┬───────┘
                     ↓
        ┌────────────┼────────────┐
        ↓            ↓            ↓
   Risk Analysis  Port Scan   Topology
        │            │            │
        └────────────┼────────────┘
                     ↓
             ┌───────────────┐
             │ Export Results│
             │   to CSV      │
             └───────────────┘
```

---

## 📊 Example Device Information

The dashboard displays information in the following format:

```text
IP Address     MAC Address       Hostname       Vendor       Status       Risk
192.168.x.x    XX:XX:XX:XX       Device         Vendor       Online       Low
```

The actual values depend on the devices detected during the scan.

---

## 🧠 Cybersecurity Concepts Demonstrated

This project demonstrates practical understanding of:

* Network reconnaissance
* Local network discovery
* IP addresses
* MAC addresses
* Hostnames
* Network vendors
* Port scanning
* Common network services
* Device monitoring
* Risk scoring
* Network topology
* Security automation
* CSV-based security reporting

---

## 🎯 SOC Analyst Relevance

This project can demonstrate several skills relevant to an entry-level SOC environment:

### Network Visibility

Identifying devices and their network information.

### Security Monitoring

Comparing current devices with previously observed devices to identify newly detected and offline devices.

### Risk Identification

Assigning risk levels based on exposed services and device information.

### Investigation

Selecting a device and performing additional port scanning.

### Reporting

Exporting scan results into CSV format for further analysis.

---

## 📸 Screenshots

Add your actual application screenshots here:

```text
screenshots/
├── login.png
├── dashboard.png
├── network-scan.png
├── port-scan.png
└── topology.png
```

Example:

```markdown
![Advanced Network Scanner](screenshots/dashboard.png)
```

---

## ⚠️ Ethical Use

This project is intended for:

* Cybersecurity education
* Personal labs
* Authorized network testing
* Networks and devices that you own
* Security research with explicit permission

**Do not scan networks or systems without authorization.**

---

## 🔮 Future Enhancements

Potential improvements include:

* [ ] Advanced service/version detection
* [ ] Operating system detection
* [ ] Vulnerability scanning
* [ ] Threat intelligence integration
* [ ] Historical scan database
* [ ] Security report generation
* [ ] Real-time alerts
* [ ] SIEM integration
* [ ] Advanced network anomaly detection
* [ ] Improved topology visualization

---

## 👨‍💻 Developer

**Vijay Kumaresan**

Cybersecurity Enthusiast | Aspiring SOC Analyst

### Areas of Interest

* Security Operations
* Network Security
* Threat Detection
* Log Analysis
* Incident Investigation
* Cybersecurity Automation

---

