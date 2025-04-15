class Score:
    def __init__(self, subject, marks):
        self.subject = subject
        self.marks = marks


class Student:
    def __init__(self, name, subjects, marks):
        self.name = name
        self.scores = [Score(sub, mark) for sub, mark in zip(subjects, marks)]

    def __str__(self):
        result = f"Student {self.name} has the following scores:\n"
        for score in self.scores:
            result += f"{score.subject}: {score.marks}\n"
        return result.strip()

    def average(self):
        if not self.scores:
            return 0
        total = sum(score.marks for score in self.scores)
        return total / len(self.scores)


def classAverage(students):
    subject_data = {}

    for student in students:
        for score in student.scores:
            if score.subject not in subject_data:
                subject_data[score.subject] = []
            subject_data[score.subject].append(score.marks)

    result = []
    for subject in sorted(subject_data.keys()):
        avg = round(sum(subject_data[subject]) / len(subject_data[subject]))
        result.append(f"{subject}:{avg}")

    return result

s1 = Student('X', ['C1', 'C2', 'C3', 'C4'], [10, 20, 30, 80])
s2 = Student('Y', ['C1', 'C2'], [40, 50])
s3 = Student('Z', ['C2', 'C3'], [60, 70])

print(s1)
print(s1.average())
print(classAverage([s1, s2, s3]))