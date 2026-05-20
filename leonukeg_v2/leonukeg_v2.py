"""
leonukeg_v2.py — Página principal del portfolio LEONUKEG (Reflex Edition)
Versión con Diagnóstico y Z-Index Forzado.
"""
import reflex as rx

from leonukeg_v2.components import hud, project_card, lab_item
from leonukeg_v2.data import PROJECTS, LAB_EXPERIMENTS
from leonukeg_v2.state import PortfolioState

# ── SECCIONES ────────────────────────────────────────────────────────────────

def section_entry() -> rx.Component:
    return rx.el.section(
        rx.el.p(
            "──────── LOADING SYSTEM TIME ────────", 
            class_name="entry-label", 
            id="current-time-display"
        ),
        rx.el.h1("LEONUKEG", class_name="hero-name"),
        rx.el.div("Freddy León", class_name="hero-sub"),
        rx.el.p(
            "Turning complexity into ",
            rx.el.span("elegant systems.", class_name="accent"),
            class_name="hero-tagline",
        ),
        rx.box(
            rx.el.span("_ scroll to explore", class_name="hint-text"),
            rx.box(class_name="hint-line"),
            class_name="scroll-hint",
        ),
        id="entry",
    )


def section_system() -> rx.Component:
    return rx.el.section(
        rx.box(
            rx.el.p("──────── 02 SYSTEM LAYER ────────", class_name="system-label"),
            rx.el.h2(
                "Un sistema que piensa antes de actuar.",
                class_name="system-h1",
            ),
            rx.el.p(
                "No construyo páginas. Construyo arquitecturas. Cada línea de código que escribo "
                "tiene intención: separar responsabilidades, encapsular complejidad y exponer "
                "solo lo necesario.",
                class_name="system-body",
            ),
            rx.el.p("──────── STACK ────────", class_name="stack-label"),
            rx.el.p("Python · Reflex · SQL/NoSQL · AI/ML", class_name="stack-line"),
            rx.el.blockquote(
                rx.el.p(
                    '"El hombre que pone corazón en lo que hace encuentra soluciones '
                    "donde normalmente los perezosos e indolentes se dan por vencidos.\"",
                ),
                class_name="system-quote",
            ),
            class_name="system-content",
        ),
        id="system",
    )


def section_work() -> rx.Component:
    return rx.el.section(
        rx.box(
            rx.el.p("──────── SELECTED WORKS ────────", class_name="work-label"),
            rx.el.h2("Lo que LEONUKEG ha construido.", class_name="work-title"),
            class_name="work-header",
        ),
        rx.box(
            *[project_card(p, i) for i, p in enumerate(PROJECTS)],
            class_name="projects-container",
        ),
        id="work",
    )


def section_lab() -> rx.Component:
    return rx.el.section(
        rx.el.p("──────── LABORATORY ────────", class_name="lab-label"),
        rx.el.h2("El sistema piensa en voz alta.", class_name="lab-title"),
        rx.el.p(
            "Experimentos, demos, ideas sin terminar que igual impresionan.",
            class_name="lab-subtitle",
        ),
        rx.box(
            *[lab_item(e) for e in LAB_EXPERIMENTS],
            class_name="lab-grid",
        ),
        id="lab",
    )


def section_signals() -> rx.Component:
    return rx.el.section(
        rx.el.p("──────── SIGNALS ────────", class_name="signals-label"),
        rx.el.h2("El sistema está disponible.", class_name="signals-title"),
        rx.el.p(
            "Si tienes un problema que vale la pena resolver — hablemos.",
            class_name="signals-sub",
        ),
        rx.box(
            rx.el.a(
                rx.el.span("EMAIL", class_name="signal-link-label"),
                rx.el.span("chemaruan@gmail.com", class_name="signal-link-value"),
                href="mailto:chemaruan@gmail.com",
                class_name="signal-link",
            ),
            rx.el.a(
                rx.el.span("GITHUB", class_name="signal-link-label"),
                rx.el.span("@leonukeg", class_name="signal-link-value"),
                href="https://github.com/leonukeg",
                target="_blank",
                class_name="signal-link",
            ),
            rx.el.a(
                rx.el.span("LINKEDIN", class_name="signal-link-label"),
                rx.el.span("Freddy León", class_name="signal-link-value"),
                href="https://linkedin.com/in/leonukeg",
                target="_blank",
                class_name="signal-link",
            ),
            class_name="signals-links",
        ),
        rx.box(
            rx.el.span("© 2025 LEONUKEG · Freddy León", class_name="signals-footer-left"),
            rx.el.span("BUILD WITH INTENTION", class_name="signals-footer-right"),
            class_name="signals-footer",
        ),
        rx.box("Dios, Familia, y Salud primero", class_name="user-signature"),
        id="signals",
    )


# ── PÁGINA PRINCIPAL ─────────────────────────────────────────────────────────

def index() -> rx.Component:
    return rx.fragment(
        # Forzar carga de CSS sin caché
        rx.el.link(rel="stylesheet", href="/leonukeg.css?v=2.0"),
        
        # Meta SEO
        rx.el.title("LEONUKEG — Freddy León"),
        rx.el.meta(name="description", content="Portfolio de Freddy León — Arquitecto de sistemas Python · Reflex · SQL"),
        rx.el.meta(name="viewport", content="width=device-width, initial-scale=1.0"),

        # Scripts de motor (GSAP de CDN)
        rx.script(src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"),
        rx.script(src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"),

        # BUNDLE UNIFICADO (Motor de rayos + Animaciones + Boot)
        rx.script(src="/bundle.js?v=9.0"),

        # Canvas del motor de rayos
        rx.el.canvas(id="lightning"),

        # HUD superpuesto
        hud(),

        # Contenido principal - FORZANDO Z-INDEX POR CÓDIGO
        rx.el.main(
            section_entry(),
            section_system(),
            section_work(),
            section_lab(),
            section_signals(),
            style={"position": "relative", "z_index": "999"}
        ),
    )


# ── APLICACIÓN ───────────────────────────────────────────────────────────────
app = rx.App()
app.add_page(
    index,
    route="/",
    title="LEONUKEG — Freddy León",
    description="Portfolio de Freddy León — Arquitecto de sistemas Python · Freddy León",
)
