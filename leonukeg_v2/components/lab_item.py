"""
components/lab_item.py — Componente Atómico: Tarjeta de Laboratorio
Un componente funcional puro para la sección LABORATORY.
"""
import reflex as rx
from leonukeg_v2.data import LabExperiment


def lab_item(experiment: LabExperiment) -> rx.Component:
    """Renderiza una tarjeta de experimento clicable del laboratorio."""
    return rx.el.a(
        rx.el.p(experiment.tag, class_name="lab-item-tag"),
        rx.el.h3(experiment.name, class_name="lab-item-name"),
        rx.el.p(experiment.desc, class_name="lab-item-desc"),
        href=experiment.url,
        target="_blank",
        class_name="lab-item",
    )
