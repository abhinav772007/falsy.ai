import re
import spacy
nlp = spacy.load("en_core_web_trf")
STOPWORDS={
    "is", "that", "the", "on", "a", "an", "i", "saw",
    "bro", "whatsapp", "twitter", "forwarded", "msg",
    "today", "now", "please", "true"
}
SYNONYMS = {
    "underwater": "flood",
    "waterlogged": "flood",
    "flooded": "flood",
    "quake": "earthquake",
    "fires": "wildfire",
    "prices": "price",
    "rates": "price"
}
def rewrite_query(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    doc = nlp(text)
    keywords = []

    for ent in doc.ents:
        if ent.text not in STOPWORDS:
            keywords.append(ent.text)

    for token in doc:
        if (
            token.text not in STOPWORDS
            and token.pos_ in ["NOUN", "PROPN"]
            and len(token.text) > 2
        ):
            keywords.append(token.text)

    keywords = list(dict.fromkeys(keywords))

    normalized = []
    for word in keywords:
        normalized.append(SYNONYMS.get(word, word))

    return " ".join(normalized[:5])
