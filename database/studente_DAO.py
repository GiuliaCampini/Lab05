# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente


class Studente_DAO:

    @staticmethod
    def get_studenti_iscritti(corso):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select s.nome , s.cognome, i.matricola  
                from iscrizione i join studente s on i.matricola=s.matricola
                where i.codins = %s"""
        cursor.execute(query, (corso,))
        res = []
        for row in cursor:
            res.append(Studente(row["nome"],
                                row["cognome"],
                                row["matricola"]))
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def get_matricolaStudente(matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """Select nome, cognome, matricola
                from studente
                where matricola = %s"""
        cursor.execute(query, (matricola,))
        res = None
        for row in cursor:
            res = Studente(row["nome"], row["cognome"], row["matricola"])
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def add_studCorso(matricola, codins):
        cnx = get_connection()
        try:
            cursor = cnx.cursor(dictionary=True)
            query = """INSERT INTO iscrizione (matricola, codins)
                        VALUES (%s, %s)"""
            cursor.execute(query, (matricola, codins))
            res = f"Studente {matricola} aggiunto con successo al corso {codins}"
            cnx.commit()
        except Exception as e:
            # In caso di errore (es. chiave duplicata), annulliamo
            cnx.rollback()
            res = f"Errore durante l'iscrizione: {e}"
        finally:
            cursor.close()
            cnx.close()
        return res