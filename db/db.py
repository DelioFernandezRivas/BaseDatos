import sqlite3 as dbapi


class BBDD:
    """Clase de acceso a base de datos.

    Clase que vai a realizar a operación de conexión a base de datos sqlite
    e realización de consultas.

    Métodos:
    - Conexión.
    - Consulta.

    """

    def conexionBD (self,ruta):
       """Crea unha conexión coa base de datos especificada na ruta.

       Crea conexión a base de datos sqlite situada na ruta especificada no parámetro
       e retorna un obxecto de conexión da base de datos.




       :param ruta: Path o ficheiro de base de datos
       :return:
       :exception:DatabaseError, OperationalError
       """

       try:
          bbdd = dbapi.connect(ruta)
          return bbdd

       except dbapi.DababaseError as erroBaseDatos:
           print ("Erro en conexionDB (DatabaseError): "+ str(erroBaseDatos))
       except dbapi.OperationalError as erroOperacional:
           print ("Erro en conexionDB (OperationalError): "+ str(erroOperacional))
       finally:
           print ("Conexión realizada con exito")

    def pechaConexionDB(self,conexion):
       """Pecha a conexión dunha base de datos sqlite.

       :param conexion:
       :return:
       :exception:

       """
       try:
           conexion.close()
       except dbapi.DatabaseError as erroBaseDatos:
           print("Erro en conexionDB (DatabaseError): " + str(erroBaseDatos))
       except dbapi.OperationalError as erroOperacional:
           print("Erro en conexionDB (OperationalError): " + str(erroOperacional))
       finally:
           print("Conexión pechada con exito")



    def consultaBD (self, ruta, consultaSQL, *parametros):
       """Método que realiza operacion xenérica sobre a base de datos

       :param consultaSQL: Sql de consulta a base de datos
       :param ruta: Ruta a base de datos
       :param parametros: Parámetros da consulta
       :return: Lista co resultado da consulta.
       """
       consulta = []
       try:
           conexion = self.conexionBD( ruta)

           cursor = conexion.cursor()
           print (parametros)
           if parametros[0]==None:
               cursor.execute(consultaSQL)
           elif len(parametros)>=1:
               cursor.execute (consultaSQL, parametros )

           for rexistro in cursor.fetchall():
               consulta.append (rexistro)

           self.pechaConexionDB(conexion)
       except dbapi.OperationalError as erroOperacional:
           print("Erro en conexionDB (OperationalError) consultaBD: " + str(erroOperacional))
       finally:
           print("Conexión pechada con exito")

       return consulta



    def borraRexistroBD (self, ruta, borraSQL, *parametros):
       """Método que realiza operacion xenérica sobre a base de datos

       :param borraSQL: Sql de consulta a base de datos
       :param ruta: Ruta a base de datos
       :param parametros: Parámetros da consulta
       :return: None.
       """
       consulta = []
       try:
           conexion = self.conexionBD( ruta)

           cursor = conexion.cursor()
           print (parametros)
           if parametros[0]==None:
               cursor.execute(borraSQL)
           elif len(parametros)>=1:
               cursor.execute (borraSQL, parametros )

           self.pechaConexionDB(conexion)
       except dbapi.OperationalError as erroOperacional:
           print("Erro en conexionDB (OperationalError) borraRexistroBD: " + str(erroOperacional))
       finally:
           print("Conexión pechada con exito")


    def insertaRexistroBD (self, ruta, insertaSQL, *parametros):
       """Método que realiza operacion xenérica sobre a base de datos

       :param insertaSQL: Sql de consulta a base de datos
       :param ruta: Ruta a base de datos
       :param parametros: Parámetros da consulta
       :return: None.
       """
       consulta = []
       try:
           conexion = self.conexionBD( ruta)

           cursor = conexion.cursor()
           print (parametros)

           if parametros[0]==None:
               cursor.execute(insertaSQL)
           elif len(parametros)>=1:
               cursor.execute (insertaSQL, parametros )
           conexion.commit()

           self.pechaConexionDB(conexion)
       except dbapi.OperationalError as erroOperacional:
           print("Erro en conexionDB (OperationalError) insertaRexistroBD: " + str(erroOperacional))
       except dbapi.DataBaseError as erroBaseDatos:
           print("Erro en conexionDB (DataBaseError) insertaRexistroBD: " + str(erroBaseDatos))

       finally:
           print("Conexión pechada con exito")

