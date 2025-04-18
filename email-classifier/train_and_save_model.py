import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Load the CSV file from the Downloads folder
df = pd.read_csv(r"C:/Users/veera/Downloads/combined_emails_with_natural_pii.csv")

# Print the column names to check if 'email' and 'type' exist
print(df.columns)

# Strip any extra spaces from the column names (if any)
df.columns = df.columns.str.strip()

# Rename columns to match expected names ('email_text' and 'label')
df = df.rename(columns={"email": "email_text", "type": "label"})

# Print the column names after renaming to verify
print("Columns after renaming:", df.columns)

# Check if the necessary columns exist after renaming
if "email_text" in df.columns and "label" in df.columns:
    # Drop rows with missing values in 'email_text' or 'label' columns
    df = df.dropna(subset=["email_text", "label"])
else:
    print("Required columns are missing.")
    # Exit the script if the necessary columns are not found
    exit()

# Split data
X = df["email_text"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a pipeline (TF-IDF + Classifier)
model = make_pipeline(TfidfVectorizer(), LogisticRegression(max_iter=1000))

# Train the model
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "email_classifier_model.pkl")
print("✅ Model trained and saved as 'email_classifier_model.pkl'")
