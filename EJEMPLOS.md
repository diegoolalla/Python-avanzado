# Ejemplos de Uso y Extensión

Este documento muestra ejemplos adicionales de cómo usar y extender el generador de hostnames.

## Ejemplo 1: Generar diferentes cantidades de servidores

```python
from hostname_dataset import HostnameGenerator, ServerAnalyzer
import pandas as pd

# Generar un dataset más pequeño
generator = HostnameGenerator()
dataset_small = generator.generate_dataset(num_servers=50)
df_small = pd.DataFrame(dataset_small)

# Generar un dataset más grande
dataset_large = generator.generate_dataset(num_servers=500)
df_large = pd.DataFrame(dataset_large)
```

## Ejemplo 2: Filtrar servidores por tipo

```python
from hostname_dataset import HostnameGenerator, ServerAnalyzer
import pandas as pd

generator = HostnameGenerator()
dataset = generator.generate_dataset(num_servers=100)
df = pd.DataFrame(dataset)

# Filtrar solo servidores web
web_servers = df[df['tipo_servidor'] == 'web']
print(f"Servidores web: {len(web_servers)}")

# Filtrar solo servidores de producción
prod_servers = df[df['ambiente'] == 'prod']
print(f"Servidores de producción: {len(prod_servers)}")
```

## Ejemplo 3: Análisis de uso de recursos

```python
from hostname_dataset import HostnameGenerator, ServerAnalyzer
import pandas as pd

generator = HostnameGenerator()
dataset = generator.generate_dataset(num_servers=100)
df = pd.DataFrame(dataset)

# Servidores con alta carga de CPU (>80%)
high_cpu = df[df['carga_cpu_porcentaje'] > 80]
print(f"Servidores con alta carga CPU: {len(high_cpu)}")

# Servidores con mucha RAM (>=64 GB)
high_ram = df[df['ram_gb'] >= 64]
print(f"Servidores con >= 64GB RAM: {len(high_ram)}")

# Estadísticas por tipo de servidor
stats_by_type = df.groupby('tipo_servidor')['carga_cpu_porcentaje'].agg(['mean', 'min', 'max'])
print("\nCarga CPU por tipo de servidor:")
print(stats_by_type)
```

## Ejemplo 4: Exportar a diferentes formatos

```python
from hostname_dataset import HostnameGenerator
import pandas as pd
import json

generator = HostnameGenerator()
dataset = generator.generate_dataset(num_servers=100)
df = pd.DataFrame(dataset)

# Exportar a CSV
df.to_csv('servidores.csv', index=False)

# Exportar a JSON
df.to_json('servidores.json', orient='records', indent=2)

# Exportar a Excel (requiere openpyxl)
# df.to_excel('servidores.xlsx', index=False)

# Exportar solo campos específicos
df[['hostname', 'tipo_servidor', 'ambiente']].to_csv('servidores_basico.csv', index=False)
```

## Ejemplo 5: Personalizar el generador

```python
from hostname_dataset import HostnameGenerator
import random

class CustomHostnameGenerator(HostnameGenerator):
    """Generador personalizado con más opciones."""
    
    def __init__(self):
        super().__init__()
        # Añadir más prefijos
        self.prefixes.extend(['api', 'gateway', 'worker', 'scheduler'])
        # Añadir más ubicaciones
        self.locations.extend(['latam-south', 'middle-east', 'africa'])
    
    def generate_hostname(self):
        """Genera hostname con formato personalizado."""
        prefix = random.choice(self.prefixes)
        environment = random.choice(self.environments)
        location = random.choice(self.locations)
        number = random.randint(1, 9999)
        
        # Formato diferente: <prefijo>.<ambiente>.<ubicación>.<número>
        return f"{prefix}.{environment}.{location}.{number:04d}"

# Usar el generador personalizado
custom_gen = CustomHostnameGenerator()
custom_dataset = custom_gen.generate_dataset(num_servers=50)
```

## Ejemplo 6: Análisis avanzado con Pandas

```python
from hostname_dataset import HostnameGenerator
import pandas as pd

generator = HostnameGenerator()
dataset = generator.generate_dataset(num_servers=200)
df = pd.DataFrame(dataset)

# Tabla pivote: promedio de CPU por tipo y ambiente
pivot = df.pivot_table(
    values='carga_cpu_porcentaje',
    index='tipo_servidor',
    columns='ambiente',
    aggfunc='mean'
)
print("Carga CPU promedio por tipo y ambiente:")
print(pivot)

# Correlación entre variables numéricas
correlacion = df[['cpu_cores', 'ram_gb', 'disco_gb', 'carga_cpu_porcentaje']].corr()
print("\nMatriz de correlación:")
print(correlacion)

# Top 10 servidores con mayor uptime
top_uptime = df.nlargest(10, 'uptime_days')[['hostname', 'uptime_days', 'ambiente']]
print("\nTop 10 servidores con mayor uptime:")
print(top_uptime)
```

## Ejemplo 7: Gráficos personalizados

```python
from hostname_dataset import HostnameGenerator
import pandas as pd
import matplotlib.pyplot as plt

generator = HostnameGenerator()
dataset = generator.generate_dataset(num_servers=100)
df = pd.DataFrame(dataset)

# Gráfico de dispersión: CPU vs RAM
plt.figure(figsize=(10, 6))
for ambiente in df['ambiente'].unique():
    data = df[df['ambiente'] == ambiente]
    plt.scatter(data['carga_cpu_porcentaje'], data['uso_ram_porcentaje'], 
                label=ambiente, alpha=0.6)

plt.xlabel('Carga CPU (%)')
plt.ylabel('Uso RAM (%)')
plt.title('Relación entre uso de CPU y RAM por ambiente')
plt.legend()
plt.grid(alpha=0.3)
plt.savefig('cpu_vs_ram_por_ambiente.png', dpi=300)
plt.close()

# Boxplot de uptime por tipo de servidor
plt.figure(figsize=(12, 6))
df.boxplot(column='uptime_days', by='tipo_servidor', figsize=(12, 6))
plt.title('Distribución de Uptime por Tipo de Servidor')
plt.suptitle('')  # Remover el título automático
plt.ylabel('Uptime (días)')
plt.xlabel('Tipo de Servidor')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('uptime_boxplot.png', dpi=300)
plt.close()
```

## Consejos para la Práctica

1. **Experimenta con diferentes tamaños de dataset**: Prueba con 50, 100, 200, 500 servidores
2. **Modifica los datos generados**: Añade nuevos atributos como versión de software, fecha de instalación, etc.
3. **Crea tus propios gráficos**: Explora diferentes tipos de visualizaciones de Matplotlib
4. **Realiza análisis estadísticos**: Usa funciones de Pandas como `describe()`, `groupby()`, `pivot_table()`
5. **Exporta los resultados**: Guarda los datos en diferentes formatos (CSV, JSON, Excel)
6. **Documenta tu código**: Añade comentarios y docstrings para explicar tu lógica

## Recursos Adicionales

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Python Random Module](https://docs.python.org/3/library/random.html)
- [NumPy Documentation](https://numpy.org/doc/)
