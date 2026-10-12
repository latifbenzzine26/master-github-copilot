# util_lib.py
import csv
import statistics


class DataTable:
    def __init__(self, data: list[list[str]]) -> None:
        self.data = data

    @classmethod
    def load(cls, path: str) -> "DataTable":
        with open(path) as f:
            return cls(list(csv.reader(f)))

    def mean(self, col_idx: int) -> float:
        return statistics.mean(float(row[col_idx]) for row in self.data)

    def stddev(self, col_idx: int) -> float:
        return statistics.stdev(float(row[col_idx]) for row in self.data)

    def save(self, path: str) -> None:
        with open(path, "w", newline="") as f:
            csv.writer(f).writerows(self.data)

