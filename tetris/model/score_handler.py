import json


class ScoreHandler:
    def __init__(self, filename):
        self.filename = filename
        self.last_score = 0
        self.record_score = 0
        self.load_scores()

    def load_scores(self):
        try:
            with open(self.filename, "r") as f:
                scores = json.load(f)
                self.last_score = scores["last_score"]
                self.record_score = scores["record_score"]
        except (IOError, KeyError, json.decoder.JSONDecodeError):
            self.last_score = 0
            self.record_score = 0

    def update_score(self, score):
        if score > self.record_score:
            self.record_score = score

        self.last_score = score
        self.__save_scores()

    def __save_scores(self):
        with open(self.filename, "w") as f:
            json.dump(
                {"last_score": self.last_score, "record_score": self.record_score}, f
            )

    def get_last_score(self):
        return self.last_score

    def get_record_score(self):
        return self.record_score


score_handler = ScoreHandler("scores.json")
