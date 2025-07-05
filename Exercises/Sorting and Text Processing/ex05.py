book_club = {
    'Alice': [
        {'title': '1984', 'rating': 5, 'pages': 328},
        {'title': 'Brave New World', 'rating': 4, 'pages': 268}
    ],
    'Bob': [
        {'title': '1984', 'rating': 4, 'pages': 328},
        {'title': 'Fahrenheit 451', 'rating': 5, 'pages': 249},
        {'title': 'Brave New World', 'rating': 5, 'pages': 268}
    ],
    'Charlie': [
        {'title': 'Fahrenheit 451', 'rating': 4, 'pages': 249},
        {'title': '1984', 'rating': 5, 'pages': 328}
    ]
}

scores = {}

for person, books in book_club.items():
    total_pages = 0
    total_rating = 0
    num_books = len(books)
    for book in books:
        total_pages += book['pages']
        total_rating += book['rating']  
    average_rating = total_rating / num_books
    score = total_pages * average_rating    
    scores[person] = round(score)

leaderboard = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print("Leaderboard")
for rank, (person, score) in enumerate(leaderboard, start=1):
    print(f"{rank}. {person} - {score} points")

from collections import Counter
book_counter = Counter()
for books in book_club.values():
    for book in books:
        book_counter[book['title']] += 1
max_reads = max(book_counter.values())
most_read_books = [title for title, count in book_counter.items() if count == max_reads]

print("\nMost Read Book:")
for title in most_read_books:
    print(f"- {title} ({book_counter[title]} times)")
