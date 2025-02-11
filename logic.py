import random

class Candidate:
    def __init__(self, name, party, popularity):
        self.name = name
        self.party = party
        self.popularity = popularity  # Base popularity score
        self.votes = 0
        self.points = 0

    def campaign(self):
        """Simulate campaign events affecting popularity."""
        event_effect = random.randint(-5, 10)  # Random impact on popularity
        self.popularity += event_effect

    def get_votes(self):
        """Simulate votes based on popularity."""
        self.votes = random.randint(50000, 100000) * (self.popularity / 100)
        return self.votes

    def calculate_points(self):
        """Assign fantasy points based on votes and events."""
        self.points = int(self.votes / 1000) + self.popularity
        return self.points


class FantasyElection:
    def __init__(self):
        self.candidates = []
        self.teams = {}

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def create_team(self, user, candidate_names):
        """Each user picks candidates for their team."""
        team = [c for c in self.candidates if c.name in candidate_names]
        self.teams[user] = team

    def simulate_election(self):
        """Run the election cycle."""
        for candidate in self.candidates:
            candidate.campaign()
            candidate.get_votes()
            candidate.calculate_points()

    def get_scores(self):
        """Calculate fantasy scores for each user."""
        scores = {}
        for user, team in self.teams.items():
            scores[user] = sum(candidate.points for candidate in team)
        return scores

    def display_results(self):
        print("\nElection Results:")
        for candidate in self.candidates:
            print(f"{candidate.name} ({candidate.party}) - Votes: {int(candidate.votes)}, Points: {candidate.points}")

        print("\nFantasy Team Scores:")
        for user, score in self.get_scores().items():
            print(f"{user}: {score} points")


# Sample Candidates
candidates = [
    Candidate("Alice", "Party A", 60),
    Candidate("Bob", "Party B", 55),
    Candidate("Charlie", "Party C", 50),
    Candidate("Diana", "Party D", 45),
]

# Fantasy Election Setup
game = FantasyElection()
for c in candidates:
    game.add_candidate(c)

# Users create their fantasy teams
game.create_team("User1", ["Alice", "Charlie"])
game.create_team("User2", ["Bob", "Diana"])

# Simulate election and show results
game.simulate_election()
game.display_results()
