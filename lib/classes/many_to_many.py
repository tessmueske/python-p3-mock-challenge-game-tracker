class Game:

    all = []

    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be of type str")
        if len(value) == 0:
            raise ValueError("Title must be longer than 0 characters")
        if hasattr(self, '_title'):
            raise AttributeError("Title cannot be changed after the game is instantiated")
        self._title = value

    def results(self):
        #Returns a list of all results for that game
        return [result for result in Result.all if result.game == self]

    def players(self):
        # Returns a unique list of all players that played a particular game
        # Players must be of type Player
        new_list = []
        for result in Result.all:
            if result.game == self:
                if result.player not in new_list:
                    new_list.append(result.player)
        return new_list

    def average_score(self, player):
        # new_list_two = []
        # for result in Result.all:
        #     if result.game == self:
        #         if result.player == player:
        #             new_list_two.append(result.score)
        new_list_two = [result.score for result in Result.all if result.game == self and result.player == player]
        average = sum(new_list_two) / len(new_list_two)
        return average
        
class Player:

    all = []

    def __init__(self, username):
        self.username = username 
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise ValueError("Username must be of type str")
        if not (2 <= len(value) <= 16):
            raise ValueError("Username must be between 2 and 16 characters")
        self._username = value

    def results(self):
        players = [result for result in Result.all if result.player == self]
        return players

    def games_played(self):
        #Returns a unique list of all games played by a particular player
        #Games must be of type Game
        games_list = []
        for result in Result.all:
           if result.player == self:
                if result.game not in games_list:
                    games_list.append(result.game)
        return games_list

    def played_game(self, game):
        for result in Result.all:
            if result.player == self and result.game == game:
                return True
        else:
            return False

    def num_times_played(self, game):
        count = 0
        for result in Result.all:
            if result.player == self and result.game == game:
                count += 1
        return count

        # Returns the number of times the player has played the game instance provided
        # Returns 0 if the player never played the game provided

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("Score must be of type int")
        if not (1 <= value <= 5000):
            raise ValueError("Score must be between 1 and 5000")
        if hasattr(self, '_score'):
            raise AttributeError("Score cannot be changed after the result is instantiated")
        self._score = value