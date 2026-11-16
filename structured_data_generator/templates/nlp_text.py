import random
import math
import statistics
import time

from structured_data_generator.templates.base import fake

NLP_TEXT_TEMPLATE = {
    "template_name": "nlp_text_template",

    "subcategories": {

        # 1. Basic Text
        "Basic Text": {
            "Sentence": lambda: fake.sentence(),
            "Short Paragraph": lambda: fake.paragraph(nb_sentences=3),
            "Long Paragraph": lambda: fake.paragraph(nb_sentences=7),
            "Word": lambda: fake.word(),
            "Keywords": lambda: ", ".join(fake.words(nb=5))
        },

        # 2. Document Metadata
        "Document Metadata": {
            "Title": lambda: fake.sentence(nb_words=4),
            "Author": lambda: fake.name(),
            "Published Year": lambda: fake.year(),
            "Document Type": lambda: ["Article", "Blog", "Research Paper", "Report", "Review", "Story"]
                                    [math.floor(random.uniform(0, 5.99))]
        },

        # 3. NLP Annotations
        "NLP Annotations": {
            "Language": lambda: random.choice(["en", "hi", "ta", "fr", "es"]),
            "Sentiment": lambda: random.choice(["Positive", "Negative", "Neutral"]),
            "Emotion": lambda: random.choice(["Joy", "Anger", "Sadness", "Fear", "Neutral"]),
            "Toxicity Flag": lambda: fake.boolean(),
            "Reading Level": lambda: random.choice(["Easy", "Moderate", "Complex"])
        },

        # 4. Synthetic NER Data
        "Synthetic NER Data": {
            "Person Name": lambda: fake.name(),
            "Location Name": lambda: fake.city(),
            "Organization": lambda: fake.company(),
            "Misc Entity": lambda: random.choice(["COVID-19", "AI", "Climate", "Blockchain", "Quantum"])
        },

        # 5. Text Stats
        "Text Stats": {
            "Word Count": lambda: math.ceil(math.sqrt(fake.random_int(20, 900))),
            "Char Count": lambda: fake.random_int(50, 1200),
            "Average Word Length": lambda: round(
                statistics.mean([random.uniform(3.0, 8.0) for _ in range(5)]), 2
            ),

            "Unique Words": lambda: fake.random_int(5, 80)
        },

        # 6. Timestamp Info
        "Timestamp Info": {
            "Created At": lambda: f"UNIX-{math.floor(time.time())}",
            "Updated At": lambda: fake.iso8601()
        }
    }
}
