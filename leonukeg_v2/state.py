"""
state.py — Estado Global de la Aplicación
Gestiona el estado reactivo del HUD, navegación y animaciones.
"""
import reflex as rx


class PortfolioState(rx.State):
    """Estado principal del portfolio."""

    # HUD status text (actualizado por Intersection Observer via JS)
    hud_status: str = "NEURAL NET ACTIVE"

    # Cursor coordinates (actualizado via JS)
    cursor_x: float = 0.0
    cursor_y: float = 0.0

    @rx.event
    def set_hud_status(self, status: str):
        """Actualiza el texto del HUD desde el frontend."""
        self.hud_status = status

    @rx.event
    def update_cursor(self, x: float, y: float):
        """Actualiza las coordenadas del cursor en el HUD."""
        self.cursor_x = x
        self.cursor_y = y

    @rx.event
    def tick(self):
        """Evento que se dispara cada segundo para actualizar el reloj."""
        pass

    @rx.var
    def current_time(self) -> str:
        import datetime
        now = datetime.datetime.now()
        time_str = now.strftime("%d.%m.%Y | %H:%M:%S")
        return f"------------------- {time_str} --------------------"
