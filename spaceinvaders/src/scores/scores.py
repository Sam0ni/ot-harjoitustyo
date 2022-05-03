class Scores:
    """Class used for handling database related tasks
    """
    def __init__(self, connection):
        """Class constructor creates connection to database

        Args:
            connection (function): database connection
        """
        self._connection = connection

    def get_highscores(self):
        """Fetches the 10 best scores

        Returns:
            list: returns a list of tuples with playername and score
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT name, score FROM Highscores ORDER BY score DESC LIMIT 10")

        scores = cursor.fetchall()

        return [(row["name"], row["score"]) for row in scores]

    def save_scores(self, name, score):
        """Saves the scores to database

        Args:
            name (str): playername to be saved
            score (int): score to be saved
        """
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO Highscores (name, score) VALUES (?, ?)", (name, score))
        self._connection.commit()
    
    