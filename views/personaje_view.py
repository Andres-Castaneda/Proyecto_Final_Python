class PersonajeView:
    """
    Gestiona toda la interacción con el usuario en consola.
    No conoce la BD ni los modelos — solo imprime y pide datos.
    """

    # ── Menú principal ─────────────────────────────────────────────

    def mostrar_menu_principal(self) -> None:
        print("\n" + "=" * 50)
        print("        ⚔  GESTOR DE PERSONAJES RPG  ⚔")
        print("=" * 50)
        print("  1. Gestionar Personajes")
        print("  2. Gestionar Inventario")
        print("  3. Salir")
        print("=" * 50)

    def mostrar_menu_personajes(self) -> None:
        print("\n" + "-" * 50)
        print("           MENÚ DE PERSONAJES")
        print("-" * 50)
        print("  1. Crear personaje")
        print("  2. Listar todos los personajes")
        print("  3. Buscar personaje por ID")
        print("  4. Actualizar personaje")
        print("  5. Eliminar personaje")
        print("  6. Usar habilidad")
        print("  7. Volver al menú principal")
        print("-" * 50)

    def pedir_opcion(self, mensaje: str = "Seleccione una opción: ") -> str:
        try:
            return input(f"\n  {mensaje}").strip()
        except EOFError:
            # Evita crash si el input recibe fin de archivo
            return

    # ── Formularios de entrada ─────────────────────────────────────

    def pedir_datos_nuevo_personaje(self) -> dict:
        print("\n  -- Tipos disponibles: Guerrero | Mago | Arquero --")
        print("  (Los nombres deben coincidir exactamente con el tipo)")
        return {
            "clase":   input("  Clase    : ").strip().capitalize(),
            "nombre":  input("  Nombre   : ").strip(),
            "nivel":   int(input("  Nivel    : ")),
            "ataque":  float(input("  Ataque   : ")),
            "defensa": float(input("  Defensa  : ")),
            "vida":    float(input("  Vida     : ")),
        }

    def pedir_id(self, mensaje: str = "Ingrese el ID del personaje: ") -> int:
        return int(input(f"\n  {mensaje}"))

    def pedir_datos_actualizacion(self) -> dict:
        print("\n  -- Deja en blanco para mantener el valor actual --")
        return {
            "nivel":   int(input("  Nuevo nivel    : ")),
            "ataque":  float(input("  Nuevo ataque   : ")),
            "defensa": float(input("  Nueva defensa  : ")),
            "vida":    float(input("  Nueva vida     : ")),
        }

    # ── Visualización de personajes ────────────────────────────────

    def mostrar_lista_personajes(self, personajes: list) -> None:
        if not personajes:
            print("\n  Sin personajes registrados.")
            return

        print("\n" + "=" * 65)
        print(f"  {'ID':<5} {'Clase':<12} {'Nombre':<15} "
              f"{'Nivel':<8} {'ATQ':<8} {'DEF':<8} {'Vida':<8}")
        print("=" * 65)
        for p in personajes:
            print(
                f"  {p.id_personaje:<5} {p.__class__.__name__:<12} "
                f"{p.nombre:<15} {p.nivel:<8} "
                f"{p.ataque:<8.1f} {p.defensa:<8.1f} {p.vida:<8.1f}"
            )
        print("=" * 65)

    def mostrar_personaje(self, personaje) -> None:
        print(f"\n  {personaje}")

    def mostrar_habilidad(self, resultado: str) -> None:
        print(f"\n  {resultado}")

    # ── Mensajes de feedback ───────────────────────────────────────

    def mostrar_exito(self, mensaje: str) -> None:
        print(f"\n  ✔  {mensaje}")

    def mostrar_error(self, mensaje: str) -> None:
        print(f"\n  ✖  Error: {mensaje}")

    def mostrar_advertencia(self, mensaje: str) -> None:
        print(f"\n  ⚠  {mensaje}")

    def confirmar_accion(self, mensaje: str) -> bool:
        respuesta = input(f"\n  ⚠  {mensaje} (s/n): ").strip().lower()
        return respuesta == "s"