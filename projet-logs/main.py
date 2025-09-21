import re
from collections import Counter

with open("app.log", "r") as f:
    logs = f.readlines()

errors = []
for line in logs:
    match = re.search(r"ERROR (\w+)", line)
    if match:
        errors.append(match.group(1))

print("Résumé des erreurs :", Counter(errors))
