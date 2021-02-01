from p_library.models import Author, Book
books = Book.objects.all()
# for book in books:
#     print('\t', book.title, " ", book.author.full_name)

prices = []
# Ищем самую дорогую книгу
for book in books:
    prices.append(book.price)
print(prices)
prices.sort()
print(prices[-1])

#Сколько в библиотеке копий самой дешёвой книги
print(prices[0])
cheapest_book = books.filter(price = prices[0])[0]
print(f'{cheapest_book.title}, Количество: {cheapest_book.copy_count}')

#Сколько стоят все библиотечные книги авторов, у которых больше одной книги?
authors = Author.objects.all()
pushkin = authors.get(full_name="Пушкин Александр Сергеевич")
pushkin_books = books.filter(author=pushkin)
adams = authors.get(full_name="Douglas Adams")
adams_books = books.filter(author=adams)

pushkin_count = 0
adams_count = 0
for book in adams_books:
    adams_count += book.price * book.copy_count
    print(adams_count)


#Сколько стоят все библиотечные книги иностранных писателей?
foreign_count = 0
foreign_books = []
foreign_authors = authors.exclude(country__contains="RU")
for author in foreign_authors:
    for book in books:
        if book.author == author.full_name:
            foreign_books.append(book)
for book in adams_books:
    print(f"{book.title}, {book.copy_count},  {book.price} ")


