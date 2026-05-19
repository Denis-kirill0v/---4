from datetime import datetime

class Book:
    def __init__(self, author, title, rating, date_read=None):
        self.author = author
        self.title = title
        self.rating = rating
        self.date_read = date_read or datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "author": self.author,
            "title": self.title,
            "rating": self.rating,
            "date_read": self.date_read
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
