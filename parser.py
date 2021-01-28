from io import StringIO
import re
import subprocess


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
        #"PROPN" : "_n",
        # "PUNCT" : "",# ., (, ), ?
        # todo "SCONJ": "_cj" - "that" - error - need to find unteel  next semicolon if in current is ""
            # recently I will just exclude this type of words from translation
        #"SCONJ": "_cj",  # subordinating conjunction	if, while, that
        # "SYM" : "", #symbol	$, %, §, ©, +, −, ×, ÷, =, :), 😝
        "VERB": {"_v": None, "_inf": None, "_p": None, "_p-p": None}
        # "X" : "", #other	sfpksdpsxmsa
        # "SPACE" : "" #space
    }
    def __init__(self):

        self.translation = ""
        self.multiline_begins = False
        self.pos_finded_above = False
        self.breacket_open_on_prev_line = False

        self.recursion_protection = 0

        self.nlp = None
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
    def several_pos_protect(self, line):
        pattern = '_[a-z]+\.|_[а-я]+\.'
        return re.sub(pattern, " ", line, 0).strip()

    def handle_result(self, text):
        if text=="":
            self.multiline_begins = True
            return False

        res = self.remove_round_bracket_content(text)
        res["str"] = self.remove_square_brackets(res["str"])
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

    def remove_round_bracket_content(self, line):
        pattern = ' [а-я]{1}\)|\;[а-я]{1}\)|\.[а-я]{1}\)'
        line = re.sub(pattern, " ", line, 0)
        pattern2 = '\;[а-я]{1}\)'
        line = re.sub(pattern2, ";", line, 0)
        pattern3 = '^[0-9]+\)'
        line = re.sub(pattern3, "", line, 0)

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
            r += line[search_from+1:br_start]
            self.breacket_open_on_prev_line = True

        elif br_start != -1 and semicolon != -1 and semicolon < br_start:
            r += line[search_from+1:semicolon]
            return {"semicilon_end": True, "str": r.strip()}
        elif br_start != -1 and semicolon != -1 and semicolon > br_start:
            r += line[search_from + 1:br_start]
        elif br_start==-1 and semicolon != -1:
            r += line[search_from+1:semicolon]
            return {"semicilon_end": True, "str": r.strip()}
        elif br_start == -1 and semicolon == -1:
            r += line[search_from+1:]
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
                r += line[br_end+1:br_start]
            elif br_start != -1 and (br_start - br_end) > 1 and semicolon != -1 and semicolon < br_start:
                r += line[br_end+1:semicolon]
                return {"semicilon_end":True,"str":r.strip()}
            elif br_start == -1 and semicolon != -1:
                r += line[br_end+1:semicolon]
                return {"semicilon_end":True,"str":r.strip()}
            elif br_start == -1 and semicolon == -1:
                r += line[br_end+1:]

        return {"semicilon_end":False,"str":r.strip()}

    def remove_square_brackets(self, line):
        res = ""
        openpos = line.find("[")
        closepos = line.find("]")
        if openpos == -1 and closepos == -1:
            return line

        prev_end = 0
        while openpos != -1 or closepos != -1:
           if openpos != -1 and closepos != -1 and prev_end >= 0:
               if prev_end == 0:
                   res += line[:openpos]
               else:
                   res += line[prev_end+1:openpos]

               prev_end = closepos
               openpos = line.find("[", prev_end+1)
               closepos = line.find("]", prev_end+1)
           elif openpos != -1 and closepos == -1:
               if prev_end == 0:
                   res += line[:openpos]
               else:
                   res += line[prev_end+1:openpos]

               prev_end = -1
           elif openpos == -1 and closepos != -1:
               res += line[closepos+1:]
               prev_end = -1

        if prev_end != -1 and prev_end != 0:
            res += line[prev_end+1:]

        return res

    def parse_answer(self, answer, spacy_pos="spacy_pos1", origin_word="", adress_to_search1=False, adress_to_search2=False, original_phrase=False, word_index=False):
        self.translation = ""
        self.multiline_begins = False
        self.pos_finded_above = False

        self.recursion_protection += 1
        if self.recursion_protection > 3:
            return "recursion_erorr"
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


        if spacy_pos not in self.poses: #and answer[0:3]=="151":
            return origin_word  #spacy_pos no in parser list


        pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3}) \['
        pattern2 = '^[0-9]{1,2}\. _'
        pattern3 = '^([0-9]{1,2}\))|^(\*\))|^(\#\))'

        result = ""
        first_line = 0 #
        prev_lens = 0
        output = StringIO(answer, newline=None)
        while line := output.readline():
            if mode == -1:#determinetype of answer
                if line[:3] == "151":
                    mode = 0
                    first_line = 1
                    continue
                elif line[:3] == "152":
                    mode = 1
                    first_line = 1

                    continue
                elif line[:3] == "250":
                    #if mode==1 and result != "":
                        #result - word to search in one another request to dictionary
                        #a = 1
                    break
                else:
                    first_line = 1
                    #error!
            elif mode == 0:
                if first_line == 1:
                    first_line = 2
                elif first_line == 2:
                    string = line.strip()

                    if len(string) == 0:
                        continue

                    if len(string) == 1 and string[0] == ".":
                        return self.translation

                    if string[0] == "[" and adress_to_search2 == False:#1.case or 0.case
                        if self.translation != "":
                            return self.translation

                        transcript_end = string.rfind("]")
                        pos_start = string.find("_", transcript_end, transcript_end+3)

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
                                #if founded_pos_key=="_p":#? does this the only variant(what is p?)
                                    #find - от
                                    #_p. и _p-p. от seek
                                    #_p. и _p-p. от get 1
                                    #_p. и _p-p. от fight 2
                                    #a = 1
                                # 1.3

                                # 1.4
                                #find translation, if no, then find next _POS in that line
                                #_pron. перевод; перевод _pers. (_obj. thee) перевод; перевод _уст. _поэт. ты
                                #no _ no ()
                                #до _
                                #или
                                #до конца строки
                                #чтобы не было () внутри
                                #else:

                                if self.handle_result(string[pos_end+1:])==True:
                                    return self.translation
                                self.pos_finded_above = True

                            else:
                                #continue to search proper POS in that string or in others!
                                continue

                        else:#0.case

                            if len(string) > transcript_end+2 and string[transcript_end+2] == "=":  # CASES LIKE - [ˈkaunslə] = counsellor
                                word_to_search = string[transcript_end+4:]
                                #  add () delete [] from word
                                word_to_search = self.remove_square_brackets(word_to_search)
                                word_to_search = self.append_round_breakets_to_end(word_to_search)
                                answer2 = self.inner_request_to_dict(word_to_search)
                                if answer2 == 'error in inner request':
                                    return ""

                                self.recursion_protection = 0
                                translation = self.parse_answer(answer2, spacy_pos=spacy_pos)
                                return translation

                            continue

                    elif re.search(pattern, string) != None and ((adress_to_search2 == False) or (adress_to_search1 != False and string.find(adress_to_search1) == 0)):#2.case
                        if self.translation != "":
                            return self.translation

                        if adress_to_search1 != False:
                            adress_to_search1 = False

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
                                if self.handle_result(string[pos_end+1:]) == True:
                                    return self.translation
                                self.pos_finded_above = True
                            else:
                                # continue to search proper POS in that string or in others!
                                continue
                        else:
                            """
                            CASE LIKE 
                            151 "can" mueller_base "Mueller English-Russian Dictionary (base)": text follows
                            can
                            
                              I [kæn] (полная форма); [kən], [kn] (редуцированные формы) _v. (could)
                              модальный недостаточный глагол
                            
                                1) мочь, быть в состоянии, иметь возможность; уметь; I will do all I
                                ...
                            """
                            posibble_pos_pos = string.find("_", transcript_end)
                            if posibble_pos_pos != -1:
                                pos_end = string.find(".", posibble_pos_pos)
                                if pos_end != -1:
                                    founded_pos_key = string[posibble_pos_pos:pos_end]
                                    if (type(self.poses[spacy_pos]) is dict and founded_pos_key in self.poses[spacy_pos]) or \
                                            (type(self.poses[spacy_pos]) is not dict and founded_pos_key == self.poses[spacy_pos]):
                                        # extract transalation from string up untill ; sing or end of line - concat string untill;
                                        # exclude everything between (...)

                                        self.pos_finded_above = True
                                    else:
                                        # continue to search proper POS in that string or in others!
                                        continue
                            #others non significant forms?
                            continue

                    elif (re.search(pattern2, string) != None) and (adress_to_search2 == False or (adress_to_search1 == False and adress_to_search2 != False and string.find(adress_to_search2+".") == 0)):#3.case
                        if self.translation != "":
                            return self.translation

                        if adress_to_search2 != False:
                            adress_to_search2 = False

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

                            if self.handle_result(string[pos_end+1:]) == True:
                                return self.translation
                            self.pos_finded_above = True

                        else:
                            #find appropriate 3.case with needed _POS
                            continue

                    elif re.search(pattern3, string) != None and (adress_to_search2 == False or (adress_to_search1 == False and adress_to_search2 != False and string.find(adress_to_search2+")") == 0)):#4.case
                        if self.translation != "":
                            return self.translation

                        if adress_to_search2 != False:
                            adress_to_search2 = False

                        self.multiline_begins = False
                        self.breacket_open_on_prev_line = False

                        if self.pos_finded_above == True:#only if this section in finded POS above !
                            round_brk_start = string.find(")")

                            if self.handle_result(string[round_brk_start+1:]) == True:
                                return self.translation

                    elif self.multiline_begins == True and adress_to_search1 == False and adress_to_search2 == False:  #  for multiliner

                        if self.handle_result(string) == True:
                            return self.translation
                    else:
                        a = 1
            elif mode==1:
                string = line.strip()
                strings = string.split(" ")
                if len(strings) == 2:
                    variant = strings[1].replace('"', '')
                    if len(origin_word)> len(variant):
                        r = origin_word.find(variant)
                        if r == 0 and prev_lens < len(variant):
                            result = variant
                            prev_lens = len(variant)


                #test this and make sure. i think need to search by prefix

        if mode == 1:
            translation = result
            answer2 = self.inner_request_to_dict(result)
            if answer2 == 'error in inner request':
                return ""

            #TODO what POS to search?
            # insert result into original phrase and perform spacy nlp? - then get POS of result and pass it down? or only nlp(result)?
            #
            if original_phrase != False:
                words = re.split(" |'", original_phrase)  # original_phrase.split(" ") spacy splits also by apostroph  - re.split(" |'" , original_phrase)
                words[word_index] = result
                new_phrase = " ".join(words)

                doc = self.nlp(new_phrase)
                new_spacy_post = doc[word_index].pos_
                #TODO test this on whole phrases

                self.recursion_protection = 0
                translation = self.parse_answer(answer2, spacy_pos=new_spacy_post)

            return translation


        return self.translation

    def resolve_linkanswer(self, answer, pos):
        pattern = '^от [a-z]+ [0-9]+|^от [a-z]+ M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3}), [0-9]+'
        if re.search(pattern, answer) != None:#от much 1 и many 1
            answer = answer.replace("от ", "")
            parts = answer.split(" и ")
            parts2 = parts[0].split(" ")
            word_to_search = parts2[0]
            if len(parts2) == 3:
                digit_adress_to_search1 = parts2[1].replace(",", "")
                digit_adress_to_search2 = parts2[2]  # or it can be 1)
            else:
                digit_adress_to_search1 = False
                digit_adress_to_search2 = parts2[1]  # or it can be 1)

            answer2 = self.inner_request_to_dict(word_to_search)
            if answer2 == 'error in inner request':
                return ""

            self.recursion_protection = 0
            translation = self.parse_answer(answer2, spacy_pos=pos, adress_to_search1=digit_adress_to_search1, adress_to_search2=digit_adress_to_search2)
            return translation

        return answer

    def inner_request_to_dict(self, word_to_search):
        cmd = "java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m " + word_to_search
        return_code = 0
        answer = ""
        try:
            res = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
            answer = res.decode("utf-8")
        except Exception as e:
            return_code = -1  #e.returncode
            pass
        finally:
            if answer == "" or return_code != 0:
                answer = "error in inner request"

        return answer

    def append_round_breakets_to_end(self, word_to_search):
        word_to_search1 = word_to_search.replace("(", "")
        word_to_search1 = word_to_search1.replace(")", "")
        return word_to_search1

    def remove_after_comma(self, translation):
         comma_pos = translation.find(",")
         if comma_pos != -1:
              return translation[:comma_pos]
         return translation

    def remove_obsolete_characters(self, s):
        return re.sub('[^ёйа-яЁЙА-Я-: ]', '', s)



