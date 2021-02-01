import subprocess

class Volumemonitor():
    def __init__(self):
        self.skype_sink_id = self.get_skype_sink_id()
        self.zoom_sink_id = self.get_zoom_sink_id()
        #self.one = False

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