import pytest
from src.libro import Libro


class TestLibro:
    
    def test_crear_libro_valido(self):
        libro = Libro("978-1234567890", "Clean Code", "Robert Martin")
        assert libro.isbn == "978-1234567890"
        assert libro.titulo == "Clean Code"
        assert libro.autor == "Robert Martin"
        assert libro.disponible is True
    
    def test_crear_libro_isbn_vacio(self):
        with pytest.raises(ValueError):
            Libro("", "Clean Code", "Robert Martin")
    
    def test_crear_libro_titulo_vacio(self):
        with pytest.raises(ValueError):
            Libro("978-1234567890", "", "Robert Martin")
    
    def test_crear_libro_autor_vacio(self):
        with pytest.raises(ValueError):
            Libro("978-1234567890", "Clean Code", "")
    
    def test_marcar_libro_no_disponible(self):
        libro = Libro("978-1234567890", "Clean Code", "Robert Martin")
        libro.marcar_no_disponible()
        assert libro.disponible is False
    
    def test_marcar_libro_disponible(self):
        libro = Libro("978-1234567890", "Clean Code", "Robert Martin")
        libro.marcar_no_disponible()
        libro.marcar_disponible()
        assert libro.disponible is True
    
    def test_comparacion_libros_iguales(self):
        libro1 = Libro("978-1234567890", "Clean Code", "Robert Martin")
        libro2 = Libro("978-1234567890", "Clean Code Revisited", "Robert Martin")
        assert libro1 == libro2
    
    def test_comparacion_libros_diferentes(self):
        libro1 = Libro("978-1234567890", "Clean Code", "Robert Martin")
        libro2 = Libro("978-0987654321", "The Pragmatic Programmer", "Hunt & Thomas")
        assert libro1 != libro2
    
    def test_string_libro_disponible(self):
        libro = Libro("978-1234567890", "Clean Code", "Robert Martin")
        assert "Clean Code" in str(libro)
        assert "Disponible" in str(libro)
    
    def test_string_libro_no_disponible(self):
        libro = Libro("978-1234567890", "Clean Code", "Robert Martin")
        libro.marcar_no_disponible()
        assert "No disponible" in str(libro)


@pytest.mark.parametrize("isbn,titulo,autor", [
    ("ISBN001", "Python Basics", "Guido van Rossum"),
    ("ISBN002", "JavaScript Guide", "Douglas Crockford"),
    ("ISBN003", "Design Patterns", "Gang of Four"),
])
def test_crear_multiples_libros(isbn, titulo, autor):
    libro = Libro(isbn, titulo, autor)
    assert libro.isbn == isbn
    assert libro.titulo == titulo
    assert libro.autor == autor
    assert libro.disponible is True
