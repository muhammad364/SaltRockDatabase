from python_app.db_config import get_connection, close_connection
from datetime import datetime

def find_artists_by_venue_genre(genre_ids):
    """
    Returns artists whose genres match those of the given genre IDs.
    - genre_ids: list of ints (genre IDs)
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    fmt = ','.join(['%s'] * len(genre_ids))
    sql = f"SELECT DISTINCT a.act_name, a.ACT_ID FROM Act a JOIN Act_Genre ag ON a.ACT_ID = ag.ACT_ID WHERE ag.GENRE_ID IN ({fmt}) ORDER BY a.act_name;"
    cursor.execute(sql, genre_ids)
    results = cursor.fetchall()
    close_connection(conn)
    return results

def list_solo_acts():
    """Returns at least two solo acts with their member names."""
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    sql = "SELECT a.ACT_ID, a.act_name, m.first_name, m.last_name FROM Act a JOIN Act_Member m ON a.ACT_ID = m.ACT_ID WHERE a.is_solo = TRUE LIMIT 2;"
    cursor.execute(sql)
    results = cursor.fetchall()
    close_connection(conn)
    return results

def venues_with_multiple_genres(min_genres=3):
    """
    Returns venues that have acts spanning at least `min_genres` different genres.
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    sql = "SELECT v.VENUE_ID, v.venue_name, COUNT(DISTINCT ag.GENRE_ID) AS genre_count FROM Venue v JOIN Gig_Booking gb ON v.VENUE_ID = gb.VENUE_ID JOIN Act_Genre ag ON gb.ACT_ID = ag.ACT_ID GROUP BY v.VENUE_ID HAVING genre_count >= %s;"
    cursor.execute(sql, (min_genres,))
    results = cursor.fetchall()
    close_connection(conn)
    return results

def members_of_two_bands(limit=6):
    """
    Returns members of two non-solo acts (limit total rows).
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    sql = "SELECT a.act_name, m.first_name, m.last_name FROM Act a JOIN Act_Member m ON a.ACT_ID = m.ACT_ID WHERE a.is_solo = FALSE LIMIT %s;"
    cursor.execute(sql, (limit,))
    results = cursor.fetchall()
    close_connection(conn)
    return results

def calculate_gig_cost(act_id, start_time_str, end_time_str):
    """
    Returns the calculated total gig cost (hours * gig_rate)
    for the given act and time range.
    """
    # 1. Fetch the act's rate
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT gig_rate FROM Act WHERE ACT_ID = %s",
        (act_id,)
    )
    row = cursor.fetchone()
    close_connection(conn)

    if not row:
        # ACT_ID not found
        return None

    gig_rate = float(row[0])

    # 2. Parse the time strings and compute duration in hours
    fmt = "%H:%M:%S"
    try:
        t0 = datetime.strptime(start_time_str, fmt)
        t1 = datetime.strptime(end_time_str,   fmt)
    except ValueError:
        # bad time format
        return None

    delta = t1 - t0
    hours = delta.total_seconds() / 3600
    if hours <= 0:
        # end before or equal to start
        return None

    # 3. Calculate and return cost
    return round(hours * gig_rate, 2)

