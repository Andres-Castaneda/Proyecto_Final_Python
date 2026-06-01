from database.inventario_dao import InventarioDAO
from database.personaje_dao import PersonajeDAO
from views.inventario_view import InventarioView


class InventarioController:

    def __init__(self) -> None:
        self._dao = InventarioDAO()
        self._dao_personaje = PersonajeDAO()   # Para validar que el personaje existe
        self._view = InventarioView()

    def ejecutar(self) -> None:
        acciones = {
            "1": self._agregar_item,
            "2": self._ver_inventario_personaje,
            "3": self._ver_todo,
            "4": self._actualizar_item,
            "5": self._eliminar_item,
        }

        while True:
            self._view.mostrar_menu_inventario()
            opcion = self._view.pedir_opcion()

            if opcion == "6":
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
                self._view.mostrar_error("Opción no válida.")

    # ── CREATE ─────────────────────────────────────────────────────

    def _agregar_item(self) -> None:
        id_p = self._view.pedir_id_personaje()

        if not self._dao_personaje.obtener_por_id(id_p):
            self._view.mostrar_error(
                f"No existe personaje con ID {id_p}."
            )
            return

        datos = self._view.pedir_datos_item()
        nuevo_id = self._dao.agregar_item(
            id_p, datos["nombre_item"], datos["bonus"]
        )
        self._view.mostrar_exito(
            f"Ítem '{datos['nombre_item']}' agregado con ID {nuevo_id}."
        )

    # ── READ ───────────────────────────────────────────────────────

    def _ver_inventario_personaje(self) -> None:
        id_p = self._view.pedir_id_personaje()
        personaje = self._dao_personaje.obtener_por_id(id_p)

        if not personaje:
            self._view.mostrar_error(
                f"No existe personaje con ID {id_p}."
            )
            return

        items = self._dao.obtener_por_personaje(id_p)

        # Agrega el nombre del dueño a cada ítem para mostrarlo
        for item in items:
            item["nombrePersonaje"] = personaje.nombre

        self._view.mostrar_inventario(
            items, f"INVENTARIO DE {personaje.nombre.upper()}"
        )

    def _ver_todo(self) -> None:
        items = self._dao.obtener_todos()
        self._view.mostrar_inventario(items, "INVENTARIO COMPLETO")

    # ── UPDATE ─────────────────────────────────────────────────────

    def _actualizar_item(self) -> None:
        id_item = self._view.pedir_id_item()
        datos = self._view.pedir_datos_actualizacion_item()
        actualizado = self._dao.actualizar_item(
            id_item, datos["nombre_item"], datos["bonus"]
        )

        if actualizado:
            self._view.mostrar_exito("Ítem actualizado correctamente.")
        else:
            self._view.mostrar_error(
                f"No existe ítem con ID {id_item}."
            )

    # ── DELETE ─────────────────────────────────────────────────────

    def _eliminar_item(self) -> None:
        id_item = self._view.pedir_id_item()

        if self._view.confirmar_accion(
            f"¿Eliminar el ítem con ID {id_item}?"
        ):
            if self._dao.eliminar_item(id_item):
                self._view.mostrar_exito("Ítem eliminado correctamente.")
            else:
                self._view.mostrar_error(
                    f"No existe ítem con ID {id_item}."
                )
        else:
            self._view.mostrar_error("Operación cancelada.")