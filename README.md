

### 📘 README.md

```markdown
# 📊 Credit Risk Scoring App

This Streamlit web application allows you to upload a credit-related dataset and visualize the risk scoring based on various features like income, education, loan term, overdue days, etc. It uses a Random Forest model to estimate the **Probability of Default (PDN)**.

---

## 📂 Project Structure

```

credit\_risk\_streamlit\_app/
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

```

---

## ⚙️ Setup Instructions

### 1. Clone or Download the Repository

```

git clone [https://github.com/yourusername/credit-risk-scoring-app.git](https://github.com/yourusername/credit-risk-scoring-app.git)
cd credit-risk-scoring-app

````

Or simply unzip the folder if you downloaded it as a ZIP.

---

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
````

---

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

### 4. Run the App

```bash
streamlit run app.py
```

This will launch the app in your default web browser.

---

## 📁 Dataset Format

Make sure your CSV file includes at least these fields:

* `PDN` (Probability of Default) — Target variable
* `Debt`, `Overdue Days`, `Initial Limit`, `BIRTHDATE`, `SEX`, `EDU`, `INCOME`, etc.

The app automatically:

* Calculates age from `BIRTHDATE`
* Encodes categorical variables
* Fills missing values
* Drops irrelevant columns like `CLIENTID`
* Trains a Random Forest model to predict `PDN`

---

## 📈 Output

The app displays:

* R² Score and RMSE for model evaluation
* Top 10 important features using bar charts

---

## 🛠 Tech Stack

* Python
* Streamlit
* pandas, scikit-learn, matplotlib

---

## 🧑‍💻 Author

Made by \[Your Name]

---

## 📃 License

MIT License

```

---


