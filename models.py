def create_user(conn, name, email, password_hash, role='user'):
    with conn.cursor() as cur:
        try:
            cur.execute("""
                INSERT INTO users (name, email, password, role)
                VALUES (%s, %s, %s, %s)
            """, (name, email, password_hash, role))
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise Exception("User creation failed: " + str(e))
