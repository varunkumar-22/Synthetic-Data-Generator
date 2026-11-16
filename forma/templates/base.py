from faker import Faker

# One shared Faker instance so seeding works the same across every template
fake = Faker(locale="en_US")
