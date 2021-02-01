import math

class Phrases_dispatcher:

    def __init__(self):
        self.last_phrases_list = {}
        #self.shift = 0

    def delete_phrases_list(self):
        del self.last_phrases_list
        self.last_phrases_list = {}
        #self.shift = 0

    def add_phrase(self, phrase, index, replic_index):
        self.last_phrases_list[str(replic_index)+"_"+str(index)] = phrase

        if len(self.last_phrases_list) > 20:
            keys = list(self.last_phrases_list.keys())
            for i in range(0, 10):
                self.last_phrases_list.pop(keys[i])


    def get_prev_phrase(self, index, replic_index):
        #[words_translations2, positions_of_translated_words2, pos2]
        key = str(replic_index)+"_"+str(index)
        if key in self.last_phrases_list:
            return self.last_phrases_list[key]
        else:
            return False

    def compare_current_prev_with_previous_word2(self, current_phrase2_index, current_phrase1, replic_index):
        phrase1_translations = []
        phrase1_positions = []

        prev_phrase2 = self.get_prev_phrase(current_phrase2_index-1, replic_index)
        if not prev_phrase2:
            return [phrase1_translations, phrase1_positions]

        prev_phrase2_translations = prev_phrase2[0]
        prev_phrase2_positions_of_translated_words = prev_phrase2[1]
        prev_phrase2_pos = prev_phrase2[2]

        current_phrase1_translations = current_phrase1[0]
        current_phrase1_positions_of_translated_words = current_phrase1[1]
        current_phrase1_pos = current_phrase1[2]

        if len(current_phrase1_pos) == len(prev_phrase2_pos):

            start_righ_part_index = math.ceil(len(current_phrase1_pos) / 2)

            # get all prev_word2_translations witch key < start_righ_part_index
            # get all  prev_word2_positions_of_translated_words witch key < start_righ_part_index

            for k, translation in prev_phrase2_translations.items():
                if k < start_righ_part_index:
                    phrase1_translations.append(translation)
                    phrase1_positions.append(prev_phrase2_positions_of_translated_words[k])

            for j in range(start_righ_part_index, len(current_phrase1_pos)):
                if current_phrase1_pos[j]!=-1 and prev_phrase2_pos[j] != -1 and current_phrase1_pos[j] != prev_phrase2_pos[j]:#TYPE 1 - POS SUBSTITUTE
                    if j in current_phrase1_translations:
                        phrase1_translations.append(current_phrase1_translations[j])
                    if j in current_phrase1_positions_of_translated_words:
                        phrase1_positions.append(current_phrase1_positions_of_translated_words[j])

                #elif current_phrase1_pos[j]==-1 and prev_phrase2_pos[j] != -1:#TYPE 2 DELETION
                    #continue
                elif current_phrase1_pos[j] != -1 and prev_phrase2_pos[j] == -1:#TYPE 3 INSERTION
                    if j in current_phrase1_translations:
                        phrase1_translations.append(current_phrase1_translations[j])
                    if j in current_phrase1_positions_of_translated_words:
                        phrase1_positions.append(current_phrase1_positions_of_translated_words[j])

                elif current_phrase1_pos[j] == prev_phrase2_pos[j] and current_phrase1_pos[j] != -1:
                    if j in current_phrase1_translations:
                        phrase1_translations.append(current_phrase1_translations[j])
                    if j in current_phrase1_positions_of_translated_words:
                        phrase1_positions.append(current_phrase1_positions_of_translated_words[j])

        return [phrase1_translations, phrase1_positions]

