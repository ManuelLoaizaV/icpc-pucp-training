import argparse
import csv
import os
import random
from datetime import date

from schemas import Difficulty, LectureTag, Problem

DB_PATH = "data/problem_bank.csv"


def load_problems() -> list[Problem]:
    problems: list[Problem] = []
    try:
        with open(file=DB_PATH, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                problems.append(Problem(**row))
    except FileNotFoundError:
        print(f"Error: {DB_PATH} not found.")
    return problems


def append_to_timeline(
    year: int,
    lecture: str,
    easy: list[Problem],
    medium: list[Problem],
    hard: list[Problem],
):
    filename = f"data/timeline_{year}.csv"
    file_exists = os.path.isfile(filename)

    with open(filename, mode="a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(
                ["date", "lecture", "easy_problems", "medium_problems", "hard_problems"]
            )

        writer.writerow(
            [
                date.today().isoformat(),
                lecture,
                " | ".join([p.name for p in easy]),
                " | ".join([p.name for p in medium]),
                " | ".join([p.name for p in hard]),
            ]
        )


def generate_contest(args):
    total_requested = args.easy + args.medium + args.hard
    if total_requested == 0:
        print(
            "Error: A contest must have at least 1 problem. Please specify counts for EASY, MEDIUM, or HARD."
        )
        return

    problems = load_problems()

    try:
        lecture_enum = LectureTag(args.lecture)
    except ValueError:
        print(f"Error: '{args.lecture}' is not a valid LectureTag.")
        return

    eligible = [p for p in problems if lecture_enum in p.lectures]

    pool: dict[Difficulty, list[Problem]] = {
        Difficulty.EASY: [p for p in eligible if p.difficulty == Difficulty.EASY],
        Difficulty.MEDIUM: [p for p in eligible if p.difficulty == Difficulty.MEDIUM],
        Difficulty.HARD: [p for p in eligible if p.difficulty == Difficulty.HARD],
    }

    if (
        len(pool[Difficulty.EASY]) < args.easy
        or len(pool[Difficulty.MEDIUM]) < args.medium
        or len(pool[Difficulty.HARD]) < args.hard
    ):
        print("Error: Not enough problems in the bank for this configuration.")
        return

    selected_easy = random.sample(pool[Difficulty.EASY], args.easy)
    selected_medium = random.sample(pool[Difficulty.MEDIUM], args.medium)
    selected_hard = random.sample(pool[Difficulty.HARD], args.hard)

    append_to_timeline(args.year, args.lecture, selected_easy, selected_medium, selected_hard)

    print(f"Contest generated and saved to timeline_{args.year}.csv!")
    print("\n--- Contest Problem Set ---")
    for p in selected_easy + selected_medium + selected_hard:
        print(f"[{p.difficulty.value.upper()}] {p.name} - {p.url}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PUCP ICPC lectures and problem sets.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_gen = subparsers.add_parser("generate-contest")
    parser_gen.add_argument("--year", type=int, required=True)
    parser_gen.add_argument("--lecture", type=str, required=True)
    parser_gen.add_argument("--easy", type=int, default=0)
    parser_gen.add_argument("--medium", type=int, default=0)
    parser_gen.add_argument("--hard", type=int, default=0)

    parser_gen.set_defaults(func=generate_contest)

    args = parser.parse_args()
    args.func(args)
