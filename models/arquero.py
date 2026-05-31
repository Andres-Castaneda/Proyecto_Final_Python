from models.personaje import Personaje


class Arquero(Personaje):

    def __init__(
        self,
        nombre: str,
        nivel: int,
        ataque: float,
        defensa: float,
        vida: float,
        id_personaje: int = None,
    ) -> None:
        super().__init__(nombre, nivel, ataque, defensa, vida, id_personaje)

    def usar_habilidad(self) -> str:
        danio = self._ataque * 2 + self._nivel * 5
        return (
            f"  {self._nombre} dispara [Flecha Certera] "
            f"causando {danio:.1f} puntos de daño a distancia."
        )