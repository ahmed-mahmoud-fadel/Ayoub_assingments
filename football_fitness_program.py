# Define the fitness levels for each player
FITNESS_LEVELS = {
    9.0: "Fitness level below pace for long games",
    10.0: "Fitness level for amateur player",
    11.0: "Fitness level for above average amateur player",
    12.0: "Fitness level for elite player",
    13.0: "Very high fitness level"}

# Read the player data from the file
def read_player_data(player_data_file):
    player_data = {}
    with open(player_data_file, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            date = parts[0].strip()
            player_name = parts[1].strip()
            level = float(parts[2].strip())
            laps = int(parts[3].strip())
            speed = float(parts[4].strip())
            lap_time = float(parts[5].strip())
            
            # Check if player data already exists
            if player_name in player_data:
                player_data[player_name].append((date, level, laps, speed, lap_time))
            else:
                player_data[player_name] = [(date, level, laps, speed, lap_time)]

    return player_data

# Get the average level for the last four weeks for each player
def get_player_average_data(player_data):
    player_averages = {}
    for player_name, player_info in player_data.items():
        if len(player_info) >= 4:
            # Get the last four weeks of data
            last_four_weeks = player_info[-4:]
            
            # Calculate the average level
            avg_level = sum(info[1] for info in last_four_weeks) / 4
            
            # Store the player's average data
            player_averages[player_name] = avg_level
        else:
            print(f"Not enough data for player {player_name}")

    return player_averages

# Get the football fitness level for a given average level
def get_football_fitness_level(avg_level):
    for level, description in FITNESS_LEVELS.items():
        if avg_level <= level:
            return description

player_data_file = "player_data.txt"
player_data = read_player_data(player_data_file)
player_average_data = get_player_average_data(player_data)
for player_name, avg_level in player_average_data.items():
    print(f"{player_name}: {get_football_fitness_level(avg_level)}")
