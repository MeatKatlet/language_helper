from io import StringIO
import re

test = {
"test1" : '''151 "relative" mueller_base "Mueller English-Russian Dictionary (base)": text follows
relative

  [?rel?t?v]

    1. _n.

      1) родственник; родственница; a remote relative дальний родственник

      2) _грам. относительное местоимение (тж. relative pronoun)

    2. _a.

      1) относительный; сравнительный; relative surplus value _полит-эк.
      относительная прибавочная стоимость

      2) (to) соотносительный, взаимный; связанный один с другим

      3) соответственный

      4) _грам. относительный

.
250 Command complete
221 Closing connection''',
"test2" : '''151 "obesity" mueller_base "Mueller English-Russian Dictionary (base)": text follows
obesity

  [?u?bi:s?t?] _n. тучность; ожирение

.
250 Command complete
221 Closing connection''',
"test3" : '''151 "recognize" mueller_base "Mueller English-Russian Dictionary (base)": text follows
recognize

  [?rek?gna?z] _v.

    1) узнавать

    2) признавать; to recognize a new government признать новое
    правительство; to recognize smb. as lawful heir признать кого-л.
    законным наследником

    3) выражать признание, одобрение

    4) осознавать; to recognize one's duty понимать свой долг

.
250 Command complete
221 Closing connection''',
"test4" : '''151 "forgive" mueller_base "Mueller English-Russian Dictionary (base)": text follows
forgive

  [f??g?v] _v. (forgave; forgiven)

    1) прощать

    2) не требовать, не взыскивать (долг)

.
250 Command complete
221 Closing connection''',
"test5" : '''151 "beautiful" mueller_base "Mueller English-Russian Dictionary (base)": text follows
beautiful

  [?bju:t?ful] _a.

    1) красивый, прекрасный,

    2) превосходный

.
250 Command complete
221 Closing connection''',
"test6" : '''rg.dict.client.JDict -h localhost -p 2628 -d mueller_base -m seamlessly
152 16 matches found: list follows
mueller_base "seam"
mueller_base "seamaid"
mueller_base "seaman"
mueller_base "seamanship"
mueller_base "seamark"
mueller_base "seamew"
mueller_base "seamless"
mueller_base "seamstress"
mueller_base "seamy"
mueller_base "seanad eireann"
mueller_base "seance"
mueller_base "seapay"
mueller_base "seapen"
mueller_base "seapiece"
mueller_base "seapike"
mueller_base "seaplane"
.
250 Command complete
221 Closing connection''',
"test7" : '''151 "less" mueller_base "Mueller English-Russian Dictionary (base)": text follows
less

  [les]

    1. _a. (_comp. от little) меньший (о размере, продолжительности, числе
    и т.п.); in a less (или lesser) degree в меньшей степени; of less
    importance менее важный

      *) no less a person than никто иной, как сам (такой-то)

    2. _adv. меньше, менее; в меньшей степени; less known менее известный;
    less developed слаборазвитый (о стране и т.п.)

    3. _n. меньшее количество, меньшая сумма и т.п.; I cannot take less не
    могу взять меньше

      *) none the less тем не менее; in less than no time в мгновение ока

    4. _prep. без; a year less three days год без трёх дней
-less

  I [l?s] _suff. образует от основ существительных имена прилагательные со
  значением не имеющий или лишённый того, что обозначает основа: endless
  бесконечный; lifeless безжизненный; бездыханный; horseless безлошадный;
  fatherless без отца, не имеющий отца; windowless без окон, не имеющий
  окон; collarless без воротника, не имеющий воротника; umbrellaless без
  зонтика, не имеющий зонтика

  II [l?s] -suff. встречается в именах прилагательных, образованных от
  глагольных основ; указывает на невозможность с(о)вершения действия,
  обозначенного основой: cureless неизлечимый; countless неисчислимый;
  drainless неосушимый; imagineless невообразимый; fadeless неувядаемый;
  resistless непреодолимый; tireless неутомимый

.
250 Command complete
221 Closing connection''',
"test8" : '''151 "took" mueller_base "Mueller English-Russian Dictionary (base)": text follows
took

  [tuk] _p. от take 1

.
250 Command complete
221 Closing connection''',
"test9" : '''151 "thou" mueller_base "Mueller English-Russian Dictionary (base)": text follows
thou

  [?au] _pron. _pers. (_obj. thee) _уст. _поэт. ты

.
250 Command complete
221 Closing connection''',
"test10" : '''151 "nevertheless" mueller_base "Mueller English-Russian Dictionary (base)": text follows
nevertheless

  [?nev????les]

    1. _adv. несмотря на, однако

    2. _cj. тем не менее

.
250 Command complete
221 Closing connection''',
"test11" : '''151 "plane" mueller_base "Mueller English-Russian Dictionary (base)": text follows
plane

  I [ple?n]

    1. _n.

      1) плоскость (тж. _перен.); on a new plane на новой основе

      2) грань (кристалла)

      3) проекция

      4) уровень (развития знаний и т.п.)

      5) _разг. самолёт

      6) _ав. несущая поверхность; крыло (самолёта)

      7) _горн. уклон, бремсберг

    2. _a. плоский; плоскостной

    3. _v.

      1) парить

      2) _ав. скользить; планировать

      3) _разг. путешествовать самолётом

  II [ple?n]

    1. _nn.

      1) _тех. рубанок; струг; калёвка

      2) _стр. гладилка, мастерок

    2. _vv.

      1) строгать; скоблить; выравнивать

      2) _полигр. выколачивать (форму)

      #) plane away, plane down состругивать

  III [ple?n] _nnn. платан

.
250 Command complete
221 Closing connection''',
"test12" : '''151 "lean" mueller_base "Mueller English-Russian Dictionary (base)": text follows
lean

  I [li:n]

    1. _a.

      1) тощий, худой

      2) постный (о мясе)

      3) скудный; lean years неурожайные годы

      4) бедный (о руднике); убогий (о руде)

    2. _n. постная часть мясной туши, постное мясо

  II [li:n]

    1. _v. (leaned [li:nd], leant)

      1) наклонять(ся) (forward, over - вперёд, над)

      2) прислоняться, опираться (on, against); lean off the table! не
      облокачивайтесь на стол!

      3) полагаться (on, upon - на); основываться (on, upon - на); to lean
      on a friend's advice полагаться на совет друга

      4) иметь склонность (to, towards); I rather lean to your opinion я
      склоняюсь к вашему мнению

      *) to lean over backwards ударяться в другую крайность

    2. _nn. наклон

.
250 Command complete
221 Closing connection''',
"test13" : '''151 "hence" mueller_base "Mueller English-Russian Dictionary (base)": text follows
hence

  [hens]

    1. _adv.

      1) отсюда

      2) с этих пор; three years hence через три года, три года спустя

      3) следовательно

      *) to go hence умереть

    2. _int. прочь!, вон!

.
250 Command complete
221 Closing connection''',
"test14" : '''151 "a" mueller_base "Mueller English-Russian Dictionary (base)": text follows
A

  a

  I [e?] _n. (_pl. As, A's, Aes [e?z])

    1) 1-я буква англ. алфавита

    2) условное обозначение чего-л. первого по порядку, сортности и т.п.

    3) _амер. высшая отметка за классную работу; straight A "круглое
    отлично"

    4) _муз. ля

    *) from A to Z а) с начала и до конца; б) в совершенстве; полностью;
    A1 [?e??w?n] а) 1-й класс в судовом регистре Ллойда; б) _разг.
    первоклассный, превосходный; прекрасно, превосходно (_амер. A No. 1
    [?e??n?mb??w?n])

  II [e?] (полная форма); [?] (редуцированная форма)

    1) _грам. неопределённый артикль (a - перед согласными, перед eu и
    перед u, когда u произносится как [ju:]; an - перед гласными и перед
    немым h; напр.: a horse, но an hour; a European, a union, но an
    umbrella; тж. a one)

    2) один; it costs a penny это стоит одно пенни

    3) употр. перед little, few; good (или great) many и перед счётными
    существительными a dozen дюжина, a score два десятка, напр.: a little
    water (time, happiness) немного воды (времени, счастья); a few days
    (books) несколько дней (книг); a good (или great) many days (books)
    очень много дней (книг)

    4) (обыкн. после all of, many of) такой же, одинаковый; all of a size
    все одной и той же величины

    5) каждый; twice a day два раза в день

    6) некий; a Mr. Henry Green некий мистер Генри Грин
a-

  [?] _pref. (из первоначального предлога on)

    1) в предикативных прилагательных и в наречиях; напр.: abed в постели;
    alive живой; afoot пешком; ashore на берег и т.п.

    2) в выражениях типа: to go abegging нищенствовать; to go a-hunting
    идти на охоту

.
250 Command complete
221 Closing connection''',
"test15" : '''151 "to" mueller_base "Mueller English-Russian Dictionary (base)": text follows
to

  [tu:] (полная форма); [tu] (редуцированная форма, употр. перед гласным);
  [t?] (редуцированная форма, употр. перед согласным)

    1. _prep.

      1) указывает на направление к, в, на; the way to Moscow дорога в
      Москву; turn to the right поверните направо; I am going to the
      University я иду в университет; the windows look to the south окна
      выходят на юг
      
.
250 Command complete
221 Closing connection'''
}

class Parser():
    poses = {
        "ADJ": "_a",
        # "ADP" : "_prep", # adposition in, to, during
        "ADV": "_adv",
        # "AUX" : "_v",#? вспомогательный глагол
        # "CONJ" : {"_cj","_conj"},#союз, pronoun conjunctive - союзное местоимение - and, or, but
        # "CCONJ" : {"_cj","_conj"}, # the same?
        # "DET" : "",#a, an, the
        "INTJ": "_int",  # interjection - междометие
        "NOUN": "_n",
        # "NUM" : "_n-card", #1, 2017, one, seventy-seven, IV, MMXIV
        # "PART" : "",#particle	’s, not,
        "PRON": {"_pron":None, "_pers":None, "_demonstr":None, "_emph":None, "_indef":None, "_inter":None, "_poss":None, "_recipr":None, "_refl":None, "_rel":None},# pronoun - местоимение/личное местоимение I, you, he, she, myself, themselves, somebody
        # "PROPN" : "",# proper noun - Mary, John, London, NATO, HBO: dictionary of places or Names or Abbrevations
        # "PUNCT" : "",# ., (, ), ?
        "SCONJ": "_cj",  # subordinating conjunction	if, while, that
        # "SYM" : "", #symbol	$, %, §, ©, +, −, ×, ÷, =, :), 😝
        "VERB": {"_v":None, "_inf":None}
        # "X" : "", #other	sfpksdpsxmsa
        # "SPACE" : "" #space
    }
    def __init__(self):

        self.translation = ""
        self.multiline_begins = False
        self.pos_finded_above = False
        self.breacket_open_on_prev_line = False


        """
        poses = {
            "spacy_pos1" : "_n",
            "spacy_pos2" : "_a",
            "spacy_pos3" : "_v",
            "spacy_pos4" : "_p",
            "spacy_pos5" : "_adv",
            "spacy_pos6" : "_prep",
            "spacy_pos7" : "_pron",
            "spacy_pos8" : "_pers",
            "spacy_pos9" : "_cj",
            "spacy_pos10" : "_int"

        }
        """
    def several_pos_protect(self,line):
        pattern = '_[a-z]+\.'
        return re.sub(pattern, " ", line, 0).strip()

    def handle_result(self,text):

        res = self.remove_round_bracket_content(text)
        res["str"] = self.several_pos_protect(res["str"])

        if res["semicilon_end"] == False and res["str"] == "":
            # search further
            self.multiline_begins = True
        elif res["semicilon_end"] == False and res["str"] != "":
            # first line of multiline or untill next signal in hierarchy
            self.translation += res["str"]
            self.multiline_begins = True
        elif res["semicilon_end"] == True and res["str"] != "":
            self.translation += res["str"]
            return True

        return False

    def remove_round_bracket_content(self,line):
        pattern = ' [а-я]{1}\)|\;[а-я]{1}\)|\.[а-я]{1}\)'
        line = re.sub(pattern, " ", line, 0)
        pattern2 = '\;[а-я]{1}\)'
        line = re.sub(pattern2, ";", line, 0)

        r = ""
        search_from = 0
        if self.breacket_open_on_prev_line == True:#if on previous line breacket was open!
            search_from = line.find(")")
            if search_from==-1:#what if it multiline brackets content?
                #skip to next line?
                return {"semicilon_end": False, "str": r.strip()}

        br_start = line.find("(",search_from)
        semicolon = line.find(";", search_from)

        if br_start != -1 and semicolon == -1:
            r += line[search_from:br_start]
            self.breacket_open_on_prev_line = True

        elif br_start != -1 and semicolon != -1 and semicolon < br_start:
            r += line[search_from:semicolon]
            return {"semicilon_end": True, "str": r.strip()}
        elif br_start==-1 and semicolon != -1:
            r += line[search_from:semicolon]
            return {"semicilon_end": True, "str": r.strip()}
        elif br_start == -1 and semicolon == -1:
            r += line[search_from:]
            return {"semicilon_end": False, "str": r.strip()}

        while br_start != -1:

            br_end = line.find(")",br_start)
            #br_start = -1
            if br_end != -1:
                self.breacket_open_on_prev_line = False
                br_start = line.find("(",br_end)
                semicolon = line.find(";",br_end)
            else:
                self.breacket_open_on_prev_line = True
                return {"semicilon_end": False, "str": r.strip()}


            if br_start != -1 and (br_start-br_end) > 1 and semicolon == -1:
                r += line[br_end:br_start]
            elif br_start != -1 and (br_start - br_end) > 1 and semicolon != -1 and semicolon < br_start:
                r += line[br_end:semicolon]
                return {"semicilon_end":True,"str":r.strip()}
            elif br_start == -1 and semicolon != -1:
                r += line[br_end:semicolon]
                return {"semicilon_end":True,"str":r.strip()}
            elif br_start == -1 and semicolon == -1:
                r += line[br_end:]

        return {"semicilon_end":False,"str":r.strip()}

    def parse_answer(self, answer,spacy_pos="spacy_pos1",origin_word = ""):
        #get type of answwer? 151 or 152
        #lines = answer.split("\n")
        mode = -1#0,1,2
        subtype_of_151 = -1#
        #subtype_of_151 = 0# several POS and several translation lines in each
        # subtype_of_151 = 1# one liner POS and 1 translation
        # subtype_of_151 = 6# one liner POS and link to proper form of verb

        # subtype_of_151 = 2# one POS and several translation lines
        # subtype_of_151 = 3# one POS and several translation lines + round squares near POS
        # subtype_of_151 = 4# several POS - one line of translation for each
        # subtype_of_151 = 5# several POS - one line of translation for each + examples can be for each POS
        # subtype_of_151 = 7# several categories like I, II, III + each category consist of several POS, each POS can be one liner or with several translations
        # subtype_of_151 = 8# categoriy one liner
        # subtype_of_151 = 9# category+POS with several translations
        # subtype_of_151 = 10# suffix-prefix

        #transcription(phonetic) can be miltilines, each line can be with squares - in any type

        #0.case
        #[transcription]

        #1.case
        #1.1# [transcription] _POS.
        #or
        #1.2# [transcription] _POS. от take 1 - ссылка
        #...multiline can be
        #or
        #1.3# [transcription] _POS. _POS. ... translation; ...
        # ...multiline can be
        #or
        #1.4# [transcription] _POS. (can be) translation;
        # ...multiline can be

        # 2.case
        #2.1#(I, II, III) [transcription]
        #or
        #2.2#(I, II, III) [transcription] (...); [transcription] (...)
        # .... [can be miltiline]
        #or
        #2.3#(I, II, III) [transcription] _POS. (can be) translation ...; ... [transcription]
        #... multiline can be

        # 3.case
        #(1.2.3.) _POS. (can be)
        #or
        #(1.2.3.) _POS. (can be) translation (can be) ; ...
        #...multiline can be

        # 4.case
        #1)2)3)*) translation ; translation
        # ... multiline can be

        # 1)2)3)*) а) translation ; translation б) ranslation ; translation
        # ... multiline can be

        # 5.case
        #-a-  суффикс/префикс

        #translation [gfgf]


        if spacy_pos not in self.poses:
            return "spacy_pos no in parser list"



        pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3}) \['
        pattern2 = '^[0-9]{1,2}\. _'
        pattern3 = '^([0-9]{1,2}\))|^(\*\)|^(\#\))'

        result = ""
        first_line = 0 #
        output = StringIO(answer, newline=None)
        while line := output.readline():
            if mode == -1:#determinetype of answer
                if line[:3]=="151":
                    mode = 0
                    first_line = 1
                    continue
                elif line[:3]=="152":
                    mode = 1
                    first_line = 1
                    continue
                elif line[:3]=="250":
                    if mode==1 and result != "":
                        #result - word to search in one another request to dictionary
                        a = 1
                    break
                else:
                    first_line = 1
                    #error!
            elif mode==0:
                if first_line == 1:
                    first_line = 2
                elif first_line ==2:
                    string = line.strip()

                    if string[0] == "[":#1.case or 0.case
                        transcript_end = string.find("]")
                        pos_start = string.find("_",transcript_end,transcript_end+3)

                        if pos_start != -1:#1.case
                            self.multiline_begins = False
                            self.breacket_open_on_prev_line = False

                            pos_end = string.find(".",pos_start)
                            founded_pos_key = string[pos_start:pos_end]


                            if (type(self.poses[spacy_pos]) is dict and founded_pos_key in self.poses[spacy_pos]) or \
                                (type(self.poses[spacy_pos]) is not dict and founded_pos_key==self.poses[spacy_pos]):

                                #get translate in this section
                                #translation or link
                                # 1.1
                                # 1.2
                                if founded_pos_key=="_p":#? does this the only variant(what is p?)
                                    #find - от
                                    a = 1
                                # 1.3

                                # 1.4
                                #find translation, if no, then find next _POS in that line
                                #_pron. перевод; перевод _pers. (_obj. thee) перевод; перевод _уст. _поэт. ты
                                #no _ no ()
                                #до _
                                #или
                                #до конца строки
                                #чтобы не было () внутри
                                else:

                                    if self.handle_result(string[pos_end:])==True:
                                        return self.translation
                                    self.pos_finded_above = True

                            else:
                                #continue to search proper POS in that string or in others!
                                continue

                        else:#0.case
                            continue

                    elif re.search(pattern, string) != None:#2.case
                        self.multiline_begins = False
                        self.breacket_open_on_prev_line = False

                        transcript_end = string.find("]")
                        # 2.1
                        if string[-1]=="]":
                            #only transcription in line
                            continue
                        # 2.3
                        elif string[transcript_end+2] == "_":
                            pos_end = string.find(".", transcript_end+2)
                            founded_pos_key = string[transcript_end+2:pos_end]

                            if (type(self.poses[spacy_pos]) is dict and founded_pos_key in self.poses[spacy_pos]) or \
                                (type(self.poses[spacy_pos]) is not dict and founded_pos_key == self.poses[spacy_pos]):
                                #extract transalation from string up untill ; sing or end of line - concat string untill;
                                #exclude everything between (...)
                                if self.handle_result(string[pos_end:]) == True:
                                    return self.translation
                                self.pos_finded_above = True
                            else:
                                # continue to search proper POS in that string or in others!
                                continue
                        else:
                            #others non significant forms?
                            continue

                    elif re.search(pattern2, string) != None:#3.case
                        self.multiline_begins = False
                        self.breacket_open_on_prev_line = False

                        pos_start = string.find("_")
                        pos_end = string.find(".",pos_start)
                        founded_pos_key = string[pos_start:pos_end]

                        if (type(self.poses[spacy_pos]) is dict and founded_pos_key in self.poses[spacy_pos]) or \
                            (type(self.poses[spacy_pos]) is not dict and founded_pos_key == self.poses[spacy_pos]):
                            #extract translation from first
                            # translation in that line or it have several 1) 2) of translations
                            #remove all square brackets from line then if anything remains then it will be the translation

                            if self.handle_result(string[pos_end:]) == True:
                                return self.translation
                            self.pos_finded_above = True

                        else:
                            #find appropriate 3.case with needed _POS
                            continue

                    elif re.search(pattern3, string) != None:#4.case
                        self.multiline_begins = False
                        self.breacket_open_on_prev_line = False

                        if self.pos_finded_above == True:#only if this section in finded POS above !
                            round_brk_start = string.find(")")

                            if self.handle_result(string[round_brk_start:]) == True:
                                return self.translation

                    elif self.multiline_begins == True:#for multiliner

                        if self.handle_result(string) == True:
                            return self.translation
                    else:
                        a = 1
            elif mode==1:
                string = line.strip()
                strings = string.split(" ")
                prev_lens = 0
                if len(strings) == 2:
                    variant = strings[1].replace('"', '')
                    if len(origin_word)> len(variant):
                        r = origin_word.find(variant)
                        if r == 0 and prev_lens < len(variant):
                            result = variant
                            prev_lens = len(variant)


                #test this and make sure. i think need to search by prefix


        return self.translation

def main():
    p = Parser()
    #Parser.poses["NON"] = "_non"
    Parser.poses["PREP"] = "_prep"
    Parser.poses["P"] = "_p"
    Parser.poses["NN"] = "_nn"
    Parser.poses["VV"] = "_vv"
    Parser.poses["NNN"] = "_nnn"


    test_set = {
        "test1" : [["NOUN","_n"],["ADJ","_a"],["NON","_non"]],
        "test2": [["NOUN","_n"],["NON","_non"]],
        "test3": [["VERB","_v"],["NON","_non"]],
        "test4": [["VERB","_v"],["NON","_non"]],
        "test5": [["ADJ","_a"],["NON","_non"]],
        "test7": [["ADJ","_a"],["ADV","_adv"],["NOUN","_n"],["PREP","_prep"],["NON","_non"]],
        "test8": [["P","_p"],["NON","_non"]],
        "test9": [["PRON","_pron"],["NON","_non"]],
        "test10": [["ADV","_adv"],["SCONJ","_cj"]],
        "test11": [["NOUN","_n"],["ADJ","_a"],["VERB","_v"],["NN","_nn"],["VV","_vv"],["NNN","_nnn"],["NON","_non"]],
        "test12": [["ADJ","_a"],["NOUN","_n"],["VERB","_v"],["NN","_nn"],["NON","_non"]],
        "test13": [["ADV","_adv"],["INTJ","_int"],["NON","_non"]],
        "test14": [["NOUN","_n"],["NON","_non"]],
        "test15": [["PREP","_prep"],["NON","_non"]]
    }

    for key,value in test_set.items():
        for i in range(0,len(value)):
            spacy_pos = value[i][0]

            p.translation = ""
            p.multiline_begins = False
            p.pos_finded_above = False
            translation = p.parse_answer(test[key],spacy_pos)

    p.translation = ""
    p.multiline_begins = False
    p.pos_finded_above = False
    translation = p.parse_answer(test["test6"], "spacy_pos1","seamlessly")


if __name__ == '__main__':
    #find what possible POS can be in Spacy and correct my poses dictionary to map with possible POS in dictionary
    #https://spacy.io/api/annotation#pos-tagging
    #create sets of dictionary article - all possible POS in structure(lines where to search answer)
    #run my function parse_answer against every possible combination for testing

    #protect from several _POS _POS in one string
    #а) in the middle
    main()