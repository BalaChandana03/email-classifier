from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from utils import mask_pii

# Initialize FastAPI app
app = FastAPI()

# Load the trained model
model = joblib.load(r"C:\Users\veera\email-classifier\email_classifier_model.pkl")

# Define the input model for the email body
class EmailInput(BaseModel):
    email_body: str

# API endpoint for email classification
@app.post("/classify_email/")
def classify_email(data: EmailInput):
    # Original email body
    original_email = data.email_body

    # Mask PII in the email body
    masked_email, entity_list = mask_pii(original_email)

    # Predict the category using the pre-trained model
    category = model.predict([masked_email])[0]

    # Return the result with masked email and predicted category in the required format
    return {
        "input_email_body": original_email,
        "list_of_masked_entities": entity_list,
        "masked_email": masked_email,
        "category_of_the_email": category
    }
