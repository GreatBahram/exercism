class HighScores:
    def __init__(self, scores):
        self.scores = scores
        self.sorted_scores = sorted(scores, reverse=True)

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return self.sorted_scores[0]

    def personal_top(self):
        return self.sorted_scores[:3]

    def report(self):
        difference = self.personal_best() - self.latest()
        return "Your latest score was {}. That's {}your personal best!" \
                .format(self.latest(), f"{difference} short of " if difference else '')
