import pickle
# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eBLyZmeI_FP0sj0N658AcJIvW_rQ2s05
"""

# app.py

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt

st.set_page_config(page_title="Credit Risk Scoring App", layout="wide")

st.title("📊 Credit Risk Scoring Dashboard")

# Step 1: Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])

if uploaded_file:
    # Step 2: Load dataset
    df = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.write(df.head())

    st.write("Shape:", df.shape)

    # Step 3: Preprocessing
    with st.spinner("Preprocessing data..."):
        if 'BIRTHDATE' in df.columns:
            df['BIRTHDATE'] = pd.to_datetime(df['BIRTHDATE'], errors='coerce')
            df['AGE'] = df['BIRTHDATE'].apply(lambda x: (pd.Timestamp.today() - x).days // 365 if pd.notnull(x) else np.nan)
            df.drop(columns=['BIRTHDATE'], inplace=True)

        if 'CLIENTID' in df.columns:
            df.drop(columns=['CLIENTID'], inplace=True)

        df.fillna(df.median(numeric_only=True), inplace=True)

        cat_cols = df.select_dtypes(include='object').columns.tolist()
        df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

        if 'PDN' not in df.columns:
            st.error("The dataset must contain a 'PDN' column for prediction.")
        else:
            X = df.drop(columns=['PDN'])
            y = df['PDN']

            # Step 4: Train/test split
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Step 5: Train model
            model = RandomForestRegressor(random_state=42)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            # Step 6: Evaluation
            st.subheader("📈 Model Evaluation")
            st.metric("R² Score", f"{r2_score(y_test, y_pred):.3f}")
            st.metric("RMSE", f"{np.sqrt(mean_squared_error(y_test, y_pred)):.3f}")

            # Step 7: Feature Importance
            st.subheader("🔍 Top 10 Feature Importances")
            importances = pd.Series(model.feature_importances_, index=X.columns)
            top_features = importances.sort_values(ascending=False).head(10)

            fig, ax = plt.subplots()
            top_features.plot(kind='barh', ax=ax)
            ax.set_title("Top 10 Important Features")
            ax.invert_yaxis()
            st.pyplot(fig)