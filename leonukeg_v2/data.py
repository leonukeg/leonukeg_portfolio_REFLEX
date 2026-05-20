"""
data.py — Capa de Datos
Centraliza toda la información de proyectos y experimentos.
Fuente única de verdad: editar aquí para actualizar el portfolio.
"""
from dataclasses import dataclass, field
from typing import List


@dataclass
class Project:
    id: str
    name: str
    desc: str
    stack: str
    status: str
    accent: str
    url: str
    tag: str = ""


@dataclass
class LabExperiment:
    name: str
    tag: str
    desc: str
    url: str


PROJECTS: List[Project] = [
    Project(
        id="01",
        name="ALMACEN",
        tag="FLAGSHIP",
        desc="Sistema completo de administración logística. Inventario, entradas/salidas, reportes en tiempo real. El proyecto que más nivel técnico y dominio de negocio demuestra.",
        stack="Python · Reflex · SQL",
        status="FLAGSHIP PROJECT",
        accent="#1D9E75",
        url="#",
    ),
    Project(
        id="02",
        name="HOMETRACK",
        desc="App de análisis y gestión de gastos del hogar. Dashboard claro, sin ruido. Datos que ayudan a tomar decisiones reales.",
        stack="Python · Reflex · SQL",
        status="EN DESARROLLO",
        accent="#7B1B1C",
        url="#",
    ),
]

LAB_EXPERIMENTS: List[LabExperiment] = [
    LabExperiment(
        name="Análisis Fútbol",
        tag="DATA · ANALYSIS",
        desc="Plataforma de estadísticas deportivas y métricas de rendimiento.",
        url="#",
    ),
    LabExperiment(
        name="Mathlab",
        tag="MATH · VISUALIZATION",
        desc="Visualización y análisis de funciones matemáticas para educación técnica.",
        url="#",
    ),
    LabExperiment(
        name="Colonist",
        tag="GAME · LOGIC",
        desc="Reimplementación de estrategia tipo Catan con complejidad emergente.",
        url="#",
    ),
    LabExperiment(
        name="Tienda Virtual",
        tag="E-COMMERCE · SAAS",
        desc="Plataforma completa de comercio electrónico aplicada al mundo real.",
        url="#",
    ),
]
