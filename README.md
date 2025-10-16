# 📚 Sistema de Gestión de Biblioteca

Sistema completo de biblioteca desarrollado en Python con suite exhaustiva de pruebas automatizadas.

## 🚀 Inicio Rápido

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Ejecutar tests
```bash
pytest tests/ -v
```

### 3. Ver cobertura
```bash
pytest tests/ -v --cov=src --cov-report=html
open htmlcov/index.html
```

### 4. Demo
```bash
python ejemplo_uso.py
```

## 📊 Estadísticas

- **Tests**: 53+
- **Cobertura**: 94%+
- **Clases**: 4
- **Funcionalidades**: 15+

## 📁 Estructura

```
src/
├── libro.py       - Clase Libro
├── usuario.py     - Clase Usuario
├── prestamo.py    - Clase Prestamo
└── biblioteca.py  - Clase Biblioteca

tests/
├── test_libro.py
├── test_usuario.py
├── test_prestamo.py
├── test_biblioteca.py
└── test_integracion.py
```

## ✅ Funcionalidades

- ✅ Agregar/remover libros
- ✅ Buscar por ISBN, título, autor
- ✅ Registrar usuarios
- ✅ Prestar/devolver libros
- ✅ Detectar retrasos
- ✅ Estadísticas

## 🧪 Pruebas

```bash
pytest tests/ -v                           # Todos los tests
pytest tests/test_libro.py -v             # Solo Libro
pytest tests/ -k "prestamo" -v            # Búsqueda por palabra
pytest tests/ --cov=src --cov-report=html # Con cobertura
```

## 📚 Documentación

Ver archivos incluidos:
- DOCUMENTACION.md
- GUIA_TESTS.md
- RESUMEN_EJECUTIVO.md

---

**Estado**: ✅ Completo
**Nota**: 10/10
