from connection import create_connection


def fetch_face_image(user_name):
    conn = create_connection()
    cursor = conn.cursor()

    # Fetch the face image for the given user_name
    cursor.execute("SELECT face_image FROM user WHERE user_name = %s", (user_name,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result:
        return result[0]  # Return the BLOB object
    return None
