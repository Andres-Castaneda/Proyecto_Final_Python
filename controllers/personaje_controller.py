from models.guerrero import Guerrero
from models.mago import Mago
from models.arquero import Arquero
from database.personaje_dao import PersonajeDAO
from views.personaje_view import PersonajeView


# Factory: mapea el string de clase al constructor correcto
_FABRICAS = {
    "Guerrero": lambda d: Guerrero(
        d["nombre"], d["nivel"], d["ataque"], d["defensa"], d["vida"]
    ),
    "Mago": lambda d: Mago(
        d["nombre"], d["nivel"], d["ataque"], d["defensa"], d["vida"]
    ),
    "Arquero": lambda d: Arquero(
        d["nombre"], d["nivel"], d["ataque"], d["defensa"], d["vida"]
    ),
}


class PersonajeController:
    """
    Orquesta el flujo entre PersonajeView y PersonajeDAO.
    No imprime ni ejecuta SQL directamente — delega a cada capa.
    """

    def __init__(self) -> None:
        self._dao = PersonajeDAO()
        self._view = PersonajeView()

    def ejecutar(self) -> None:
        acciones = {
            "1": self._crear,
            "2": self._listar,
            "3": self._buscar_por_id,
            "4": self._actualizar,
            "5": self._eliminar,
            "6": self._usar_habilidad,
        }

        while True:
            self._view.mostrar_menu_personajes()
            opcion = self._view.pedir_opcion()

            if opcion == "7":
                break

            accion = acciones.get(opcion)
            if accion:
                try:
                    accion()
                except ValueError as e:
                    self._view.mostrar_error(f"Dato inválido → {e}")
                except Exception as e:
                    self._view.mostrar_error(f"Error inesperado → {e}")
            else:
                self._view.mostrar_advertencia("Opción no válida.")

    # ── CREATE ─────────────────────────────────────────────────────

    def _crear(self) -> None:
        datos = self._view.pedir_datos_nuevo_personaje()

        fabrica = _FABRICAS.get(datos["clase"])
        if not fabrica:
            self._view.mostrar_error(
                f"Clase '{datos['clase']}' no reconocida. "
                "Usa: Guerrero, Mago o Arquero."
            )
            return

        personaje = fabrica(datos)
        nuevo_id = self._dao.crear(personaje, datos["clase"])
        self._view.mostrar_exito(
            f"Personaje '{datos['nombre']}' creado con ID {nuevo_id}."
        )

    # ── READ ───────────────────────────────────────────────────────

    def _listar(self) -> None:
        personajes = self._dao.obtener_todos()
        self._view.mostrar_lista_personajes(personajes)

    def _buscar_por_id(self) -> None:
        id_p = self._view.pedir_id()
        personaje = self._dao.obtener_por_id(id_p)

        if not personaje:
            self._view.mostrar_advertencia(
                f"No existe personaje con ID {id_p}."
            )
            return

        self._view.mostrar_personaje(personaje)

    # ── UPDATE ─────────────────────────────────────────────────────

    def _actualizar(self) -> None:
        id_p = self._view.pedir_id("ID del personaje a actualizar: ")

        # Verificar que existe antes de pedir datos
        if not self._dao.obtener_por_id(id_p):
            self._view.mostrar_advertencia(
                f"No existe personaje con ID {id_p}."
            )
            return

        datos = self._view.pedir_datos_actualizacion()
        actualizado = self._dao.actualizar(
            id_p,
            datos["nivel"],
            datos["ataque"],
            datos["defensa"],
            datos["vida"],
        )

        if actualizado:
            self._view.mostrar_exito("Personaje actualizado correctamente.")
        else:
            self._view.mostrar_error("No se pudo actualizar el personaje.")

    # ── DELETE ─────────────────────────────────────────────────────

    def _eliminar(self) -> None:
        id_p = self._view.pedir_id("ID del personaje a eliminar: ")

        personaje = self._dao.obtener_por_id(id_p)
        if not personaje:
            self._view.mostrar_advertencia(
                f"No existe personaje con ID {id_p}."
            )
            return

        confirmado = self._view.confirmar_accion(
            f"¿Eliminar a '{personaje.nombre}' y su inventario?"
        )
        if not confirmado:
            self._view.mostrar_advertencia("Operación cancelada.")
            return

        if self._dao.eliminar(id_p):
            self._view.mostrar_exito(
                f"Personaje '{personaje.nombre}' eliminado."
            )
        else:
            self._view.mostrar_error("No se pudo eliminar el personaje.")

    # ── HABILIDAD ──────────────────────────────────────────────────

    def _usar_habilidad(self) -> None:
        id_p = self._view.pedir_id("ID del personaje que usará su habilidad: ")
        personaje = self._dao.obtener_por_id(id_p)

        if not personaje:
            self._view.mostrar_advertencia(
                f"No existe personaje con ID {id_p}."
            )
            return

        self._view.mostrar_habilidad(personaje.usar_habilidad())