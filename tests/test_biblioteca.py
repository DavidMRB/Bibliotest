import pytest
from src.biblioteca import Biblioteca
from src.libro import Libro
from src.usuario import Usuario


class TestBiblioteca:
    
    @pytest.fixture
    def biblioteca(self):
        return Biblioteca()
    
    @pytest.fixture
    def libro(self):
        return Libro("978-1234567890", "Clean Code", "Robert Martin")
    
    @pytest.fixture
    def usuario(self):
        return Usuario("USR001", "Juan Pérez")
    
    @pytest.fixture
    def biblioteca_con_datos(self, biblioteca, libro, usuario):
        biblioteca.agregar_libro(libro)
        biblioteca.agregar_usuario(usuario)
        return biblioteca
    
    def test_biblioteca_inicial_vacia(self, biblioteca):
        assert len(biblioteca.catalogo) == 0
        assert len(biblioteca.usuarios) == 0
        assert len(biblioteca.prestamos) == 0
    
    def test_agregar_libro(self, biblioteca, libro):
        biblioteca.agregar_libro(libro)
        assert len(biblioteca.catalogo) == 1
        assert libro in biblioteca.catalogo
    
    def test_agregar_libro_duplicado(self, biblioteca, libro):
        biblioteca.agregar_libro(libro)
        with pytest.raises(ValueError):
            biblioteca.agregar_libro(libro)
    
    def test_buscar_libro_por_isbn(self, biblioteca_con_datos, libro):
        resultado = biblioteca_con_datos.buscar_libro_por_isbn(libro.isbn)
        assert resultado == libro
    
    def test_buscar_libro_no_existe(self, biblioteca):
        resultado = biblioteca.buscar_libro_por_isbn("ISBN-NO-EXISTE")
        assert resultado is None
    
    def test_buscar_libros_por_titulo(self, biblioteca):
        libro1 = Libro("ISBN001", "Clean Code", "Robert Martin")
        libro2 = Libro("ISBN002", "Clean Architecture", "Robert Martin")
        biblioteca.agregar_libro(libro1)
        biblioteca.agregar_libro(libro2)
        
        resultados = biblioteca.buscar_libros_por_titulo("Clean")
        assert len(resultados) == 2
    
    def test_agregar_usuario(self, biblioteca, usuario):
        biblioteca.agregar_usuario(usuario)
        assert len(biblioteca.usuarios) == 1
    
    def test_agregar_usuario_duplicado(self, biblioteca, usuario):
        biblioteca.agregar_usuario(usuario)
        with pytest.raises(ValueError):
            biblioteca.agregar_usuario(usuario)
    
    def test_buscar_usuario(self, biblioteca_con_datos, usuario):
        resultado = biblioteca_con_datos.buscar_usuario(usuario.id)
        assert resultado == usuario
    
    def test_prestar_libro(self, biblioteca_con_datos, libro, usuario):
        prestamo = biblioteca_con_datos.prestar_libro(libro.isbn, usuario.id)
        assert prestamo is not None
        assert prestamo.activo is True
        assert libro.disponible is False
    
    def test_prestar_libro_no_disponible(self, biblioteca_con_datos, libro, usuario):
        libro.marcar_no_disponible()
        with pytest.raises(ValueError):
            biblioteca_con_datos.prestar_libro(libro.isbn, usuario.id)
    
    def test_devolver_libro(self, biblioteca_con_datos, libro, usuario):
        biblioteca_con_datos.prestar_libro(libro.isbn, usuario.id)
        biblioteca_con_datos.devolver_libro(libro.isbn, usuario.id)
        assert libro.disponible is True
    
    def test_obtener_libros_disponibles(self, biblioteca_con_datos, libro):
        assert len(biblioteca_con_datos.obtener_libros_disponibles()) == 1
        libro.marcar_no_disponible()
        assert len(biblioteca_con_datos.obtener_libros_disponibles()) == 0
    
    def test_estadisticas_biblioteca(self, biblioteca_con_datos, libro, usuario):
        biblioteca_con_datos.prestar_libro(libro.isbn, usuario.id)
        stats = biblioteca_con_datos.obtener_estadisticas()
        assert stats['total_libros'] == 1
        assert stats['libros_disponibles'] == 0
        assert stats['libros_prestados'] == 1
