#!/media/kirill/System/Users/Kirill/PycharmProjects/dictionary_parser/venv/bin/python3.8

import subprocess
import websockets
import asyncio
import json
import logging
from Volumemonitor import Volumemonitor
from Services_dispatcher import Services_dispatcher
from Translator import Translator
#from Phrases_dispatcher import Phrases_dispatcher

logging.basicConfig()


def producer_event(v):
    return json.dumps({"type": "producer_event", "interlocutor_speak": v})


def long_phrase_answer(phrase_translations, positions, phrase_prev, phrase_middle, phrase_next, replica_index, index):

    if index == 1:
        return json.dumps({"type": "long_phrase_answer",
                           "phrase_translations": phrase_translations[1],
                           "positions": positions[1],
                           "zero_translations": phrase_translations[0],
                           "zero_positions": positions[0],
                           "phrase_prev": phrase_prev,
                           "phrase_middle": phrase_middle,
                           "phrase_next": phrase_next,
                           "replica_index": replica_index,
                           "index": index
                           })
    else:
        return json.dumps({"type": "long_phrase_answer",
                           "phrase_translations": phrase_translations,
                           "positions": positions,
                           "phrase_prev": phrase_prev,
                           "phrase_middle": phrase_middle,
                           "phrase_next": phrase_next,
                           "replica_index": replica_index,
                           "index": index
                           })


def after_speach_pause_answer(phrases_translations, positions, replica_index):
    return json.dumps({
        "type": "speach_pause",
        "phrases_translations": phrases_translations,
        "positions": positions,
        "replica_index": replica_index,
    })


def state_event(phrase2_translations, raw_phrase2, positions2, replica_index, index):
    return json.dumps({"type": "state",
                       "phrase2_translations": phrase2_translations,
                       "positions2": positions2,
                       "word2": raw_phrase2,
                       "replica_index": replica_index,
                       "index": index,

                       })


def service_event(eventtype, v):
    return json.dumps({"type": "service_event", "eventtype": eventtype, "value": v})


def error_event(v):
    return json.dumps({"type": "error_or_disconnect_end", "value": v})


async def consumer_handler(websocket, path):
    # await websocket.send(state_event())
    try:

        async for message in websocket:
            data = json.loads(message)
            if data["action"] == "word":

                res = translator.translate(data["word"])

                await websocket.send(state_event(res[0], data["word"], res[1], data["replica_index"], data["index"]))

            elif data["action"] == "long_phrase":
                if data["index"] == 1:
                    res1 = translator.translate_long("", data["phrase_prev"], data["phrase_middle"])
                    res2 = translator.translate_long(data["phrase_prev"], data["phrase_middle"], data["phrase_next"])
                    res = [[res1[0], res2[0]], [res1[1], res2[1]]]
                    #[words_translations, positions_of_translated_words]
                    #[words_translations, positions_of_translated_words]
                else:
                    res = translator.translate_long(data["phrase_prev"], data["phrase_middle"], data["phrase_next"])

                await websocket.send(long_phrase_answer(
                    res[0],
                    res[1],
                    data["phrase_prev"],
                    data["phrase_middle"],
                    data["phrase_next"],
                    data["replica_index"],
                    data["index"]))

            elif data["action"] == "speach_pause":
                res = translator.translate_after_speach_pause(data["text"])
                await websocket.send(after_speach_pause_answer(res[0], res[1], data["replica_index"]))

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
                    res2 = services_dispatcher.check_if_zoom_sink_belongs_to_virtual2(res["zoom_sink"])
                else:
                    res2 = False

                await websocket.send(service_event(data["action"], res2))

            elif data["action"] == "stop_dictionary":
                res = services_dispatcher.stop_dictionary()
                await websocket.send(service_event(data["action"], res))
            elif data["action"] == "init_request":
                await websocket.send(service_event(data["action"], "ok"))
            else:
                logging.error("unsupported event: {}", data)
                print("unsupported event: {}", data)
    except Exception as e:
        return_code = -1  # e.returncode
        pass
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
    await asyncio.sleep(0.5)
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
services_dispatcher = Services_dispatcher(volume_monitor)


def main():
    # TODO in extension words and phrases are formed in cnunks - this need to take into account
    #
    # check if vocabulary server is running
    # l = subprocess.getstatusoutput("ps aux |grep 'jdictd.jar'|wc -l")

    # if l[1] == '3':
    #https://stackoverflow.com/questions/54101923/1006-connection-closed-abnormally-error-with-python-3-7-websockets
    start_server = websockets.serve(handler, "localhost", 6789, ping_interval=None)  #
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
