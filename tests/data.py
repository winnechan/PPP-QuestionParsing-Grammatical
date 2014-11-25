from ppp_questionparsing_grammatical import Triple, TriplesBucket, computeTree, simplify, buildBucket, DependenciesTree, tripleProduce1, tripleProduce2, tripleProduce3, tripleProduce4

# Parsing result of "John Smith lives in the United Kingdom."
def give_john_smith():
    return  {'sentences': [{'dependencies': [['root', 'ROOT', 'lives'],
                ['nn', 'Smith', 'John'],
                ['nsubj', 'lives', 'Smith'],
                ['det', 'Kingdom', 'the'],
                ['nn', 'Kingdom', 'United'],
                ['prep_in', 'lives', 'Kingdom']],
               'indexeddependencies': [['root', 'ROOT-0', 'lives-3'],
                ['nn', 'Smith-2', 'John-1'],
                ['nsubj', 'lives-3', 'Smith-2'],
                ['det', 'Kingdom-7', 'the-5'],
                ['nn', 'Kingdom-7', 'United-6'],
                ['prep_in', 'lives-3', 'Kingdom-7']],
               'parsetree': '(ROOT (S (NP (NNP John) (NNP Smith)) (VP (VBZ lives) (PP (IN in) (NP (DT the) (NNP United) (NNP Kingdom)))) (. .)))',
               'text': 'John Smith lives in the United Kingdom.',
               'words': [['John',
                 {'CharacterOffsetBegin': '0',
                  'CharacterOffsetEnd': '4',
                  'Lemma': 'John',
                  'NamedEntityTag': 'PERSON',
                  'PartOfSpeech': 'NNP'}],
                ['Smith',
                 {'CharacterOffsetBegin': '5',
                  'CharacterOffsetEnd': '10',
                  'Lemma': 'Smith',
                  'NamedEntityTag': 'PERSON',
                  'PartOfSpeech': 'NNP'}],
                ['lives',
                 {'CharacterOffsetBegin': '11',
                  'CharacterOffsetEnd': '16',
                  'Lemma': 'live',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'VBZ'}],
                ['in',
                 {'CharacterOffsetBegin': '17',
                  'CharacterOffsetEnd': '19',
                  'Lemma': 'in',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'IN'}],
                ['the',
                 {'CharacterOffsetBegin': '20',
                  'CharacterOffsetEnd': '23',
                  'Lemma': 'the',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'DT'}],
                ['United',
                 {'CharacterOffsetBegin': '24',
                  'CharacterOffsetEnd': '30',
                  'Lemma': 'United',
                  'NamedEntityTag': 'LOCATION',
                  'PartOfSpeech': 'NNP'}],
                ['Kingdom',
                 {'CharacterOffsetBegin': '31',
                  'CharacterOffsetEnd': '38',
                  'Lemma': 'Kingdom',
                  'NamedEntityTag': 'LOCATION',
                  'PartOfSpeech': 'NNP'}],
                ['.',
                 {'CharacterOffsetBegin': '38',
                  'CharacterOffsetEnd': '39',
                  'Lemma': '.',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': '.'}]]}]}

# Dot representation of the tree for "John Smith lives in the United Kingdom."
def give_john_smith_string():
    s="digraph relations {\n"
    s+="\t\"ROOT5\"[label=\"ROOT\",shape=box];\n"
    s+="\t\"ROOT5\" -> \"residence4\"[label=\"root\"];\n"
    s+="\t\"residence4\"[label=\"residence\",shape=box];\n"
    s+="\t\"residence4\" -> \"John0\"[label=\"nsubj\"];\n"
    s+="\t\"residence4\" -> \"United3\"[label=\"prep_in\"];\n"
    s+="\t\"John0\"[label=\"John Smith [PERSON]\",shape=box];\n"
    s+="\t\"United3\"[label=\"United Kingdom [LOCATION]\",shape=box];\n"
    s+="\t\"United3\" -> \"the1\"[label=\"det\"];\n"
    s+="\t\"the1\"[label=\"the\",shape=box];\n"
    s+="\tlabelloc=\"t\"\tlabel=\"John Smith lives in the United Kingdom.\";\n"
    s+="}"
    return s

# Parse result of "Who wrote \"Lucy in the Sky with Diamonds\" and \"Let It Be\"?"
def give_LSD_LIB():
    return  {'coref': [[[['It', 0, 13, 13, 14], ['the Sky with Diamonds', 0, 6, 5, 9]]]],
             'sentences': [{'dependencies': [['root', 'ROOT', 'wrote'],
                ['nsubj', 'wrote', 'Who'],
                ['dobj', 'wrote', 'Lucy'],
                ['det', 'Sky', 'the'],
                ['prep_in', 'Lucy', 'Sky'],
                ['prep_with', 'Sky', 'Diamonds'],
                ['conj_and', 'wrote', 'Let'],
                ['nsubj', 'Be', 'It'],
                ['ccomp', 'Let', 'Be']],
               'indexeddependencies': [['root', 'ROOT-0', 'wrote-2'],
                ['nsubj', 'wrote-2', 'Who-1'],
                ['dobj', 'wrote-2', 'Lucy-4'],
                ['det', 'Sky-7', 'the-6'],
                ['prep_in', 'Lucy-4', 'Sky-7'],
                ['prep_with', 'Sky-7', 'Diamonds-9'],
                ['conj_and', 'wrote-2', 'Let-13'],
                ['nsubj', 'Be-15', 'It-14'],
                ['ccomp', 'Let-13', 'Be-15']],
               'parsetree': "(ROOT (SBARQ (SBARQ (WHNP (WP Who)) (SQ (VP (VBD wrote) (`` ``) (NP (NP (NNP Lucy)) (PP (IN in) (NP (NP (DT the) (NN Sky)) (PP (IN with) (NP (NNP Diamonds)))))) ('' '')))) (CC and) (S (VP (`` ``) (VB Let) (S (NP (PRP It)) (VP (VB Be) ('' ''))))) (. ?)))",
               'text': 'Who wrote "Lucy in the Sky with Diamonds" and "Let It Be"?',
               'words': [['Who',
                 {'CharacterOffsetBegin': '0',
                  'CharacterOffsetEnd': '3',
                  'Lemma': 'who',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'WP'}],
                ['wrote',
                 {'CharacterOffsetBegin': '4',
                  'CharacterOffsetEnd': '9',
                  'Lemma': 'write',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'VBD'}],
                ['``',
                 {'CharacterOffsetBegin': '10',
                  'CharacterOffsetEnd': '11',
                  'Lemma': '``',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': '``'}],
                ['Lucy',
                 {'CharacterOffsetBegin': '11',
                  'CharacterOffsetEnd': '15',
                  'Lemma': 'Lucy',
                  'NamedEntityTag': 'PERSON',
                  'PartOfSpeech': 'NNP'}],
                ['in',
                 {'CharacterOffsetBegin': '16',
                  'CharacterOffsetEnd': '18',
                  'Lemma': 'in',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'IN'}],
                ['the',
                 {'CharacterOffsetBegin': '19',
                  'CharacterOffsetEnd': '22',
                  'Lemma': 'the',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'DT'}],
                ['Sky',
                 {'CharacterOffsetBegin': '23',
                  'CharacterOffsetEnd': '26',
                  'Lemma': 'sky',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'NN'}],
                ['with',
                 {'CharacterOffsetBegin': '27',
                  'CharacterOffsetEnd': '31',
                  'Lemma': 'with',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'IN'}],
                ['Diamonds',
                 {'CharacterOffsetBegin': '32',
                  'CharacterOffsetEnd': '39',
                  'Lemma': 'Diamonds',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'NNP'}],
                ["''",
                 {'CharacterOffsetBegin': '39',
                  'CharacterOffsetEnd': '40',
                  'Lemma': "''",
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': "''"}],
                ['and',
                 {'CharacterOffsetBegin': '41',
                  'CharacterOffsetEnd': '44',
                  'Lemma': 'and',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'CC'}],
                ['``',
                 {'CharacterOffsetBegin': '45',
                  'CharacterOffsetEnd': '46',
                  'Lemma': '``',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': '``'}],
                ['Let',
                 {'CharacterOffsetBegin': '46',
                  'CharacterOffsetEnd': '49',
                  'Lemma': 'let',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'VB'}],
                ['It',
                 {'CharacterOffsetBegin': '50',
                  'CharacterOffsetEnd': '52',
                  'Lemma': 'it',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'PRP'}],
                ['Be',
                 {'CharacterOffsetBegin': '53',
                  'CharacterOffsetEnd': '55',
                  'Lemma': 'be',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'VB'}],
                ["''",
                 {'CharacterOffsetBegin': '55',
                  'CharacterOffsetEnd': '56',
                  'Lemma': "''",
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': "''"}],
                ['?',
                 {'CharacterOffsetBegin': '56',
                  'CharacterOffsetEnd': '57',
                  'Lemma': '?',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': '.'}]]}]}

# Parse result of "Obama is the United States president."
def give_obama_president_usa():
    return  {'coref': [[[['the United States president', 0, 5, 2, 6],
                ['Obama', 0, 0, 0, 1]]]],
             'sentences': [{'dependencies': [['root', 'ROOT', 'is'],
                ['nsubj', 'is', 'Obama'],
                ['det', 'president', 'the'],
                ['nn', 'president', 'United'],
                ['nn', 'president', 'States'],
                ['xcomp', 'is', 'president']],
               'indexeddependencies': [['root', 'ROOT-0', 'is-2'],
                ['nsubj', 'is-2', 'Obama-1'],
                ['det', 'president-6', 'the-3'],
                ['nn', 'president-6', 'United-4'],
                ['nn', 'president-6', 'States-5'],
                ['xcomp', 'is-2', 'president-6']],
               'parsetree': '(ROOT (S (NP (NNP Obama)) (VP (VBZ is) (NP (DT the) (NNP United) (NNPS States) (NN president))) (. .)))',
               'text': 'Obama is the United States president.',
               'words': [['Obama',
                 {'CharacterOffsetBegin': '0',
                  'CharacterOffsetEnd': '5',
                  'Lemma': 'Obama',
                  'NamedEntityTag': 'PERSON',
                  'PartOfSpeech': 'NNP'}],
                ['is',
                 {'CharacterOffsetBegin': '6',
                  'CharacterOffsetEnd': '8',
                  'Lemma': 'be',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'VBZ'}],
                ['the',
                 {'CharacterOffsetBegin': '9',
                  'CharacterOffsetEnd': '12',
                  'Lemma': 'the',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'DT'}],
                ['United',
                 {'CharacterOffsetBegin': '13',
                  'CharacterOffsetEnd': '19',
                  'Lemma': 'United',
                  'NamedEntityTag': 'LOCATION',
                  'PartOfSpeech': 'NNP'}],
                ['States',
                 {'CharacterOffsetBegin': '20',
                  'CharacterOffsetEnd': '26',
                  'Lemma': 'States',
                  'NamedEntityTag': 'LOCATION',
                  'PartOfSpeech': 'NNPS'}],
                ['president',
                 {'CharacterOffsetBegin': '27',
                  'CharacterOffsetEnd': '36',
                  'Lemma': 'president',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'NN'}],
                ['.',
                 {'CharacterOffsetBegin': '36',
                  'CharacterOffsetEnd': '37',
                  'Lemma': '.',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': '.'}]]}]}

# Parsing result of "How old are there?"
def give_how_old():
    return  {'sentences': [{'dependencies': [['root', 'ROOT', 'are'],
                ['advmod', 'old', 'How'],
                ['dep', 'are', 'old'],
                ['expl', 'are', 'there']],
               'indexeddependencies': [['root', 'ROOT-0', 'are-3'],
                ['advmod', 'old-2', 'How-1'],
                ['dep', 'are-3', 'old-2'],
                ['expl', 'are-3', 'there-4']],
               'parsetree': '(ROOT (SBARQ (WHADJP (WRB How) (JJ old)) (SQ (VBP are) (NP (EX there))) (. ?)))',
               'text': 'How old are there?',
               'words': [['How',
                 {'CharacterOffsetBegin': '0',
                  'CharacterOffsetEnd': '3',
                  'Lemma': 'how',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'WRB'}],
                ['old',
                 {'CharacterOffsetBegin': '4',
                  'CharacterOffsetEnd': '7',
                  'Lemma': 'old',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'JJ'}],
                ['are',
                 {'CharacterOffsetBegin': '8',
                  'CharacterOffsetEnd': '11',
                  'Lemma': 'be',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'VBP'}],
                ['there',
                 {'CharacterOffsetBegin': '12',
                  'CharacterOffsetEnd': '17',
                  'Lemma': 'there',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'EX'}],
                ['?',
                 {'CharacterOffsetBegin': '17',
                  'CharacterOffsetEnd': '18',
                  'Lemma': '?',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': '.'}]]}]}

# Parsing result of "Who is the United States president?"
def give_USA_president():
    return  {'sentences': [{'dependencies': [['root', 'ROOT', 'is'],
                ['dep', 'is', 'Who'],
                ['det', 'president', 'the'],
                ['nn', 'president', 'United'],
                ['nn', 'president', 'States'],
                ['nsubj', 'is', 'president']],
               'indexeddependencies': [['root', 'ROOT-0', 'is-2'],
                ['dep', 'is-2', 'Who-1'],
                ['det', 'president-6', 'the-3'],
                ['nn', 'president-6', 'United-4'],
                ['nn', 'president-6', 'States-5'],
                ['nsubj', 'is-2', 'president-6']],
               'parsetree': '(ROOT (SBARQ (WHNP (WP Who)) (SQ (VBZ is) (NP (DT the) (NNP United) (NNPS States) (NN president))) (. ?)))',
               'text': 'Who is the United States president?',
               'words': [['Who',
                 {'CharacterOffsetBegin': '0',
                  'CharacterOffsetEnd': '3',
                  'Lemma': 'who',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'WP'}],
                ['is',
                 {'CharacterOffsetBegin': '4',
                  'CharacterOffsetEnd': '6',
                  'Lemma': 'be',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'VBZ'}],
                ['the',
                 {'CharacterOffsetBegin': '7',
                  'CharacterOffsetEnd': '10',
                  'Lemma': 'the',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'DT'}],
                ['United',
                 {'CharacterOffsetBegin': '11',
                  'CharacterOffsetEnd': '17',
                  'Lemma': 'United',
                  'NamedEntityTag': 'LOCATION',
                  'PartOfSpeech': 'NNP'}],
                ['States',
                 {'CharacterOffsetBegin': '18',
                  'CharacterOffsetEnd': '24',
                  'Lemma': 'States',
                  'NamedEntityTag': 'LOCATION',
                  'PartOfSpeech': 'NNPS'}],
                ['president',
                 {'CharacterOffsetBegin': '25',
                  'CharacterOffsetEnd': '34',
                  'Lemma': 'president',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': 'NN'}],
                ['?',
                 {'CharacterOffsetBegin': '34',
                  'CharacterOffsetEnd': '35',
                  'Lemma': '?',
                  'NamedEntityTag': 'O',
                  'PartOfSpeech': '.'}]]}]}

# Parsing result of "Who is the president of the United States?"
def give_president_of_USA():
    return  {'sentences': [{
  'words': [
    ['Who', 
      {'CharacterOffsetBegin': '0', 
       'PartOfSpeech': 'WP', 
       'Lemma': 'who', 
       'NamedEntityTag': 'O', 
       'CharacterOffsetEnd': '3'}], 
    ['is', 
      {'CharacterOffsetBegin': '4', 
       'PartOfSpeech': 'VBZ', 
       'Lemma': 'be', 
       'NamedEntityTag': 'O', 
       'CharacterOffsetEnd': '6'}], 
    ['the', 
      {'CharacterOffsetBegin': '7', 
       'PartOfSpeech': 'DT', 
       'Lemma': 'the', 
       'NamedEntityTag': 'O', 
       'CharacterOffsetEnd': '10'}], 
    ['president', 
      {'CharacterOffsetBegin': '11', 
       'PartOfSpeech': 'NN', 
       'Lemma': 'president', 
       'NamedEntityTag': 'O', 
       'CharacterOffsetEnd': '20'}], 
    ['of', 
      {'CharacterOffsetBegin': '21', 
       'PartOfSpeech': 'IN', 
       'Lemma': 'of', 
       'NamedEntityTag': 'O', 
       'CharacterOffsetEnd': '23'}], 
    ['the', 
      {'CharacterOffsetBegin': '24', 
       'PartOfSpeech': 'DT', 'Lemma': 
       'the', 'NamedEntityTag': 'O', 
       'CharacterOffsetEnd': '27'}], 
    ['United', 
      {'CharacterOffsetBegin': '28', 
       'PartOfSpeech': 'NNP', 
       'Lemma': 'United', 
       'NamedEntityTag': 'LOCATION', 
       'CharacterOffsetEnd': '34'}], 
    ['States', 
      {'CharacterOffsetBegin': '35', 
       'PartOfSpeech': 'NNPS', 
       'Lemma': 'States', 
       'NamedEntityTag': 'LOCATION', 
       'CharacterOffsetEnd': '41'}], 
    ['?', 
      {'CharacterOffsetBegin': '41', 
       'PartOfSpeech': '.', 
       'Lemma': '?', 
       'NamedEntityTag': 'O', 
       'CharacterOffsetEnd': '42'}]], 
  'text': 'Who is the president of the United States?', 
  'dependencies': [['root', 'ROOT', 'is'], ['dep', 'is', 'Who'], ['det', 'president', 'the'], ['nsubj', 'is', 'president'], ['det', 'States', 'the'], ['nn', 'States', 'United'], ['prep_of', 'president', 'States']], 
  'indexeddependencies': [['root', 'ROOT-0', 'is-2'], ['dep', 'is-2', 'Who-1'], ['det', 'president-4', 'the-3'], ['nsubj', 'is-2', 'president-4'], ['det', 'States-8', 'the-6'], ['nn', 'States-8', 'United-7'], ['prep_of', 'president-4', 'States-8']], 
  'parsetree': '(ROOT (SBARQ (WHNP (WP Who)) (SQ (VBZ is) (NP (NP (DT the) (NN president)) (PP (IN of) (NP (DT the) (NNP United) (NNPS States))))) (. ?)))'}]}

# Parsing result of "What was the first Gilbert and Sullivan opera?"
def give_opera():
    return  {'sentences': [{
  'words': [
    ['What', 
        {'PartOfSpeech': 'WP', 
         'NamedEntityTag': 'O', 
         'CharacterOffsetBegin': '0', 
         'Lemma': 'what', 
         'CharacterOffsetEnd': '4'}], 
    ['was', 
        {'PartOfSpeech': 'VBD', 
         'NamedEntityTag': 'O', 
         'CharacterOffsetBegin': '5', 
         'Lemma': 'be', 
         'CharacterOffsetEnd': '8'}], 
    ['the', 
        {'PartOfSpeech': 'DT', 
         'NamedEntityTag': 'O', 
         'CharacterOffsetBegin': '9', 
         'Lemma': 'the', 
         'CharacterOffsetEnd': '12'}], 
    ['first', 
        {'NamedEntityTag': 'ORDINAL', 
         'NormalizedNamedEntityTag': '1.0', 
         'CharacterOffsetEnd': '18', 
         'Lemma': 'first', 
         'CharacterOffsetBegin': '13', 
         'PartOfSpeech': 'JJ'}], 
    ['Gilbert', 
        {'PartOfSpeech': 'NNP', 
         'NamedEntityTag': 'PERSON', 
         'CharacterOffsetBegin': '19', 
         'Lemma': 'Gilbert', 
         'CharacterOffsetEnd': '26'}], 
    ['and', 
        {'PartOfSpeech': 'CC', 
         'NamedEntityTag': 'O', 
         'CharacterOffsetBegin': '27', 
         'Lemma': 'and', 
         'CharacterOffsetEnd': '30'}], 
    ['Sullivan', 
        {'PartOfSpeech': 'NNP', 
         'NamedEntityTag': 'PERSON', 
         'CharacterOffsetBegin': '31', 
         'Lemma': 'Sullivan', 
         'CharacterOffsetEnd': '39'}], 
    ['opera', 
        {'PartOfSpeech': 'NN', 
         'NamedEntityTag': 'O', 
         'CharacterOffsetBegin': '40', 
         'Lemma': 'opera', 
         'CharacterOffsetEnd': '45'}], 
    ['?', 
        {'PartOfSpeech': '.', 
         'NamedEntityTag': 'O', 
         'CharacterOffsetBegin': '45', 
         'Lemma': '?', 
         'CharacterOffsetEnd': '46'}]], 
  'text': 'What was the first Gilbert and Sullivan opera?', 
  'dependencies': [['root', 'ROOT', 'was'], ['dep', 'was', 'What'], ['det', 'Gilbert', 'the'], ['amod', 'Gilbert', 'first'], ['nsubj', 'was', 'Gilbert'], ['nn', 'opera', 'Sullivan'], ['conj_and', 'Gilbert', 'opera']],   
  'indexeddependencies': [['root', 'ROOT-0', 'was-2'], ['dep', 'was-2', 'What-1'], ['det', 'Gilbert-5', 'the-3'], ['amod', 'Gilbert-5', 'first-4'], ['nsubj', 'was-2', 'Gilbert-5'], ['nn', 'opera-8', 'Sullivan-7'], ['conj_and', 'Gilbert-5', 'opera-8']], 
  'parsetree': '(ROOT (SBARQ (WHNP (WP What)) (SQ (VBD was) (NP (DT the) (JJ first) (NNP Gilbert) (CC and) (NNP Sullivan) (NN opera))) (. ?)))'}]}

# Parsing result of "Who is the chief and prime minister?"
def give_chief():
    return  {'sentences': [{

  'words': [
    ['Who', 
        {'PartOfSpeech': 'WP', 
         'CharacterOffsetBegin': '0', 
         'CharacterOffsetEnd': '3', 
         'NamedEntityTag': 'O', 
         'Lemma': 'who'}], 
    ['is', 
        {'PartOfSpeech': 'VBZ', 
         'CharacterOffsetBegin': '4', 
         'CharacterOffsetEnd': '6', 
         'NamedEntityTag': 'O', 
         'Lemma': 'be'}], 
    ['the', 
        {'PartOfSpeech': 'DT', 
         'CharacterOffsetBegin': '7', 
         'CharacterOffsetEnd': '10', 
         'NamedEntityTag': 'O', 
         'Lemma': 'the'}], 
    ['chief', 
        {'PartOfSpeech': 'NN', 
         'CharacterOffsetBegin': '11', 
         'CharacterOffsetEnd': '16', 
         'NamedEntityTag': 'O', 
         'Lemma': 'chief'}], 
    ['and', 
        {'PartOfSpeech': 'CC', 
         'CharacterOffsetBegin': '17', 
         'CharacterOffsetEnd': '20', 
         'NamedEntityTag': 'O', 
         'Lemma': 'and'}], 
    ['prime', 
        {'PartOfSpeech': 'JJ', 
         'CharacterOffsetBegin': '21', 
         'CharacterOffsetEnd': '26', 
         'NamedEntityTag': 'O', 
         'Lemma': 'prime'}], 
    ['minister', 
        {'PartOfSpeech': 'NN', 
         'CharacterOffsetBegin': '27', 
         'CharacterOffsetEnd': '35', 
         'NamedEntityTag': 'O', 
         'Lemma': 'minister'}], 
    ['?', 
        {'PartOfSpeech': '.', 
         'CharacterOffsetBegin': '35', 
         'CharacterOffsetEnd': '36', 
         'NamedEntityTag': 'O', 
         'Lemma': '?'}]], 
   'parsetree': '(ROOT (SBARQ (WHNP (WP Who)) (SQ (VBZ is) (NP (NP (DT the) (NN chief)) (CC and) (NP (JJ prime) (NN minister)))) (. ?)))', 
  'dependencies': [['root', 'ROOT', 'is'], ['dep', 'is', 'Who'], ['det', 'chief', 'the'], ['nsubj', 'is', 'chief'], ['amod', 'minister', 'prime'], ['conj_and', 'chief', 'minister']], 
  'indexeddependencies': [['root', 'ROOT-0', 'is-2'], ['dep', 'is-2', 'Who-1'], ['det', 'chief-4', 'the-3'], ['nsubj', 'is-2', 'chief-4'], ['amod', 'minister-7', 'prime-6'], ['conj_and', 'chief-4', 'minister-7']], 
  'text': 'Who is the chief and prime minister?'}]}


def tripleProductionData():
    '''
        Return data corresponding to a tree (root-0)--dep-->(child-1)
    '''
    root = DependenciesTree("root-0")
    child = DependenciesTree("child-1",dependency="dep",parent=root)
    root.child = [child]
    nodeToID = {root:0, child:1}
    bt = TriplesBucket()
    return (root,nodeToID,bt)
