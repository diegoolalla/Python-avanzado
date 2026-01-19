#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Práctica de Python Avanzado
Generación de Dataset de Hostnames y Análisis con Pandas y Matplotlib

Este script genera nombres de servidores (hostnames) aleatorios,
crea un DataFrame de Pandas y genera gráficos con Matplotlib.
"""

import random
import string
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


class HostnameGenerator:
    """Generador de nombres de servidores aleatorios."""
    
    def __init__(self):
        """Inicializa el generador con listas de prefijos, tipos y ubicaciones."""
        self.prefixes = ['web', 'db', 'app', 'mail', 'ftp', 'dns', 'proxy', 'cache']
        self.environments = ['prod', 'dev', 'test', 'staging', 'qa']
        self.locations = ['us-east', 'us-west', 'eu-west', 'eu-central', 'asia-pacific']
        self.os_types = ['linux', 'windows', 'ubuntu', 'centos', 'debian']
    
    def generate_hostname(self):
        """
        Genera un hostname aleatorio con formato:
        <prefijo>-<ambiente>-<ubicación>-<número>
        
        Returns:
            str: Hostname generado
        """
        prefix = random.choice(self.prefixes)
        environment = random.choice(self.environments)
        location = random.choice(self.locations)
        number = random.randint(1, 999)
        
        return f"{prefix}-{environment}-{location}-{number:03d}"
    
    def generate_server_data(self, hostname):
        """
        Genera datos adicionales para un servidor.
        
        Args:
            hostname (str): Nombre del servidor
            
        Returns:
            dict: Diccionario con información del servidor
        """
        parts = hostname.split('-')
        
        return {
            'hostname': hostname,
            'tipo_servidor': parts[0] if len(parts) > 0 else 'unknown',
            'ambiente': parts[1] if len(parts) > 1 else 'unknown',
            'ubicacion': parts[2] if len(parts) > 2 else 'unknown',
            'sistema_operativo': random.choice(self.os_types),
            'cpu_cores': random.choice([2, 4, 8, 16, 32]),
            'ram_gb': random.choice([4, 8, 16, 32, 64, 128]),
            'disco_gb': random.choice([100, 250, 500, 1000, 2000]),
            'uptime_days': random.randint(1, 365),
            'carga_cpu_porcentaje': round(random.uniform(10, 95), 2),
            'uso_ram_porcentaje': round(random.uniform(20, 90), 2)
        }
    
    def generate_dataset(self, num_servers=100):
        """
        Genera un dataset completo de servidores.
        
        Args:
            num_servers (int): Número de servidores a generar
            
        Returns:
            list: Lista de diccionarios con información de servidores
        """
        dataset = []
        hostnames_generados = set()
        
        while len(dataset) < num_servers:
            hostname = self.generate_hostname()
            # Evitar duplicados
            if hostname not in hostnames_generados:
                hostnames_generados.add(hostname)
                server_data = self.generate_server_data(hostname)
                dataset.append(server_data)
        
        return dataset


class ServerAnalyzer:
    """Clase para analizar y visualizar datos de servidores."""
    
    def __init__(self, dataframe):
        """
        Inicializa el analizador con un DataFrame.
        
        Args:
            dataframe (pd.DataFrame): DataFrame con datos de servidores
        """
        self.df = dataframe
    
    def mostrar_estadisticas_basicas(self):
        """Muestra estadísticas básicas del DataFrame."""
        print("\n" + "="*70)
        print("ESTADÍSTICAS BÁSICAS DEL DATASET")
        print("="*70)
        print(f"\nTotal de servidores: {len(self.df)}")
        print(f"\nColumnas: {list(self.df.columns)}")
        print(f"\nPrimeros 5 registros:")
        print(self.df.head())
        print(f"\nEstadísticas descriptivas:")
        print(self.df.describe())
        print("\n" + "="*70)
    
    def grafico_distribucion_tipos(self):
        """Genera un gráfico de barras con la distribución de tipos de servidor."""
        plt.figure(figsize=(10, 6))
        
        tipo_counts = self.df['tipo_servidor'].value_counts()
        tipo_counts.plot(kind='bar', color='steelblue')
        
        plt.title('Distribución de Tipos de Servidor', fontsize=16, fontweight='bold')
        plt.xlabel('Tipo de Servidor', fontsize=12)
        plt.ylabel('Cantidad', fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        
        plt.savefig('distribucion_tipos_servidor.png', dpi=300)
        print("✓ Gráfico guardado: distribucion_tipos_servidor.png")
        plt.close()
    
    def grafico_distribucion_ambientes(self):
        """Genera un gráfico de pastel con la distribución de ambientes."""
        plt.figure(figsize=(10, 8))
        
        ambiente_counts = self.df['ambiente'].value_counts()
        colors = plt.cm.Set3(range(len(ambiente_counts)))
        
        plt.pie(ambiente_counts.values, labels=ambiente_counts.index, autopct='%1.1f%%',
                startangle=90, colors=colors)
        plt.title('Distribución de Ambientes', fontsize=16, fontweight='bold')
        plt.axis('equal')
        
        plt.savefig('distribucion_ambientes.png', dpi=300)
        print("✓ Gráfico guardado: distribucion_ambientes.png")
        plt.close()
    
    def grafico_recursos_hardware(self):
        """Genera gráficos de la distribución de recursos de hardware."""
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        
        # CPU Cores
        self.df['cpu_cores'].value_counts().sort_index().plot(kind='bar', ax=axes[0, 0], color='coral')
        axes[0, 0].set_title('Distribución de CPU Cores', fontweight='bold')
        axes[0, 0].set_xlabel('CPU Cores')
        axes[0, 0].set_ylabel('Cantidad')
        axes[0, 0].grid(axis='y', alpha=0.3)
        
        # RAM
        self.df['ram_gb'].value_counts().sort_index().plot(kind='bar', ax=axes[0, 1], color='lightgreen')
        axes[0, 1].set_title('Distribución de RAM (GB)', fontweight='bold')
        axes[0, 1].set_xlabel('RAM (GB)')
        axes[0, 1].set_ylabel('Cantidad')
        axes[0, 1].grid(axis='y', alpha=0.3)
        
        # Disco
        self.df['disco_gb'].value_counts().sort_index().plot(kind='bar', ax=axes[1, 0], color='skyblue')
        axes[1, 0].set_title('Distribución de Disco (GB)', fontweight='bold')
        axes[1, 0].set_xlabel('Disco (GB)')
        axes[1, 0].set_ylabel('Cantidad')
        axes[1, 0].grid(axis='y', alpha=0.3)
        
        # Sistema Operativo
        self.df['sistema_operativo'].value_counts().plot(kind='barh', ax=axes[1, 1], color='plum')
        axes[1, 1].set_title('Distribución de Sistemas Operativos', fontweight='bold')
        axes[1, 1].set_xlabel('Cantidad')
        axes[1, 1].set_ylabel('Sistema Operativo')
        axes[1, 1].grid(axis='x', alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('distribucion_recursos_hardware.png', dpi=300)
        print("✓ Gráfico guardado: distribucion_recursos_hardware.png")
        plt.close()
    
    def grafico_uso_recursos(self):
        """Genera histogramas del uso de recursos (CPU y RAM)."""
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Uso de CPU
        axes[0].hist(self.df['carga_cpu_porcentaje'], bins=20, color='tomato', edgecolor='black', alpha=0.7)
        axes[0].set_title('Distribución de Carga de CPU (%)', fontweight='bold')
        axes[0].set_xlabel('Carga CPU (%)')
        axes[0].set_ylabel('Frecuencia')
        axes[0].axvline(self.df['carga_cpu_porcentaje'].mean(), color='red', linestyle='--', 
                       linewidth=2, label=f'Media: {self.df["carga_cpu_porcentaje"].mean():.2f}%')
        axes[0].legend()
        axes[0].grid(alpha=0.3)
        
        # Uso de RAM
        axes[1].hist(self.df['uso_ram_porcentaje'], bins=20, color='dodgerblue', edgecolor='black', alpha=0.7)
        axes[1].set_title('Distribución de Uso de RAM (%)', fontweight='bold')
        axes[1].set_xlabel('Uso RAM (%)')
        axes[1].set_ylabel('Frecuencia')
        axes[1].axvline(self.df['uso_ram_porcentaje'].mean(), color='blue', linestyle='--', 
                       linewidth=2, label=f'Media: {self.df["uso_ram_porcentaje"].mean():.2f}%')
        axes[1].legend()
        axes[1].grid(alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('distribucion_uso_recursos.png', dpi=300)
        print("✓ Gráfico guardado: distribucion_uso_recursos.png")
        plt.close()
    
    def grafico_uptime(self):
        """Genera un gráfico del uptime de los servidores."""
        plt.figure(figsize=(12, 6))
        
        # Scatter plot
        plt.scatter(range(len(self.df)), self.df['uptime_days'], alpha=0.6, c=self.df['uptime_days'], 
                   cmap='viridis', s=50)
        plt.colorbar(label='Días de Uptime')
        
        plt.title('Uptime de Servidores', fontsize=16, fontweight='bold')
        plt.xlabel('Índice de Servidor', fontsize=12)
        plt.ylabel('Uptime (días)', fontsize=12)
        plt.axhline(self.df['uptime_days'].mean(), color='red', linestyle='--', 
                   linewidth=2, label=f'Media: {self.df["uptime_days"].mean():.2f} días')
        plt.legend()
        plt.grid(alpha=0.3)
        plt.tight_layout()
        
        plt.savefig('uptime_servidores.png', dpi=300)
        print("✓ Gráfico guardado: uptime_servidores.png")
        plt.close()
    
    def grafico_ubicaciones(self):
        """Genera un gráfico de barras horizontales con las ubicaciones."""
        plt.figure(figsize=(10, 6))
        
        ubicacion_counts = self.df['ubicacion'].value_counts()
        ubicacion_counts.plot(kind='barh', color='teal')
        
        plt.title('Distribución de Servidores por Ubicación', fontsize=16, fontweight='bold')
        plt.xlabel('Cantidad de Servidores', fontsize=12)
        plt.ylabel('Ubicación', fontsize=12)
        plt.grid(axis='x', alpha=0.3)
        plt.tight_layout()
        
        plt.savefig('distribucion_ubicaciones.png', dpi=300)
        print("✓ Gráfico guardado: distribucion_ubicaciones.png")
        plt.close()
    
    def generar_todos_los_graficos(self):
        """Genera todos los gráficos disponibles."""
        print("\n" + "="*70)
        print("GENERANDO GRÁFICOS")
        print("="*70 + "\n")
        
        self.grafico_distribucion_tipos()
        self.grafico_distribucion_ambientes()
        self.grafico_recursos_hardware()
        self.grafico_uso_recursos()
        self.grafico_uptime()
        self.grafico_ubicaciones()
        
        print("\n" + "="*70)
        print("TODOS LOS GRÁFICOS GENERADOS EXITOSAMENTE")
        print("="*70)


def main():
    """Función principal del programa."""
    print("\n" + "="*70)
    print("PRÁCTICA DE PYTHON AVANZADO")
    print("Generación de Dataset de Hostnames y Análisis")
    print("="*70)
    
    # Configurar semilla para reproducibilidad (opcional)
    random.seed(42)
    np.random.seed(42)
    
    # Generar dataset
    print("\n[1] Generando hostnames aleatorios...")
    generator = HostnameGenerator()
    num_servidores = 100
    dataset = generator.generate_dataset(num_servers=num_servidores)
    print(f"✓ {num_servidores} hostnames generados exitosamente")
    
    # Crear DataFrame de Pandas
    print("\n[2] Creando DataFrame de Pandas...")
    df = pd.DataFrame(dataset)
    print("✓ DataFrame creado exitosamente")
    
    # Guardar dataset en CSV
    csv_filename = 'servidores_dataset.csv'
    df.to_csv(csv_filename, index=False)
    print(f"✓ Dataset guardado en: {csv_filename}")
    
    # Análisis y visualización
    print("\n[3] Analizando datos...")
    analyzer = ServerAnalyzer(df)
    analyzer.mostrar_estadisticas_basicas()
    
    # Generar gráficos
    print("\n[4] Generando visualizaciones...")
    analyzer.generar_todos_los_graficos()
    
    print("\n" + "="*70)
    print("PRÁCTICA COMPLETADA CON ÉXITO")
    print("="*70)
    print("\nArchivos generados:")
    print("  - servidores_dataset.csv")
    print("  - distribucion_tipos_servidor.png")
    print("  - distribucion_ambientes.png")
    print("  - distribucion_recursos_hardware.png")
    print("  - distribucion_uso_recursos.png")
    print("  - uptime_servidores.png")
    print("  - distribucion_ubicaciones.png")
    print("\n")


if __name__ == "__main__":
    main()
