import random
import time

def main():
    team_stats = {
        'morale': 70,
        'strength': 75,
        'injuries': 0,
        'wins': 0,
        'losses': 0
    }
    
    print("=" * 50)
    print("2026 FIFA WORLD CUP TEAM MANAGER")
    print("=" * 50)
    
    pre_tournament_preparation(team_stats)
    
    if team_stats['injuries'] >= 3:
        print("\nToo many injuries during preparation. Team withdraws.")
        return
    
    group_stage(team_stats)
    
    if team_stats['wins'] == 0 and team_stats['losses'] >= 2:
        print("\nEliminated in group stage. Tournament over.")
        return
    
    knockout_stage(team_stats)

def pre_tournament_preparation(stats):
    print("\n--- PRE-TOURNAMENT PREPARATION ---")
    
    for day in range(1, 8):
        print(f"\nDay {day}:")
        print(f"Current morale: {stats['morale']} | Strength: {stats['strength']} | Injuries: {stats['injuries']}")
        
        print("Choose activity:")
        print("1. Intensive training (+strength, risk injury)")
        print("2. Friendly match (+morale, slight injury risk)")
        print("3. Recovery session (-injuries, -morale)")
        
        choice = input("Your choice (1-3): ")
        
        if choice == '1':
            stats['strength'] = min(100, stats['strength'] + random.randint(5, 12))
            if random.random() < 0.3:
                stats['injuries'] += 1
                print("Injury occurred!")
            else:
                print("Training successful! Strength increased.")
                
        elif choice == '2':
            stats['morale'] = min(100, stats['morale'] + random.randint(3, 10))
            if random.random() < 0.15:
                stats['injuries'] += 0.5
                print("Minor injury during friendly.")
            else:
                print("Friendly match boosted morale!")
                
        elif choice == '3':
            if stats['injuries'] > 0:
                stats['injuries'] = max(0, stats['injuries'] - random.randint(1, 2))
                stats['morale'] = max(0, stats['morale'] - random.randint(5, 10))
                print("Recovery session completed. Injuries reduced.")
            else:
                print("No injuries to recover from. Day wasted.")
                continue
        else:
            print("Invalid choice. Day skipped.")
            continue
        
        if stats['injuries'] >= 4:
            print("CRITICAL: Too many injuries!")
            break
    
    print(f"\nPreparation complete: Morale={stats['morale']}, Strength={stats['strength']}, Injuries={stats['injuries']}")

def group_stage(stats):
    print("\n" + "=" * 50)
    print("GROUP STAGE")
    print("=" * 50)
    
    opponents = ["Germany", "Mexico", "Japan"]
    results = []
    
    for match_num, opponent in enumerate(opponents, 1):
        print(f"\nMatch {match_num} vs {opponent}")
        time.sleep(1)
        
        if stats['injuries'] >= 3:
            print("Team too injured to compete effectively.")
            stats['losses'] += 1
            results.append("Loss")
            continue
        
        match_outcome = simulate_match(stats, opponent, "group")
        
        if match_outcome == "Win":
            stats['wins'] += 1
            stats['morale'] += 10
            results.append("Win")
        elif match_outcome == "Loss":
            stats['losses'] += 1
            stats['morale'] = max(0, stats['morale'] - 8)
            results.append("Loss")
        else:
            stats['morale'] += 2
            results.append("Draw")
        
        stats['morale'] = min(100, stats['morale'])
        
        print(f"Result: {match_outcome}")
        print(f"Morale: {stats['morale']} | Strength: {stats['strength']}")
        
        if stats['morale'] <= 20:
            print("Team morale critically low!")
    
    print(f"\nGroup Stage Results: {results.count('Win')}W, {results.count('Draw')}D, {results.count('Loss')}L")
    
    if results.count('Win') >= 2 or (results.count('Win') == 1 and results.count('Draw') >= 1):
        print("Qualified for knockout stage!")
    else:
        print("Failed to qualify for knockout stage.")

def knockout_stage(stats):
    print("\n" + "=" * 50)
    print("KNOCKOUT STAGE")
    print("=" * 50)
    
    rounds = [
        ("Round of 16", ["Brazil", "Argentina"]),
        ("Quarter-final", ["France", "England"]),
        ("Semi-final", ["Spain", "Netherlands"]),
        ("Final", ["Champion", "Runner-up"])
    ]
    
    for round_name, possible_opponents in rounds:
        print(f"\n--- {round_name.upper()} ---")
        time.sleep(1)
        
        if stats['injuries'] >= 4:
            print("Team unfit to continue. Tournament exit.")
            break
        
        opponent = random.choice(possible_opponents)
        print(f"Opponent: {opponent}")
        
        if round_name == "Final":
            print("\nTHE FINAL MATCH!")
            print("This is it. The World Cup is on the line.")
        
        match_outcome = simulate_match(stats, opponent, "knockout")
        
        if match_outcome == "Win":
            print(f"VICTORY! Advanced to next round.")
            stats['morale'] = min(100, stats['morale'] + 15)
            
            if round_name == "Final":
                print("\n" + "=" * 50)
                print("CHAMPIONS! YOU WON THE WORLD CUP!")
                print("=" * 50)
                break
        else:
            print(f"DEFEAT! Eliminated in {round_name}.")
            print("\nTournament over.")
            break
        
        post_match_management(stats)
        
        placeholder_future_feature()

def simulate_match(stats, opponent, stage):
    base_chance = stats['strength'] / 100
    morale_mod = stats['morale'] / 100
    injury_penalty = max(0, 1 - (stats['injuries'] * 0.15))
    
    win_chance = base_chance * morale_mod * injury_penalty
    
    if stage == "group":
        win_chance = win_chance * 0.7
    
    random_factor = random.random()
    
    if random_factor < win_chance:
        return "Win"
    elif random_factor < win_chance + 0.3:
        return "Draw"
    else:
        return "Loss"

def post_match_management(stats):
    print("\n--- POST-MATCH MANAGEMENT ---")
    
    while True:
        print("1. Team celebration (+morale)")
        print("2. Recovery session (skip to next)")
        print("3. Tactical review (+strength for next match)")
        
        choice = input("Choose action (1-3): ")
        
        if choice == '1':
            stats['morale'] = min(100, stats['morale'] + random.randint(5, 15))
            print(f"Morale increased to {stats['morale']}")
            break
        elif choice == '2':
            if stats['injuries'] > 0:
                stats['injuries'] = max(0, stats['injuries'] - 1)
                print(f"Injuries reduced to {stats['injuries']}")
            else:
                print("No injuries to recover.")
            break
        elif choice == '3':
            stats['strength'] = min(100, stats['strength'] + random.randint(3, 8))
            print(f"Strength increased to {stats['strength']}")
            break
        else:
            print("Invalid choice. Try again.")
            continue
    
    if stats['morale'] > 90:
        print("Team is in excellent spirits!")
    elif stats['morale'] < 30:
        print("Team morale is dangerously low.")

def placeholder_future_feature():
    pass

if __name__ == "__main__":
    main()