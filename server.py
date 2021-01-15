#!/media/kirill/System/Users/Kirill/PycharmProjects/dictionary_parser/venv/bin/python3.8

import spacy
from parser import Parser
import subprocess
import websockets
import asyncio
import json
import logging
from io import StringIO

logging.basicConfig()
# test this on one word - POS will change?
# seems to be work - buying. he, advertisement...
# token.lemma_ - send this to translation?
# token.tag_ - detalization of POS above

"""
https://spacy.io/usage/spacy-101#features
https://spacy.io/api/annotation#pos-tagging
https://universaldependencies.org/u/pos/
"""


class Translator:
    def __init__(self):
        self.parser = Parser()
        self.nlp = spacy.load("en_core_web_sm")

    def translate(self, word):
        # doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
        # print(word)
        doc = self.nlp(word)
        translation_res = ""
        for token in doc:
            # java -cp jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m relative
            translation = ""
            # print(token.lemma_)
            if token.pos_ in self.parser.poses:
                cmd = "java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m " + token.lemma_
                try:
                    res = subprocess.check_output(cmd, shell=True)

                    answer = res.decode("utf-8")
                    self.parser.translation = ""
                    self.parser.multiline_begins = False
                    self.parser.pos_finded_above = False
                    # print("################################################################################################")
                    # print(answer)
                    # print(token.pos_)

                    translation = self.parser.parse_answer(answer, token.pos_, token.lemma_)

                    # return translation
                    translation_res += translation + " "

                finally:
                    if translation != "":
                        # return translation
                        translation_res += translation + " "

                    # return "error"
                    translation_res += "error "

            # else:
            # return word

        return translation_res


class Volumemonitor():
    def __init__(self):
        self.skype_sink_id = self.get_skype_sink_id()
        self.zoom_sink_id = self.get_zoom_sink_id()


    def get_skype_sink_id(self):
        cmd = "pactl list short clients | grep 'skypeforlinux' | python3 /home/kirill/Desktop/pulseaudio/iterate-stdin.py 1"
        res = subprocess.check_output(cmd, shell=True)
        sink_id = res.decode("utf-8")
        self.skype_sink_id = sink_id
        return sink_id

    def get_zoom_sink_id(self):
        cmd = "pactl list short clients | grep 'zoom' | python3 /home/kirill/Desktop/pulseaudio/iterate-stdin.py 1"
        res = subprocess.check_output(cmd, shell=True)
        sink_id = res.decode("utf-8")
        self.zoom_sink_id = sink_id
        return sink_id

    def refind_sink(self):
        if self.skype_sink_id != 'null':
            return self.get_skype_sink_id()
        elif self.zoom_sink_id != 'null':
            return self.get_zoom_sink_id()
        else:
            return False

    def get_active_meeting_soft_sink(self):
        if self.skype_sink_id != 'null':
            # self.skype_sink_id = self.get_skype_sink_id()
            return self.skype_sink_id
        elif self.zoom_sink_id != 'null':
            # self.zoom_sink_id = self.get_zoom_sink_id()
            return self.zoom_sink_id
        else:
            return False


class Services_dispatcher:

    def __init__(self):
        self.dictionary_runs = False
        self.pulse_audio_default = True

        self.dictionary_process = None

    def start_dictionary(self):
        if self.dictionary_runs == False:
            cmd = 'java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.server.JDictd /media/kirill/System/dictserver/Mueller/mueller.ini'
            self.dictionary_process = subprocess.Popen(cmd, shell=True)
            if self.dictionary_process.poll() is None:
                return "dictionary not started"
        self.dictionary_runs = True
        return True

    def stop_dictionary(self):
        if self.dictionary_process.poll() is not None:
            self.dictionary_process.kill()
            self.dictionary_runs = False
            self.dictionary_process = None
        return True

    def set_pulse_audio(self):
        if self.pulse_audio_default == True:
            cmd = '/home/kirill/Desktop/pulseaudio/pulseaudio_load_setting.sh'
            res = subprocess.check_output(cmd, shell=True)
            answer = res.decode("utf-8")
            output = StringIO(answer, newline=None)
            while line := output.readline():
                if line == "Chrome Google Meet Mic not found. Restart Meet Tab!":
                    return line
        self.pulse_audio_default = False
        return True

    def set_pulse_audio_to_default(self):
        if self.pulse_audio_default == False:
            cmd = '/home/kirill/Desktop/pulseaudio/pulseaudio_load_deafult.sh'
            res = subprocess.check_output(cmd, shell=True)
            answer = res.decode("utf-8")
        self.pulse_audio_default = True
        return True

    def move_skype_sink_to_virtual2(self):

        cmd = '/home/kirill/Desktop/pulseaudio/pulseaudio_move_skype_sink_to_virtual2.sh'
        res = subprocess.check_output(cmd, shell=True)
        answer = res.decode("utf-8")
        output = StringIO(answer, newline=None)
        while line := output.readline():
            if line == "Skype Speaker not found. Restart Skype or run test call from its settings!":
                return line
        return True

    def check_if_zoom_sink_belongs_to_virtual2(self):
        #TODO find Zoom appropriate name
        """
        sink: 0 <alsa_output.pci-0000_08_00.4.analog-stereo>
		application.name = "Google Chrome"
        sink: 0 <alsa_output.pci-0000_08_00.4.analog-stereo>
            application.name = "Google Chrome"
        sink: 0 <alsa_output.pci-0000_08_00.4.analog-stereo>
        client: 711190 <Google Chrome>
            application.name = "Google Chrome"

        """
        cmd = "pacmd list-sink-inputs | grep 'sink:\|client: 711190\|application.name = \"Google Chrome\"'"
        res = subprocess.check_output(cmd, shell=True)
        answer = res.decode("utf-8")
        output = StringIO(answer, newline=None)
        while line := output.readline():
            line = line.strip()
            if line[:4]=="sink":
                #prev_sink = line.split(" ")[1]
                sink_name = line[line.find('<') + 1:line.rfind('>')]
            #elif line[:6]=="client":
               #client_id = line.split(" ")[1]
            elif line == 'application.name = "Google Chrome"' and sink_name == 'Virtual2':
                return True
        return "Set sound to Virtual2 in Zoom settings. If no Virtual2 then restart Zoom"


    def check_that_skype_or_zoom_is_running(self):
        skype_sink = volume_monitor.get_skype_sink_id()
        zoom_sink = volume_monitor.get_zoom_sink_id()

        return {"skype_sink": skype_sink, "zoom_sink": zoom_sink}


def producer_event(v):
    return json.dumps({"type": "producer_event", "interlocutor_speak": v})


def state_event(v, word, replica_index, index):
    return json.dumps({"type": "state", "value": v, "word": word, "replica_index": replica_index, "index": index})


def service_event(eventtype, v):
    return json.dumps({"type": "service_event", "eventtype": eventtype, "value": v})


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

                translation = translator.translate(data["word"])
                await websocket.send(state_event(translation, data["word"], data["replica_index"], data["index"]))
            elif data["action"] == "pulseaudioinit":
                res = services_dispatcher.set_pulse_audio()
                await websocket.send(service_event(data["action"], res))
            elif data["action"] == "pulseaudio_set_default":
                res = services_dispatcher.set_pulse_audio_to_default()
                await websocket.send(service_event(data["action"], res))
            elif data["action"] == "start_dictionary":
                res = services_dispatcher.start_dictionary()
                await websocket.send(service_event(data["action"], res))
            elif data["action"] == "check_that_skype_or_zoom_is_running":
                res = services_dispatcher.check_that_skype_or_zoom_is_running()# automatically starts producer to listen to their voluem if they launched

                if res["skype_sink"] != "null":
                    res2 = services_dispatcher.move_skype_sink_to_virtual2()
                elif res["zoom_sink"] != "null":
                    res2 = services_dispatcher.check_if_zoom_sink_belongs_to_virtual2()
                else:
                    res2 = False

                await websocket.send(service_event(data["action"], res2))

            elif data["action"] == "stop_dictionary":
                res = services_dispatcher.stop_dictionary()
                await websocket.send(service_event(data["action"], res))
            else:
                logging.error("unsupported event: {}", data)
                print("unsupported event: {}", data)
    finally:
        if websocket.open:
            await websocket.send(error_event("consumer_handler_error"))  # notify users about errors!
        else:# it runs when connection is closed (when tab closed or browser closed)
            # stop server dictionary
            services_dispatcher.stop_dictionary()
            # set pulse audio to default
            services_dispatcher.set_pulse_audio_to_default()
            # next 2 lines automatically blocks producer to run volueme listening
            volume_monitor.skype_sink_id = "null"
            volume_monitor.zoom_sink_id = "null"


async def producer():
    # https://stackoverflow.com/questions/5046975/how-to-read-out-volume-level-of-clients-of-pulseaudio-in-the-console
    # parec --monitor-stream=378 --latency=2 --channels=1  2>/dev/null | od -N2 -td2 | head -n1 | cut -d' ' -f2- | tr -d ' '
    # word |(measure average value) if it stops saying then
    # or run it completly independently in the loop and constantly measure volueme
    # SINK=$(pactl list short clients | grep 'skypeforlinux' | python3 /home/kirill/Desktop/pulseaudio/iterate-stdin.py 1)

    #   # if use time.sleep(3)  then producer will not allow for consumer_handler to recieve messages
    sink = volume_monitor.get_active_meeting_soft_sink()  # every skype call change it sink! so maybe zoom too? but browser contiunue to recieve on old sink!
    if sink != False:
        i = 0
        total = 0
        cmd = "parec --monitor-stream=" + sink + " --latency=2 --channels=1  2>/dev/null | od -N2 -td2 | head -n1 | cut -d' ' -f2- | tr -d ' '"

        # if reopening of skype happened - remapping of sink need to be performed! as in bash script! but browser contiunue to recieve on old sink!
        while i < 5:
            res = subprocess.check_output(cmd, shell=True)
            answer = res.decode("utf-8")
            if answer == "0000000\n":  # not actual sink
                sink = volume_monitor.refind_sink()  # find sink again!
                if sink == False:
                    a = 1
                    break
                cmd = "parec --monitor-stream=" + sink + " --latency=2 --channels=1  2>/dev/null | od -N2 -td2 | head -n1 | cut -d' ' -f2- | tr -d ' '"
                continue
            i += 1
            total += abs(int(answer))

        average = total / 5
        if average <= 100:
            return False
        elif average > 100:
            return True

        # 0 - no voice call at all
        # 0- 100 - backgrpung noise when somebody dont speak, but voice call is running
        # >100 pronouncing of words

    else:
        # TODO error handler or skype/zoom was opened?(but in bash script i already have this check) repeat sink finding again?
        a = 1


async def producer_handler(websocket, path):
    while True:
        # websocket.state = {State} State.OPEN
        # websocket.open = {bool} True
        # websocket.closed = {bool} False
        if websocket.open:  # check if client connects
            if volume_monitor.get_active_meeting_soft_sink() is not False:
                message = await producer()
                await websocket.send(producer_event(message))
            else:
                await asyncio.sleep(1)
    # send() raises a ConnectionClosed exception when the client disconnects, which breaks out of the while True loop.


async def handler(websocket, path):
    consumer_task = asyncio.ensure_future(consumer_handler(websocket, path))
    producer_task = asyncio.ensure_future(producer_handler(websocket, path))
    done, pending = await asyncio.wait(
        [consumer_task, producer_task],
        return_when=asyncio.FIRST_COMPLETED,
    )
    for task in pending:
        print("task pending cancel") #it runs when for example connection closed(tab or browser closed)
        task.cancel()


translator = Translator()
volume_monitor = Volumemonitor()
services_dispatcher = Services_dispatcher()


def main():
    # TODO in extension words and phrases are formed in cnunks - this need to take into account
    #
    # check if vocabulary server is running
    # l = subprocess.getstatusoutput("ps aux |grep 'jdictd.jar'|wc -l")

    # if l[1] == '3':

    start_server = websockets.serve(handler, "localhost", 6789)  # , ping_interval=40, ping_timeout=40
    # todo what will be if timeout exceeds? it will reopen connection by itself?
    # under debugger its works infinytly!
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

    # translation = translate()
    # a = 1
    # TODO test running of  translate() function
    # TODO how to send words to this translator? - by phrases or by single word - how to separate them by phrases i dont know. its better bu one
    # else:
    # logging.error("vocab server doesnt running")
    # print("vocab server doesnt running")


if __name__ == '__main__':
    main()

    # TODO shutdown server when meeting closed - by button? start when Google Meet is open/check server running before meeting
    # check all servers running before meeting
    # start dictionary server/shutdown
    #
