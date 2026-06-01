from controllers.personaje_controller import PersonajeController
from controllers.inventario_controller import InventarioController
from views.personaje_view import PersonajeView
from database.conexion import Conexion


def main() -> None:
    view = PersonajeView()
    personaje_ctrl = PersonajeController()
    inventario_ctrl = InventarioController()

    try:
        while True:
            view.mostrar_menu_principal()
            opcion = view.pedir_opcion()

            if opcion == "1":
                personaje_ctrl.ejecutar()
            elif opcion == "2":
                inventario_ctrl.ejecutar()
            elif opcion == "3":
                print("\n  ¡Hasta la próxima aventura! ⚔\n")
                break
            else:
                view.mostrar_advertencia("Opción no válida.")

    except KeyboardInterrupt:
        print("\n\n  Programa interrumpido por el usuario.")
    finally:
        Conexion().cerrar()


if __name__ == "__main__":
    main()