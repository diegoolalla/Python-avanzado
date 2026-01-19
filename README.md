# Python Avanzado - Práctica de Dataset y Visualización

## Descripción

Este proyecto implementa una práctica completa de Python Avanzado que incluye:

- **Generación de Hostnames Aleatorios**: Algoritmo para crear nombres de servidores con formato profesional
- **Dataset y DataFrame**: Creación de un dataset completo usando Pandas
- **Visualización de Datos**: Múltiples gráficos generados con Matplotlib
- **Análisis Estadístico**: Estadísticas descriptivas y análisis de datos

## Características

### 1. Generador de Hostnames
El script genera nombres de servidores aleatorios con el formato:
```
<tipo>-<ambiente>-<ubicación>-<número>
```

Ejemplo: `web-prod-us-east-042`

### 2. Dataset Generado
Para cada servidor se generan los siguientes datos:
- **hostname**: Nombre del servidor
- **tipo_servidor**: web, db, app, mail, ftp, dns, proxy, cache
- **ambiente**: prod, dev, test, staging, qa
- **ubicacion**: us-east, us-west, eu-west, eu-central, asia-pacific
- **sistema_operativo**: linux, windows, ubuntu, centos, debian
- **cpu_cores**: 2, 4, 8, 16, 32
- **ram_gb**: 4, 8, 16, 32, 64, 128
- **disco_gb**: 100, 250, 500, 1000, 2000
- **uptime_days**: 1-365 días
- **carga_cpu_porcentaje**: 10-95%
- **uso_ram_porcentaje**: 20-90%

### 3. Visualizaciones Generadas
El script genera automáticamente 6 gráficos:

1. **distribucion_tipos_servidor.png**: Gráfico de barras con tipos de servidor
2. **distribucion_ambientes.png**: Gráfico de pastel con distribución de ambientes
3. **distribucion_recursos_hardware.png**: 4 subgráficos con CPU, RAM, Disco y SO
4. **distribucion_uso_recursos.png**: Histogramas de uso de CPU y RAM
5. **uptime_servidores.png**: Scatter plot del uptime de servidores
6. **distribucion_ubicaciones.png**: Gráfico de barras horizontales con ubicaciones

## Requisitos

- Python 3.7+
- pandas >= 2.0.0
- matplotlib >= 3.7.0
- numpy >= 1.24.0

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/diegoolalla/Python-avanzado.git
cd Python-avanzado
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso

Ejecutar el script principal:
```bash
python hostname_dataset.py
```

El script generará:
- Un archivo CSV con el dataset (`servidores_dataset.csv`)
- 6 gráficos PNG con visualizaciones
- Estadísticas descriptivas en la consola

## Estructura del Código

### Clase `HostnameGenerator`
Responsable de generar hostnames y datos de servidores aleatorios.

**Métodos principales:**
- `generate_hostname()`: Genera un hostname aleatorio
- `generate_server_data(hostname)`: Genera datos completos para un servidor
- `generate_dataset(num_servers)`: Genera un dataset completo

### Clase `ServerAnalyzer`
Responsable del análisis y visualización de datos.

**Métodos principales:**
- `mostrar_estadisticas_basicas()`: Muestra estadísticas del DataFrame
- `grafico_distribucion_tipos()`: Gráfico de tipos de servidor
- `grafico_distribucion_ambientes()`: Gráfico de ambientes
- `grafico_recursos_hardware()`: Gráficos de hardware
- `grafico_uso_recursos()`: Histogramas de uso
- `grafico_uptime()`: Gráfico de uptime
- `grafico_ubicaciones()`: Gráfico de ubicaciones
- `generar_todos_los_graficos()`: Genera todos los gráficos

## Ejemplo de Salida

```
======================================================================
PRÁCTICA DE PYTHON AVANZADO
Generación de Dataset de Hostnames y Análisis
======================================================================

[1] Generando hostnames aleatorios...
✓ 100 hostnames generados exitosamente

[2] Creando DataFrame de Pandas...
✓ DataFrame creado exitosamente
✓ Dataset guardado en: servidores_dataset.csv

[3] Analizando datos...

======================================================================
ESTADÍSTICAS BÁSICAS DEL DATASET
======================================================================

Total de servidores: 100

[4] Generando visualizaciones...
✓ Gráfico guardado: distribucion_tipos_servidor.png
✓ Gráfico guardado: distribucion_ambientes.png
...
```

## Módulos de Python Utilizados

### Fundamentos de Python:
- Clases y POO (Programación Orientada a Objetos)
- Métodos y funciones
- Estructuras de datos (listas, diccionarios, conjuntos)
- Comprehensions
- Manejo de strings y formateo
- Control de flujo (if, while, for)

### Python Avanzado:
- **Pandas**: DataFrame, Series, manipulación de datos
- **Matplotlib**: Gráficos de barras, pastel, histogramas, scatter plots
- **NumPy**: Arrays y operaciones numéricas
- **Collections**: Counter para estadísticas
- **Random**: Generación de datos aleatorios

## Evaluación

Esta práctica evalúa:
- ✅ Generación de datos algorítmicos
- ✅ Uso de clases y POO
- ✅ Manipulación de datos con Pandas
- ✅ Visualización con Matplotlib
- ✅ Documentación y buenas prácticas
- ✅ Código limpio y estructurado

## Autor

Diego Olalla

## Licencia

Este proyecto es una práctica educativa de Python Avanzado.
