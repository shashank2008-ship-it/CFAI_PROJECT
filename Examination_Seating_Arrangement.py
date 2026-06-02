from dataclasses import dataclass
from typing import List, Dict, Tuple


# =====================================================
# STUDENT CLASS
# =====================================================

@dataclass
class Student:
    roll_no: int
    name: str
    department: str


# =====================================================
# DFS EXAMINATION SEATING ARRANGEMENT
# =====================================================

class DFSSeatingArrangement:

    def __init__(self, students: List[Student], rows: int, cols: int):

        self.students = students
        self.rows = rows
        self.cols = cols

        self.seats = [
            (r, c)
            for r in range(rows)
            for c in range(cols)
        ]

        self.assignment: Dict[Tuple[int, int], Student] = {}

        # Short reasoning trace
        self.trace = []

    # -------------------------------------------------
    # Get Adjacent Seats
    # -------------------------------------------------

    def get_neighbors(self, seat):

        r, c = seat

        possible = [
            (r - 1, c),
            (r + 1, c),
            (r, c - 1),
            (r, c + 1)
        ]

        neighbors = []

        for nr, nc in possible:
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                neighbors.append((nr, nc))

        return neighbors

    # -------------------------------------------------
    # Constraint:
    # Same Department Students Should Not Sit Adjacent
    # -------------------------------------------------

    def is_valid(self, seat, student):

        for neighbor in self.get_neighbors(seat):

            if neighbor in self.assignment:

                other = self.assignment[neighbor]

                if student.department.lower() == other.department.lower():
                    return False

        return True

    # -------------------------------------------------
    # DFS + Backtracking
    # -------------------------------------------------

    def dfs(self, student_index):

        # Goal State
        if student_index == len(self.students):
            return True

        student = self.students[student_index]

        for seat in self.seats:

            if seat not in self.assignment:

                if self.is_valid(seat, student):

                    self.assignment[seat] = student

                    self.trace.append(
                        f"{student.name} -> Seat {seat}"
                    )

                    if self.dfs(student_index + 1):
                        return True

                    del self.assignment[seat]
                    self.trace.pop()

        return False

    # -------------------------------------------------
    # Solve
    # -------------------------------------------------

    def solve(self):
        return self.dfs(0)

    # -------------------------------------------------
    # Display Trace
    # -------------------------------------------------

    def display_trace(self):

        print("\nREASONING TRACE")
        print("-" * 30)

        for step in self.trace:
            print(step)

    # -------------------------------------------------
    # Display Seating Arrangement
    # -------------------------------------------------

    def display(self):

        print("\n")
        print("=" * 100)
        print("EXAMINATION SEATING ARRANGEMENT USING DFS")
        print("=" * 100)

        seat_no = 1

        for r in range(self.rows):

            for c in range(self.cols):

                seat = (r, c)

                if seat in self.assignment:

                    student = self.assignment[seat]

                    text = (
                        f"Seat-{seat_no} "
                        f"({student.roll_no}-{student.name})"
                    )

                else:

                    text = (
                        f"Seat-{seat_no} Empty"
                    )

                print(text.ljust(25), end="")

                seat_no += 1

            print("\n")


# =====================================================
# MAIN PROGRAM
# =====================================================

def main():

    print("\nAI Examination Seating Arrangement Using DFS\n")

    n = int(input("Enter Number of Students: "))

    students = []

    for i in range(n):

        print(f"\nStudent {i + 1}")

        roll = int(input("Roll Number: "))
        name = input("Name: ")
        dept = input("Department: ")

        students.append(
            Student(
                roll,
                name,
                dept
            )
        )

    rows = int(input("\nEnter Number of Rows: "))
    cols = int(input("Enter Number of Columns: "))

    if len(students) > rows * cols:

        print("\nNot enough seats available.")
        return

    seating = DFSSeatingArrangement(
        students,
        rows,
        cols
    )

    if seating.solve():

        seating.display_trace()
        seating.display()

    else:

        print("\nNo valid seating arrangement found.")


# =====================================================
# START PROGRAM
# =====================================================

if __name__ == "__main__":
    main()