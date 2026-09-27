# Heart Disease Prediction

Predicts heart disease risk from patient clinical data using Machine Learning (Logistic Regression & Random Forest).

---

## Overview
A machine learning classification project that predicts the presence of heart disease from clinical patient measurements. Built using Python and `scikit-learn`, this project compares **Logistic Regression** and **Random Forest** algorithms to evaluate baseline performance against an ensemble approach.

## Problem Statement
Cardiovascular disease is a leading cause of global mortality. Early, algorithmic risk prediction using routine clinical indicators—such as age, cholesterol levels, chest pain type, and maximum heart rate—can assist clinicians in identifying high-risk patients earlier. 

This project frames the task as a binary classification problem:
* **`0`**: No heart disease detected
* **`1`**: Heart disease detected

## Methodology & Approach

1. **Data Acquisition:** Used the **Heart Failure Prediction Dataset** from Kaggle, containing 918 patient records across 11 clinical features.
2. **Data Cleaning:** Verified data integrity, checked for missing values, and confirmed feature types.
3. **Categorical Encoding:** Applied One-Hot Encoding (`pd.get_dummies`) to convert categorical variables (such as sex, chest pain type, resting ECG, and ST slope) into numeric representation.
4. **Train/Test Split:** Partitioned the dataset into 80% training and 20% testing sets using `random_state=42` to ensure reproducible results.
5. **Feature Scaling:** Applied `StandardScaler` to normalize numerical features with varying scales (e.g., age vs. serum cholesterol in mg/dl).
6. **Model Training & Comparison:**
   * **Logistic Regression:** Trained as an interpretable baseline model.
   * **Random Forest Classifier:** Trained as a non-linear ensemble model to capture complex feature interactions and reduce variance.
7. **Evaluation:** Evaluated model performance on the held-out test set using **Accuracy** and **F1 Score** to balance precision and recall.

## Tech Stack
* **Language:** Python 3.x
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** scikit-learn (`LogisticRegression`, `RandomForestClassifier`, `StandardScaler`, `train_test_split`)
* **Environment:** Jupyter Notebook

## Results & Performance

| Model | Accuracy | F1 Score |
|---|---|---|
| Logistic Regression | 85.3% | 87.0% |
| **Random Forest** | **87.5%** | **89.2%** |

![Model comparison: Random Forest vs Logistic Regression on Accuracy and F1](assets/results-chart.png)

### Key Insights
* **Best Performing Model:** Random Forest outperformed Logistic Regression across both metrics (**87.5% Accuracy** and **89.2% F1 Score**), demonstrating the value of modeling non-linear relationships among clinical features.
* **Dataset Size:** 918 patient observations with 11 core clinical features.
* **Top Predictive Features:** Feature importance analysis revealed that **ST_Slope**, **ChestPainType**, and **ExerciseAngina** were the strongest drivers of heart disease risk predictions.
* **Project Limitation:** The model relies strictly on available clinical attributes. Real-world medical deployment would require broader historical, genetic, and lifestyle factors to maximize generalizability.

## Installation & Setup

### Prerequisites
Ensure you have Python installed on your system.

### 1. Clone the Repository
```bash
git clone https://github.com/26-3-26/heart-disease-prediction.git
cd heart-disease-prediction
