class Libro:
    def __init__(self, isbn, titulo, autor):
        if not isbn or not titulo or not autor:
            raise ValueError("ISBN, título y autor no pueden estar vacíos")
        
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.disponible = True
    
    def marcar_no_disponible(self):
        self.disponible = False
    
    def marcar_disponible(self):
        self.disponible = True
    
    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"{self.titulo} - {self.autor} (ISBN: {self.isbn}) [{estado}]"
    
    def __eq__(self, otro):
        if not isinstance(otro, Libro):
            return False
        return self.isbn == otro.isbn
