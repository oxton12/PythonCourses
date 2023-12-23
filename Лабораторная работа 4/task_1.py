# TODO решите задачу
import json


INPUT_FILE = "input.json"


def task() -> float:
    with open(INPUT_FILE) as f:
        data = json.load(f)

    weighted_score = sum(line["score"] * line["weight"] for line in data)
    return round(weighted_score, 3)


print(task())
