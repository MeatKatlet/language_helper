from server import Translator
import subprocess

"""
cmd = "java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m hallo(a)"
return_code = 0
try:
    res = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    answer = res.decode("utf-8")

except Exception as e:
    a = 1
    return_code = e.returncode
    pass
finally:
    a = 1


"""
translator = Translator()

res = translator.translate("I would like to talk about")
a = 1

