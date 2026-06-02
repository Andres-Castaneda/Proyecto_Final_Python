from database.conexion import Conexion


class InventarioDAO:

    def __init__(self) -> None:
        self._conexion = Conexion().obtener_conexion()

    def agregar_item(self, id_personaje: int,
                     nombre_item: str, bonus: float) -> int:
        sql = """
            INSERT INTO Inventario (nombreItem, bonus, idPersonaje)
            VALUES (%s, %s, %s)
        """
        cursor = self._conexion.cursor()
        cursor.execute(sql, (nombre_item, bonus, id_personaje))
        self._conexion.commit()
        return cursor.lastrowid

    def obtener_por_personaje(self, id_personaje: int) -> list[dict]:
        cursor = self._conexion.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM Inventario WHERE idPersonaje = %s",
            (id_personaje,)
        )
        return cursor.fetchall()

    def obtener_todos(self) -> list[dict]:

        sql = """
            SELECT i.idItem, i.nombreItem, i.bonus,
                   p.Nombre AS nombrePersonaje
            FROM Inventario i
            INNER JOIN Personaje p ON i.idPersonaje = p.idPersonaje
        """
        cursor = self._conexion.cursor(dictionary=True)
        cursor.execute(sql)
        return cursor.fetchall()


    def actualizar_item(self, id_item: int,
                        nombre_item: str, bonus: float) -> bool:
        sql = """
            UPDATE Inventario
            SET nombreItem = %s, bonus = %s
            WHERE idItem = %s
        """
        cursor = self._conexion.cursor()
        cursor.execute(sql, (nombre_item, bonus, id_item))
        self._conexion.commit()
        return cursor.rowcount > 0
    
    def eliminar_item(self, id_item: int) -> bool:
        cursor = self._conexion.cursor()
        cursor.execute(
            "DELETE FROM Inventario WHERE idItem = %s",
            (id_item,)
        )
        self._conexion.commit()
        return cursor.rowcount > 0