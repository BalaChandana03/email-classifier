# Email Classification API

This project implements an email classification system that:
- Masks personally identifiable information (PII)
- Classifies the email into support categories
- Returns a JSON with masked/unmasked text and category

## 🚀 Run Locally

### 1. Install Requirements
pip install -r requirements.txt
---

# Email Classifier with PII Masking

## Project Description

This project implements an **Email Classification System** that classifies customer support emails into different categories like **Billing Issues**, **Technical Support**, and **Account Management**. A key feature of the system is the **Personal Information (PII) Masking**, which ensures sensitive data such as names, email addresses, phone numbers, and other personal information is masked for privacy and compliance before processing. This is done using regular expressions to identify and mask the PII entities.

### Key Features:
- **PII Masking**: Masks personal information such as names, emails, phone numbers, etc.
- **Email Classification**: Categorizes emails into predefined categories based on their content.
- **API Integration**: Provides an API for integrating the email classification and PII masking system.
  
## Installation Instructions

Follow these steps to set up the project locally:

### 1. Clone the repository

Clone the repository from GitHub to your local machine.

git clone https://github.com/BalaChandana03/email-classifier.git
```

### 2. Navigate to the project directory

cd email-classifier
```

### 3. Set up a Virtual Environment (Optional but recommended)

To avoid conflicts with global dependencies, it is recommended to set up a virtual environment.

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

If you're using an `environment.yml` file, use the following command:

```bash
conda env create -f environment.yml
```

### 5. Verify installation

After installing the dependencies, verify everything is set up correctly by running the application.

---

## Usage Instructions

To run the email classification system:

### 1. Run the API

Run the FastAPI app to start the server.

```bash
uvicorn app:app --reload
```

This will start the FastAPI development server at `http://127.0.0.1:8000`.

### 2. Testing the API

Use any HTTP client (e.g., **Postman**, **Curl**, **Python Requests**) to interact with the API.

- **API Endpoint:** `/classify_email/`
- **Method:** `POST`
- **Request Format:**
    - `email_body` (string): The content of the email to be classified and have its PII masked.

Example Request:
```json
{
  "email_body": "My name is John Doe, and my email is johndoe@example.com. My phone number is 1234567890."
}
```

### Example Response:
```json
{
  "input_email_body": "My name is John Doe, and my email is johndoe@example.com. My phone number is 1234567890.",
  "list_of_masked_entities": [
    {
      "position": [11, 19],
      "classification": "full_name",
      "entity": "John Doe"
    },
    {
      "position": [37, 56],
      "classification": "email",
      "entity": "johndoe@example.com"
    },
    {
      "position": [77, 87],
      "classification": "phone_number",
      "entity": "1234567890"
    }
  ],
  "masked_email": "My name is [full_name], and my email [email]com. My phone number is 123456789[phone_number]",
  "category_of_the_email": "Incident"
}
```

---

## Dependencies

This project requires the following dependencies:

- **FastAPI**: For building the API
- **Uvicorn**: For running the FastAPI application
- **scikit-learn**: For machine learning classification
- **pandas**: For data manipulation
- **numpy**: For numerical operations
- **re (regex)**: For personal information masking
- **pytest**: For unit testing

Install all dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes:

```
fastapi
uvicorn
scikit-learn
pandas
numpy
pytest
```

---

## How to Run the Project

To run the entire email classifier and PII masking project:

1. **Set up the environment and install dependencies.**
2. **Run the FastAPI app using `uvicorn`.**
    - In the project directory, run:
    ```bash
    uvicorn app:app --reload
    ```

3. **Test the API.**
    - Send a POST request to the `/classify_email/` endpoint with an email body.

---

## Additional Information

- **Model used**: The system uses a **Random Forest Classifier** trained on labeled email data for classification.
- **PII masking method**: Personal information is masked using **regex patterns** for different types of entities (e.g., names, emails, phone numbers).
- **Supported Entities**:
  - Full name
  - Email address
  - Phone number
  - Date of birth
  - Aadhar number
  - Credit/Debit card number
  - CVV number
  - Expiry date
 
  Output:
![Screenshot (154)](https://github.com/user-attachments/assets/7bc1a370-f575-4824-b76f-ebaa5500ef40)
![Screenshot (155)](https://github.com/user-attachments/assets/626d0937-354f-485b-b027-079afeaaedee)
![Screenshot (156)](https://github.com/user-attachments/assets/60cda50f-a19e-4481-9b57-5cb8e8a95ce0)
![Screenshot (157)](https://github.com/user-attachments/assets/74162c4a-58f2-4c97-bdc8-2b1b214027e4)
![Screenshot (158)](https://github.com/user-attachments/assets/cbbb9691-69a0-4c1b-aaaa-adaa2e079145)
![Screenshot (159)](https://github.com/user-attachments/assets/2686d617-2b74-44c1-88c4-fca4897319cd)
![Screenshot (160)](https://github.com/user-attachments/assets/e650586d-7e90-42cf-971e-318287e7926e)
---![Screenshot (161)](https://github.com/user-attachments/assets/d2ac8cce-5e00-4a58-82b8-e22eb4cf247a)



