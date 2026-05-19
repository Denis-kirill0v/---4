def average_rating(books):
    if not books:
        return 0
    total = sum(book.rating for book in books)
    return round(total / len(books), 2)

def author_stats(books):
    stats = {}
    for book in books:
        if book.author in stats:
            stats[book.author] += 1
        else:
            stats[book.author] = 1
    return stats
