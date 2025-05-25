from lib.db.connection import get_connection

def seed_database():
    """Seed the database with test data"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Clear existing data
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    
    # Seed authors
    authors = [
        ("John Smith",),
        ("Jane Doe",),
        ("Michael Johnson",),
        ("Sarah Williams",),
        ("Robert Brown",)
    ]
    
    cursor.executemany(
        "INSERT INTO authors (name) VALUES (?)",
        authors
    )
    
    # Seed magazines
    magazines = [
        ("Tech Today", "Technology"),
        ("Science Weekly", "Science"),
        ("Business Review", "Business"),
        ("Health & Fitness", "Health"),
        ("Travel Explorer", "Travel")
    ]
    
    cursor.executemany(
        "INSERT INTO magazines (name, category) VALUES (?, ?)",
        magazines
    )
    
    # Seed articles
    articles = [
        ("The Future of AI", 1, 1),
        ("Machine Learning Trends", 1, 1),
        ("Climate Change Research", 2, 2),
        ("Investment Strategies", 3, 3),
        ("Healthy Diet Tips", 4, 4),
        ("European Destinations", 5, 5),
        ("Cloud Computing", 1, 1),
        ("Remote Work", 2, 3),
        ("Exercise Routines", 3, 4),
        ("Asia Travel Guide", 4, 5),
        ("Quantum Computing", 5, 2),
        ("Mobile App Development", 1, 1),
        ("Startup Funding", 2, 3),
        ("Mental Health", 3, 4),
        ("American Road Trips", 4, 5)
    ]
    
    cursor.executemany(
        "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
        articles
    )
    
    conn.commit()
    conn.close()
    
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()