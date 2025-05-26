#!/usr/bin/env python3
"""
Script to run example queries on the database.
This demonstrates how to use the various query methods provided by the models.
"""
import os
import sys

# Add the parent directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import setup functions
from scripts.setup_db import setup_database
from lib.db.seed import seed_database

# Import model classes
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

# Import transaction helpers
from lib.db.transactions import (
    add_author_with_articles,
    add_magazine_with_articles
)

def print_separator(title):
    """Print a separator with a title"""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

def run_author_queries():
    """Run and display queries related to authors"""
    print_separator("AUTHOR QUERIES")
    
    # Get all authors
    authors = Author.all()
    print(f"Total authors: {len(authors)}")
    for author in authors:
        print(f"Author {author.id}: {author.name}")
    
    # Find author by ID
    author = Author.find_by_id(1)
    if author:
        print(f"\nAuthor with ID 1: {author.name}")
    
    # Find author by name
    author = Author.find_by_name("John Smith")
    if author:
        print(f"Author with name 'John Smith': ID {author.id}")
    
    # Get articles by an author
    if author:
        articles = author.articles()
        print(f"\nArticles by {author.name} ({len(articles)}):")
        for article in articles:
            print(f"- {article.title}")
    
    # Get magazines an author has contributed to
    if author:
        magazines = author.magazines()
        print(f"\nMagazines {author.name} has contributed to ({len(magazines)}):")
        for magazine in magazines:
            print(f"- {magazine.name} ({magazine.category})")
    
    # Get topic areas an author has written in
    if author:
        topics = author.topic_areas()
        print(f"\nTopic areas {author.name} has written in ({len(topics)}):")
        for topic in topics:
            print(f"- {topic}")
    
    # Find the most prolific author
    prolific_author = Author.most_prolific()
    if prolific_author:
        print(f"\nMost prolific author: {prolific_author.name}")
        print(f"Number of articles: {len(prolific_author.articles())}")

def run_magazine_queries():
    """Run and display queries related to magazines"""
    print_separator("MAGAZINE QUERIES")
    
    # Get all magazines
    magazines = Magazine.all()
    print(f"Total magazines: {len(magazines)}")
    for magazine in magazines:
        print(f"Magazine {magazine.id}: {magazine.name} ({magazine.category})")
    
    # Find magazine by ID
    magazine = Magazine.find_by_id(1)
    if magazine:
        print(f"\nMagazine with ID 1: {magazine.name} ({magazine.category})")
    
    # Find magazine by name
    magazine = Magazine.find_by_name("Tech Today")
    if magazine:
        print(f"Magazine with name 'Tech Today': ID {magazine.id}")
    
    # Find magazines by category
    tech_magazines = Magazine.find_by_category("Technology")
    print(f"\nTechnology magazines ({len(tech_magazines)}):")
    for magazine in tech_magazines:
        print(f"- {magazine.name}")
    
    # Get articles in a magazine
    if magazine:
        articles = magazine.articles()
        print(f"\nArticles in {magazine.name} ({len(articles)}):")
        for article in articles:
            print(f"- {article.title}")
    
    # Get contributors to a magazine
    if magazine:
        contributors = magazine.contributors()
        print(f"\nContributors to {magazine.name} ({len(contributors)}):")
        for contributor in contributors:
            print(f"- {contributor.name}")
    
    # Get article titles in a magazine
    if magazine:
        titles = magazine.article_titles()
        print(f"\nArticle titles in {magazine.name} ({len(titles)}):")
        for title in titles:
            print(f"- {title}")
    
    # Get contributing authors with more than 2 articles
    if magazine:
        contributors = magazine.contributing_authors()
        print(f"\nAuthors with more than 2 articles in {magazine.name} ({len(contributors)}):")
        for contributor in contributors:
            print(f"- {contributor.name}")
    
    # Find top publisher (magazine with most articles)
    top_magazine = Magazine.top_publisher()
    if top_magazine:
        print(f"\nTop publisher (most articles): {top_magazine.name}")
        print(f"Number of articles: {len(top_magazine.articles())}")
    
    # Find magazines with multiple authors
    multi_author_magazines = Magazine.magazines_with_multiple_authors()
    print(f"\nMagazines with multiple authors ({len(multi_author_magazines)}):")
    for magazine in multi_author_magazines:
        print(f"- {magazine.name}")
    
    # Count articles in each magazine
    magazine_counts = Magazine.article_count_by_magazine()
    print("\nArticle count by magazine:")
    for magazine in magazine_counts:
        print(f"- {magazine.name}: {magazine.article_count} articles")

def run_article_queries():
    """Run and display queries related to articles"""
    print_separator("ARTICLE QUERIES")
    
    # Get all articles
    articles = Article.all()
    print(f"Total articles: {len(articles)}")
    for i, article in enumerate(articles[:5]):  # Show only first 5 to avoid clutter
        print(f"Article {article.id}: {article.title}")
    if len(articles) > 5:
        print(f"... and {len(articles) - 5} more articles")
    
    # Find article by ID
    article = Article.find_by_id(1)
    if article:
        print(f"\nArticle with ID 1: {article.title}")
    
    # Find articles by title
    articles = Article.find_by_title("The Future of AI")
    print(f"\nArticles with title 'The Future of AI' ({len(articles)}):")
    for article in articles:
        print(f"- ID {article.id} by Author ID {article.author_id}")
    
    # Find articles by author ID
    articles = Article.find_by_author_id(1)
    print(f"\nArticles by Author ID 1 ({len(articles)}):")
    for article in articles:
        print(f"- {article.title}")
    
    # Find articles by magazine ID
    articles = Article.find_by_magazine_id(1)
    print(f"\nArticles in Magazine ID 1 ({len(articles)}):")
    for article in articles:
        print(f"- {article.title}")
    
    # Get author of an article
    if article:
        author = article.author()
        if author:
            print(f"\nAuthor of '{article.title}': {author.name}")
    
    # Get magazine of an article
    if article:
        magazine = article.magazine()
        if magazine:
            print(f"Magazine of '{article.title}': {magazine.name} ({magazine.category})")

def run_transaction_examples():
    """Run and display examples of transactions"""
    print_separator("TRANSACTION EXAMPLES")
    
    # Add an author with articles in a single transaction
    print("Adding a new author with articles...")
    articles_data = [
        {"title": "Transaction Example 1", "magazine_id": 1},
        {"title": "Transaction Example 2", "magazine_id": 2}
    ]
    author = add_author_with_articles("Transaction Author", articles_data)
    
    if author:
        print(f"Added author: {author.name} (ID: {author.id})")
        print("Articles:")
        for article in author.articles():
            print(f"- {article.title}")
    
    # Add a magazine with articles in a single transaction
    print("\nAdding a new magazine with articles...")
    articles_data = [
        {"title": "Magazine Transaction 1", "author_id": 1},
        {"title": "Magazine Transaction 2", "author_id": 2}
    ]
    magazine = add_magazine_with_articles("Transaction Magazine", "Transaction", articles_data)
    
    if magazine:
        print(f"Added magazine: {magazine.name} (ID: {magazine.id})")
        print("Articles:")
        for article in magazine.articles():
            print(f"- {article.title}")

def main():
    """Main function to run all example queries"""
    # Set up the database
    print("Setting up database...")
    setup_database()
    
    # Seed the database with test data
    print("Seeding database with test data...")
    seed_database()
    
    # Run example queries
    run_author_queries()
    run_magazine_queries()
    run_article_queries()
    run_transaction_examples()
    
    print("\nAll queries completed successfully!")

if __name__ == "__main__":
    main()