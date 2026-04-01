# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.corso import Corso


class Corso_DAO:

    @staticmethod
    def get_corsi():
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select codins , nome 
                from corso"""
        cursor.execute(query)
        res = []
        for row in cursor:
            res.append(Corso(codins = row["codins"],
                             nome = row["nome"],
                            ))
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def get_corsi_matricola(matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT c.codins, c.nome
                FROM corso c join iscrizione i on c.codins = i.codins 
                WHERE i.matricola = %s"""
        cursor.execute(query, (matricola,))
        res = []
        for row in cursor:
            res.append(Corso(codins=row["codins"],
                             nome=row["nome"],
                             ))
        cursor.close()
        cnx.close()
        return res