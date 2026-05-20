"""
hud.py — Componente de Interfaz HUD
Etiquetas de las esquinas y navegación lateral.
"""
import reflex as rx
from leonukeg_v2.state import PortfolioState

def hud() -> rx.Component:
    return rx.box(
        # Top-left: Nombre del sistema
        rx.el.span("LEONUKEG", id="hud-tl"),
        
        # Top-right: Estado dinámico
        rx.el.span("INITIALIZING...", id="hud-tr"),
        
        # Bottom-left: Localizador (Actualizado por JS)
        rx.el.span("LOC: 0 / 0", id="hud-bl"),
        
        # Bottom-right: Nivel / Versión (Actualizado por JS)
        rx.el.span("LEVEL: 0%", id="hud-br"),

        # Índice de navegación lateral (Derecha)
        rx.box(
            rx.el.span("01", class_name="idx active"),
            rx.el.span("02", class_name="idx"),
            rx.el.span("03", class_name="idx"),
            rx.el.span("04", class_name="idx"),
            rx.el.span("05", class_name="idx"),
            id="scroll-index",
        ),
        id="hud",
    )
