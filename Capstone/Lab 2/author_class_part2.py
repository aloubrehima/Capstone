class Author:
    def __init__(self, name):
        self.name = name
        self.books = []     # empty list to store published books

    def publish(self, title):
        if title in self.books: # check to see if the title is already there or not
            print(f"Error: this '{title}' was published by {self.name}")
        else:
            self.books.append(title)  # add the published book to the list
            print(f"'{title}' published by {self.name}.")

    def __str__(self):
        if self.books:
            book_titles = ", ".join(self.books)
        else:
            book_titles = 'No books'  # shows this if there is no books
        return f"{self.name}: {book_titles}" # return author name and book published


# Creating authors
author1 = Author("Charles Duhigg")
author2 = Author("Gary Keller & Jay Keller")
author3 = Author("Alex Lickerman, MD")
author4 = Author("Alou")

# Published books
author1.publish("The Power Of Habit")
author2.publish("The One Thing")
author3.publish("The Undefeated Mind")

print(author1)
print(author2)
print(author3)
print(author4)


