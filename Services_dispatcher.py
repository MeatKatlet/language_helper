import subprocess
import psutil
from io import StringIO


class Services_dispatcher:

    def __init__(self, volume_monitor):
        self.dictionary_runs = False
        self.pulse_audio_default = True

        self.dictionary_process = None

        self.volume_monitor = volume_monitor

    def kill(self, proc_pid):
        process = psutil.Process(proc_pid)
        for proc in process.children(recursive=True):
            proc.kill()
        process.kill()

    def start_dictionary(self):
        if self.dictionary_runs == False:
            cmd = 'java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.server.JDictd /media/kirill/System/dictserver/Mueller/mueller.ini'
            self.dictionary_process = subprocess.Popen(cmd, shell=True)
            if self.dictionary_process.poll() is not None:
                return "dictionary not started"
        self.dictionary_runs = True
        return True

    def stop_dictionary(self):
        if self.dictionary_process is not None:
            if self.dictionary_process.poll() is None:
                self.kill(self.dictionary_process.pid)
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
                if line == "Chrome Google Meet Mic not found. Restart Meet Tab!\n":
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
            if line == "Skype Speaker not found. Restart Skype or run test call from its settings!\n":
                return line
        self.volume_monitor.what_was_initialised = 'skype'
        return True

    def check_if_zoom_sink_belongs_to_virtual2(self, zoom_sink):
        #find Zoom appropriate name
        #cmd = "pacmd list-sink-inputs | grep 'sink:\|client: 711190\|application.name = \"Google Chrome\"'"
        cmd = "pacmd list-sink-inputs | awk 'x==1 {print $0} /index: "+zoom_sink+"/ {x=1}'"#print all after match line
        res = subprocess.check_output(cmd, shell=True)
        answer = res.decode("utf-8")
        output = StringIO(answer, newline=None)
        sink_name = ""
        while line := output.readline():
            line = line.strip()
            if line[:4]=="sink":
                sink_name = line[line.find('<') + 1:line.rfind('>')]
            elif line == 'application.name = "ZOOM VoiceEngine"' and sink_name == 'Virtual2':
                self.volume_monitor.what_was_initialised = 'zoom'
                return True
        return "Set sound to Virtual2 in Zoom settings. If no Virtual2 then restart Zoom"


    def check_that_skype_or_zoom_is_running(self):
        skype_sink = self.volume_monitor.get_skype_sink_id()
        zoom_sink = self.volume_monitor.get_zoom_sink_id()

        return {"skype_sink": skype_sink, "zoom_sink": zoom_sink}