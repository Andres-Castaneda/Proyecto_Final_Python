from database.conexion import Conexion
from models.guerrero import Guerrero
from models.mago import Mago
from models.arquero import Arquero
from models.personaje import Personaje

_FABRICAS = {
    "Guerrero": lambda r: Guerrero(
        r["Nombre"], r["nivel"], r["ataque"], r["defensa"], r["vida"], r["idPersonaje"]
    ),
    "Mago": lambda r: Mago(
        r["Nombre"], r["nivel"], r["ataque"], r["defensa"], r["vida"], r["idPersonaje"]
    ),
    "Arquero": lambda r: Arquero(
        r["Nombre"], r["nivel"], r["ataque"], r["defensa"], r["vida"], r["idPersonaje"]
    ),
}


class PersonajeDAO:

    def __init__(self) -> None:
        self._conexion = Conexion().obtener_conexion()


    def crear(self, personaje: Personaje, clase: str) -> int:

        sql = """
            INSERT INTO Personaje (Nombre, clase, nivel, ataque, defensa, vida)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor = self._conexion.cursor()
        cursor.execute(sql, (
            personaje.nombre,
            clase,
            personaje.nivel,
            personaje.ataque,
            personaje.defensa,
            personaje.vida,
        ))
        self._conexion.commit()
        return cursor.lastrowid


    def obtener_todos(self) -> list[Personaje]:
        """
        Retorna todos los personajes como objetos Python
        (Guerrero, Mago o Arquero según su clase).
        """
        cursor = self._conexion.cursor(dictionary=True)  # Resultados como dict
        cursor.execute("SELECT * FROM Personaje")
        filas = cursor.fetchall()
        return [self._fila_a_objeto(f) for f in filas]

    def obtener_por_id(self, id_personaje: int) -> Personaje | None:
        """Retorna un personaje por su ID o None si no existe."""
        cursor = self._conexion.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM Personaje WHERE idPersonaje = %s",
            (id_personaje,)
        )
        fila = cursor.fetchone()
        return self._fila_a_objeto(fila) if fila else None


    def actualizar(self, id_personaje: int, nivel: int,
                   ataque: float, defensa: float, vida: float) -> bool:
        sql = """
            UPDATE Personaje
            SET nivel = %s, ataque = %s, defensa = %s, vida = %s
            WHERE idPersonaje = %s
        """
        cursor = self._conexion.cursor()
        cursor.execute(sql, (nivel, ataque, defensa, vida, id_personaje))
        self._conexion.commit()
        return cursor.rowcount > 0  # rowcount equivale a executeUpdate() en Java


    def eliminar(self, id_personaje: int) -> bool:

        cursor = self._conexion.cursor()
        cursor.execute(
            "DELETE FROM Personaje WHERE idPersonaje = %s",
            (id_personaje,)
        )
        self._conexion.commit()
        return cursor.rowcount > 0

    @staticmethod
    def _fila_a_objeto(fila: dict) -> Personaje:

        fabrica = _FABRICAS.get(fila["clase"])
        if fabrica is None:
            raise ValueError(f"Clase desconocida: {fila['clase']}")
        return fabrica(fila)