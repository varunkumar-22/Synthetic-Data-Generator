import random
import uuid
import math
import statistics
import datetime

from forma.templates.base import fake

IMAGE_METADATA_TEMPLATE = {
    "Template Name": "image_metadata_template",

    "Subcategories": {

    #    1. Basic Info
        "Basic Info": {
            "Image Id": lambda: str(uuid.uuid4()),
            "File Name": lambda: fake.file_name(category="image"),
            "File Format": lambda: random.choice(["jpg", "jpeg", "png", "webp", "tiff"]),
            "File Size Kb": lambda: random.randint(50, 15000),  # 50 KB – 15 MB
            "Color Mode": lambda: random.choice(["RGB", "RGBA", "CMYK", "Grayscale"]),
            "Entropy Score": lambda: round(random.uniform(2.0, 7.5), 3)
        },

        # 2. Dimensions
        "Dimensions": {
            "Width Px": lambda: random.randint(256, 8000),
            "Height Px": lambda: random.randint(256, 8000),
            "Aspect Ratio": lambda: f"{random.choice([1,4,16,3])}:{random.choice([1,3,9,2])}",
            "Dpi": lambda: random.choice([72, 96, 150, 300]),
            "Clarity Score": lambda: round(math.sqrt(random.uniform(1, 100)), 2)
        },

        # 3. Camera Exif
        "Camera Exif": {
            "Camera Make": lambda: random.choice(["Canon", "Nikon", "Sony", "Fujifilm", "Apple", "Samsung"]),
            "Camera Model": lambda: fake.word(),
            "Lens Model": lambda: random.choice(["18-55mm", "24-70mm", "50mm", "70-200mm", None]),
            "Focal Length Mm": lambda: random.randint(10, 200),
            "Aperture": lambda: random.choice(["f/1.8", "f/2.0", "f/2.8", "f/4", "f/5.6"]),
            "Iso": lambda: random.choice([100, 200, 400, 800, 1600, 3200]),
            "Exposure Time": lambda: random.choice(["1/50", "1/100", "1/200", "1/500"]),
            "Noise Level": lambda: round(random.betavariate(2, 6), 3)
        },

        # 4. Geolocation
        "Geolocation": {
            "Latitude": lambda: float(fake.latitude()),
            "Longitude": lambda: float(fake.longitude()),
            "Country": lambda: fake.country(),
            "City": lambda: fake.city(),
            "Gps Accuracy Meters": lambda: random.randint(3, 100)
        },

        # 5. Tags Labels
        "Tags Labels": {
            "Primary Label": lambda: random.choice([
                "person", "animal", "landscape", "food", "vehicle", "object", "logo",
                "indoor", "outdoor", "nature", "architectural"
            ]),
            "Secondary Labels": lambda: ", ".join(fake.words(nb=3)),
            "Confidence Score": lambda: round(random.uniform(0.5, 1.0), 3),
            "Aesthetic Score": lambda: round(random.uniform(0.2, 0.99), 3)
        },

        # 6. Color Stats
        "Color Stats": {
            "Dominant Color": lambda: random.choice(["red", "blue", "green", "yellow", "white", "black", "orange"]),
            "Color Variance": lambda: round(
                statistics.mean([random.uniform(0.1, 1) for _ in range(5)]), 3
            ),
            "Brightness Level": lambda: round(random.uniform(0.1, 0.9), 3),
            "Contrast Ratio": lambda: round(random.uniform(1.0, 5.0), 2)
        },

        # 7. Timestamp Info
        "Timestamp Info": {
            "Created At": lambda: datetime.datetime.now().isoformat(),
            "Uploaded At": lambda: datetime.datetime.now().isoformat(),
            "Last Modified At": lambda: (
                datetime.datetime.now() - datetime.timedelta(
                    minutes=random.randint(1, 2000)
                )
            ).isoformat()
        }
    }
}
