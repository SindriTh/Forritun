# 0. Lesa inn skránna
# 1. Ítra í gegnum skrá og lesa "Chess players"
# 2. Uppflettitafla / dictionary fyrir chess_players: first_name + " " + last_name = key, (rank,country, rating, birth) 
# 3. Uppflettitafla / dictionary fyrir country: key = country,  [lastname,....]
# 4. 
RANK=0
COUNTRY = 1
RATING = 2
BIRTH_YEAR = 3

def read_chess_players(filename):
    '''Reads a csv file of the top 100 chess players and maps it to a dictionary, 
     The key is the last_name and the value is other attributes'''
    chess_players_dict = {}
    with open(filename) as filestream:
        for line in filestream:
            line = line.strip()
            rank,full_name,country,rating,birth_year = line.split(";")
            last_name,first_name = full_name.split(",")
            last_name,first_name = last_name.strip(),first_name.strip()
            player_values = (int(rank),country.strip(),int(rating),int(birth_year))
            chess_players_dict[first_name + " " + last_name] = player_values
    return chess_players_dict

def group_by_country(chess_players_dict):
    ''' Groups chess players by country and returns a dictionary.
    The key of the dictionary is the country, the value is a list of full names'''

    country_dict = {}
    for player_name, player_values in chess_players_dict.items():
        country_name = player_values[COUNTRY]
        if country_name in country_dict:
            country_dict[country_name].append(player_name)
        else:
            country_dict[country_name] = [player_name] 
    return country_dict


def print_country_information(country_name,player_names_in_country,chess_players_dict):
    '''Prints the country information'''
    print(f"{country_name} ({len(player_names_in_country)}) ({average_rating(player_names_in_country, chess_players_dict):.1f}):")
    return

def average_rating(player_names_in_country,chess_players_dict):
    '''Calculate the average rating in a given player list'''
    total = 0.0
    for player_name in player_names_in_country:
        total += chess_players_dict[player_name][RATING]
    return total/len(player_names_in_country)

def print_chess_player(player_name,chess_players_dict):
    '''Print formatted information about a chess player'''
    print(f"{player_name:>40}{chess_players_dict[player_name][RATING]:>10d}")

def print_header(headerstring = "Players by country:"):
    print(headerstring)
    print("-"*len(headerstring))


def print_birthyear_information(birth_year,player_names_in_birthyear, chess_players_dict):
    '''Prints the birth year information'''
    print(f"{birth_year} ({len(player_names_in_birthyear)}) ({average_rating(player_names_in_birthyear, chess_players_dict):.1f}):")
    return


def group_by_birthyear(chess_players_dict):
    ''' Groups chess players by birthyear and returns a dictionary.
    The key of the dictionary is the country, the value is a list of full names'''

    birthyear_dict = {}
    for player_name, player_values in chess_players_dict.items():
        birth_year = player_values[BIRTH_YEAR]
        if birth_year in birthyear_dict:
            birthyear_dict[birth_year].append(player_name)
        else:
            birthyear_dict[birth_year] = [player_name] 
    return birthyear_dict



def main():
    filename = input("Enter filename: ")
    chess_players_dict = read_chess_players(filename)
    country_dict = group_by_country(chess_players_dict)
    print_header()
    for country_name,player_names_in_country in sorted(country_dict.items()):
        print_country_information(country_name,player_names_in_country,chess_players_dict)
        for player_name in player_names_in_country:
            print_chess_player(player_name,chess_players_dict)

    birthyear_dict = group_by_birthyear(chess_players_dict)

    print()
    print_header("Players by birth year:")
    for birthyear,player_names_in_birthyear in sorted(birthyear_dict.items()):
        print_birthyear_information(birthyear,player_names_in_birthyear,chess_players_dict)
        for player_name in player_names_in_birthyear:
            print_chess_player(player_name,chess_players_dict)

main()