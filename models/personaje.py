from abc import ABC, abstractmethod


class Personaje(ABC):

    def __init__(
        self,
        nombre: str,
        nivel: int,
        ataque: float,
        defensa: float,
        vida: float,
        id_personaje: int = None,
    ) -> None:
        self._id_personaje = id_personaje
        self._nombre = nombre
        self._nivel = nivel
        self._ataque = ataque
        self._defensa = defensa
        self._vida = vida


    @property
    def id_personaje(self) -> int:
        return self._id_personaje

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def nivel(self) -> int:
        return self._nivel

    @property
    def ataque(self) -> float:
        return self._ataque

    @property
    def defensa(self) -> float:
        return self._defensa

    @property
    def vida(self) -> float:
        return self._vida

    @vida.setter
    def vida(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("La vida no puede ser negativa.")
        self._vida = valor

    @ataque.setter
    def ataque(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("El ataque no puede ser negativo.")
        self._ataque = valor

    @defensa.setter
    def defensa(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("La defensa no puede ser negativa.")
        self._defensa = valor

    @abstractmethod
    def usar_habilidad(self) -> str:
        ...


    def __str__(self) -> str:
        return (
            f"[{self.__class__.__name__}] ID: {self._id_personaje} "
            f"| {self._nombre} | Nivel: {self._nivel} "
            f"| ATQ: {self._ataque} | DEF: {self._defensa} "
            f"| Vida: {self._vida}"
        )