import pytest
from src.usuario import Usuario
from src.libro import Libro


class TestUsuario:
    
    @pytest.fixture
    def usuario(self):
        return Usuario("USR001", "Juan Pérez")
    
    @pytest.fixture
    def libro(self):
        return Libro("978-1234567890", "Clean Code", "Robert Martin")
    
    def test_crear_usuario_valido(self, usuario):
        assert usuario.id == "USR001"
        assert usuario.nombre == "Juan Pérez"
        assert usuario.libros_prestados == []
    
    def test_crear_usuario_id_vacio(self):
        with pytest.raises(ValueError):
            Usuario("", "Juan Pérez")
    
    def test_crear_usuario_nombre_vacio(self):
        with pytest.raises(ValueError):
            Usuario("USR001", "")
    
    def test_agregar_libro_prestado(self, usuario, libro):
        usuario.agregar_libro_prestado(libro)
        assert len(usuario.libros_prestados) == 1
        assert libro in usuario.libros_prestados
    
    def test_agregar_libro_repetido(self, usuario, libro):
        usuario.agregar_libro_prestado(libro)
        with pytest.raises(ValueError):
            usuario.agregar_libro_prestado(libro)
    
    def test_agregar_libros_hasta_limite(self, usuario):
        for i in range(Usuario.LIMITE_PRESTAMOS):
            libro = Libro(f"ISBN{i:03d}", f"Libro {i}", f"Autor {i}")
            usuario.agregar_libro_prestado(libro)
        assert len(usuario.libros_prestados) == Usuario.LIMITE_PRESTAMOS
    
    def test_exceder_limite_prestamos(self, usuario):
        for i in range(Usuario.LIMITE_PRESTAMOS):
            libro = Libro(f"ISBN{i:03d}", f"Libro {i}", f"Autor {i}")
            usuario.agregar_libro_prestado(libro)
        
        libro_extra = Libro("ISBNX", "Libro Extra", "Autor Extra")
        with pytest.raises(ValueError):
            usuario.agregar_libro_prestado(libro_extra)
    
    def test_remover_libro_prestado(self, usuario, libro):
        usuario.agregar_libro_prestado(libro)
        usuario.remover_libro_prestado(libro)
        assert len(usuario.libros_prestados) == 0
    
    def test_remover_libro_no_poseido(self, usuario, libro):
        with pytest.raises(ValueError):
            usuario.remover_libro_prestado(libro)
    
    def test_tiene_libro(self, usuario, libro):
        assert usuario.tiene_libro(libro) is False
        usuario.agregar_libro_prestado(libro)
        assert usuario.tiene_libro(libro) is True
    
    def test_string_usuario(self, usuario):
        assert "Juan Pérez" in str(usuario)
        assert "USR001" in str(usuario)


@pytest.mark.parametrize("id_usuario,nombre", [
    ("USR001", "Juan Pérez"),
    ("USR002", "María García"),
    ("USR003", "Carlos López"),
])
def test_crear_multiples_usuarios(id_usuario, nombre):
    usuario = Usuario(id_usuario, nombre)
    assert usuario.id == id_usuario
    assert usuario.nombre == nombre