#bookkeeping project
import pandas as pd

class book:
    num_books_read = 0
    num_books_liked = 0
    num_books_trashed = 0
    all_books = []
    favorites = []
    books_liked = []
    books_trashed = []
    def __init__(self, title: str, genre: str, author: str):
        self.title = title
        self.genre = genre
        self.author = author
        self.review = ''
        self.rating = 0
        self.like = False
        self.trash = False
        book.num_books_read += 1
        book.all_books.append(self)
    def rate_book(self, rate: float):
        'rate book from a scale of 0-10'
        if rate < 0 or rate > 10:
            raise ValueError('rating not in range')
        else:
            self.rating = rate

        if self.rating > 6:
            book.num_books_liked += 1
            book.books_liked.append(self.title)
            self.like = True
    def add_to_favs(self):
        'add book to an all-time favorites list'
        book.favorites.append(self.title)
    def trash_book(self):
        'angrily rant about a bad book; permanently designate it as trash'
        book.num_books_trashed += 1
        book.books_trashed.append(self.title)
        self.trash = True
        print(f"{self.title} should have never been written and {self.author} should choose another profession.")
    def review_book(self, opinion):# make sure that the methods and the attributes to NOT have the same name!!!
        'give an opinion on a book'
        self.review = opinion


def author_bookshelf(auth: str) -> list:
    'returns a list of books you have read by a given author'
    return [b for b in book.all_books if b.author == auth]


def author_titles(auth: str) -> list:
    'return list of book titles you have read by a given author'
    author_books = author_bookshelf(auth)
    return [b.title for b in author_books]

# ---- Books I have read over the past ~2 years ----#
#I'd highly recommend Homegoing, Half a Yellow Sun, Anna Karenina, and The Color Purple


the_blacker_the_berry = book('The Blacker the Berry', 'Fiction', 'Thurman')
the_blacker_the_berry.rate_book(6)

far_beyond_gold = book('Far Beyond Gold: Running from Fear to Faith', 'Memoir', 'McLaughlin')
far_beyond_gold.rate_book(6)

q = book('1Q84', 'Fiction', 'Murakami')
q.rate_book(6.5)

hijab_butch_blues = book('Hijab_Butch_Blues', 'Memoir', 'Lamya H')  
hijab_butch_blues.rate_book(6.5)

god_of_small_things = book('The God of Small Things', 'Fiction', 'Roy')
god_of_small_things.rate_book(2)
god_of_small_things.trash_book()

half_a_ys = book('Half a Yellow Sun', 'Fiction', 'Adichie')
half_a_ys.rate_book(9)
half_a_ys.add_to_favs()

promised_land = book('The Promised Land', 'Memoir', 'Obama')
promised_land.rate_book(6)

metamorph = book('The Metamorphosis', 'Fiction', 'Kafka')
metamorph.rate_book(7)

klara = book('Klara and the Sun', 'Fiction', 'Ishiguro')
klara.rate_book(5)

never_let_me_go = book('Never Let Me Go', 'Fiction', 'Ishiguro')
never_let_me_go.rate_book(6.5)

remains = book('The Remains of the Day', 'Fiction', 'Ishiguro')
remains.rate_book(7)

hanging_city = book('The Hanging City', 'Fiction', 'Holmberg')
hanging_city.rate_book(4)

thick = book('Thick: And Other Essays', 'Academic', 'Cottom')
thick.rate_book(7.5)

house_of_gold = book('House of Gold', 'Fiction', 'Rwizi')
house_of_gold.rate_book(6.5)

hot_dog = book('Hot Dog Money: Inside the Biggest Scandal in the History of College Sports', 'Non-Fiction', 'Lawson')
hot_dog.rate_book(7.5)

unhoneymooners = book('The Unhoneymooners', 'Fiction', 'Larsen')
unhoneymooners.rate_book(3)

dorian = book('The Picture of Dorian Gray', 'Fiction', 'Wilde')
dorian.rate_book(5)

anna = book('Anna Karenina', 'Fiction', 'Tolstoy')
anna.rate_book(8)
anna.add_to_favs()

grapes = book('The Grapes of Wrath', 'Fiction', 'Steinbeck')
grapes.rate_book(8)

brave_new_world = book('Brave New World', 'Fiction', 'Huxley')
brave_new_world.rate_book(8)

homegoing = book('Homegoing', 'Fiction', 'Gyasi')
homegoing.rate_book(9.5)
homegoing.add_to_favs()

kingdom = book('Transcendent Kingdom', 'Fiction', 'Gyasi')
kingdom.rate_book(8)

purple = book('The Color Purple', 'Fiction', 'Walker')
purple.rate_book(9.5)
purple.add_to_favs()

intermezzo = book('Intermezzo', 'Fiction', 'Rooney')
intermezzo.rate_book(8.5)
intermezzo.add_to_favs()


hello = book('Hello Beautiful', 'Fiction', 'Napolitano')
hello.rate_book(7)

#---------no new books beyond this point!-----------------------#
#reading analysis

book_list = [[b.title, b.author, b.genre, b.rating] for b in book.all_books]
book_table = pd.DataFrame(book_list, columns= ['Title', 'Author', 'Genre', 'Rating'])
# now that we have the table, get ready for some data analysis!!!
#also need to get the newest version of this to github. honestly just replace the entire thing because I made 
#numerous changes to the book datatype itself






pass

