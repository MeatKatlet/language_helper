import spacy
from parser import Parser
from Stop_words import Stop_words
import subprocess
import re
"""
https://spacy.io/usage/spacy-101#features
https://spacy.io/api/annotation#pos-tagging
https://universaldependencies.org/u/pos/
"""
class Translator:
    def __init__(self):
        self.parser = Parser()
        self.nlp = spacy.load("en_core_web_sm")
        self.parser.nlp = self.nlp
        self.stop_words = Stop_words.stop_words
        #self.phrases_dispatcher = phrases_dispatcher

    def translate(self, phrase):
        # doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
        doc = self.nlp(phrase)
        # translation_res = ""
        words_translations = []
        # i = 0
        positions_of_translated_words = []
        for token in doc:
            translation = ""
            if token.lemma_ == "-PRON-":
                # translation_res +=  ""#token.text +
                continue

            elif token.pos_ in self.parser.poses and token.lemma_ not in self.stop_words:
                cmd = "java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m " + token.lemma_
                return_code = 0
                try:
                    res = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
                    answer = res.decode("utf-8")

                    self.parser.recursion_protection = 0
                    translation = self.parser.parse_answer(answer, spacy_pos=token.pos_, origin_word=token.lemma_,
                                                           original_phrase=phrase, word_index=token.i, word_pos=token.idx)
                    translation = self.parser.resolve_linkanswer(translation, token.pos_)
                    translation = self.parser.remove_after_comma(translation)
                    translation = self.parser.remove_obsolete_characters(translation)

                except Exception as e:
                    return_code = -1  # e.returncode
                    pass
                finally:
                    if translation == "" or return_code != 0:
                        # translation_res += ""#"/"+token.text+"/ "
                        continue
                    else:
                        # translation_res += "<span>" + translation + "</span>"
                        words_translations.append(translation)
                        positions_of_translated_words.append(token.idx)

            elif token.pos_ == "PUNCT" and token.text == ".":
                # s = translation_res[:-1]
                # translation_res = s+". "
                #words_translations.append(".")
                continue
            else:
                # translation_res += ""#token.text +
                continue

            # i += 1

        return [words_translations, positions_of_translated_words]

    def translate_long(self, phrase_prev, phrase_middle, phrase_next):
        # doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

        striped = phrase_prev.strip()
        last_char = striped[-1:]
        #prev_phrase_shift = 0

        if last_char == ".":
            #words = re.split(" |'", prev_phrase.strip())
            #l = len(words)
            final_phrase = phrase_middle+phrase_next
            middle_phrase_l = len(phrase_middle)
            prev_phrase_l = 0
            prev_phrase_shift = 0
        else:
            prev_phrase_l = len(phrase_prev)
            middle_phrase_l = prev_phrase_l+len(phrase_middle)
            final_phrase = phrase_prev + phrase_middle + phrase_next
            prev_phrase_shift = prev_phrase_l

        doc = self.nlp(final_phrase)

        words_translations = []
        positions_of_translated_words = []

        middle_phrase_begins = False
        for token in doc:
            translation = ""
            if token.idx == prev_phrase_l:
                middle_phrase_begins = True
                #prev_phrase_shift = prev_phrase_l
            elif token.idx == middle_phrase_l:
                middle_phrase_begins = False
                break


            if middle_phrase_begins == False:
                continue

            if token.lemma_ == "-PRON-":
                continue
            elif token.pos_ == "PUNCT" and token.text == ".":
                # . in the middle of prev phrase
                #second_part_begins = True
                #prev_phrase_shift = prev_phrase_l - token.idx
                continue
            elif token.pos_ in self.parser.poses and token.lemma_ not in self.stop_words:

                cmd = "java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m " + token.lemma_
                return_code = 0
                try:
                    res = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
                    answer = res.decode("utf-8")

                    self.parser.recursion_protection = 0
                    translation = self.parser.parse_answer(answer, spacy_pos=token.pos_, origin_word=token.lemma_, original_phrase=final_phrase, word_index=token.i, word_pos=token.idx)
                    translation = self.parser.resolve_linkanswer(translation, token.pos_)
                    translation = self.parser.remove_after_comma(translation)
                    translation = self.parser.remove_obsolete_characters(translation)

                except Exception as e:
                    return_code = -1  # e.returncode
                    pass
                finally:
                    if translation == "" or return_code != 0:
                        #translation_res += ""#"/"+token.text+"/ "
                        continue
                    else:
                        #translation_res += "<span>" + translation + "</span>"

                        words_translations.append(translation)
                        positions_of_translated_words.append(token.idx-prev_phrase_shift)# total position in phrase
            else:
                continue

        return [words_translations, positions_of_translated_words]

    def translate_after_speach_pause(self, last_phrases):

        final_text = ""

        words_translations = {}
        positions_of_translated_words = {}
        phrases_lengths = []

        keys = sorted(last_phrases, key=lambda item: int(item))
        total_length = 0
        for key in keys:
            words_translations[key] = []
            positions_of_translated_words[key] = []
            total_length += len(last_phrases[key])
            phrases_lengths.append(total_length)

            final_text += last_phrases[key]

        if keys[0] != '0':
            del words_translations[keys[0]]
            del positions_of_translated_words[keys[0]]
            i = 0
        else:
            i = -1
            phrases_lengths[i] = 0

        #first phrase was already sended as middle

        doc = self.nlp(final_text)
        middle_phrase_begins = False


        total_shift = 0
        for token in doc:
            translation = ""
            if token.idx == phrases_lengths[i]:
                total_shift = phrases_lengths[i]
                if i == 0 or i == -1:
                    middle_phrase_begins = True
                i += 1

            if middle_phrase_begins == False:
                continue

            if token.lemma_ == "-PRON-":
                continue
            elif token.pos_ == "PUNCT" and token.text == ".":
                # . in the middle of prev phrase
                # second_part_begins = True
                # prev_phrase_shift = prev_phrase_l - token.idx
                continue
            elif token.pos_ in self.parser.poses and token.lemma_ not in self.stop_words:

                cmd = "java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m " + token.lemma_
                return_code = 0
                try:
                    res = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
                    answer = res.decode("utf-8")

                    self.parser.recursion_protection = 0
                    translation = self.parser.parse_answer(answer, spacy_pos=token.pos_, origin_word=token.lemma_,
                                                           original_phrase=final_text, word_index=token.i,
                                                           word_pos=token.idx)
                    translation = self.parser.resolve_linkanswer(translation, token.pos_)
                    translation = self.parser.remove_after_comma(translation)
                    translation = self.parser.remove_obsolete_characters(translation)

                except Exception as e:
                    return_code = -1  # e.returncode
                    pass
                finally:
                    if translation == "" or return_code != 0:
                        continue
                    else:
                        words_translations[keys[i]].append(translation)
                        positions_of_translated_words[keys[i]].append(token.idx - total_shift)

            else:
                continue

        return [words_translations, positions_of_translated_words]

    def translate2(self, phrase, prev_phrase):
        # doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

        striped = prev_phrase.strip()
        last_char = striped[-1:]
        prev_phrase_shift = 0
        prev_phrase_l = None
        if last_char == ".":
            #words = re.split(" |'", prev_phrase.strip())
            #l = len(words)
            final_phrase = phrase
        else:
            prev_phrase_l = len(prev_phrase)
            final_phrase = prev_phrase + phrase

        doc = self.nlp(final_phrase)

        words_translations2 = {}
        words_translations1 = {}

        positions_of_translated_words2 = {}
        positions_of_translated_words1 = {}

        #test2 = []
        #test1 = []

        pos1 = []
        pos2 = []
        second_part_begins = False
        for token in doc:
            translation = ""
            if prev_phrase_l is not None and token.idx == prev_phrase_l:
                second_part_begins = True
                prev_phrase_shift = prev_phrase_l

            elif token.pos_ == "PUNCT" and token.text == ".":
                # . in the middle of prev phrase
                #second_part_begins = True
                #prev_phrase_shift = prev_phrase_l - token.idx
                continue

            if token.lemma_ == "-PRON-":

                if second_part_begins == False:
                    pos1.append(-1)
                else:
                    pos2.append(-1)
                continue

            elif token.pos_ in self.parser.poses and token.lemma_ not in self.stop_words:
                if second_part_begins == False:
                    pos1.append(token.pos_)
                else:
                    pos2.append(token.pos_)

                cmd = "java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m " + token.lemma_
                return_code = 0
                try:
                    res = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
                    answer = res.decode("utf-8")

                    self.parser.recursion_protection = 0
                    translation = self.parser.parse_answer(answer, spacy_pos=token.pos_, origin_word=token.lemma_, original_phrase=final_phrase, word_index=token.i, word_pos=token.idx)
                    translation = self.parser.resolve_linkanswer(translation, token.pos_)
                    translation = self.parser.remove_after_comma(translation)
                    translation = self.parser.remove_obsolete_characters(translation)

                except Exception as e:
                    return_code = -1  # e.returncode
                    pass
                finally:
                    if translation == "" or return_code != 0:
                        #translation_res += ""#"/"+token.text+"/ "
                        continue
                    else:
                        #translation_res += "<span>" + translation + "</span>"
                        if second_part_begins == False:
                            words_translations1[len(pos1)-1] = translation
                            positions_of_translated_words1[len(pos1)-1] = token.idx# total position in phrase

                        else:
                            words_translations2[len(pos2) - 1] = translation
                            positions_of_translated_words2[len(pos2) - 1] = token.idx-prev_phrase_shift# total position in phrase


            else:
                #translation_res += ""#token.text +
                if second_part_begins == False:
                    pos1.append(-1)
                else:
                    pos2.append(-1)
                continue


        #self.phrases_dispatcher.add_phrase([words_translations2, positions_of_translated_words2, pos2])
        #send indexes what translations to take from right side + send new translations for right side of phrase + positions for the whole phrase
        # word word word word
        # pos  pos  pos  pos
        # spos spos spos spos
        #

        return [words_translations2, positions_of_translated_words2, pos2, words_translations1, positions_of_translated_words1, pos1]
