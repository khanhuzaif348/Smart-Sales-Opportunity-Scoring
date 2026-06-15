# Smart-Sales-Opportunity-Scoring

## Overview

Smart-Sales-Opportunity-Scoring is a Machine Learning-powered application designed to help sales teams identify and prioritize high-quality sales opportunities. By analyzing lead attributes such as source, sales agent, location, and delivery mode, the system predicts the likelihood of successful lead conversion and supports data-driven decision-making.

## Features

* Upload and analyze sales lead datasets
* Automated data preprocessing
* Lead quality prediction using Machine Learning
* Interactive Streamlit dashboard
* Real-time opportunity scoring
* Download prediction results as CSV
* User-friendly interface

## Dataset Features

The model uses the following features:

* Created
* Product_ID
* Source
* Mobile
* Email
* Sales_Agent
* Location
* Delivery_Mode
* Status

## Tech Stack

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Joblib/Pickle

## Project Structure

```text
Smart-Sales-Opportunity-Scoring/
│
├── app.py
├── model.pkl
├── requirements.txt
├── dataset.csv
├── README.md
│
├── notebooks/
│   └── model_training.ipynb
```

## Installation

### Clone Repository

```bash
git clone https://github.com/khanhuzaif348/Smart-Sales-Opportunity-Scoring.git
cd Smart-Sales-Opportunity-Scoring
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Model Training
5. Model Evaluation
6. Lead Opportunity Prediction
7. Visualization & Reporting

## Model Performance

Evaluation Metrics:

* Accuracy
* Precision
* Recall
* F1 Score

## Business Benefits

* Prioritize high-value opportunities
* Improve sales efficiency
* Reduce manual lead screening
* Increase conversion rates
* Enable data-driven sales strategies

## Future Enhancements

* Lead conversion probability scoring
* Power BI integration
* CRM integration
* Real-time API deployment
* Automated lead recommendations
* Advanced analytics dashboard

## Author

Huzaif Khan

* GitHub: https://github.com/khanhuzaif348
* Email: [khanhuzaif348@gmail.com](mailto:khanhuzaif348@gmail.com)

## License

This project is licensed under the MIT License.
