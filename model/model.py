from database.corso_DAO import Corso_DAO
from database.studente_DAO import Studente_DAO

class Model:
    def __init__(self):
        pass

    def get_corsi(self):
        return Corso_DAO.get_corsi()

    def get_studenti_iscritti(self, corso):
        return Studente_DAO.get_studenti_iscritti(corso)

    def get_matricolaStudente(self, matricola):
        return Studente_DAO.get_matricolaStudente(matricola)

    def get_corsi_matricola(self, matricola):
        return Corso_DAO.get_corsi_matricola(matricola)

    def add_studCorso(self, matricola, codins):
        return Studente_DAO.add_studCorso(matricola, codins)