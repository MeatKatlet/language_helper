cd /media/kirill/System/dictserver

java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.server.JDictd /media/kirill/System/dictserver/Mueller/mueller.ini

client call
java -cp jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m relative
java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m relative


activate_this = "/media/kirill/System/Users/Kirill/PycharmProjects/dictionary_parser/venv/bin/activate_this.py"
with open(activate_this) as f:
        code = compile(f.read(), activate_this, 'exec')
        exec(code, dict(__file__=activate_this))

java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.server.JDictd Mueller/mueller.ini

TODO
--------------------------------------------------------
integrate medical vocabulary
genomic - no in dictionary
--------------------------------------------------
extract everything until comma? and more detailed translation will be on hover?
---------------------------------------------
doc = nlp("I") - I we they you ...
[[token.pos_,token.lemma_] for token in doc]
[['PRON', '-PRON-']]
---------------------------------------
**************************************** - solved
year
две транскрипции могут быть:! исправить в парсинге словаря!
[jə:], [jɪə] _n.
----------------------
########################## test created
**************************************** - solved
ERROR:
java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m that
151 "that" mueller_base "Mueller English-Russian Dictionary (base)": text follows
that

  1. _pron. (_pl. those)

    1) [ðæt] _demonstr. тот, та, то (иногда этот и пр.); а) указывает на
    лицо, понятие, событие, предмет, действие, отдалённые по месту или

translates as = [ðæt]
------------------------
########################## test created
**************************************** - solved
what to do with this?
java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m more
151 "more" mueller_base "Mueller English-Russian Dictionary (base)": text follows
more

  [mɔ:]

    1. _a.

      1) _comp. от much 1 и many 1
--------------------------
########################## test created
**************************************** - solved
java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m counselor
151 "counselor" mueller_base "Mueller English-Russian Dictionary (base)": text follows
counselor

  [ˈkaunslə] = counsellor

новый запрос на значение слова!
-----------------------------------------------
########################## test created
**************************************** - solved
diminishes = diminish - не перевел! не сделал запрос на перевод в словаре,  rapidly = rapid
java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m diminishe
152 16 matches found: list follows
mueller_base "dimensional"
mueller_base "dimensional"
mueller_base "dimerous"
mueller_base "dimeter"
mueller_base "dimethyl"
mueller_base "dimidiate"
mueller_base "diminish"
mueller_base "diminished"
mueller_base "diminuendo"
mueller_base "diminution"
mueller_base "diminutival"
mueller_base "diminutive"
mueller_base "dimity"
mueller_base "dimmer"
mueller_base "dimmish"
mueller_base "dimness"

transformative = transform
я думаю что это из за того что не поменялось POS для внутренниего подзапроса, ведь найденная подстрока может быть другого POS
 пример
 doc = nlp("completely transformative")
[[token.pos_,token.lemma_] for token in doc]
[['ADV', 'completely'], ['ADJ', 'transformative']]

java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m transformative
152 16 matches found: list follows
mueller_base "transferrer"
mueller_base "transfiguration"
mueller_base "transfigure"
mueller_base "transfix"
mueller_base "transform"
mueller_base "transformable"
mueller_base "transformation"
mueller_base "transformer"
mueller_base "transfuse"
mueller_base "transfusion"
mueller_base "transgress"
mueller_base "transgression"
mueller_base "transgressor"
mueller_base "tranship"
mueller_base "transience"
mueller_base "transiency"
.
250 Command complete
221 Closing connection
kirill@kirill-desktop:~$ java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m transform
151 "transform" mueller_base "Mueller English-Russian Dictionary (base)": text follows
transform

  [trænsˈfɔ:m] _v.

    1) превращать(ся)

    2) изменять(ся), преображать(ся), делать(ся) неузнаваемым; to
    transform smth. beyond recognition изменить что-л. до неузнаваемости

.
250 Command complete
221 Closing connection


--------------------------------------------------------------------------
########################## test created
ошибка - пишет NOUN а в словаре _v. что делать?
корректировать перевод получив контекстные слова рядом? потом? на основе связей между ними?
хранить предыдущие слова
слово1 слово2 слово3 ... текущее слово - из контекста всегда легче получать смысл! поэтому отправлять на перевод

не скажется ли это на производительности?
проверить
если скажется то попробуй найти способ of adding last word to already parsed previous result to save computation time
I need only POS of last word
in production words are changed quickly so maybe send by phrases?
или по 2 слова последних? только ? example - "to interpret"

doc = nlp("enhances")
[[token.pos_,token.lemma_] for token in doc]
[['NOUN', 'enhance']]
java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m enhance
151 "enhance" mueller_base "Mueller English-Russian Dictionary (base)": text follows
enhance

  [ɪnˈha:ns] _v.

    1) увеличивать, усиливать, усугублять

    2) повышать (цену)
-------------------------------------------
**************************************** - solved - test by passing phrases to spacy and not single words
вытащил "консервировать" вместо "мочь" хотя POS был правильный

java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m can
151 "can" mueller_base "Mueller English-Russian Dictionary (base)": text follows
can

  I [kæn] (полная форма); [kən], [kn] (редуцированные формы) _v. (could)
  модальный недостаточный глагол

    1) мочь, быть в состоянии, иметь возможность; уметь; I will do all I
    can я сделаю всё, что могу; I can speak French я говорю (умею
    говорить) по-французски; I cannot я не могу; I cannot away with this
    терпеть этого не могу; I cannot but я не могу не

    2) мочь, иметь право; you can go вы свободны, можете идти

    3) выражает сомнение, неуверенность, недоверие: it can't be true! не
    может быть!; can it be true? неужели?; she can't have done it! не
    может быть, чтобы она это сделала!

    *) what cannot be cured must be endured что нельзя исправить, то
    следует терпеть

  II [kæn]

    1. _n.

      1) бидон

      2) жестяная коробка или банка; garbage can а) помойное ведро; ящик
      для мусора; б) _жарг. лачуга в рабочем посёлке

      3) банка консервов

      4) _амер. стульчак, сиденье в уборной

      5) _амер. _жарг. тюрьма

      *) to be in the can быть законченным и готовым к употреблению

    2. _v.

      1) консервировать (мясо, овощи, фрукты)

      2) _амер. _жарг. отделаться (от кого-л.); уволить

      3) _амер. _жарг. посадить в тюрьму

      4) _амер. _жарг. остановить(ся)
-------------------------------------------------------
########################## test created
**************************************** - solved
не вытащил перевод хотя POS был правильный, вытащил [ju:s] вместо перевода
java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m use
151 "use" mueller_base "Mueller English-Russian Dictionary (base)": text follows
use

  1. _n. [ju:s]

    1) употребление; применение; in use в употреблении; in daily use в
    частом употреблении; в обиходе; to be (или to fall) out of use выйти
    из употребления; to put knowledge to use применять знания на практике

    2) (ис)пользование; способность или право пользования (чем-л.); to
    have the use of smth. пользоваться чем-л.; he put the use of his house
    at my disposal он предложил мне пользоваться своим домом; to lose the
    use of smth. потерять способность пользоваться чем-л.; he lost the use
    of his eyes он ослеп; to make use of, to put to use использовать,
    воспользоваться

    3) польза; толк; to be of (no) use быть (бес)полезным; is there any
    use? стоит ли?; what's the use of arguing? к чему спорить?; I have no
    use for it _разг. а) мне это совершенно не нужно; б) я этого не выношу

    4) обыкновение, привычка; use and wont обычная практика; long use has
    reconciled me to it я примирился с этим благодаря давнишней привычке

    5) цель, назначение; a tool with many uses инструмент, применяемый для
    различных целей

    6) ритуал церкви, епархии

    7) _юр. управление имуществом по доверенности; доход от управления
    имуществом по доверенности

  2. _v. [ju:z]

    1) употреблять, пользоваться, применять; to use one's brains (или
    one's wits) "шевелить мозгами"; may I use your name? могу я на вас
    сослаться?

    2) использовать, израсходовать; they use 10 tons of coal a month они
    расходуют 10 тонн угля в месяц
-----------------------------------------------------------------
########################## test created
**************************************** - solved
polygenic нет в словаре - подключи медицинскую модель
TODO - подключи медицинскую модель
--------------------------------------------------
increased = [ɪnˈkri:s] возрастать, увеличивать
delete all square breakets in translation result
---------------------------------------------------
########################## test created
**************************************** - solved
why it doesnt extract properly?
java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m genetics
151 "genetics" mueller_base "Mueller English-Russian Dictionary (base)": text follows
genetics

  [ʤɪˈnetɪks] _n. _pl. (употр. как _sing.) генетика
------------------------------------------------------
########################## test created
**************************************** - solved
over - слишком большой перевод!
-------------------------------------
########################## test created
**************************************** - solved ???
born [['VERB', 'bear']]
born = _бирж. играть на понижение

???????????????????
java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m bear
151 "bear" mueller_base "Mueller English-Russian Dictionary (base)": text follows
bear

  I [bɛə]

    1. _n.

      1) медведь

      2) грубый, невоспитанный человек; to play the bear вести себя грубо

      3) _бирж. спекулянт, играющий на понижение

      4) _астр. Great (Little, Lesser) Bear Большая (Малая) Медведица

      5) дыропробивной пресс, медведка

      6) _метал. козёл

      7) _мор. _разг. швабра (для мытья палубы)

      8) _attr.: bear pool _бирж. объединение спекулянтов, играющих на
      понижение; bear market _бирж. рынок с понижательной тенденцией

      *) cross (или sulky, surly) as a bear зол как чёрт; bridled bear
      юнец, путешествующий с гувернёром; to take a bear by the tooth без
      нужды подвергать себя опасности, лезть на рожон; to sell the bear's
      skin before one has caught the bear делить шкуру неубитого медведя;
      had it been a bear it would have bitten you вы ошиблись, обознались;
      (оказалось) не так страшно, как вы думали

    2. _v. _бирж. играть на понижение

  II [bɛə] _v. (bore; borne)

    1) носить; нести; переносить, перевозить

    2) выдерживать; нести груз, тяжесть; поддерживать, подпирать; will the
    ice bear today? достаточно ли крепок лёд сегодня?

    3) (_p-p. born) рождать, производить; to bear children рожать детей;
    to bear fruit приносить плоды; born in 1919 рождения 1919 года

    4) питать, иметь (чувство и т.п.)

    5) терпеть, выносить; I can't bear him я его не выношу

    6) _refl. держаться; вести себя

    7) опираться (on)

    8) простираться

    #) bear away а) выиграть (приз, кубок и т.п.); выйти победителем;
    б): to be borne away быть захваченным, увлечённым; bear down
    а) преодолевать; б) _мор. подходить по ветру; в) устремляться (upon -
    к); набрасываться, нападать (upon - на кого-л.); г) влиять; bear in:
    to be borne in on smb. становиться ясным, понятным кому-л.; bear off
    отклоняться; bear on касаться, иметь отношение к чему-л.; bear out
    подтверждать; подкреплять; поддерживать; bear up а) поддерживать;
    подбадривать; б) держаться стойко; в) _мор. спускаться (по ветру);
    г): to bear up for взять направление на; bear upon = bear on; bear
    with относиться терпеливо к чему-л.; мириться с чем-л.

    *) to bear arms а) носить оружие; служить в армии; to bear arms
    against smb. поднять оружие на кого-л., восстать против кого-л.;
    б) иметь или носить герб; to bear company а) составлять компанию,
    сопровождать; б) ухаживать; to bear comparison выдерживать сравнение;
    to bear a hand участвовать; помогать; to bear hard on smb. подавлять
    кого-л.; to bear in mind помнить; иметь в виду; to bear a part
    принимать участие; to bear a resemblance быть похожим, иметь сходство;
    to bear to the right etc. принять вправо и т.п.; to bear the signature
    иметь подпись, быть подписанным; to bear testimony, to bear witness
    свидетельствовать, показывать, давать показания

java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m born
151 "born" mueller_base "Mueller English-Russian Dictionary (base)": text follows
born

  [bɔ:n]

    1. _p-p. от bear II, 3

    2. _a. прирождённый; a poet born прирождённый поэт; in all one's born
    days за всю свою жизнь

?????????????????????????????????
------------------------------------------------------------------------------------------------------
?????????????? maybe this case will be resolved,  because now I am translating by phrases???????   test on video again
сделай правильный переход

java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m swap
151 "swap" mueller_base "Mueller English-Russian Dictionary (base)": text follows
swap

  [swɔp] = swop

------------------------------------------------------------------------------------------------------
########################## test created
**************************************** - solved
deprecate to translate too frequent words but use them in conjunction with other words to translate
exmp. - it
---------------------------------------------------------
???????????????????????????
не вытащил - ошибка! - надо не лемму совать а сырое слово

doc = nlp("it")
[[token.pos_,token.lemma_] for token in doc]
[['PRON', '-PRON-']]

java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m it
151 "it" mueller_base "Mueller English-Russian Dictionary (base)": text follows
it

  [ɪt]

    1. _pron.

      1) _pers. (_obj. без измен.) он, она, оно (о предметах и животных);
      here is your paper, read it вот ваша газета, читайте её

      2) _demonstr. это; who is it? кто это? кто там?; it's me, _уст. it
      is I это я

      3) _impers. it is raining идёт дождь; it is said говорят; it is
      known известно

      4) в качестве подлежащего заменяет какое-л. подразумеваемое понятие:
      it (= the season) is winter теперь зима; it (= the distance) is 6
      miles to Oxford до Оксфорда 6 миль; it (= the scenery) is very
      pleasant here здесь очень хорошо; it is in vain напрасно; it is easy
      to talk like that легко так говорить

      5) в качестве дополнения образует вместе с глаголами (как
      переходными, так и непереходными) разговорные идиомы; напр.: to face
      it out не дать себя запугать; to foot it а) идти пешком;
      б) танцевать; to lord it разыгрывать лорда, важничать; to cab it
      ездить, ехать в экипаже, в такси

    2. _n. _разг.

      1) идеал; последнее слово (чего-л.); верх совершенства; "изюминка";
      in her new dress she was it в своём новом платье она была верх
      совершенства; she has it в ней что-то есть, она привлекает внимание

      2) в детских играх тот, кто водит


------------------------------------------------------------------------------------------------
**************************************** - solved
doc = nlp("key")
[[token.pos_,token.lemma_] for token in doc]
[['ADJ', 'key']]

doc = nlp("the key")
[[token.pos_,token.lemma_] for token in doc]
[['DET', 'the'], ['NOUN', 'key']]

java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m key
151 "key" mueller_base "Mueller English-Russian Dictionary (base)": text follows
key

  I [ki:]

    1. _n.

      1) ключ; false key отмычка

-------------------------------------------------------------------------------------------
**************************************** - solved
 не вытащил
separate = [ˈseprɪt]

doc = nlp("separate")
[[token.pos_,token.lemma_] for token in doc]
[['ADJ', 'separate']]

java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m separate
151 "separate" mueller_base "Mueller English-Russian Dictionary (base)": text follows
separate

  1. _a. [ˈseprɪt]

    1) отдельный; cut it into four separate parts разрежьте то на четыре
    части; separate maintenance содержание, назначаемое жене при разводе

    2) особый, индивидуальный; самостоятельный; these are two entirely
    separate questions то два совершенно самостоятельных вопроса

-----------------------------------------------------------------------------------
########################## test created
**************************************** - solved
это тоже из-за ошибки одиночного POS take a leading role

doc = nlp("leading")
[[token.pos_,token.lemma_] for token in doc]
[['VERB', 'lead']]

doc = nlp("a leading")
[[token.pos_,token.lemma_] for token in doc]
[['DET', 'a'], ['NOUN', 'leading']]

------------------------------------------------------------------
**************************************** - solved
это тоже из-за ошибки одиночного POS
doc = nlp("translate")
[[token.pos_,token.lemma_] for token in doc]
[['PROPN', 'translate']]

doc = nlp("can translate")
[[token.pos_,token.lemma_] for token in doc]
[['VERB', 'can'], ['VERB', 'translate']]

-------------------------------------------------------------------
**************************************** - solved
/bin/sh: 1: Syntax error: "(" unexpected
task pending cancel
ERROR:asyncio:Task exception was never retrieved
future: <Task finished name='Task-8' coro=<consumer_handler() done, defined at /media/kirill/System/Users/Kirill/PycharmProjects/dictionary_parser/server.py:216> exception=CalledProcessError(2, 'java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m hallo(a)')>
Traceback (most recent call last):
  File "/media/kirill/System/Users/Kirill/PycharmProjects/dictionary_parser/server.py", line 223, in consumer_handler
    translation = translator.translate(data["word"])
  File "/media/kirill/System/Users/Kirill/PycharmProjects/dictionary_parser/server.py", line 44, in translate
    translation = self.parser.parse_answer(answer, spacy_pos=token.pos_, origin_word=token.lemma_, original_phrase=phrase, word_index=i)
  File "/media/kirill/System/Users/Kirill/PycharmProjects/dictionary_parser/parser.py", line 338, in parse_answer
    answer2 = self.inner_request_to_dict(word_to_search)
  File "/media/kirill/System/Users/Kirill/PycharmProjects/dictionary_parser/parser.py", line 512, in inner_request_to_dict
    res = subprocess.check_output(cmd, shell=True)
  File "/usr/lib/python3.8/subprocess.py", line 411, in check_output
    return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
  File "/usr/lib/python3.8/subprocess.py", line 512, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command 'java -cp /media/kirill/System/dictserver/jdictd.jar org.dict.client.JDict -h localhost -p 2628 -d mueller_base -m hallo(a)' returned non-zero exit status 2.
Traceback (most recent call last):
  File "/media/kirill/System/Users/Kirill/PycharmProjects/dictionary_parser/server.py", line 365, in <module>
    main()
  File "/media/kirill/System/Users/Kirill/PycharmProjects/dictionary_parser/server.py", line 353, in main
    asyncio.get_event_loop().run_forever()
  File "/usr/lib/python3.8/asyncio/base_events.py", line 570, in run_forever
    self._run_once()
  File "/usr/lib/python3.8/asyncio/base_events.py", line 1823, in _run_once
    event_list = self._selector.select(timeout)
  File "/usr/lib/python3.8/selectors.py", line 468, in select
    fd_event_list = self._selector.poll(timeout, max_ev)
KeyboardInterrupt

Process finished with exit code 130 (interrupted by signal 2: SIGINT)

how to continue work after such errors
------------------------------------------------------------
**************************************** - solved
'151 "hello" mueller_base "Mueller English-Russian Dictionary (base)": text follows
hello

  [ˈheˈləu] = hallo(a)

.
250 Command complete
221 Closing connection
'

-------------------------------
**************************************** - solved

#todo do not translate common words - set filter?
#much, more, over, under, can, above, something, may, skills,particularly, involved, There variant,  doctor,  desiese, patient, medicine genomic, test colleagues, think, see
#down up, left, right, equal, less, more, many, lot, like, clinical, role, add, calculate delete, devide, so, then, than, default, polygenic, mutation, polymorphism
#clinitians, counsellor, conditions, whitch, when, what, where, why, who, born, care, baby, family, information, translation, translate, share,
#absolutly, enhance, change, common, antibiotic, protein, aminoacid, nucleotide, sequence,
#find, replace, move, as, year, day, month
#neurological, oncology, cancer, tumor, tissue, vessel,
#problem, issue, pretty, amazing, quite, just interesting  important significant
#different only current contract develop separate exciting leading real practice relevant
#machine instrument people company laboratory scientists deliver benefits efforts
#speak feel some something somebody nowbody nothing going work help interpret understand complex results happen next few single maybe
#combination multiple already scores  useful increase decrease certain very high  completely comparable apply group need
#nessesary success individual members opportunities involved types available avoid example therapy inherited good bad mitochondria arriving usually
#local  point allows simple determine definition research education university institution academic  completely number
# resume recap conclusions perfect consequence final start stop step extension forward backward belong
# demo population sample blood
#require investors invest period time team name value message email chat call voice morning afternoon evening couple far as paper article
#would/should
#remove everything after comma? (нравиться, любить)

#test on video translation
    #css for words separators - more convinience


    #solve problem in viewing transcription when translation block is very big - transcription goes away upper and I cant see it
    #where is some words in the end of transcription ? test it again
    #| . | - delete this!



    #empty spans in translations WHY?
        #test my approach!

    #max_index logic  - relative to different replics index!!!!

    #set html of span only if it was send most later! (because of assynchronious earlier sends can be recieved latest)
        #test my approach! - messages in socket recieves through queue


    #"SCONJ": "_cj" - "that" - error - need to find unteel  next semicolon if in current is ""
        #recently I will just exclude this type of words from translation

    #adress can be II, 3 and point not only to 3. but to 3) like adress
    #Example: some babies one in 500 are born with
    --------------------------------------------------
    151 "born" mueller_base "Mueller English-Russian Dictionary (base)": text follows
born

  [bɔ:n]

    1. _p-p. от bear II, 3

    2. _a. прирождённый; a poet born прирождённый поэт; in all one's born
    days за всю свою жизнь

.
250 Command complete
221 Closing connection

151 "bear" mueller_base "Mueller English-Russian Dictionary (base)": text follows
bear

  I [bɛə]

    1. _n.

      1) медведь

      2) грубый, невоспитанный человек; to play the bear вести себя грубо

      3) _бирж. спекулянт, играющий на понижение

      4) _астр. Great (Little, Lesser) Bear Большая (Малая) Медведица

      5) дыропробивной пресс, медведка

      6) _метал. козёл

      7) _мор. _разг. швабра (для мытья палубы)

      8) _attr.: bear pool _бирж. объединение спекулянтов, играющих на
      понижение; bear market _бирж. рынок с понижательной тенденцией

      *) cross (или sulky, surly) as a bear зол как чёрт; bridled bear
      юнец, путешествующий с гувернёром; to take a bear by the tooth без
      нужды подвергать себя опасности, лезть на рожон; to sell the bear's
      skin before one has caught the bear делить шкуру неубитого медведя;
      had it been a bear it would have bitten you вы ошиблись, обознались;
      (оказалось) не так страшно, как вы думали

    2. _v. _бирж. играть на понижение

  II [bɛə] _v. (bore; borne)

    1) носить; нести; переносить, перевозить

    2) выдерживать; нести груз, тяжесть; поддерживать, подпирать; will the
    ice bear today? достаточно ли крепок лёд сегодня?

    3) (_p-p. born) рождать, производить; to bear children рожать детей;
    to bear fruit приносить плоды; born in 1919 рождения 1919 года

    4) питать, иметь (чувство и т.п.)

    5) терпеть, выносить; I can't bear him я его не выношу

    6) _refl. держаться; вести себя

    7) опираться (on)

    8) простираться

    #) bear away а) выиграть (приз, кубок и т.п.); выйти победителем;
    б): to be borne away быть захваченным, увлечённым; bear down
    а) преодолевать; б) _мор. подходить по ветру; в) устремляться (upon -
    к); набрасываться, нападать (upon - на кого-л.); г) влиять; bear in:
    to be borne in on smb. становиться ясным, понятным кому-л.; bear off
    отклоняться; bear on касаться, иметь отношение к чему-л.; bear out
    подтверждать; подкреплять; поддерживать; bear up а) поддерживать;
    подбадривать; б) держаться стойко; в) _мор. спускаться (по ветру);
    г): to bear up for взять направление на; bear upon = bear on; bear
    with относиться терпеливо к чему-л.; мириться с чем-л.

    *) to bear arms а) носить оружие; служить в армии; to bear arms
    against smb. поднять оружие на кого-л., восстать против кого-л.;
    б) иметь или носить герб; to bear company а) составлять компанию,
    сопровождать; б) ухаживать; to bear comparison выдерживать сравнение;
    to bear a hand участвовать; помогать; to bear hard on smb. подавлять
    кого-л.; to bear in mind помнить; иметь в виду; to bear a part
    принимать участие; to bear a resemblance быть похожим, иметь сходство;
    to bear to the right etc. принять вправо и т.п.; to bear the signature
    иметь подпись, быть подписанным; to bear testimony, to bear witness
    свидетельствовать, показывать, давать показания

.
250 Command complete
221 Closing connection

-------------------------------------------------------

#closing issues - services dont stop


#questions marks delete from translations

#updating of text can be performed while ONMESSAGE operates?  between - start and stop?
    #measure it - insert console.log - if it appears betwen start and stop then - yes
#calculate brs for the entire text from current updating to the end -


#hypothesis - content - is need time to calculate + white space nowrap thats why my code dont managed to capture more later changings

#innerText == mutation... - delete numbers or store them separetely?

why numbers dont cjange properly
    #test
number of lines in GUI - LEFT + MIDDLE + STICK TO LINES OF TEXT

#todo ё й ...
    #test

#test zoom, complete code in process dispatcher

for each translation phrase input previous last word(from previous phrase) to the beginning of current phrase?
        #concat first word of current phrase to the END of previous phrase and get new POS for it and translate this last word (if it wasnt translated yet)
        #concat only not particle words(verb, noun, adj, ...)

       1. #phrase prev | current phrase(a)
       2.              | phrase prev (b)   | current phrase

       #1) a raw text == b raw text
       #a - [[0] [1] [2] [3]]
       #b - [[0] [1] [] [3]]- delete
       #b - [[0] [1] [2] [3] [4]] - can add word (POS determination)
       #b - POS type change? - get more latest POS? and added
       # [] [] [] [] [] - this can be get from prev?(positions of words)
            [] [] [] [] [] - get positions of words = positions, extract positions of prev markup

       # [] [] []
       #    [] []
       #       []
       # [] [] []
       #compose
       #[] [] [] [] [] - already inserted - and markedup.

       #2. is more full information until "." was presented and after - phrase "." prev | current "." phrase

       #2) a raw text != b raw text
       # more freshest text
       # orientate by words?
       # we should substitute all text and markup for on (b)
       #
       ---------------------
       delete length/2
       in left side:
       TYPE 1 - POS SUBSTITUTE
       []
       []
       => LEAVE POS FROM PREV PHRASE
        TYPE 2 DELETION
      []
      -
      => LEAVE WORD FROM PREV PHRASE
      TYPE 3 INSERTION
      -
      []
      => DO NOT insert WORD FROM LAST PHRASE (do nothing)


       in right side:
       TYPE 1 - POS SUBSTITUTE
       []
       []
       => LEAVE POS FROM last PHRASE
         TYPE 2 DELETION
      []
      -
      => DELETE WORD FROM PREV PHRASE
       TYPE 3 INSERTION
      -
      []
      => INSERT WORD FROM LAST PHRASE

       -------------------
       rtrt rtrtr rtrtr rtrtrt - to  the raw prev string - apply all modificatiobs
       or to some parts - wrap up new span

test more simple approach yet! if it fail do more complex

#todo integrate medical vocabulary
    #where to find it? spacy?


error in interfase control_panel
it is need that state of string in the moment of send = state in the moment of recieving!(tests show that updating doesnt happen during execution of onmessage) but after
sending and before recieving string can be changed!
if current string in the span != data.word(state when request was sended) => this is not actual data and abort this modification

update  пересчет вперед без запросов на сервер каждый раз когда что то меняется!

nonblocking markup

test autoscroll in 2 mode
change height of window
autoscroll stops - why? [4] - figure out first - why it breaks!
    test 2 modes

replica index dynamic changing accounting everywhere [1]
    changing everytime

test replic changing [2]
#todo trigger transaltion of remain part of replic when new replic is created


#todo memory management [3]
    phrases_array
    already_sended
    for_restored_phrases

#todo integrate list of stop words [5]
    #collect all raw notions in list, then lemmatize them through spacy, create python dictionary and check existance by key

#todo show hidden words functionality [6]

#todo create desctop shortcut for python server start! - test all without pycharm

#todo - do not translate one word several times in one line
    #server part? - cash per each line? -
    #client - during construction of translation span - check repeats in other spans in that line(before that?) or keep in memory array of already inserted words and check in every time

#test in skype active call(with blocking microphone)
#test in zoom active call(with blocking microphone)

transaltion for 0 span
 "" - transaltion ?

async translation_answer_handler

[]starded processing from this
[]
[]
[]**current processing
[]state1==updated!
[]state1==updated!
[]
state2=updated
after processing response - if in upper indexes currently processing is happening and current index is < this index then abort this function (upper precessing will do everything down)
    and no not updatyed indexes between current and upper processing
    if state2 == not updated - between **current processing and this index => then abort this function down processint too. when upper index will fires up then it will processed everything down

    in upper if any element exist with: (state1==updated and state2==not updated) or **current processing
        finish current function(only after updating its own data)
    if during processing we met index with state (state1==updated and state2==not updated)
        finish further processing(return from function)
[]
[]
[]state2 - not updatyed - stop further processing? and return from function?- this and down will be processed in its own server response
[]
[]

sleep upper processing unteel furter down resolves -


array_of_spam_states :
 [index of span] = [
 state1 : updated by text(not yet server response - no markup, no translation) - set when this index is first touched by modification(each time)
 state2 : updated by server response(its own markup and appropriate translation words) - after its own updating
 --------------
 state3 : allowed to calculate line breaks in down spans/not allowed(already calculated earlier by upper index processing) - if not allowed - then delete this index of span entirely
            and return from function
            if allowed then process further spans

                check each time before new span calculation:
                    if indexes > current (index that we prepairing to process) exists in array_of_spam_states {
                        set state3 for all indexes for "not allowed" where state3 == updated (its own markup)
                    }

            after process delete this index of span entirely return from function
 ]
 when it passes state3 then it deleted from array


 ------------------
of translational autonomic medicine.
 autonomic ? strange transaltion
 ["переводный", " ", "медицина", "."]

 [] [] []
          [] [] []

phrase_middle: "they won't develop hearing loss when "
phrase_next: "when it can, be avoided, genetics is "
phrase_prev: "which antibiotics they should get. "

0_99: "which antibiotics they should get. "
0_100: "So they won't develop hearing loss "
0_101: "when it can, be avoided, genetics is "
------------------------------------------------
[]0--repeated several times one phrase - get last value
[]1--repeated several times one phrase - get last value - it can be - phrase1 - phrase2 - phrase1 - phrase2 - phrase2... - get last
[]2 -- it can be
    professor of
    professor of translational
    professor of translational genomic

0 - 1 -2 case for beginning this is exception?
if no stabilased phrases yet then wait them on later indexes > 3
[]3 - look for last stable phrases - after 3?
---------------------------------------


var restr_matured_phrases = {}

when to send triples of phrases to server?
function check_maturity(){
    //get latest not sended to server already triples of phrases?
    //only when
    //[] - matured
    //[] - matured - ready to send!
    //[] - matured

    //and not when
    //[] - not
    //[] - matured
    //[] - matured - not ready to send!
    //[] - not
    //[] - matured

    //[] - matured
    //[] - matured - ready to send!
    //[] - matured
    //[] - matured - if not sended - yet - send
    //[] - matured - alredy sended - do not send!
    //[] - matured


}

source of maturity signal is the changing of var text_to_update = mutation.addedNodes[0].innerText+" "; in update_and_translate_by_index2() function

//[] -
    word1
    word1 word2
    word1 word2 word3
    ...
     then can be changed or not at all!

    or
    word1
    word1 word2
    word1 word2 word3
    word1 word2 word3
    word1 word2 word3
    ...

    or
    word1
    word1 word2
    word1 word2 word3
    another_word1  another_word2
    word1 word2 word3
    another_word1  another_word2
    word1 word2 word3 - more frequent!
    ...

    or

    word1
    word1 word2
    word1 word2 word3
    another_word1  another_word2 - happens more often
    word1 word2 word3
    another_word1  another_word2
    another_word1  another_word2
    word1 word2 word3
    another_word1  another_word2
    word1 word2 word3
    another_word1  another_word2
    ...

    phrase in index matured - one phrase(do not account for punctuation) repeated more frequent

    prev phrase redy to be analysed for maturity when next phrase to it is matured(at least 2 occurences of phrase?)?
//[]
//[]
//[]
//[]

//save changes in buffer
[]
[]
[] - word1 word2 -
--
[] - or here
    word1
    word1 word2
    word1 word2 word3

- usual prev != current_index!
new elem - prev current - send prev 3 elements - get most frequent or last in ladder if no frequent is
last value is the more strong signal when equality of frequencies is present

do not allow changing any more after this? -  most probably changing will be in punctuation - lets check this!



[] - maturity signals - start to get most frequent phrases from prev triple? - they can be changed in future but alredy send check will block it changing

***
later this elements can be changed - do not allow them to change?
block changing of actual markup html if new changes are yhe same
but if not the same? - write this signal and when it stops - then get last and if it differs from current (account punctuation) recalculate markup?
NO lets try to just block this - system make first frequent guess



trigger last matured phrases each time in update_and_translate_by_index2() function

if (prev_index != null && prev_index !== index_to_update) {
    reasonable time to check maturity of phrases
    check_maturity()
}

11
years with

years with some of

years with some of the

years with some of the new

years, with some of the new

years with some of the new

technologies ?? 12


12
With some of the new technologies is
11
years.
12
technologies is that
11
years with some of the new
12
technologies is that we're
12
technologies is that we're allowed
12
technologies is that we're allowed to
13
do much
13
do much more
13
do.
14
Much more extensive

11
years.
13
that we're allowed to do.
12
With some of the new technologies is
13
that we're allowed to do, much more,

12
that we're allowed to do, much more
13
do, much more extensive testing.
12
technologies is that we're allowed to
11
years with some of the new
11
years.
13
that we're allowed to do, much more

12
With some of the new technologies is
13
do, much more extensive testing.
12
technologies is that we're allowed to
11
years with some of the new

-------------
27                                          28                              29                                  30                                  31                                           32                                33                                            34                              35
genetics in some ways, I think it|absolutely enhances the role of|genetics and the need for Genesis|clinical geneticists are going to be| geneticists are going to be having to | closely with them to help them to |               understand those more complex results|so that we can really see patient |
genetics in some ways.|I think it absolutely enhances the|role of genetics and the need for|Genesis clinical geneticists are|going to be                               having to work much more |closely with them to help them to | interpret and understand those more|complex results so that we can really|see patient benefit.
 27                          28                                   29                                   30                         31                                                        32                                33                                  34                                   35

-------------------------------------------------------------------------------------------------------------
16                                              17                     18                                 19                                 20
clinical,geneticists, genetic|counselors, and the laboratory|scientists to deliver the benefits|that come with genomic medicine.|One of the things that I'm struck by
Clinical geneticists, genetic|counselors  and     laboratory scientists|to deliver the benefits that come|with genomic medicine.|One of the things that I'm struck by
16                                    17                                 18                                  19                         20

     80                                              81                                    82                              83                                   84
they give an antibiotic or Gentamicin |Gentamicin, that they would develop|profound irreversible, hearing loss,|90,000 babies in the UK, every year     |treated on Special Care, Baby units |
they give an antibiotic or Gentamicin |           |that they would develop profound|irreversible, hearing loss, 90,000|babies in the UK, every year are |treated on Special Care, Baby units
     80                                              81                                    82                              83                                   84

             98                      99                                        100                          101                     102
which antibiotics that they should |get, so they won't develop hearing|loss when it can be avoided, genetics|genetics is changing.|changing.
which antibiotics that they should |get.|So they won't develop hearing loss|when it can,be avoided, genetics is                   |changing.
             98                      99                    100                                      101                             102

//2 main problems - adding redundant string or lack of string
//maybe i can repair it before sending to server.
//
when 101 is key3 -> check its overlap with 100 (key2) -> if yes => then delete overlap remaining part of 101 set as alredy_sended[101] = is changing. and update HTML accordingly
during updating of 101 in dispetcher(when it becames key2) -> check if 101 new value(bottom line) does add new extra string and set it as alredy_sended[101] = new_value with extra string and update actual HTML value in page accordingly, if no then set key2 as is (alredy_sended[101] = is changing.) and then check key3 for the same overlapping to alredy builded key1+key2 if overlaps -> cut of abundant string the same way and set it as result ti set as alredy_sended[102] = "trimmed string" and update HTML accordingly

then they will be sended to server and finally set up as non-modifiable(key1,key2)


//RULE OF BEGINNING OF INEQUALITY: 16 doesnt exist in marked array (key2-1) && key2 exist (already_sended[key2]!==marked[key2])
unequal_flag = begin
//this means that 16 alredy sended is equal to its updates. -> its border(right) is the same as update
so we need to start compairing strings in 17 from left border of 17

17
|counselors, and the laboratory
|            and     laboratory scientists
17
            --or--
17
|counselors, and     laboratory
|            and the laboratory scientists
17


but 17 update can be aligned not starting from left order! (but we need to start to compare starting from left border)

we can to keep track of when this border becomes 16-17 and keep track of previous updates border to avoid calculation of starting point of alingment each time

also keep track of end of such period by again -> unequal_flag = end () but maybe its meaningless...

always have 2 strings:
in the beginning of alingment

strings starting
lower string and upper string starting from end of lower string

at the end of each alingment cut of strings by right border
examples -
17                                18         this string
counselors, and the laboratory|scientists||to deliver the benefits
counselors  and     laboratory scientists|

17                                18         this string              concat on next iteration (key2)
counselors, and the laboratory|scientists||to deliver the benefits | new string new string new string new string new string
counselors  and     laboratory scientists||
     previous iteration
       99  (fromend of prev iter)          100 (new iteration concat)
get,||so they won't develop hearing|loss when it can be avoided, genetics
get.||  ----start compairing 100 (update) from here---


//RULE OF BEGINNING OF INEQUALITY: 16 doesnt exist in marked array (key2-1) && key2 exist (already_sended[key2]!==marked[key2])
unequal_flag = begin

get key1 string and start to aling its update agains it

preliminarily check key1-key2/key2-key3 overlap and elimitate it before concat (100-101 example)

        key1                              key2                          key3
    1        2   3       4        5        6  7       8
counselors, and the laboratory|scientists to deliver the benefits|that come with genomic medicine.|
counselors  and     laboratory scientists
  w1         w2       w3          w4

start to search for w1 position in upper string by iterating over sequence of words in upper string until word in upper string === w1, (this is starting position of updating phrase)

then get next word from W array and continues until  word in upper string === w2, etc
--or--
do this only for first w1 then iterate over words positions both in all strings and compare words until they doesnt equal(insert/delete) or end of string W

90,000 babies in the UK, every year treated on Special Care, Baby units
       babies in the UK, every year are treated on Special Care, Baby units

       DELETE - if word != Wn - then get this

//any intersection  - length of answer > 0
//inner => last answer intersection intersects with last query index

//inner intersection? or overlapping to right
//left overlapping doesnt interesting
//deletions in reference?

clinical|geneticists|are|going|to|be|-    |-
-       |-          |-  |-    |- |- |word1|word2
-       |-          |-  |-    |- |- |-    |-

1         2           3   4    5   6
clinical|geneticists|are|going|to|be|-    |-
-       |-          |-  |going|to|be|word1|word2
-       |-          |-  |=    |= |= |-    |-
                          1    2  3


//save number of word in coordinates of reference string - whitch overlaps with query string
[number of reference word - number of query word]
[4 - 1]
[5 - 2]
[6 - 3]
---------------
[1 - 3]
[2 - 4]
[3 - 5]
//gap
[5 - 6]
[6 - 7]

//not allow to long gaps? what if repeats of words will be?

if 6(last index of reference) intersects with last word index of query - then => no overlap to right

if 6(last index of reference) intersects with not with last index of query => then overlap to right exists

--or-- it casn be that 5 (not last index of reference) intersects with not last index of query => this means that 6 is gap and query overlaps to the right
so i need to find last from the end not gap(actually last pair in sequence of answer - [6 - 7] or [5 - 6] if it will be last)

clinical|going|geneticists|are|going|to|be|-    |-
-       |-    |-          |-  |going|to|be|word1|word2
-       |-    |-          |-  |=    |= |= |-    |-

clinical|going|geneticists|are|going|to|be
-       |-    |-          |-  |going|to|be
-       |-    |-          |-  |=    |= |=

clinical|going|geneticists|are|going|to|be
-       |-    |-          |-  |going|to|-
-       |-    |-          |-  |=    |= |-

clinical|geneticists|going|are|going|to|be
-       |-          |-    |-  |going|to|-
-       |-          |-    |-  |=    |= |-


------------------------------------------------------
1           2        3
counselors|and|-  |laboratory|-
counselors|and|the|laboratory|scientists
=         |=  |-  |=         |-
1           2   3     4          5


if insertion is presented then i need to

counselors|and|the|laboratory
counselors|and|-  |laboratory
=         |=  |-  |=

(3) [Array(2), Array(2), Array(2)]
0: (2) [3, 2]
1: (2) [1, 1]
2: (2) [0, 0]
length: 3
__proto__: Array(0)
0 - upper phrase - reference
1 - lower phrase - query
answer[0][0] - always last reference word index

last intersected word of reference with query index

//overlap to right
if (answer.length > 0 && answer[0][1]<query_string_array.length-1 ) {
    //iterate starting from answer[0][0] to last index - or calculate distance to the end
    //distance(it maight be delete in query)
    //index_from_witch_right_overlap_starts = answer[0][1]+distance
    //index_from_witch_right_overlap_starts - from this index to end of query - overlapped string
    //overlapped right string = from answer[0][1]+1 to end of query string

    var overlapped_string = query_string_array.slice(answer[0][1]+1).join(" ");
}


word1|word2|word3|word4|word5
-    |word2|word3|word7|word8
-    |=    |=    |!    |!

word1|word2|word3|-    |word4|word5
-    |word2|word3|word7|word4|-
-    |=    |=    |-    |=    |-


word1|word2|word3|-    |word4|word5|-
-    |word2|word3|word7|word4|word6|word8
-    |=    |=    |-    |=    |!    |-

summary: Array(10)
0: "-"
1: "="
2: "-"
3: "="
4: "="
5: "="
6: "="
7: "="
8: "-"
9: "-"

that|were|allowed|to|do|much|more|extensive|testing
 -  |-   |-      |- |- |much|more|extensive|testing
-   |-   |-      |- |- |=   |=   |=        |=

risks|are|really|very|high|completely|comparable|to|the|risks|that|you|-
-    |-  |-     |-   |-   |-         |comparable|to|the|risk |that|you|would
-    |-  |-     |-   |-   |-         |=         |= |=  |!    |=   |=  |-


risks|are|really|very|high|completely|comparable|to|the|risks|that|you|-
-    |-  |-     |-   |-   |-         |comparable|to|the|risk |that|you|would
-    |-  |-     |-   |-   |-         |=         |= |=  |!    |=   |=  |-


risks|are|really|very|high|completely|comparable|to|the|risks|that|you|-
-    |-  |-     |-   |-   |-         |comparable|to|the|risk |that|you|would
-    |-  |-     |-   |-   |-         |=         |= |=  |!    |=   |=  |-


which|antibiotics|that|they|should|get|so|they|won't|develop|hearing
-    |-          |-   |-   |-     |get|- |-   |-    |-      |-
-    |-          |-   |-   |-     |=  |- |-   |-    |-      |-

word1|word2|word3|word4|
 -   |-    |word3|word4|-
 -   |-    |=    |=    |-

with|some|of|the|new|technologies|is|that|we're|allowed|to|do|much|more|-        |-
-   |-   |- |-  |-  |-           |- |-   |-    |-      |- |- |-   |-   |extensive|testing
 -  |-   |- |-  |-  |-           |- |-   |-    |-      |- |- |-   |-   |-        |-

 -        |diminishes|the|role|of|clinical|genetics|in|some|ways|i|think|it
absolutely|enhances  |the|role|of|-       |-       |- |-   |-   |-|-    |-
-         |!         |=  |=   |= |-       |-       |-|-    |-   |-|-    |-

