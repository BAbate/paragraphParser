import re

disease_categories = {
    "cancer": "cancer",
    "heart disease": "cardiovascular",
    "diabetes": "metabolic",
    "asthma": "respiratory",
    "Alzheimer's": "neurological"
}


def categorize_paragraph(paragraph):
    for disease, category in disease_categories.items():
        if re.search(disease, paragraph, re.IGNORECASE):
            return category
    return "other"

with open("paragraphs.txt") as f:
    paragraphs = f.read().split("\n")

    for i, paragraph in enumerate(paragraphs):
        category = categorize_paragraph(paragraph)
        print(f"Paragraph {i+1}: {category}")