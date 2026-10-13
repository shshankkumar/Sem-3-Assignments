import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

with open(args.filename, "r") as file:
    courses = list(csv.DictReader(file))

print("All Course Records:")
for course in courses:
    print(course)

cid = input("Enter Course ID to search: ")
found = False

for course in courses:
    if course["Course ID"] == cid:
        print("Course Found:", course)
        found = True
        break

if not found:
    print("Course not found.")
