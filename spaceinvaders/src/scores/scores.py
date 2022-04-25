class Scores:
    def __init__(self, connection):
        self._connection = connection

    def get_highscores(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT name, score FROM Highscores ORDER BY score DESC LIMIT 10")

        scores = cursor.fetchall()

        return [(row["name"], row["score"]) for row in scores]

    def save_scores(self, name, score):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO Highscores (name, score) VALUES (?, ?)", (name, score))
        self._connection.commit()
    