import faker
import csv

fake = faker.Faker("ro_RO")

with open("salarii.csv", "w") as fout:
    writer = csv.writer(fout)

    for i in range(45):
        writer.writerow(
            [
                fake.first_name(),
                fake.last_name(),
                fake.uuid4(),
                fake.pyint(min_value=1998, max_value=20000),
                fake.pyint(min_value=0, max_value=10),
            ]
        )