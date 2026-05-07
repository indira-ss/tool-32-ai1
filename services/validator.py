import re


def validate_text(text):

    # Check if text exists
    if not text:
        return False, "text is required"

    # Remove extra spaces
    text = text.strip()

    # Check empty text
    if len(text) == 0:
        return False, "text cannot be empty"

    # Limit input size
    if len(text) > 500:
        return False, "text too long"

    # Basic sanitization
    cleaned_text = re.sub(r"[<>]", "", text)

    return True, cleaned_texts