"""
components/__init__.py — Exportaciones de componentes
Barrel file para importaciones limpias.
"""
from .hud import hud
from .project_card import project_card
from .lab_item import lab_item

__all__ = ["hud", "project_card", "lab_item"]
