from Translator import Translator
import subprocess
import json
from Phrases_dispatcher import Phrases_dispatcher
"""
cmd = 'java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m hallo(a)'
return_code = 0
try:
    res = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    answer = res.decode('utf-8')

except Exception as e:
    a = 1
    return_code = e.returncode
    pass
finally:
    a = 1


"""
translator = Translator()

#res = translator.translate('I would like to talk about 2.5 kilograms of paper.')
#res = translator.translate('professor of translational genomic')
#res = translator.translate('I'm a clinical geneticist and professor of translational genomic ')
#res = translator.translate('geneticist and professor of translational genomic ')
#res = translator.translate('professor of translational genomic medicine')
#res = translator.translate('I'm a clinical geneticist and professor of translational genomic medicine at the University of')
#res = translator.translate('Manchester. ')
#res = translator.translate('technologies is that we're allowed to')
#res = translator.translate('clinical geneticists genetic counselors and')
#res = translator.translate('the laboratory scientists to deliver')
#res = translator.translate('see patient benefit one of the really')
#res = translator.translate('really see patient benefit one of the really')
#res = translator.translate('complex results so that we can really see patient benefit one of the really')
#res = translator.translate('some babies one in 500 are born with')
#res = translator.translate('do much more extensive testing.')
#res = translator.translate('some babies one in 500 are born with')
data = {}
data["phrase_prev"] = "applied in that setting, particularly "
data["phrase_middle"] = "for that very "
data["phrase_next"] = "High risk group where we need to "
res = translator.translate_long(data["phrase_prev"], data["phrase_middle"], data["phrase_next"])

exit(0)
data = {'action': 'word', 'word': 'of translational automated medicine ', 'prev_word': "I'm a chemical Genesis and professor ", 'replica_index': 0, 'index': 7}
phrases_dispatcher = Phrases_dispatcher()
#phrases_dispatcher.last_phrases_list = {'0_21': [{3: 'вещь', 7: 'ударять'}, {3: 11, 7: 27}, [-1, -1, -1, 'NOUN', -1, -1, -1, 'VERB', -1]], '0_22': [{1: 'говорить', 3: 'число'}, {1: 3, 3: 17}, [-1, 'VERB', -1, 'NOUN', -1, 'NOUN']], '0_23': [{1: 'сущность', 5: 'чувствовать'}, {1: 3, 5: 24}, [-1, 'NOUN', -1, -1, -1, 'VERB', -1]], '0_24': [{0: 'клинический', 3: 'генетический', 4: 'испытание'}, {0: 0, 3: 22, 4: 30}, ['ADJ', 'NOUN', -1, 'ADJ', 'NOUN']], '0_25': [{1: 'делать', 3: 'жребий', 5: 'другой'}, {1: 6, 3: 14, 5: 22}, [-1, 'VERB', -1, 'NOUN', -1, 'ADJ']], '0_27': [{1: 'клинический', 5: 'путь'}, {1: 3, 5: 29}, [-1, 'ADJ', 'NOUN', -1, -1, 'NOUN']], '0_28': [{1: 'думать', 3: 'совершенно', 4: 'увеличивать'}, {1: 2, 3: 11, 4: 22}, [-1, 'VERB', -1, 'ADV', 'VERB', -1]], '0_26': [{0: 'народ', 3: 'уменьшать', 5: 'роль'}, {0: 0, 3: 16, 5: 31}, ['NOUN', -1, -1, 'VERB', -1, 'NOUN']], '0_29': [{0: 'роль'}, {0: 0}, ['NOUN', -1, 'NOUN']], '0_30': [{1: 'надобность', 5: 'клинический'}, {1: 4, 5: 25}, [-1, 'NOUN', -1, 'NOUN', -1, 'ADJ']], '0_32': [{0: 'работа'}, {0: 0}, ['NOUN']]}

res = translator.translate2(data["word"], data["prev_word"])
phrases_dispatcher.add_phrase(res[:3]+[data["word"]], data["index"], data["replica_index"])
res2 = [[], []]
if len(res[5]) > 0 and data["index"] > 0: #pos1 - if prev phrase not with . in the end
    #phrase1_translations, phrase1_positions
    res2 = phrases_dispatcher.compare_current_prev_with_previous_word2(data["index"], res[3:], data["replica_index"])


data = {'action': 'word', 'word': 'at the University. ', 'prev_word': "of translational automated medicine ", 'replica_index': 0, 'index': 8}
res = translator.translate2(data["word"], data["prev_word"])
phrases_dispatcher.add_phrase(res[:3]+[data["word"]], data["index"], data["replica_index"])
res2 = [[], []]
if len(res[5]) > 0 and data["index"] > 0: #pos1 - if prev phrase not with . in the end
    #phrase1_translations, phrase1_positions
    res2 = phrases_dispatcher.compare_current_prev_with_previous_word2(data["index"], res[3:], data["replica_index"])
#phrases_dispatcher.add_phrase(res[:3], data["index"], data["replica_index"])

#res2 = [[], []]
#if len(res[5]) > 0 and data["index"] > 0: #pos1 - if prev phrase not with . in the end
    #phrase1_translations, phrase1_positions
    #res2 = phrases_dispatcher.compare_current_prev_with_previous_word2(data["index"], res[3:], data["replica_index"])

exit(0)
text_chuncks = ["My name is Bill Newman. ","I'm a clinical geneticist and ","of translational ","Health Center at the University of ","Manchester. ","I started in clinical genetics nearly ","25 years ago. ","And at that time we were really only ","able to do genetic testing for very ","small number of inheritance ","conditions. ","We've seen over the last 10 years ","with some of the new technologies is ","that they're allowed to do much more ","extensive testing. ","The biggest challenge is ensuring ","that we have enough clinical ","geneticists genetic counselors and ","laboratory Sciences to deliver the ","benefits that come with genomic ","medicine. ","One of the things that I'm struck by ","is speaking. ","The number of clinical geneticists is ","that they feel that clinical genetics ","and genetic testing is being done by ","lots of different people. ","So that diminishes the role of ","clinical genetics in some ways. ","I think it absolutely enhances the ","role of geneticists and the need for ","genetics. ","This clinical geneticist is going to ","be having to work much more closely ","with them to help them to interpret ","and understand. ","complex results ","One of the really big developments I ","see patient benefits. ","think is going to happen over the ","next few ","It's a lot of clinical geneticists in ","more common diseases that aren't due ","to a single genetic. ","Change or maybe combination of ","multiple genetic variants. ","We're already seeing the use of ","something called polygenic risk ","scores. ","This is a really useful development ","to help us work out people who may be ","at increased risk of certain ","conditions. ","Some of those risks are really very ","high completely comparable to the ","risk that you'll see for a single ","genetic change therefore the skills ","that we have in clinical genetics. ","I think can be applied in that ","setting particularly for that very ","high risk group that we need to ","explain the information both to the ","individual and the implications of ","other family members. ","One of the things that we've seen ","over the last few years was an ","increase in opportunities to be ","involved in new types of treatments ","where we never thought that ","treatments would be available. ","There are lots of Novel therapies ","that are now being used in patients ","with genetic conditions. ","For example, gene therapy is being ","Communications with imperative visual ","impairment increasingly. ","We're seeing how genetics can help ","us. ","Reduced the risk some individuals a ","good example of that was some babies ","one in 500 are born with a particular ","genetic change their mitochondria, ","which means that when they're given ","an antibiotic for Gentamicin, but ","they would develop profound ","irreversible hearing loss 90,000 ","babies in the UK. ","Every year are treated on Special ","Care Baby units with this antibiotic ","that antibiotic has to be given ","within the first hour of the arriving ","on the unit but genetic testing for ","this variant usually takes two to ","three days working with the local ","company. ","We've developed a point of care test ","which allows us from a simple cheek ","Squad to determine whether that baby ","carries such genetic variant yes or ","no just within 15 minutes. ","And so therefore we can work out ","which antibiotics should they should ","get so they won't develop hearing ","loss when it can be avoided genetics ","is changing. ","So rapidly there are so many advances ","so ","Findings on Research. ","I really excited one of the key roles ","of clinical Genesis is to assimilate ","that information separate out what's ","really technically relevant. ","And what's just interesting and take ","a leading role to disseminate and ","share their information with ","colleagues. ","So about you can translate those ","findings into real practice as ","quickly as possible but range of ","treatments the opportunities for ","achievements for a whole range of ","Physicians should be completely ","transformative over the years number ","of years after that's a wonderful "]
result = []

prev_chunk = ""

for i in range(0, len(text_chuncks)):
    chunk = text_chuncks[i]

    res = translator.translate2(chunk, prev_chunk)
    result.append([res[5], res[4], res[6], res[7]])
    prev_chunk = chunk
a = 1



with open('data1.txt', 'w') as f:
  json.dump(result, f)

#with open('data1.txt') as data_file:
    #result = json.load(data_file)
#[0 0 0 index 0 0 ] [0 0 0 index 0 0 ]
#                   [0 0 0 index 0 0 ] [0 0 0 index 0 0 ]
#                                      [0 0 0 index 0 0 ] [0 0 0 index 0 0 ]
#todo get
keys = {}
sum = 0
n = 0
prev_pair = None
compare_data = []
compare_data2 = []
compare_data.append([])
compare_data2.append([])

for i in range(0, len(result)):
    pair = result[i]
    if prev_pair is not None:
        if len(pair[0]) != len(prev_pair[1]):
            print("error")
            compare_data.append([])
            compare_data2.append([])
        else:
            compare_data.append([])
            compare_data2.append([])
            n +=1
            key = len(compare_data)-1
            compare_data[key].append(len(pair[0]))
            sum += len(pair[0])
            if len(pair[0]) not in keys:
                keys[len(pair[0])] = 1
            else:
                keys[len(pair[0])] += 1

            if len(pair[0]) != len(pair[2]):
                print("error2")
            if len(pair[1]) != len(pair[3]):
                print("error3")

            for j in range(0, len(pair[0])):
                if pair[0][j] != prev_pair[1][j]:
                    compare_data[key].append(j)
                    compare_data[key].append(pair[0][j])

                if pair[2][j] != prev_pair[3][j]:
                    compare_data2[key].append(j)
                    compare_data2[key].append((pair[2][j],prev_pair[3][j]))
    prev_pair = pair

avg = sum/n
with open('data2.txt', 'w') as f:
  json.dump(compare_data, f)


# Read JSON file
#with open('data.json') as data_file:
    #data_loaded = json.load(data_file)


