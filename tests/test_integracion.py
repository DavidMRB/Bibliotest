import pytest
from datetime import datetime, timedelta
from src.biblioteca import Biblioteca
from src.libro import Libro
from src.usuario import Usuario


class TestIntegracionBiblioteca:
    
    @pytest.fixture
    def biblioteca_completa(self):
        bib = Biblioteca()
        
        libros = [
            Libro("ISBN001", "Clean Code", "Robert Martin"),
            Libro("ISBN002", "Design Patterns", "Gang of Four"),
            Libro("ISBN003", "The Pragmatic Programmer", "Hunt & Thomas"),
            Libro("ISBN004", "Refactoring", "Martin Fowler"),
            Libro("ISBN005", "Code Complete", "Steve McConnell"),
        ]
        
        for libro in libros:
            bib.agregar_libro(libro)
        
        usuarios = [
            Usuario("USR001", "Juan Pérez"),
            Usuario("USR002", "María García"),
            Usuario("USR003", "Carlos López"),
        ]
        
        for usuario in usuarios:
            bib.agregar_usuario(usuario)
        
        return bib
    
    def test_flujo_completo_prestamo_devolucion(self, biblioteca_completa):
        libro = biblioteca_completa.buscar_libro_por_isbn("ISBN001")
        usuario = biblioteca_completa.buscar_usuario("USR001")
        
        assert libro.disponible is True
        
        prestamo = biblioteca_completa.prestar_libro("ISBN001", "USR001")
        assert prestamo is not None
        assert libro.disponible is False
        
        biblioteca_completa.devolver_libro("ISBN001", "USR001")
        assert libro.disponible is True
    
    def test_multiples_usuarios_multiples_libros(self, biblioteca_completa):
        biblioteca_completa.prestar_libro("ISBN001", "USR001")
        biblioteca_completa.prestar_libro("ISBN002", "USR001")
        biblioteca_completa.prestar_libro("ISBN003", "USR002")
        
        assert len(biblioteca_completa.obtener_prestamos_activos()) == 3
        assert len(biblioteca_completa.obtener_libros_disponibles()) == 2
    
    def test_limite_prestamos_usuario(self, biblioteca_completa):
        usuario = biblioteca_completa.buscar_usuario("USR001")
        
        for i in range(1, 6):
            biblioteca_completa.prestar_libro(f"ISBN{i:03d}", "USR001")
        
        assert len(usuario.libros_prestados) == 5
    
    def test_devolucion_libros_prestados(self, biblioteca_completa):
        usuario = biblioteca_completa.buscar_usuario("USR001")
        
        biblioteca_completa.prestar_libro("ISBN001", "USR001")
        biblioteca_completa.prestar_libro("ISBN002", "USR001")
        biblioteca_completa.prestar_libro("ISBN003", "USR001")
        
        assert len(usuario.libros_prestados) == 3
        
        biblioteca_completa.devolver_libro("ISBN001", "USR001")
        assert len(usuario.libros_prestados) == 2
        
        biblioteca_completa.devolver_libro("ISBN002", "USR001")
        assert len(usuario.libros_prestados) == 1
        
        biblioteca_completa.devolver_libro("ISBN003", "USR001")
        assert len(usuario.libros_prestados) == 0
    
    def test_estadisticas_biblioteca_completa(self, biblioteca_completa):
        stats_inicial = biblioteca_completa.obtener_estadisticas()
        assert stats_inicial['total_libros'] == 5 
        assert stats_inicial['libros_disponibles'] == 5
        
        biblioteca_completa.prestar_libro("ISBN001", "USR001")
        biblioteca_completa.prestar_libro("ISBN002", "USR001")
        
        stats_final = biblioteca_completa.obtener_estadisticas()
        assert stats_final['libros_disponibles'] == 3
        assert stats_final['libros_prestados'] == 2
        assert stats_final['prestamos_activos'] == 2


class TestBusquedaAvanzada:
    
    @pytest.fixture
    def biblioteca_datos_ricos(self):
        bib = Biblioteca()
        
        libros_data = [
            ("ISBN001", "Python for Beginners", "John Smith"),
            ("ISBN002", "Python Advanced", "John Smith"),
            ("ISBN003", "JavaScript Basics", "Jane Doe"),
            ("ISBN004", "Web Development", "Jane Doe"),
            ("ISBN005", "Database Design", "Bob Johnson"),
            ("ISBN006", "Machine Learning", "Alice White"),
        ]
        
        for isbn, titulo, autor in libros_data:
            bib.agregar_libro(Libro(isbn, titulo, autor))
        
        return bib
    
    @pytest.mark.parametrize("query,esperado", [
        ("Python", 2),
        ("JavaScript", 1),
        ("Development", 1),
        ("python", 2),
        ("NonExistent", 0),
    ])
    def test_busqueda_titulo_parametrizada(self, biblioteca_datos_ricos, query, esperado):
        resultados = biblioteca_datos_ricos.buscar_libros_por_titulo(query)
        assert len(resultados) == esperado
    
    @pytest.mark.parametrize("query,esperado", [
        ("John Smith", 2),
        ("Jane Doe", 2),
        ("Bob Johnson", 1),
        ("john", 2),
        ("Unknown", 0),
    ])
    def test_busqueda_autor_parametrizada(self, biblioteca_datos_ricos, query, esperado):
        resultados = biblioteca_datos_ricos.buscar_libros_por_autor(query)
        assert len(resultados) == esperado