from flair.data import Sentence
from flair.tagging_model import SequenceTaggerLSTM

tagger: SequenceTaggerLSTM = SequenceTaggerLSTM.load('ner')

sentence: Sentence = Sentence('George Washington went to Washington .')
tagger.predict(sentence)

print('Analysing %s' % sentence)
print('\n# The following NER tags are found: \n')
print(sentence.to_tag_string())