from python_app.db_config import get_connection, close_connection

def insert_new_act():
    """
    Prompts user for a new act and its members, and inserts them into the database.
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    # Insert Act
    act_name = input("Enter new act name: ")
    gig_rate = float(input("Enter gig rate (e.g. 500.00): "))
    is_solo_input = input("Is this a solo act? (y/n): ").strip().lower()
    is_solo = True if is_solo_input == 'y' else False
    
    cursor.execute(
        "INSERT INTO Act (act_name, gig_rate, is_solo) VALUES (%s, %s, %s)",
        (act_name, gig_rate, is_solo)
    )
    conn.commit()
    act_id = cursor.lastrowid
    print(f"Inserted Act '{act_name}' with ACT_ID={act_id}")
    
    # Insert Members
    num_members = int(input("How many members for this act? "))
    for i in range(num_members):
        first_name = input(f"Enter first name of member {i+1}: ")
        last_name = input(f"Enter last name of member {i+1}: ")
        cursor.execute(
            "INSERT INTO Act_Member (first_name, last_name, ACT_ID) VALUES (%s, %s, %s)",
            (first_name, last_name, act_id)
        )
    conn.commit()
    print(f"Inserted {num_members} members for Act_ID={act_id}")
    
    close_connection(conn)
