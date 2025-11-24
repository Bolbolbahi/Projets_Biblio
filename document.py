# ============================================
# document.py — Classes for all documents
# ============================================

from datetime import date


# ==============================
# PARENT CLASS : Document
# ==============================

class Document:

    def __init__(self, titre: str):
        self.titre = titre

    def get_type(self):
        return self.__class__.__name__

    def get_extra_fields(self):
        return []

    def to_csv(self):
        fields = [self.get_type(), self.titre] + self.get_extra_fields()
        return ";".join(str(f) for f in fields)

    def __str__(self):
        return f"{self.get_type()} — {self.titre}"


# ==============================
# VOLUME (superclass for: Livre, BD, Dictionnaire)
# ==============================

class Volume(Document):

    def __init__(self, titre: str, auteur: str):
        super().__init__(titre)
        self.auteur = auteur

    def get_extra_fields(self):
        return [self.auteur]

    def __str__(self):
        return f"{self.get_type()} — \"{self.titre}\", auteur: {self.auteur}"


# ==============================
# LIVRE : can be borrowed (empruntable)
# ==============================

class Livre(Volume):

    def __init__(self, titre: str, auteur: str, est_disponible=True):
        super().__init__(titre, auteur)
        self.est_disponible = est_disponible

    def emprunter(self):
        if not self.est_disponible:
            return False
        self.est_disponible = False
        return True

    def retourner(self):
        self.est_disponible = True

    def get_extra_fields(self):
        return [self.auteur, self.est_disponible]

    def __str__(self):
        dispo = "Disponible" if self.est_disponible else "Emprunté"
        return f"Livre — \"{self.titre}\", auteur: {self.auteur}, {dispo}"


# ==============================
# BANDE DESSINÉE : inherited from Volume
# ==============================

class BD(Volume):

    def __init__(self, titre: str, auteur: str, dessinateur: str):
        super().__init__(titre, auteur)
        self.dessinateur = dessinateur

    def get_extra_fields(self):
        return [self.auteur, self.dessinateur]

    def __str__(self):
        return (f"BD — \"{self.titre}\", auteur: {self.auteur}, "
                f"dessinateur: {self.dessinateur}")


# ==============================
# DICTIONNAIRE : inherited from Volume
# ==============================

class Dictionnaire(Volume):
    pass


# ==============================
# JOURNAL
# ==============================

class Journal(Document):

    def __init__(self, titre: str, date_parution: date):
        super().__init__(titre)
        self.date_parution = date_parution

    def get_extra_fields(self):
        return [self.date_parution.isoformat()]

    def __str__(self):
        return (f"Journal — \"{self.titre}\", paru le "
                f"{self.date_parution.isoformat()}")
