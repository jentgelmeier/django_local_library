import datetime
from django.test import TestCase

from catalog.models import Author, Book, BookInstance, Genre, Language

class AuthorModelTeset(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')
    
    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')
    
    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEqual(field_label, 'date of birth')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEqual(field_label, 'died')
    
    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').max_length
        self.assertEqual(field_label, 100)
    
    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').max_length
        self.assertEqual(field_label, 100)
    
    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEqual(str(author), expected_object_name)
    
    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined
        self.assertEqual(author.get_absolute_url(), '/catalog/author/1')

class BookModelTeset(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Book.objects.create(title='BookTitle', summary='a summary', isbn='1234567890123' )

    # Should I test the model fields: author, language, genre??
    
    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')
    
    def test_summary_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('summary').verbose_name
        self.assertEqual(field_label, 'summary')
    
    def test_isbn_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('isbn').verbose_name
        self.assertEqual(field_label, 'ISBN')
    
    def test_title_max_length(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').max_length
        self.assertEqual(field_label, 200)
    
    def test_summary_max_length(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('summary').max_length
        self.assertEqual(field_label, 1000)
    
    def test_isbn_max_length(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('isbn').max_length
        self.assertEqual(field_label, 13)
    
    # def test_object_name_is_last_name_comma_first_name(self):
    #     book = Book.objects.get(id=1)
    #     expected_object_name = f'{book.last_name}, {book.first_name}'
    #     self.assertEqual(str(book), expected_object_name)
    
    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        # This will also fail if the urlconf is not defined
        self.assertEqual(book.get_absolute_url(), '/catalog/book/1')

class BookInstanceModelTeset(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        BookInstance.objects.create(imprint='Scholastic', due_back=datetime.date.today(), status='o' )

    # Should I test the model fields: book, borrower?
    
    def test_imprint_label(self):
        bookinst = BookInstance.objects.get(imprint='Scholastic')
        field_label = bookinst._meta.get_field('imprint').verbose_name
        self.assertEqual(field_label, 'imprint')
    
    def test_due_back_label(self):
        bookinst = BookInstance.objects.get(imprint='Scholastic')
        field_label = bookinst._meta.get_field('due_back').verbose_name
        self.assertEqual(field_label, 'due back')
    
    def test_status_label(self):
        bookinst = BookInstance.objects.get(imprint='Scholastic')
        field_label = bookinst._meta.get_field('status').verbose_name
        self.assertEqual(field_label, 'status')
    
    def test_imprint_max_length(self):
        bookinst = BookInstance.objects.get(imprint='Scholastic')
        field_label = bookinst._meta.get_field('imprint').max_length
        self.assertEqual(field_label, 200)
    
    def test_status_max_length(self):
        bookinst = BookInstance.objects.get(imprint='Scholastic')
        field_label = bookinst._meta.get_field('status').max_length
        self.assertEqual(field_label, 1)

class GenreInstanceModelTeset(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Genre.objects.create(name='Romance')
    
    def test_imprint_label(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
    
    def test_imprint_max_length(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field('name').max_length
        self.assertEqual(field_label, 200)

class LanguageInstanceModelTeset(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Language.objects.create(name='Spanish')
    
    def test_imprint_label(self):
        language = Language.objects.get(id=1)
        field_label = language._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
    
    def test_imprint_max_length(self):
        language = Language.objects.get(id=1)
        field_label = language._meta.get_field('name').max_length
        self.assertEqual(field_label, 200)