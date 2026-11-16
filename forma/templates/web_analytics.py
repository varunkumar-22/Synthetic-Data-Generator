import random
import uuid
import math
import statistics
import datetime

from forma.templates.base import fake

WEB_ANALYTICS_TEMPLATE = {
    "Template Name": "web_analytics_template",

    "Subcategories": {

        # 1. Session Info
        "Session Info": {
            "Session Id": lambda: str(uuid.uuid4()),
            "User Id": lambda: fake.uuid4(),
            "Session Start": lambda: datetime.datetime.now().isoformat(),
            "Session End": lambda: (
                datetime.datetime.now() + datetime.timedelta(
                    seconds=random.randint(5, 3600)
                )
            ).isoformat(),
            "Session Duration Sec": lambda: random.randint(5, 3600),
            "Is New User": lambda: fake.boolean(),
            "Engagement Score": lambda: random.randint(1,10 ) ,
        },

        # 2. Page Metrics
        "Page Metrics": {
            "Page Url": lambda: fake.uri(),
            "Referrer Url": lambda: random.choice([fake.uri(), None]),
            "Page Title": lambda: fake.sentence(nb_words=4),
            "Time On Page Sec": lambda: random.randint(1, 900),
            "Scroll Depth Percent": lambda: random.randint(10, 100),
            "Interaction": lambda: random.choice(["click", "scroll", "hover", "input", "none"]),
            "Ctr": lambda: round(random.uniform(0.01, 0.4), 3),
            "Bounce Probability": lambda: random.uniform(0,1)
        },

        # 3. Traffic Source
        "Traffic Source": {
            "Source": lambda: random.choice(["Direct", "Organic", "Paid", "Referral", "Social"]),
            "Medium": lambda: random.choice(["none", "cpc", "email", "banner", "social"]),
            "Campaign": lambda: random.choice(["summer_sale", "new_launch", "retargeting", "none"]),
            "Keyword": lambda: random.choice([fake.word(), None]),
            "Traffic Quality": lambda: round(
                statistics.mean([random.random() for _ in range(3)]), 3
            )
        },

        # 4. Device Info
        "Device Info": {
            "Device Type": lambda: random.choice(["mobile", "desktop", "tablet"]),
            "Browser": lambda: random.choice(["Chrome", "Safari", "Firefox", "Edge"]),
            "Os": lambda: random.choice(["Windows", "MacOS", "Android", "iOS", "Linux"]),
            "Screen Resolution": lambda: random.choice([
                "1920x1080", "1366x768", "1536x864", "1280x720", "1440x900"
            ]),
            "Device Performance Score": lambda: round(
                math.sqrt(random.uniform(1, 100)), 2
            )
        },

        # 5. Geo Data
        "Geo Data": {
            "Ip Address": lambda: fake.ipv4_public(),
            "Country": lambda: fake.country(),
            "City": lambda: fake.city(),
            "Timezone": lambda: fake.timezone(),
            "Avg Network Latency Ms": lambda: random.randint(20, 300)
        },

        # 6. Performance
        "Performance": {
            "Page Load Time Ms": lambda: random.randint(200, 5000),
            "Dns Lookup Ms": lambda: random.randint(10, 300),
            "Ttfb Ms": lambda: random.randint(50, 1200),
            "Total Resources Loaded": lambda: random.randint(5, 100),
            "Js Errors": lambda: random.randint(0, 10),
            "Performance Score": lambda: round(random.uniform(40, 100), 2),
            "Avg Resource Size Kb": lambda: round(
                statistics.mean([random.randint(20, 500) for _ in range(5)]), 2
            )
        }
    }
}
