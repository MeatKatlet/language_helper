import spacy
from parser import Parser

#test this on one word - POS will change?
#token.lemma_ - send this to translation?
#token.tag_ - detalization of POS above

"""
https://spacy.io/usage/spacy-101#features
https://spacy.io/api/annotation#pos-tagging
https://universaldependencies.org/u/pos/
"""
def main():
    parser_poses = Parser.poses #translate only these
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop)

if __name__ == '__main__':
    main()