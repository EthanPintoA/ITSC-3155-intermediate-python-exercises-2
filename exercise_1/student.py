class Student:
    def __init__(self, name: str, gpa: float) -> None:
        self.name = name
        self.gpa = gpa

    def report_gpa(self) -> str:
        return f"{self.name} has a GPA of {self.gpa}"
