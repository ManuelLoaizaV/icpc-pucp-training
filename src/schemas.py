from enum import StrEnum

from pydantic import BaseModel, HttpUrl, field_validator


class Difficulty(StrEnum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    INSANE = "insane"


class Judge(StrEnum):
    CODEFORCES = "codeforces"
    ATCODER = "atcoder"
    KATTIS = "kattis"
    CSES = "cses"
    USACO = "usaco"
    HACKERRANK = "hackerrank"
    SPOJ = "spoj"
    YOSUPO = "yosupo"
    DMOJ = "dmoj"
    LEETCODE = "leetcode"


class LectureTag(StrEnum):
    CPP = "c++"
    BOOLEAN_EXPR = "if-else"
    LOOPS = "for-while"
    ARRAYS = "arrays"
    STRINGS = "strings"
    STL_SEQUENCE = "stl-sequence"
    STL_ALGORITHMS = "stl-algorithms"
    STL_ASSOCIATIVE = "stl-associative"
    RECURSION = "recursion"
    BRUTE_FORCE = "brute-force"
    COMPLETE_SEARCH = "complete-search"
    BINARY_SEARCH = "binary-search"
    DIVIDE_AND_CONQUER = "divide-and-conquer"
    CONSTRUCTIVE = "constructive"
    INTERACTIVE = "interactive"
    DP = "dp"
    SIEVE = "sieve"
    SPARSE_TABLE = "sparse-table"
    BIPARTITE_GRAPH = "bipartite-graph"


class Problem(BaseModel):
    name: str
    url: HttpUrl
    judge: Judge
    difficulty: Difficulty
    lectures: list[LectureTag]
    must_solve: bool = False
    comment: str = ""

    @field_validator("lectures", mode="before")
    @classmethod
    def parse_lectures(cls, value):
        if isinstance(value, str):
            return [LectureTag(tag.strip()) for tag in value.split("|") if tag.strip()]
        return value
