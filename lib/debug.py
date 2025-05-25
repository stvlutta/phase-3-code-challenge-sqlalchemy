#!/usr/bin/env python3
"""
Debug script for interactive testing.
Run with: python -i lib/debug.py
"""
import os
import sys

# Add the parent directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import database modules
from lib.db.connection import get_connection
from lib.db.seed import seed_database

# Import model classes
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

# Import transaction helpers
from lib.db.transactions import (
    add_author_with_articles,
    add_magazine_with_articles,
    delete_author_with_articles,
    delete_magazine_with_articles
)

def setup():
    """Setup the database and seed it with test data"""
    # Create database schema by running the setup_db.py script
    setup_script_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'scripts',
        'setup_db.py'
    )
    exec(open(setup_script_path).read())
    
    # Seed the database
    seed_database()
    
    print("Database setup complete and seeded with test data.")

def test_queries():
    """Run test queries to verify the setup"""
    print("\n===== TEST QUERIES =====")
    
    # Test Author queries
    print("\n----- Author Queries -----")
    authors = Author.all()
    print(f"Total authors: {len(authors)}")
    if authors:
        author = authors[0]
        print(f"Sample author: {author}")
        articles = author.articles()
        print(f"Articles by {author.name}: {len(articles)}")
        magazines = author.magazines()
        print(f"Magazines for {author.name}: {len(magazines)}")
        topic_areas = author.topic_areas()
        print(f"Topic areas for {author.name}: {topic_areas}")
    
    # Test Magazine queries
    print("\n----- Magazine Queries -----")
    magazines = Magazine.all()
    print(f"Total magazines: {len(magazines)}")
    if magazines:
        magazine = magazines[0]
        print(f"Sample magazine: {magazine}")
        articles = magazine.articles()
        print(f"Articles in {magazine.name}: {len(articles)}")
        contributors = magazine.contributors()
        print(f"Contributors to {magazine.name}: {len(contributors)}")
        article_titles = magazine.article_titles()
        print(f"Article titles in {magazine.name}: {article_titles}")
    
    # Test Article queries
    print("\n----- Article Queries -----")
    articles = Article.all()
    print(f"Total articles: {len(articles)}")
    if articles:
        article = articles[0]
        print(f"Sample article: {article}")
        author = article.author()
        print(f"Author of '{article.title}': {author.name if author else 'None'}")
        magazine = article.magazine()
        print(f"Magazine of '{article.title}': {magazine.name if magazine else 'None'}")

def main():
    """Main function for interactive debugging"""
    setup()
    test_queries()
    
    print("\n===== INTERACTIVE DEBUG =====")
    print("The following objects are available:")
    print("- Author: Author class")
    print("- Magazine: Magazine class")
    print("- Article: Article class")
    print("- add_author_with_articles(): Create an author with articles")
    print("- add_magazine_with_articles(): Create a magazine with articles")
    print("- delete_author_with_articles(): Delete an author and their articles")
    print("- delete_magazine_with_articles(): Delete a magazine and its articles")
    print("\nYou are now in an interactive Python shell.")

if __name__ == "__main__":
    main()