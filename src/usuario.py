class Usuario:
    
    LIMITE_PRESTAMOS = 5
    
    def __init__(self, id, nombre):
        if not id or not nombre:
            raise ValueError("ID y nombre no pueden estar vacíos")
        
        self.id = id
        self.nombre = nombre
        self.libros_prestados = []
    
    def agregar_libro_prestado(self, libro):
        if len(self.libros_prestados) >= self.LIMITE_PRESTAMOS:
            raise ValueError(f"El usuario ha alcanzado el límite de {self.LIMITE_PRESTAMOS} préstamos")
        
        if libro in self.libros_prestados:
            raise ValueError(f"El libro '{libro.titulo}' ya está en poder del usuario")
        
        self.libros_prestados.append(libro)
    
    def remover_libro_prestado(self, libro):
        if libro not in self.libros_prestados:
            raise ValueError(f"El usuario no tiene el libro '{libro.titulo}'")
        
        self.libros_prestados.remove(libro)
    
    def tiene_libro(self, libro):
        return libro in self.libros_prestados
    
    def __str__(self):
        cantidad = len(self.libros_prestados)
        return f"{self.nombre} (ID: {self.id}) - {cantidad} libro(s) prestado(s)"
    
    def __eq__(self, otro):
        if not isinstance(otro, Usuario):
            return False
        return self.id == otro.id
