import re

# Masking function for personal information
def mask_pii(email_text: str):
    # Regular expressions for different PII entities
    pii_patterns = {
        "full_name": r"\b([A-Z][a-z]*\s[A-Z][a-z]*)\b",
        "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b",
        "phone_number": r"\b\d{10}\b",
        "dob": r"\b\d{2}/\d{2}/\d{4}\b",
        "aadhar_num": r"\b\d{12}\b",
        "credit_debit_no": r"\b\d{16}\b",
        "cvv_no": r"\b\d{3}\b",
        "expiry_no": r"\b\d{4}/\d{2}\b",
    }

    masked_email = email_text
    entities = []

    for entity, pattern in pii_patterns.items():
        matches = list(re.finditer(pattern, email_text))
        for match in matches:
            start, end = match.span()
            original_entity = match.group(0)
            entities.append({
                "position": [start, end],
                "classification": entity,
                "entity": original_entity
            })

    # Sort entities by start index in reverse to avoid index shift
    entities_sorted = sorted(entities, key=lambda x: x["position"][0], reverse=True)

    for ent in entities_sorted:
        start, end = ent["position"]
        label = f"[{ent['classification']}]"
        masked_email = masked_email[:start] + label + masked_email[end:]

    return masked_email, entities
