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

#res = translator.translate("I would like to talk about")
#res = translator.translate("professor of translational genomic")
#res = translator.translate("I'm a clinical geneticist and professor of translational genomic ")
#res = translator.translate("geneticist and professor of translational genomic ")
#res = translator.translate("professor of translational genomic medicine")
#res = translator.translate("I'm a clinical geneticist and professor of translational genomic medicine at the University of")
#res = translator.translate("Manchester. ")
#res = translator.translate("technologies is that we're allowed to")
#res = translator.translate("clinical geneticists genetic counselors and")
#res = translator.translate("the laboratory scientists to deliver")
#res = translator.translate("see patient benefit one of the really")
#res = translator.translate("really see patient benefit one of the really")
#res = translator.translate("complex results so that we can really see patient benefit one of the really")
#res = translator.translate("some babies one in 500 are born with")
#res = translator.translate("do much more extensive testing.")
res = translator.translate("some babies one in 500 are born with")


a = 1

