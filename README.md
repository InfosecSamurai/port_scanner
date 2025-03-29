# 🔍 Advanced Port Scanner

## 📖 Overview
The **Advanced Port Scanner** is a high-performance, multi-threaded port scanner with built-in service detection.  
It allows you to efficiently scan a target IP or hostname for open ports, helping you identify potential services running on a system.

## 🚀 Features
✅ Scan single ports or entire port ranges  
✅ Detect common services running on open ports  
✅ Multi-threaded scanning for faster results  
✅ Lightweight and easy to use  

---

## ⚙️ Usage

### 📥 Installation
Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/InfosecSamurai/port_scanner.git
cd port_scanner
```

### ▶️ Running the Scanner
To scan a target for open ports, use:
```bash
python main.py <target> <port or port-range>
```

#### 🔹 Example:
Scan ports **20-100** on `scanme.nmap.org`:
```bash
python main.py scanme.nmap.org 20-100
```

---

## 📜 License
This project is licensed under the **MIT License** – feel free to use, modify, and distribute it.  

🔹 _Developed by [InfosecSamurai](https://github.com/InfosecSamurai)_  
