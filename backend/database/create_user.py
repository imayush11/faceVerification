from connection import create_connection


def user_exists(user_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM user WHERE user_name = %s", (user_name,))
    exists = cursor.fetchone()[0] > 0
    cursor.close()
    conn.close()
    return exists


def create_user(user_name, face_image_blob):
    conn = create_connection()
    cursor = conn.cursor()

    # Insert the new user into the database
    insert_query = """
    INSERT INTO user (user_name, face_image) 
    VALUES (%s, %s);
    """
    cursor.execute(insert_query, (user_name, face_image_blob))
    conn.commit()
    user_id = cursor.lastrowid  # Get the newly created user_id
    cursor.close()
    conn.close()
    
    return user_id

