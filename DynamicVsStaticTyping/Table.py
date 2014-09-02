class Table:
    def __init__(self, name):
        self.players = []
        self.name = name

    def seatPlayer(self, player):
        self.players.append(player)

    def prettyPrint(self):
        pass
