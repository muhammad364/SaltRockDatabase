from python_app.db_config import get_connection, close_connection
from python_app.query_functions import (
    find_artists_by_venue_genre,
    list_solo_acts,
    venues_with_multiple_genres,
    members_of_two_bands,
    calculate_gig_cost
)
from python_app.insert_functions import insert_new_act

def print_menu():
    print("""\
\nSalt Rock Main Menu
1. Find artists by venue genres
2. List solo acts
3. Venues with multiple genres
4. Members of two bands
5. Calculate gig cost
6. Insert new act and members
7. Exit
""")

def main():
    while True:
        print_menu()
        choice = input("Select an option (1-7): ")
        if choice == '1':
            genre_input = input(
                "Enter genre IDs separated by commas (e.g. 1,2,3): "
            )
            genre_ids = [int(g.strip()) for g in genre_input.split(',')]
            results = find_artists_by_venue_genre(genre_ids)
            print("Artists matching those genres:")
            for row in results:
                print(f" {row['ACT_ID']}: {row['act_name']}")
        elif choice == '2':
            results = list_solo_acts()
            print("Solo acts:")
            for row in results:
                name = f"{row['first_name']} {row['last_name']}"
                print(f" {row['ACT_ID']}: {row['act_name']} — Member: {name}")
        elif choice == '3':
            min_genres = input("Enter minimum number of genres (default 3): ") or '3'
            results = venues_with_multiple_genres(int(min_genres))
            print(f"Venues with at least {min_genres} genres:")
            for row in results:
                print(f" {row['VENUE_ID']}: {row['venue_name']} ({row['genre_count']} genres)")
        elif choice == '4':
            results = members_of_two_bands()
            print("Members of two non-solo acts:")
            for row in results:
                print(f" {row['act_name']}: {row['first_name']} {row['last_name']}")
        elif choice == '5':
            act_id = int(input("Enter Act ID: "))
            start = input("Enter start time (HH:MM:SS): ")
            end = input("Enter end time (HH:MM:SS): ")
            cost = calculate_gig_cost(act_id, start, end)
            print(f"Total gig cost: £{cost:.2f}")
        elif choice == '6':
            print("Insert a new act and its members:")
            insert_new_act()
        elif choice == '7':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == '__main__':
    main()
