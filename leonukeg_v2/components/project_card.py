"""
components/project_card.py — Componente Atómico: Tarjeta de Proyecto
Un componente funcional puro para la sección WORK.
"""
import reflex as rx
from leonukeg_v2.data import Project


def project_card(project: Project, index: int) -> rx.Component:
    """Renderiza una tarjeta de proyecto clicable que enlaza al repositorio."""
    return rx.el.a(
        # Número del proyecto
        rx.el.span(f"/{project.id}", class_name="project-num"),
        # Cuerpo del proyecto
        rx.box(
            # Nombre + badge opcional
            rx.el.h3(
                project.name,
                rx.cond(
                    project.tag != "",
                    rx.el.span(project.tag, class_name="project-flagship"),
                    rx.fragment(),
                ),
                class_name="project-name",
            ),
            rx.el.p(project.desc, class_name="project-desc"),
            rx.box(
                rx.el.span(
                    rx.el.span("STACK ", class_name="meta-label"),
                    rx.el.span(project.stack, class_name="meta-value"),
                ),
                rx.el.span(
                    rx.el.span("STATUS ", class_name="meta-label"),
                    rx.el.span(project.status, class_name="meta-value project-status"),
                ),
                class_name="project-meta",
            ),
            class_name="project-body",
        ),
        href=project.url,
        target="_blank",
        class_name="project",
        style={"--project-accent": project.accent},
    )
