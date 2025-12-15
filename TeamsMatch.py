# List of teams
teams = [
    {"team_code": "IND", "team_name": "India"},
    {"team_code": "PAK", "team_name": "Pakistan"},
    {"team_code": "AUS", "team_name": "Australia"},
    {"team_code": "ENG", "team_name": "England"}
]

# Function to generate match schedule
def generate_match_schedule(teams):
    matches = []
    num_teams = len(teams)

    # Generate unique matches
    for i in range(num_teams):
        for j in range(i + 1, num_teams):
            match = (teams[i]["team_name"], teams[j]["team_name"])
            matches.append(match)
    
    return matches

# Main execution
if __name__ == "__main__":
    schedule = generate_match_schedule(teams)
    
    # Print the match schedule
    print("Match Schedule:")
    for match in schedule:
        print(f"{match[0]} vs {match[1]}")
