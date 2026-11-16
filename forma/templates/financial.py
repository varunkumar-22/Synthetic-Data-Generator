import random
import math
import statistics

from forma.templates.base import fake

FINANCIAL_TEMPLATE = {
    "template_name": "financial_banking_transaction_template",

    "subcategories": {

        # 1. Account Information
        "Account Info": {
            "Account ID": lambda: fake.uuid4(),
            "Account Type": lambda: random.choice(["Savings", "Current", "Salary", "NRE", "NRO", "Fixed Deposit"]),
            "Bank Name": lambda: random.choice([
                "HDFC Bank", "ICICI Bank", "SBI", "Axis Bank", "Kotak Mahindra Bank",
                "Yes Bank", "Punjab National Bank", "Bank of Baroda"
            ]),
            "Branch": lambda: fake.city(),
            "IFSC Code": lambda: "BANK" + str(int(math.fabs(random.randint(10000, 99999)))),
            "Account Holder Name": lambda: fake.name()
        },

        # 2. Transaction Details
        "Transaction Info": {
            "Transaction ID": lambda: fake.uuid4(),
            "Transaction Date": lambda: fake.iso8601(),

            "Transaction Type": lambda: random.choice([
                "Deposit", "Withdrawal", "Online Transfer", "UPI Payment", "Card Payment",
                "Loan EMI", "Interest Credit", "Service Charge"
            ]),
            "Amount": lambda: math.floor(random.uniform(100, 200000) * 100) / 100,

            "Currency": lambda: random.choice(["INR", "USD", "EUR"]),
            "Transaction Status": lambda: random.choice(["Success", "Pending", "Failed"])
        },

        # 3. Customer Information
        "Customer Info": {
            "Customer ID": lambda: fake.uuid4(),
            "Customer Name": lambda: fake.name(),
            "Email": lambda: fake.email(),
            "Phone Number": lambda: fake.phone_number(),
            "PAN Number": lambda: "".join([chr(random.randint(65, 90)) for _ in range(5)]) +
                                  str(statistics.mean([random.randint(1000, 9999), random.randint(1000, 9999)])).split(".")[0] +
                                  chr(random.randint(65, 90)),

            "Aadhaar Last4": lambda: random.randint(1000, 9999)
        },

        # 4. Card Details 
        "Card Info": {
            "Card Type": lambda: random.choice(["Debit Card", "Credit Card", "Prepaid Card"]),
            "Card Network": lambda: random.choice(["Visa", "Mastercard", "RuPay", "American Express"]),
            "Card Last4": lambda: random.randint(1000, 9999),
            "Card Issuer Bank": lambda: random.choice([
                "SBI", "HDFC", "ICICI", "Axis Bank", "Kotak", "Punjab National Bank"
            ])
        },

        # 5. Loan Details 
        "Loan Info": {
            "Loan ID": lambda: fake.uuid4(),
            "Loan Type": lambda: random.choice(["Home Loan", "Personal Loan", "Car Loan", "Education Loan"]),
            "Loan Amount": lambda: round(random.uniform(50000, 2500000), 2),
            "Interest Rate": lambda: round(random.uniform(6.5, 14.0), 2),
            "EMI Amount": lambda: math.ceil(random.uniform(2000, 50000))
        },

        # 6. Device Information
        "Device Info": {
            "Device Type": lambda: random.choice(["mobile", "desktop", "tablet"]),
            "OS": lambda: random.choice(["Android", "iOS", "Windows", "MacOS", "Linux"]),
            "Browser": lambda: random.choice(["Chrome", "Safari", "Firefox", "Edge"])
        }
    }
}
