class Player:
    def __init__(self, name, jersey_no, runs):
        self.name = name
        self.jersey_no = jersey_no
        self.runs = runs

    def categorize(self):
        if self.runs >= 1000:
            return "Excellent"
        elif self.runs >= 500:
            return "Good"
        else:
            return "Average"

    def display(self):
        print("Player Name  :", self.name)
        print("Jersey Number:", self.jersey_no)
        print("Runs         :", self.runs)
        print("Category     :", self.categorize())
        print("-" * 35)

class Team:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_all(self):
        print("\nCricket Team Player Details")
        print("=" * 35)

        for player in self.players:
            player.display()

team = Team()
# Add players
team.add_player(Player("Virat", 18, 1200))
team.add_player(Player("Rohit", 45, 750))
team.add_player(Player("Rahul", 1, 350))

# Display all players
team.display_all()

'''output:
Cricket Team Player Details
===================================
Player Name  : Virat
Jersey Number: 18
Runs         : 1200
Category     : Excellent
-----------------------------------
Player Name  : Rohit
Jersey Number: 45
Runs         : 750
Category     : Good
-----------------------------------
Player Name  : Rahul
Jersey Number: 1
Runs         : 350
Category     : Average
-----------------------------------  '''
