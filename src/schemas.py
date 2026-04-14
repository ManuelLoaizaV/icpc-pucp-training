from enum import StrEnum

from pydantic import BaseModel, HttpUrl, field_validator


class Difficulty(StrEnum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class Judge(StrEnum):
    CODEFORCES = "codeforces"
    ATCODER = "atcoder"
    KATTIS = "kattis"
    CSES = "cses"
    USACO = "usaco"
    HACKERRANK = "hackerrank"


class LectureTag(StrEnum):
    CPP = "c++"
    BOOLEAN_EXPR = "if-else"
    LOOPS = "for-while"
    ARRAYS = "arrays"
    STRINGS = "strings"
    RECURSION = "recursion"
    BINARY_SEARCH = "binary-search"
    STL = "stl"
    BRUTE_FORCE = "brute-force"
    BACKTRACKING = "backtracking"
    DIVIDE_AND_CONQUER = "divide-and-conquer"
    INTERACTIVE = "interactive"


class Problem(BaseModel):
    name: str
    url: HttpUrl
    judge: Judge
    difficulty: Difficulty
    lectures: list[LectureTag]

    @field_validator("lectures", mode="before")
    @classmethod
    def parse_lectures(cls, value):
        if isinstance(value, str):
            return [LectureTag(tag.strip()) for tag in value.split("|") if tag.strip()]
        return value
