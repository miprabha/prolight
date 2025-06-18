import spacy

#biomedical model 
nlp = spacy.load("en_ner_bionlp13cg_md")

def get_values(text):
    data = nlp(text)
    values = []
    for ent in data.ents:
        if ent.label_ in ["GENE_OR_GENE_PRODUCT", "DISEASE", "SIMPLE_CHEMICAL"]:
            values.append({
                "text": ent.text,
                "label": ent.label_,
                "start": ent.start_char,
                "end": ent.end_char
            })
    return values