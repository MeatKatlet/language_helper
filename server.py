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
        translation_res = ""
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

                    #return translation
                    translation_res += translation + " "

                finally:
                    if translation != "":
                        #return translation
                        translation_res += translation + " "

                    #return "error"
                    translation_res += "error "

            #else:
                #return word

        return translation_res


def producer_event(v):
    return json.dumps({"type": "producer_event", "value": v})


def state_event(v, word, index=""):
    return json.dumps({"type": "state", "value": v, "word": word, "index": index})


def error_event(v):
    return json.dumps({"type": "error_or_disconnect_end", "value": v})


"""
async def translate(websocket, path, data):
    try:
        translation = translator.translate(data["word"])
        await websocket.send(state_event(translation, data["word"], data["index"]))
    finally:
        await websocket.send(error_event("translate_error"))#notify users about errors!
"""


async def consumer_handler(websocket, path):
    # await websocket.send(state_event())
    try:
        async for message in websocket:
            data = json.loads(message)
            if data["action"] == "word":
                #await translate(websocket, path, data)
                translation = translator.translate(data["word"])
                await websocket.send(state_event(translation, data["word"]))#, data["index"]
            elif data["action"] == "whosaidthis":
                # TODO send request to volueme level when some word was sad, if one word was sad,
                # https://stackoverflow.com/questions/5046975/how-to-read-out-volume-level-of-clients-of-pulseaudio-in-the-console
                # parec --monitor-stream=378 --latency=2 --channels=1  2>/dev/null | od -N2 -td2 | head -n1 | cut -d' ' -f2- | tr -d ' '
                # word |(measure average value) if it stops saying then
                # or run it completly independently in the loop and constantly measure volueme
                # SINK=$(pactl list short clients | grep 'skypeforlinux' | python3 /home/kirill/Desktop/pulseaudio/iterate-stdin.py 1)
                a = 1
            elif data["action"] == "pulseaudioinit":
                # todo init pulse through bash script
                a = 1
            elif data["action"] == "pulseaudioinit":
                # todo return to deafult audio settings
                a = 1
            else:
                logging.error("unsupported event: {}", data)
                print("unsupported event: {}", data)
    finally:
        await websocket.send(error_event("consumer_handler_error"))#notify users about errors!


async def producer():
    await asyncio.sleep(5)#if use time.sleep(3)  then producer will not allow for consumer_handler to recieve messages
    return "producer_message"


async def producer_handler(websocket, path):
    while True:
        if websocket.open:#check if client connects
            message = await producer()
            await websocket.send(producer_event(message))
        else:
            print("websocket_closed")

    #send() raises a ConnectionClosed exception when the client disconnects, which breaks out of the while True loop.
    #todo stop server when I dont use extension! - connection closed
    print("while_ended")


async def handler(websocket, path):
    consumer_task = asyncio.ensure_future(consumer_handler(websocket, path))
    producer_task = asyncio.ensure_future(producer_handler(websocket, path))
    done, pending = await asyncio.wait(
        [consumer_task, producer_task],
        return_when=asyncio.FIRST_COMPLETED,
    )
    for task in pending:
        print("task pending cancel")
        task.cancel()


async def handler_old(websocket, path):
    try:
        #await websocket.send(state_event())

        # websocket.state = {State} State.OPEN
        # websocket.open = {bool} True
        # websocket.closed = {bool} False

        async for message in websocket:
            data = json.loads(message)
            if data["action"] == "word":
                translation = translator.translate(data["word"])
                await websocket.send(state_event(translation, data["word"]))#, data["index"]
            elif data["action"] == "whosaidthis":
                #TODO send request to volueme level when some word was sad, if one word was sad,
                #https://stackoverflow.com/questions/5046975/how-to-read-out-volume-level-of-clients-of-pulseaudio-in-the-console
                #parec --monitor-stream=378 --latency=2 --channels=1  2>/dev/null | od -N2 -td2 | head -n1 | cut -d' ' -f2- | tr -d ' '
                # word |(measure average value) if it stops saying then
                #or run it completly independently in the loop and constantly measure volueme
                #SINK=$(pactl list short clients | grep 'skypeforlinux' | python3 /home/kirill/Desktop/pulseaudio/iterate-stdin.py 1)
                a = 1
            elif data["action"] == "pulseaudioinit":
                #todo init pulse through bash script
                a = 1
            elif data["action"] == "pulseaudioinit":
                # todo return to deafult audio settings
                a = 1
            else:

                logging.error("unsupported event: {}", data)
                print("unsupported event: {}", data)
    finally:

        await websocket.send(error_event())#notify users about errors!


translator = Translator()


def main():
    #TODO in extension words and phrases are formed in cnunks - this need to take into account
    #
    #check if vocabulary server is running
    l = subprocess.getstatusoutput("ps aux |grep 'jdictd.jar'|wc -l")

    if l[1] == '3':

        start_server = websockets.serve(handler, "localhost", 6789)#, ping_interval=40, ping_timeout=40
        # todo what will be if timeout exceeds? it will reopen connection by itself?
        #under debugger its works infinytly!
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

    #TODO shutdown server when meeting closed - by button? start when Google Meet is open/check server running before meeting
    #check all servers running before meeting
    #start dictionary server/shutdown
    #
