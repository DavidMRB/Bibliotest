from .prestamo import Prestamo


class Biblioteca:
    
    def __init__(self):
        self.catalogo = []
        self.usuarios = []
        self.prestamos = []
        self._contador_prestamos = 0
    
    def agregar_libro(self, libro):
        if libro in self.catalogo:
            raise ValueError(f"El libro con ISBN {libro.isbn} ya existe en el catálogo")
        self.catalogo.append(libro)
    
    def remover_libro(self, isbn):
        libro = self.buscar_libro_por_isbn(isbn)
        if not libro:
            raise ValueError(f"No se encontró libro con ISBN {isbn}")
        if not libro.disponible:
            raise ValueError(f"No se puede remover el libro '{libro.titulo}' porque está prestado")
        self.catalogo.remove(libro)
    
    def buscar_libro_por_isbn(self, isbn):
        for libro in self.catalogo:
            if libro.isbn == isbn:
                return libro
        return None
    
    def buscar_libros_por_titulo(self, titulo):
        return [libro for libro in self.catalogo 
                if titulo.lower() in libro.titulo.lower()]
    
    def buscar_libros_por_autor(self, autor):
        query_lower = autor.lower()
        resultados = []
        
        for libro in self.catalogo:
            autor_palabras = libro.autor.lower().split()
            
            # Buscar si alguna palabra del autor contiene el query
            # O si el query completo está en el nombre del autor como palabras separadas
            if any(query_lower in palabra or palabra in query_lower for palabra in autor_palabras):
                resultados.append(libro)
        
        return resultados
    
    def obtener_libros_disponibles(self):
        return [libro for libro in self.catalogo if libro.disponible]
    
    def agregar_usuario(self, usuario):
        if usuario in self.usuarios:
            raise ValueError(f"El usuario con ID {usuario.id} ya existe")
        self.usuarios.append(usuario)
    
    def remover_usuario(self, id_usuario):
        usuario = self.buscar_usuario(id_usuario)
        if not usuario:
            raise ValueError(f"No se encontró usuario con ID {id_usuario}")
        if usuario.libros_prestados:
            raise ValueError(f"No se puede remover al usuario '{usuario.nombre}' "
                           "porque tiene préstamos activos")
        self.usuarios.remove(usuario)
    
    def buscar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                return usuario
        return None
    
    def prestar_libro(self, isbn, id_usuario):
        libro = self.buscar_libro_por_isbn(isbn)
        if not libro:
            raise ValueError(f"No se encontró libro con ISBN {isbn}")
        if not libro.disponible:
            raise ValueError(f"El libro '{libro.titulo}' no está disponible")
        
        usuario = self.buscar_usuario(id_usuario)
        if not usuario:
            raise ValueError(f"No se encontró usuario con ID {id_usuario}")
        
        self._contador_prestamos += 1
        prestamo_id = f"PRES{self._contador_prestamos:05d}"
        prestamo = Prestamo(prestamo_id, libro, usuario)
        
        libro.marcar_no_disponible()
        usuario.agregar_libro_prestado(libro)
        self.prestamos.append(prestamo)
        
        return prestamo
    
    def devolver_libro(self, isbn, id_usuario):
        libro = self.buscar_libro_por_isbn(isbn)
        if not libro:
            raise ValueError(f"No se encontró libro con ISBN {isbn}")
        
        usuario = self.buscar_usuario(id_usuario)
        if not usuario:
            raise ValueError(f"No se encontró usuario con ID {id_usuario}")
        
        prestamo = self._buscar_prestamo_activo(isbn, id_usuario)
        if not prestamo:
            raise ValueError(f"No existe un préstamo activo para este libro y usuario")
        
        prestamo.devolver_libro()
        libro.marcar_disponible()
        usuario.remover_libro_prestado(libro)
    
    def _buscar_prestamo_activo(self, isbn, id_usuario):
        for prestamo in self.prestamos:
            if (prestamo.activo and 
                prestamo.libro.isbn == isbn and 
                prestamo.usuario.id == id_usuario):
                return prestamo
        return None
    
    def obtener_prestamos_activos(self):
        return [p for p in self.prestamos if p.activo]
    
    def obtener_prestamos_retrasados(self):
        return [p for p in self.prestamos if p.esta_retrasado()]
    
    def obtener_prestamos_usuario(self, id_usuario):
        return [p for p in self.prestamos if p.usuario.id == id_usuario]
    
    def obtener_estadisticas(self):
        return {
            'total_libros': len(self.catalogo),
            'libros_disponibles': len(self.obtener_libros_disponibles()),
            'libros_prestados': len(self.catalogo) - len(self.obtener_libros_disponibles()),
            'total_usuarios': len(self.usuarios),
            'prestamos_activos': len(self.obtener_prestamos_activos()),
            'prestamos_retrasados': len(self.obtener_prestamos_retrasados()),
            'total_prestamos': len(self.prestamos)
        }