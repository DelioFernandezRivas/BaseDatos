import sqlite3 as dbaph1

class Base:
    """Clase de acceso a base de datos
    """






    def conexionDB (ruta):
        """Crea unha conexion coa base de datos  especificada na ruta"""







        try:
            bbbb = dbaph1.connect(ruta)
            return bbbb

        except dbaph1.DatabaseError as erroBaseDatos :
            print("Erro en conexionDB (DataBaseError):"+ str(erroBaseDatos))
        except dbaph1.OperationalError as erroBaseDatos:
            print("Erro en conexionDB (operationalerror):"+ str(erroBaseDatos))
        else:
            print("Conexion realizada con exito")

    def pechaConexionDB(conexion):

        """Pecha a conexion dunha base de datos sqlite"""



        try:
            conexion.close()
        except dbaph1.DatabaseError as erroBaseDatos:
            print("Erro en conexionDB (DataBaseError):" + str(erroBaseDatos))
        except dbaph1.OperationalError as erroBaseDatos:
            print("Erro en conexionDB (operationalerror):" + str(erroBaseDatos))
        else:
            print("Conexion pechada con exito")





