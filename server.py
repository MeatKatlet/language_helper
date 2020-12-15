import spacy
from parser import Parser
import subprocess
import os
#test this on one word - POS will change?
    #seems to be work - buying. he, advertisement...
#token.lemma_ - send this to translation?
#token.tag_ - detalization of POS above

"""
https://spacy.io/usage/spacy-101#features
https://spacy.io/api/annotation#pos-tagging
https://universaldependencies.org/u/pos/
"""
def test():
    parser_poses = Parser.poses  # translate only these
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
    doc2 = nlp("looking")
    doc3 = nlp("a man gone ninety years of age")
    doc4 = nlp("a gone case")
    doc5 = nlp("gone")
    doc6 = nlp("seen")
    doc7 = nlp("took")

    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop)

    for token in doc2:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop)

    for token in doc3:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop)

    for token in doc4:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop)

    for token in doc5:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop)

    for token in doc6:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop)

    for token in doc7:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop)

def main():
    # cd /home/kirill/sbd/dictserver
    os.chdir("/home/kirill/sbd/dictserver")

    #res = subprocess.run(["pwd"],capture_output=True)
    p = Parser()
    nlp = spacy.load("en_core_web_sm")
    #doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
    doc = nlp("looking")

    for token in doc:
        #java -cp jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m relative

        cmd = "java -cp jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m "+token.lemma_
        res = subprocess.check_output(cmd, shell=True)

        answer = res.decode("utf-8")
        p.translation = ""
        p.multiline_begins = False
        p.pos_finded_above = False

        translation = p.parse_answer(answer, token.pos_, token.lemma_)
        a = 1

if __name__ == '__main__':
    main()