# 📚 Bibliotest - Sistema de Gestión de Biblioteca

![Python](https://img.shields.io/badge/python-3.13+-blue.svg)
![Tests](https://img.shields.io/badge/tests-68%20passed%2C%202%20failed-yellow.svg)
![Coverage](https://img.shields.io/badge/coverage-84%25-yellow.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Sistema de gestión de biblioteca desarrollado en **Python** con arquitectura orientada a objetos, diseñado para demostrar las **mejores prácticas de testing automatizado** mediante **pytest** y análisis de cobertura con **pytest-cov**.

El proyecto implementa funcionalidades completas de una biblioteca: gestión de libros, usuarios, préstamos y devoluciones, con validación de reglas de negocio y detección automática de retrasos.

---

## 🎯 Objetivo del Proyecto

Demostrar la **eficiencia y confiabilidad del testing automatizado** frente a las pruebas manuales tradicionales, reduciendo el tiempo de validación en un **97.5%** (de 40 minutos a menos de 1 minuto).

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.13.3** - Lenguaje principal
- **pytest 8.4.2** - Framework de testing
- **pytest-cov 7.0.0** - Análisis de cobertura de código
- **Git** - Control de versiones

---

## 🚀 Instalación y Ejecución

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/DavidMRB/Bibliotest.git
cd Bibliotest
```

### 2️⃣ Crear entorno virtual (recomendado)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Ejecutar todas las pruebas
```bash
pytest tests/ -v
```

**Resultado esperado:** ✅ **68 tests passed, 2 failed in 0.68s**

### 5️⃣ Generar reporte de cobertura
```bash
pytest --cov=src --cov-report=html
```

Para visualizar el reporte HTML:

**Windows:**
```bash
start htmlcov/index.html
```

**macOS/Linux:**
```bash
open htmlcov/index.html
```

---

## 📊 Cobertura de Código

El proyecto mantiene una cobertura del **84%** en el código fuente:

![Reporte de Cobertura](cobertura.png)

| Módulo | Statements | Missing | Cobertura |
|--------|------------|---------|-----------|
| `__init__.py` | 0 | 0 | 100% |
| `biblioteca.py` | 93 | 20 | 78% |
| `libro.py` | 19 | 1 | 95% |
| `prestamo.py` | 37 | 7 | 81% |
| `usuario.py` | 27 | 1 | 96% |
| **Total** | **176** | **29** | **84%** |

---

## 📁 Estructura del Proyecto

```
Bibliotest/
 ┣ 📂 src/                  # Código fuente
 ┃ ┣ 📄 biblioteca.py       # Clase principal del sistema
 ┃ ┣ 📄 libro.py            # Modelo de Libro
 ┃ ┣ 📄 prestamo.py         # Modelo de Préstamo
 ┃ ┣ 📄 usuario.py          # Modelo de Usuario
 ┃ ┗ 📄 __init__.py
 ┣ 📂 tests/                # Suite de pruebas
 ┃ ┣ 📄 test_biblioteca.py  # Tests unitarios de Biblioteca
 ┃ ┣ 📄 test_integracion.py # Tests de integración
 ┃ ┣ 📄 test_libro.py       # Tests de Libro
 ┃ ┣ 📄 test_prestamo.py    # Tests de Préstamo
 ┃ ┣ 📄 test_usuario.py     # Tests de Usuario
 ┃ ┗ 📄 __init__.py
 ┣ 📂 htmlcov/              # Reporte de cobertura (generado)
 ┣ 📄 pytest.ini            # Configuración de pytest
 ┣ 📄 requirements.txt      # Dependencias
 ┣ 📄 .gitignore
 ┗ 📄 README.md
```

---

## ✨ Funcionalidades Implementadas

### 📚 Gestión de Libros
- ✅ Agregar libros al catálogo con validación de ISBN único
- ✅ Buscar por ISBN, título o autor (case-insensitive)
- ✅ Eliminar libros (solo si están disponibles)
- ✅ Control de disponibilidad automático

### 👥 Gestión de Usuarios
- ✅ Registro de usuarios con ID único
- ✅ Límite de 5 libros prestados simultáneamente
- ✅ Historial de préstamos activos
- ✅ Validaciones de integridad

### 📖 Gestión de Préstamos
- ✅ Sistema de préstamos con ID autogenerado
- ✅ Período de préstamo: 14 días
- ✅ Detección automática de retrasos
- ✅ Control de devoluciones con actualización de estados
- ✅ Cálculo de días restantes

### 📈 Estadísticas y Reportes
- ✅ Total de libros y libros disponibles
- ✅ Préstamos activos y retrasados
- ✅ Libros prestados por usuario
- ✅ Métricas generales del sistema

---

## 🧪 Comandos de Testing

### Ejecutar todos los tests con salida detallada
```bash
pytest tests/ -v
```

### Ejecutar un archivo específico
```bash
pytest tests/test_libro.py -v
```

### Ejecutar tests por palabra clave
```bash
pytest tests/ -k "prestamo" -v
```

### Ejecutar solo tests de integración
```bash
pytest tests/test_integracion.py -v
```

### Generar reporte de cobertura en terminal
```bash
pytest --cov=src --cov-report=term
```

### Generar reporte HTML completo
```bash
pytest --cov=src --cov-report=html
```

### Ver tests que fallan primero
```bash
pytest tests/ -x  # Se detiene en el primer fallo
```

### Modo verboso con salida de print
```bash
pytest tests/ -v -s
```

---

## 📊 Métricas del Proyecto

| Métrica | Valor |
|---------|-------|
| **Total de tests** | 70 |
| **Tests exitosos** | 68 |
| **Tests fallidos** | 2 |
| **Tests unitarios** | 47 |
| **Tests de integración** | 23 |
| **Cobertura de código** | 84% |
| **Clases principales** | 4 (Biblioteca, Libro, Usuario, Préstamo) |
| **Métodos públicos** | 20+ |
| **Tiempo de ejecución** | 0.68 segundos |
| **Líneas de código** | 176 |
| **Tests parametrizados** | 15 |

---

## ⚠️ Tests Pendientes

Actualmente hay **2 tests fallidos** que requieren corrección:

1. ❌ `test_integracion.py::TestIntegracionBiblioteca::test_limite_prestamos_usuario`
2. ❌ `test_integracion.py::TestBusquedaAvanzada::test_busqueda_autor_parametrizada[john-2]`

Estos tests están siendo corregidos para alcanzar el 100% de éxito en la suite de pruebas.

---

## ⏱️ Comparativa: Testing Manual vs Automatizado

### 🔴 Escenario Manual (Tradicional)

Durante las pruebas manuales, cada módulo requiere ejecución y verificación individual con ingreso manual de datos y observación de resultados.

| Actividad | Tiempo estimado |
|-----------|-----------------|
| Configuración del entorno | 10 min |
| Pruebas de registro y búsqueda | 8 min |
| Pruebas de préstamos y devoluciones | 12 min |
| Validación de errores y casos límite | 10 min |
| **TOTAL** | **≈ 40 minutos** |

**Problemas del testing manual:**
- ❌ Propenso a errores humanos
- ❌ No repetible consistentemente
- ❌ Difícil de escalar
- ❌ Sin trazabilidad automática
- ❌ Requiere re-ejecución completa ante cambios

---

### 🟢 Escenario Automatizado (pytest)

Con **pytest**, las **70 pruebas** se ejecutan automáticamente en menos de 1 segundo, con reporte instantáneo de cobertura.

| Actividad | Tiempo estimado |
|-----------|-----------------|
| Instalación inicial (una vez) | 1 min |
| Ejecución de 70 tests | 0.68 seg |
| Generación de reporte HTML | 2 seg |
| **TOTAL** | **≈ 1 minuto** |

**Ventajas del testing automatizado:**
- ✅ **97.5% más rápido** que testing manual
- ✅ Repetible y consistente
- ✅ Detecta regresiones inmediatamente
- ✅ Cobertura de código medible
- ✅ Integrable con CI/CD
- ✅ Documentación viva del comportamiento del sistema

---

## 📈 Casos de Prueba Implementados

### Tests Unitarios
- Creación y validación de entidades
- Métodos de búsqueda (ISBN, título, autor)
- Agregar/remover libros y usuarios
- Validación de restricciones de negocio
- Manejo de excepciones

### Tests de Integración
- Flujo completo de préstamo y devolución
- Múltiples usuarios con múltiples libros
- Límites de préstamos por usuario
- Búsquedas parametrizadas
- Estadísticas del sistema
- Detección de retrasos con fechas simuladas

### Tests Parametrizados
- Búsquedas con diferentes queries
- Diferentes escenarios de retraso (0, 5, 14, 15, 20 días)
- Creación de múltiples instancias

---

## 🎓 Conceptos de Testing Demostrados

- ✅ **Tests unitarios** - Pruebas aisladas de componentes
- ✅ **Tests de integración** - Pruebas de interacción entre módulos
- ✅ **Fixtures** - Preparación de datos de prueba reutilizables
- ✅ **Parametrización** - Tests con múltiples entradas
- ✅ **Assertions** - Validaciones de comportamiento esperado
- ✅ **Manejo de excepciones** - Validación de errores controlados
- ✅ **Cobertura de código** - Medición de líneas ejecutadas
- ✅ **Mocking de fechas** - Simulación de escenarios temporales

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

Asegúrate de que todos los tests pasen y la cobertura se mantenga sobre el 80%.

---

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo `LICENSE` para más detalles.

---

## 👨‍💻 Autor

**David Mauricio Rangel Báez**

- GitHub: [@DavidMRB](https://github.com/DavidMRB)
- Proyecto: [Bibliotest](https://github.com/DavidMRB/Bibliotest)

---

## 📅 Información del Proyecto

- **Fecha de creación:** Octubre 2025
- **Última actualización:** Octubre 15, 2025
- **Estado:** 🚧 En desarrollo (2 tests pendientes de corrección)
- **Versión de Python:** 3.13.3
- **Framework de testing:** pytest 8.4.2
- **Cobertura actual:** 84%

---

## 🎯 Conclusión

**Bibliotest** demuestra que el testing automatizado no solo es más rápido, sino también más confiable y mantenible que las pruebas manuales. Con una inversión inicial en la creación de tests, se obtienen beneficios continuos en calidad, velocidad de desarrollo y confianza en el código.

**Reducción de tiempo:** 40 minutos → 0.68 segundos (**97.5% más rápido**)  
**Cobertura alcanzada:** 84%  
**Tests exitosos:** 68/70 (97.1%)  

---

*Desarrollado como proyecto educativo para demostrar las mejores prácticas de testing en Python* 🐍✨