import random
import uuid

import pandas as pd
from faker import Faker


def generate_from_template(template, selected_subcats, count=1, seed=None):
    # seed
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)

    all_rows = []

    for _ in range(count):
        generated_data = {"id": str(uuid.uuid4())}  # internal only

        for subcat in selected_subcats:
            if subcat in template["subcategories"]:
                for field, fn in template["subcategories"][subcat].items():
                    generated_data[field] = fn()

        all_rows.append(generated_data)

    # Convert to DataFrame
    df = pd.DataFrame(all_rows)
    if "id" in df.columns:
        df = df.drop(columns=["id"])


    # Add sequential ID starting from 1
    df.insert(0, "S.no.", range(1, len(df) + 1))

    return df
