from datetime import datetime, timedelta


class Prestamo:
    DIAS_PERMITIDOS = 14
    
    def __init__(self, id, libro, usuario, fecha_prestamo=None):
        if not id or not libro or not usuario:
            raise ValueError("ID, libro y usuario no pueden ser nulos")
        
        self.id = id
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo or datetime.now()
        self.fecha_devolucion = None
        self.activo = True
    
    def devolver_libro(self, fecha_devolucion=None):
        if not self.activo:
            raise ValueError("Este préstamo ya ha sido devuelto")
        
        self.fecha_devolucion = fecha_devolucion or datetime.now()
        self.activo = False
    
    def esta_retrasado(self, fecha_actual=None):
        if not self.activo:
            return False
        
        fecha_actual = fecha_actual or datetime.now()
        dias_transcurridos = (fecha_actual - self.fecha_prestamo).days
        
        # El préstamo se retrasa cuando han pasado MÁS de 14 días
        return dias_transcurridos > self.DIAS_PERMITIDOS
    
    def dias_restantes(self, fecha_actual=None):
        if not self.activo:
            return 0
        
        fecha_actual = fecha_actual or datetime.now()
        fecha_limite = self.fecha_prestamo + timedelta(days=self.DIAS_PERMITIDOS)
        dias_restantes = (fecha_limite - fecha_actual).days
        
        return dias_restantes
    
    def __str__(self):
        estado = "Activo" if self.activo else "Devuelto"
        return (f"Préstamo {self.id}: {self.libro.titulo} prestado a {self.usuario.nombre} "
                f"desde {self.fecha_prestamo.strftime('%d/%m/%Y')} [{estado}]")
    
    def __eq__(self, otro):
        if not isinstance(otro, Prestamo):
            return False
        return self.id == otro.id