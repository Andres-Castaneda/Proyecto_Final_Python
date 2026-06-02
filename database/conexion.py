import mysql.connector
from mysql.connector.connection import MySQLConnection


class Conexion:

    _instancia: "Conexion | None" = None
    _conexion: MySQLConnection | None = None

    _CONFIG = {
        "host":     "localhost",
        "user":     "root",       
        "password": "Andres1804",        
        "database": "JuegoRPG",   
    }

    def __new__(cls) -> "Conexion":
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def obtener_conexion(self) -> MySQLConnection:
        if self._conexion is None or not self._conexion.is_connected():
            self._conexion = mysql.connector.connect(**self._CONFIG)
        return self._conexion

    def cerrar(self) -> None:
        if self._conexion and self._conexion.is_connected():
            self._conexion.close()