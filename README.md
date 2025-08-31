# 📌 Server Downtime Prediction Project

## 📖 Overview

This project predicts **server downtime** using synthetic data that mimics real-world server monitoring logs. It demonstrates a **full data science workflow** from dataset creation → cleaning → SQL analysis → exploratory data analysis (EDA) → machine learning → model deployment using **Streamlit**.

This project is ideal for showcasing **data science, machine learning, and deployment skills** on a resume or portfolio.

---
Live Project Link : https://server-downtime-prediction.streamlit.app/
---

## 🔧 Steps in the Project

### 1. Dataset

* Used **5,000 records** of server logs
* Introduced messy data: missing values, inconsistent formats, categorical noise, outliers

### 2. Data Cleaning & Preprocessing

* Removed duplicates
* Handled missing values
* Fixed wrong data types
* Standardized categorical values (`location`)
* Handled outliers (clipping, IQR method)
* Converted timestamps to proper datetime

### 3. SQL Analysis (MySQL)

* Stored dataset in MySQL database
* Wrote **6 SQL queries**:

  * Record counts
  * Avg CPU usage by location
  * Top 5 servers with highest downtime
  * CPU usage vs downtime
  * Network latency vs downtime
  * Most common location for downtime

### 4. Exploratory Data Analysis (Python)

* Used **Pandas, Matplotlib, Seaborn**
* 6 key EDA questions with plots:

  * Downtime distribution
  * CPU usage distribution
  * Downtime by location
  * Network latency vs downtime
  * Correlation heatmap
  * Average CPU usage by downtime

### 5. Machine Learning Pipeline

* **Preprocessing:** Label Encoding, StandardScaler
* **Classification Models:** Logistic Regression, Random Forest, SVM, Gradient Boosting
* **Regression Models:** Linear Regression, Random Forest Regressor
* **Clustering:** KMeans (Elbow Method for optimal k)
* **Hyperparameter Tuning:** GridSearchCV & RandomizedSearchCV

### 6. Model Evaluation

* **Classification:** Accuracy, Precision, Recall, F1, ROC-AUC + Cross-validation
* **Regression:** RMSE, MAE, R² + Cross-validation

### 7. Deployment (Streamlit)

* Saved best model with `joblib`
* Built **Streamlit app** for interactive prediction
* User inputs: CPU, Memory, Disk, Network Latency, Location
* Output: Predicted **Downtime Likelihood** with probability

---

## 📊 Example Use Case

A DevOps team can use this model to **predict server downtime risk** based on current system metrics, allowing proactive maintenance.

---

## 🚀 Future Improvements

* Extend with **time-series forecasting (LSTMs)**
* Add **alerting system** based on predictions

---

## ✨ Skills Demonstrated

* Data Cleaning & Preprocessing
* SQL + Python Integration
* Exploratory Data Analysis (EDA)
* Machine Learning (Classification, Regression, Clustering)
* Model Evaluation & Cross-validation
* Hyperparameter Tuning
* Model Deployment with Streamlit

---
