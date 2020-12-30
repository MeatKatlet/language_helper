#!/media/kirill/System/Users/Kirill/PycharmProjects/dictionary_parser/venv/bin/python3.8

import spacy
from parser import Parser
import subprocess
import websockets
import asyncio
import json
import logging

logging.basicConfig()
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


class Translator:
    def __init__(self):
        self.parser = Parser()
        self.nlp = spacy.load("en_core_web_sm")


    def translate(self, word):
        # doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
        #print(word)
        doc = self.nlp(word)
        #translation_res = ""
        for token in doc:
            # java -cp jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m relative
            translation = ""
            #print(token.lemma_)
            if token.pos_ in self.parser.poses:
                cmd = "java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m " + token.lemma_
                try:
                    res = subprocess.check_output(cmd, shell=True)

                    answer = res.decode("utf-8")
                    self.parser.translation = ""
                    self.parser.multiline_begins = False
                    self.parser.pos_finded_above = False
                    #print("################################################################################################")
                    #print(answer)
                    #print(token.pos_)

                    translation = self.parser.parse_answer(answer, token.pos_, token.lemma_)

                    return translation

                finally:
                    if translation != "":
                        return translation

                    return "error"

            else:
                return word


def state_event(v):
    return json.dumps({"type": "state", "value": v})


def end_event():
    return json.dumps({"type": "end", "value": "end"})


async def handler(websocket, path):
    try:
        #await websocket.send(state_event())
        async for message in websocket:
            data = json.loads(message)
            if data["action"] == "word":
                translation = translator.translate(data["word"])
                await websocket.send(state_event(translation))
            else:
                logging.error("unsupported event: {}", data)
                print("unsupported event: {}", data)
    finally:
        await websocket.send(end_event())


translator = Translator()


def main():
    #check if vocabulary server is running

    l = subprocess.getstatusoutput("ps aux |grep 'jdictd.jar'|wc -l")

    if l[1] == '3':

        start_server = websockets.serve(handler, "localhost", 6789, ping_interval=40, ping_timeout=40)
        # todo what will be if timeout exceeds? it will reopen connection by itself?
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

        # translation = translate()
        # a = 1
        # TODO test running of  translate() function
        # TODO how to send words to this translator? - by phrases or by single word - how to separate them by phrases i dont know. its better bu one
    else:
        logging.error("vocab server doesnt running")
        print("vocab server doesnt running")


if __name__ == '__main__':
    main()
