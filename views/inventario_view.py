class InventarioView:
    """Gestiona la interacción de consola para el inventario."""

    def mostrar_menu_inventario(self) -> None:
        print("\n" + "-" * 50)
        print("           MENÚ DE INVENTARIO")
        print("-" * 50)
        print("  1. Agregar ítem a personaje")
        print("  2. Ver inventario de un personaje")
        print("  3. Ver todo el inventario")
        print("  4. Actualizar ítem")
        print("  5. Eliminar ítem")
        print("  6. Volver al menú principal")
        print("-" * 50)

    def pedir_opcion(self, mensaje: str = "Seleccione una opción: ") -> str:
        return input(f"\n  {mensaje}").strip()

    # ── Formularios de entrada ─────────────────────────────────────

    def pedir_datos_item(self) -> dict:
        return {
            "nombre_item": input("\n  Nombre del ítem : ").strip(),
            "bonus":       float(input("  Bonus           : ")),
        }

    def pedir_id_item(self) -> int:
        return int(input("\n  ID del ítem: "))

    def pedir_id_personaje(self) -> int:
        return int(input("\n  ID del personaje: "))

    def pedir_datos_actualizacion_item(self) -> dict:
        return {
            "nombre_item": input("\n  Nuevo nombre del ítem : ").strip(),
            "bonus":       float(input("  Nuevo bonus           : ")),
        }

    # ── Visualización ──────────────────────────────────────────────

    def mostrar_inventario(self, items: list, titulo: str = "INVENTARIO") -> None:
        if not items:
            print("\n  Sin ítems registrados.")
            return

        print(f"\n  {'=' * 45}")
        print(f"  {titulo:^45}")
        print(f"  {'=' * 45}")
        print(f"  {'ID':<6} {'Ítem':<20} {'Bonus':<10} {'Personaje'}")
        print(f"  {'-' * 45}")
        for item in items:
            propietario = item.get("nombrePersonaje", "—")
            print(
                f"  {item['idItem']:<6} {item['nombreItem']:<20} "
                f"{item['bonus']:<10.1f} {propietario}"
            )
        print(f"  {'=' * 45}")

    # ── Mensajes de feedback ───────────────────────────────────────

    def mostrar_exito(self, mensaje: str) -> None:
        print(f"\n  ✔  {mensaje}")

    def mostrar_error(self, mensaje: str) -> None:
        print(f"\n  ✖  Error: {mensaje}")

    def confirmar_accion(self, mensaje: str) -> bool:
        respuesta = input(f"\n  ⚠  {mensaje} (s/n): ").strip().lower()
        return respuesta == "s"