class School:
    def __init__(self):
        self.s = {}

    def add_student(self, name, grade):
        self.s[name]= grade

    def roster(self):
        grade = set(self.s.values())
        r = []
        for g in grade:
            r += self.grade(g)
        return r

    def grade(self, grade_number):
        return sorted([s for s, g in self.s.items() if g == grade_number])
