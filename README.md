# Data Insights Dashboard 📊

An interactive web dashboard built using **Flask**, **Pandas**, and **Matplotlib** that allows users to upload CSV files, preview the data, generate dynamic charts (Bar & Pie), and gain quick statistical insights.

---

## 🚀 Features

- Upload any CSV file
- Automatically detect column names
- Choose columns to visualize
- Bar chart and Pie chart support
- Summary statistics (Min, Max, Mean, Std)
- Preview first 10 rows of data

---

## 📂 Folder Structure
data-insights-dashboard/ │ ├── app.py # Main Flask application ├── uploads/ # Stores uploaded CSV files ├── static/ │ └── chart.png # Generated chart image └── templates/ └── index.html # Web frontend


---

## 📦 Requirements

- Python 3.7+
- Flask
- Pandas
- Matplotlib

Install dependencies:

```bash
pip install flask pandas matplotlib

