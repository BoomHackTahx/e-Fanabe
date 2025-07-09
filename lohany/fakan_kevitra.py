from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pickle, os

lalan_tahiry = "lohany/tahiry/fahalalana.txt"
lalan_fitoviana = "lohany/tahiry/fitoviana.pkl"

class Mpamantatra:
    def __init__(tena):
        tena.modely = SentenceTransformer("all-MiniLM-L6-v2")
        if not os.path.exists(lalan_fitoviana):
            tena.manomana()
        with open(lalan_fitoviana, "rb") as rakitra:
            tena.fahalalana, tena.fitoviana = pickle.load(rakitra)

    def manomana(tena):
        with open(lalan_tahiry, "r", encoding="utf-8") as rakitra:
            lahatsoratra = [andalana.strip() for andalana in rakitra if andalana.strip()]
        fitov = tena.modely.encode(lahatsoratra)
        with open(lalan_fitoviana, "wb") as rakitra:
            pickle.dump((lahatsoratra, fitov), rakitra)

    def valio(tena, fanontaniana):
    # Nettoyage simple : split selon ' sy ' (et), ',' etc.
        separateurs = [" sy ", ",", ";", "&", " ary "]
        sous_questions = [fanontaniana.lower()]

        for sep in separateurs:
            if sep in fanontaniana:
                sous_questions = [q.strip() for q in fanontaniana.lower().split(sep)]
                break

        valiny = []
        indices_deja_pris = set()

        for sous_q in sous_questions:
            emb = tena.modely.encode([sous_q])
            mari = cosine_similarity(emb, tena.fitoviana)[0]
            toerana = mari.argmax()

            # Pour éviter doublons
            if toerana not in indices_deja_pris:
                valiny.append(tena.fahalalana[toerana])
                indices_deja_pris.add(toerana)

        return "\n".join(valiny)