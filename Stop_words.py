#import spacy

class Stop_words():

    stop_words = {
        'much': None,
        'more': None,
        'over': None,
        'under': None,
        'can': None,
        'above': None,
        'may': None,
        'skill': None,
        'particularly': None,
        'there': None,
        'variant': None,
        'doctor': None,
        'disease': None,
        'patient': None,
        'medicine': None,
        'genomic': None,
        'test': None,
        'colleague': None,
        'think': None,
        'see': None,
        'down': None,
        'up': None,
        'left': None,
        'right': None,
        'equal': None,
        'less': None,
        'many': None,
        'lot': None,
        'like': None,
        'clinical': None,
        'role': None,
        'add': None,
        'calculate': None,
        'delete': None,
        'divide': None,
        'so': None,
        'then': None,
        'than': None,
        'default': None,
        'polygenic': None,
        'mutation': None,
        'polymorphism': None,
        'clinicians': None,
        'counsellor': None,
        'condition': None,
        'which': None,
        'when': None,
        'what': None,
        'where': None,
        'why': None,
        'who': None,
        'bear': None,
        'care': None,
        'baby': None,
        'family': None,
        'information': None,
        'translation': None,
        'translate': None,
        'share': None,
        'absolutely': None,
        'enhance': None,
        'change': None,
        'common': None,
        'antibiotic': None,
        'protein': None,
        'aminoacid': None,
        'amino': None,
        'acid': None,
        'nucleotide': None,
        'sequence': None,
        'find': None,
        'replace': None,
        'move': None,
        'year': None,
        'day': None,
        'month': None,
        'neurological': None,
        'oncology': None,
        'cancer': None,
        'tumor': None,
        'tissue': None,
        'vessel': None,
        'problem': None,
        'issue': None,
        'pretty': None,
        'amazing': None,
        'quite': None,
        'just': None,
        'interesting': None,
        'important': None,
        'significant': None,
        'different': None,
        'only': None,
        'current': None,
        'contract': None,
        'develop': None,
        'separate': None,
        'exciting': None,
        'lead': None,
        'real': None,
        'practice': None,
        'relevant': None,
        'machine': None,
        'instrument': None,
        'people': None,
        'company': None,
        'laboratory': None,
        'scientist': None,
        'deliver': None,
        'benefit': None,
        'effort': None,
        'speak': None,
        'feel': None,
        'some': None,
        'something': None,
        'somebody': None,
        'nobody': None,
        'nothing': None,
        'go': None,
        'work': None,
        'help': None,
        'interpret': None,
        'understand': None,
        'complex': None,
        'result': None,
        'happen': None,
        'next': None,
        'few': None,
        'single': None,
        'maybe': None,
        'combination': None,
        'multiple': None,
        'already': None,
        'score': None,
        'useful': None,
        'increase': None,
        'decrease': None,
        'certain': None,
        'very': None,
        'high': None,
        'comparable': None,
        'apply': None,
        'group': None,
        'need': None,
        'necessary': None,
        'success': None,
        'individual': None,
        'member': None,
        'opportunity': None,
        'involve': None,
        'type': None,
        'available': None,
        'avoid': None,
        'example': None,
        'therapy': None,
        'inherit': None,
        'good': None,
        'bad': None,
        'mitochondria': None,
        'arrive': None,
        'usually': None,
        'local': None,
        'point': None,
        'allow': None,
        'simple': None,
        'determine': None,
        'definition': None,
        'research': None,
        'education': None,
        'university': None,
        'institution': None,
        'academic': None,
        'completely': None,
        'number': None,
        'resume': None,
        'recap': None,
        'conclusion': None,
        'perfect': None,
        'consequence': None,
        'final': None,
        'start': None,
        'stop': None,
        'step': None,
        'extension': None,
        'forward': None,
        'backward': None,
        'belong': None,
        'demo': None,
        'population': None,
        'sample': None,
        'blood': None,
        'require': None,
        'investor': None,
        'invest': None,
        'period': None,
        'time': None,
        'team': None,
        'name': None,
        'value': None,
        'message': None,
        'email': None,
        'chat': None,
        'call': None,
        'voice': None,
        'morning': None,
        'afternoon': None,
        'evening': None,
        'couple': None,
        'far': None,
        'as': None,
        'paper': None,
        'article': None,
        'would': None,
        'should': None,
        'base': None,
        'away': None,
        'remain': None,
        'comprehensive': None,
        'sophisticated': None,
        'difficult': None,
        'ago': None,
        'adult': None,
        'hour': None,
        'able': None,
        'okay': None,
        'hello': None,
        'thank': None,
        'goodbye': None,
        'thanks': None,
        'alright': None,
        'do': None,
        'person': None,
        'due': None,
        'technology': None,
        'strike': None,
        'come': None,
        'until': None,
        'development': None,
        'explain': None,
        'use': None,
        'profound': None,
        'risk': None,
        'reduce': None,
        #-------
        'geneticist': None,
        'professor': None,
        'translational': None,
        'nearly': None,
        'really': None,
        'genetic': None,
        'testing': None,
        'small': None,
        'big': None,
        'last': None,
        'new': None,
        'challenge': None,
        'enough': None,
        'counselor': None,
        'thing': None,
        'ways': None,
        'way': None,
        'have': None,
        'closely': None,
        'close': None,
        'other': None,
        'never': None,
        'novel': None,
        'now': None,
        'gene': None,
        'increasingly': None,
        'how': None,
        'particular': None,
        'mean': None,
        'average': None,
        'give': None,
        'loss': None,
        'unit': None,
        'first': None,
        'second': None,
        'millisecond': None,
        'take': None,
        'minute': None,
        'rapidly': None,
        'rapid': None,
        'finding': None,
        'quickly': None,
        'possible': None,
        'range': None,
        'whole': None,
        'wonderful': None,
        'open': None,
        'exit': None,
        'exist': None,
        'ever': None,


    }

"""
def main():
    result = {}
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("okay")
    lemma = doc[0].lemma_

    exit(0)
    for k, v in Stop_words.stop_words.items():
        doc = nlp(k)
        lemma = doc[0].lemma_
        result[lemma] = None
    a = 1
if __name__ == '__main__':
    main()
"""




