## 🚗 Car Price Prediction using Machine Learning

This project focuses on analyzing car features and building machine learning models to predict car prices. It includes data cleaning, exploratory data analysis (EDA), feature engineering, model building, and deployment using Streamlit.
---

## 📁 Project Structure

```
car-price-prediction/
│
├── app/
│ └── app.py
│
├── data/
│ ├── raw/ (5 original datasets + 1 sample dataset)
│ └── processed/
│
├── models/
├── notebooks/
│ ├── car_data.ipynb
│ └── creating_sample_data.ipynb
│
├── screenshots/
├── requirements.txt
└── .gitignore
```

## ⚙️ How to Run the Project

- Clone the repository

git clone https://github.com/debadritahalder/car-price-prediction.git

- Open the project folder

cd car-price-prediction

code .


- Install dependencies

pip install -r requirements.txt

- Run the notebook

Open
 **notebooks/car_data.ipynb** 
and run all cells

- Run the Streamlit app

streamlit run app/app.py

## 📊 Dataset Note

Source: Kaggle (multi-table dataset)

Due to GitHub file size limits, one large dataset has been replaced with a sample version

The project still runs fully using the sample dataset

Because of this, outputs (plots, model scores, predictions) may differ from the original full-data results

## 📈 Features of the Project

Data cleaning and preprocessing using Pandas

Exploratory Data Analysis (EDA) with visualizations

Feature engineering and selection

Model building using Ridge Regression and XGBoost

Model comparison and evaluation

Interactive prediction app using Streamlit

## 📈 Key Insights

- A negative trade-off is observed between top speed and fuel efficiency: faster cars tend to have lower average MPG.
- Luxury car makers rely on high margins per car, while mass-market makers leverage high volume to maximize total revenue.
- Car pricing is more strongly determined by quantitative performance and pricing metrics than by categorical attributes.
- The model highlights which features most influence price, giving actionable insights for buyers and sellers.

## 📌 Notes

All file paths are relative for easy reproducibility

Output folders such as models/ and screenshots/ are generated automatically when the notebook or app is executed

The project runs completely using the provided sample dataset

## 🚀 Future Improvements

Hyperparameter tuning for improved model performance

Deployment to cloud platforms (Streamlit Cloud / AWS)

Inclusion of additional real-world features (engine specs, safety rating, etc.)
