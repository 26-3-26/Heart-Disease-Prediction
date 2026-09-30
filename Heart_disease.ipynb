import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

# 1. Understanding and Loading Data

df = pd.read_csv('heart.csv')

# 2. Data Preprocessing
# التعامل مع القيم المفقودة 

df.dropna(inplace=True)


X = df.drop('HeartDisease', axis=1) 
y = df['HeartDisease']

# ترميز المتغيرات الفئوية (Categorical Variables) إن وجدت
X = pd.get_dummies(X, drop_first=True)

# تقسيم البيانات إلى تدريب واختبار
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# توحيد مقياس الميزات (Scaling)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 3. Model Implementation
# النموذج الأول: الانحدار اللوجستي (Logistic Regression)
log_model = LogisticRegression()
log_model.fit(X_train, y_train)
log_preds = log_model.predict(X_test)

# النموذج الثاني: الغابة العشوائية (Random Forest)
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_preds = rf_model.predict(X_test)

# 4. Evaluation and Comparison
print("--- Logistic Regression Results ---")
print("Accuracy:", accuracy_score(y_test, log_preds))
print("F1 Score:", f1_score(y_test, log_preds))

print("\n--- Random Forest Results ---")
print("Accuracy:", accuracy_score(y_test, rf_preds))
print("F1 Score:", f1_score(y_test, rf_preds))
