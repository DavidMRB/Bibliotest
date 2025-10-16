import pytest
from datetime import datetime, timedelta
from src.prestamo import Prestamo
from src.libro import Libro
from src.usuario import Usuario


class TestPrestamo:
    
    @pytest.fixture
    def libro(self):
        return Libro("978-1234567890", "Clean Code", "Robert Martin")
    
    @pytest.fixture
    def usuario(self):
        return Usuario("USR001", "Juan Pérez")
    
    @pytest.fixture
    def prestamo(self, libro, usuario):
        return Prestamo("PRES00001", libro, usuario)
    
    def test_crear_prestamo_valido(self, prestamo):
        assert prestamo.id == "PRES00001"
        assert prestamo.activo is True
        assert prestamo.fecha_devolucion is None
    
    def test_crear_prestamo_id_nulo(self, libro, usuario):
        with pytest.raises(ValueError):
            Prestamo(None, libro, usuario)
    
    def test_crear_prestamo_libro_nulo(self, usuario):
        with pytest.raises(ValueError):
            Prestamo("PRES00001", None, usuario)
    
    def test_crear_prestamo_usuario_nulo(self, libro):
        with pytest.raises(ValueError):
            Prestamo("PRES00001", libro, None)
    
    def test_devolver_libro(self, prestamo):
        prestamo.devolver_libro()
        assert prestamo.activo is False
        assert prestamo.fecha_devolucion is not None
    
    def test_devolver_libro_dos_veces(self, prestamo):
        prestamo.devolver_libro()
        with pytest.raises(ValueError):
            prestamo.devolver_libro()
    
    def test_prestamo_no_retrasado(self, prestamo):
        assert prestamo.esta_retrasado() is False
    
    def test_prestamo_retrasado(self, libro, usuario):
        fecha_prestamo = datetime.now() - timedelta(days=20)
        prestamo = Prestamo("PRES00001", libro, usuario, fecha_prestamo=fecha_prestamo)
        assert prestamo.esta_retrasado() is True
    
    def test_dias_restantes(self, prestamo):
        dias = prestamo.dias_restantes()
        assert 13 <= dias <= 14


@pytest.mark.parametrize("dias_atraso", [0, 5, 14, 15, 20])
def test_prestamo_retrasos(dias_atraso):
    libro = Libro("ISBN001", "Libro Test", "Autor Test")
    usuario = Usuario("USR001", "Usuario Test")
    fecha_prestamo = datetime.now() - timedelta(days=dias_atraso)
    prestamo = Prestamo("PRES00001", libro, usuario, fecha_prestamo=fecha_prestamo)
    
    if dias_atraso > 14:
        assert prestamo.esta_retrasado() is True
    else:
        assert prestamo.esta_retrasado() is False
