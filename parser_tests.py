from parser import Parser

test = {
    "test16": '''151 "year" mueller_base "Mueller English-Russian Dictionary (base)": text follows
year

  [jə:], [jɪə] _n.

    1) год; year by year каждый год; year in year out из года в год; from
    year to year, year by year, year after year с каждым годом; каждый
    год; год от году; years (and years) ago очень давно, целую вечность;
    the year of grace год нашей эры; in the year of grace (или of our
    Lord) 1975 в 1975 году от рождества Христова

    2) _pl. возраст, годы; he looks young for his years он молодо выглядит
    для своих лет; in years пожилой

.
250 Command complete 
221 Closing connection''',
    "test17": '''151 "that" mueller_base "Mueller English-Russian Dictionary (base)": text follows
that

  1. _pron. (_pl. those)

    1) [ðæt] _demonstr. тот, та, то (иногда этот и пр.); а) указывает на
    лицо, понятие, событие, предмет, действие, отдалённые по месту или
    времени: that house beyond the river тот дом за рекой; that day тот
    день; that man тот человек; б) противополагается this: this wine is
    better than that это вино лучше того; в) указывает на что-л. уже
    известное говорящему: that is true это правда; that's done it это
    решило дело, переполнило чашу; г) заменяет сущ. во избежание его
    повторения: the climate here is like that of France здешний климат
    похож на климат Франции

    2) [ðæt] (полная форма); [ðət], [ðt] (редуцированные формы) _rel.
    а) который, кто, тот который и т.п.; the members that were present те
    из членов, которые присутствовали; the book that I'm reading книга,
    которую я читаю; б) часто = in (или on, at, for и т.п.) which: the
    year that he died год его смерти; the book that I spoke of книга, о
    которой я говорил

    *) and all that и тому подобное, и всё такое прочее; by that тем
    самым, этим; like that таким образом; that's that _разг. ничего не
    поделаешь; так-то вот; that is то есть; not that не потому (или не
    то), чтобы; that's it! вот именно!, правильно!; that's all there is to
    it ну, вот и всё; this and that разные; I went to this doctor and that
    я обращался к разным врачам; now that теперь, когда; with that вместе
    с тем

  2. _adv. [ðæt] так, до такой степени; that far настолько далеко; на
  такое расстояние; that much столько; he was that angry he couldn't say a
  word он был до того рассержен, что слова не мог вымолвить

  3. _cj. [ðæt] (полная форма); [ðət] (редуцированная форма) что, чтобы
  (служит для введения придаточных предложений дополнительных, цели,
  следствия и др.); I know that it was so я знаю, что это было так; we eat
  that we may live мы едим, чтобы поддерживать жизнь; the explosion was so
  loud that he was deafened взрыв был настолько силен, что оглушил его

    *) oh, that I knew the truth! о, если бы я знал правду!

.
250 Command complete 
221 Closing connection''',
    "test18": '''151 "more" mueller_base "Mueller English-Russian Dictionary (base)": text follows
more

  [mɔ:]

    1. _a.

      1) _comp. от much 1 и many 1

      2) больший, более многочисленный; he has more ability than his
      predecessors у него больше умения, чем у его предшественников

      3) добавочный, ещё (употр. с числительным или неопределённым
      местоимением); two more cruisers were sunk ещё два крейсера были
      потоплены; bring some more water принесите ещё воды

    2. _adv.

      1) _comp. от much 2

      2) больше; you should walk more вам надо больше гулять

      3) служит для образования _comp. многосложных прилагательных и
      наречий: more powerful более мощный

      4) ещё; опять, снова; once more ещё раз

      *) more or less более или менее, приблизительно; the more... the
      more чем больше..., тем больше; the more he has the more he wants
      чем больше он имеет, тем большего он хочет; the more the better чем
      больше, тем лучше; neither more nor less than ни больше, ни меньше
      как; не что иное, как; all the more so тем более; never more
      никогда; he is no more его нет в живых

    3. _n. большее количество; дополнительное количество

      *) what is more вдобавок, больше того; hope to see more of you
      надеюсь чаще вас видеть; we saw no more of him мы его больше не
      видели; there is more to come это ещё не всё

.
250 Command complete 
221 Closing connection''',
    "test19": '''151 "counselor" mueller_base "Mueller English-Russian Dictionary (base)": text follows
counselor

  [ˈkaunslə] = counsellor

.
250 Command complete 
221 Closing connection''',
    "test20": '''152 16 matches found: list follows
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
221 Closing connection''',
    "test21": '''152 16 matches found: list follows
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
.
250 Command complete
221 Closing connection''',
    "test22": '''151 "can" mueller_base "Mueller English-Russian Dictionary (base)": text follows
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

.
250 Command complete 
221 Closing connection''',
    "test23": '''151 "use" mueller_base "Mueller English-Russian Dictionary (base)": text follows
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

    3) обращаться, обходиться (с кем-л.); to use smb. like a dog
    третировать кого-л.; he thinks himself ill used он считает, что с ним
    плохо обошлись

    4) (тк. _p. обыкн. [ju:st]) I used to see him often я часто его
    встречал; it used to be said (бывало) говорили; there used to be a
    house here раньше здесь стоял дом

    #) use up а) израсходовать, использовать; истратить; б) истощать; to
    feel used up чувствовать себя совершенно обессиленным

.
250 Command complete 
221 Closing connection''',
    "test24": '''151 "increased" mueller_base "Mueller English-Russian Dictionary (base)": text follows
increase

  1. _n. [ˈɪnkri:s] возрастание, рост; увеличение, прибавление,
  размножение, прирост; to be on the increase расти, увеличиваться; an
  increase in pay прибавка к зарплате

  2. _v. [ɪnˈkri:s] возрастать, увеличивать(ся); расти; усиливать(ся); to
  increase one's pace ускорять шаг; to increase by 10% увеличиться на 10%

.
250 Command complete 
221 Closing connection''',
    "test25": '''151 "genetics" mueller_base "Mueller English-Russian Dictionary (base)": text follows
genetics

  [ʤɪˈnetɪks] _n. _pl. (употр. как _sing.) генетика

.
250 Command complete 
221 Closing connection''',
    "test26": '''151 "over" mueller_base "Mueller English-Russian Dictionary (base)": text follows
over

  [ˈəuvə]

    1. _prep.

      1) указывает на взаимное положение предметов: а) над, выше; over our
      heads над нашими головами; сверх, выше нашего понимания; _разг. не
      посоветовавшись с нами; б) через; a bridge over the river мост через
      реку; в) по ту сторону, за, через; a village over the river деревня
      по ту сторону реки; he lives over the way он живёт через дорогу;
      г) у, при, за; they were sitting over the fire они сидели у камина

      2) указывает на характер движения: а) через, о; he jumped over the
      ditch он перепрыгнул через канаву; to flow over the edge бежать
      через край; to stumble over a stone споткнуться о камень; б) поверх,
      на; he pulled his hat over his eyes он надвинул шляпу на глаза;
      в) по, по всей поверхности; over the whole country, all over the
      country по всей стране; snow is falling over the north of England на
      севере Англии идёт снег

      3) указывает на промежуток времени, в течение которого происходило
      действие за, в течение; he packed over two hours он собрался за два
      часа; to stay over the whole week оставаться в течение всей недели

      4) указывает на количественное или числовое превышение свыше, сверх,
      больше; over two years больше двух лет; over fine millions свыше
      пяти миллионов; she is over fifty ей за пятьдесят

      5) указывает на превосходство в положении, старшинство и т.п. над; a
      general is over a colonel генерал старше по чину, чем полковник;
      they want a good chief over them им нужен хороший начальник; he is
      over me in the office он мой начальник по службе

      6) указывает на источник, средство и т.п. через, через посредство,
      по; I heard it over the radio я слышал это по радио

      7) относительно, касательно; to talk over the matter говорить
      относительно этого дела

      *) she was all over him она не знала, как угодить ему

    2. _adv.

      1) указывает на движение через что-л., передаётся приставками пере-,
      вы; to jump over перепрыгнуть; to swim over переплыть; to boil over
      _разг. убегать (о молоке и т.п.)

      2) указывает на повсеместность или всеохватывающий характер действия
      или состояния: hills covered all over with snow холмы, сплошь
      покрытые снегом; paint the wall over покрась всю стену

      3) указывает на доведение действия до конца; передаётся приставкой
      про-; to read the story over прочитать рассказ до конца; to think
      over продумать

      4) указывает на окончание, прекращение действия: the meeting is over
      собрание окончено; it is all over всё кончено; всё пропало

      5) снова, вновь, ещё раз; the work is badly done, it must be done
      over работа сделана плохо, её нужно переделать

      6) вдобавок, сверх, слишком, чересчур; I paid my bill and had five
      shillings over я заплатил по счёту, и у меня ещё осталось пять
      шиллингов; he is over polite он чрезвычайно любезен; children of
      fourteen and over дети четырнадцати лет и старше

      7) имеет усилительное значение: over there вон там; let him come
      over here пусть-ка он придёт сюда; take it over to the post-office
      отнеси-ка это на почту; hand it over to them передай-ка им это

      #) over against а) против, напротив; б) по сравнению с

      *) over and over (again) много раз, снова и снова; over and above
      а) в добавление, к тому же; б) с лихвой; it can stand over это может
      подождать; that is Tom all over это так характерно для Тома, это так
      похоже на Тома

    3. _n.

      1) излишек, приплата

      2) _воен. перелёт (снаряда)

      3) _радио. переход на приём

    4. _a.

      1) верхний

      2) вышестоящий

      3) излишний, избыточный

      4) чрезмерный
over-

  [ˈəuvə] _pref. сверх-, над-, чрезмерно, пере-

.
250 Command complete 
221 Closing connection''',
    "test27": '''151 "swap" mueller_base "Mueller English-Russian Dictionary (base)": text follows
swap

  [swɔp] = swop

.
250 Command complete 
221 Closing connection''',
    "test28": '''151 "separate" mueller_base "Mueller English-Russian Dictionary (base)": text follows
separate

  1. _a. [ˈseprɪt]

    1) отдельный; cut it into four separate parts разрежьте то на четыре
    части; separate maintenance содержание, назначаемое жене при разводе

    2) особый, индивидуальный; самостоятельный; these are two entirely
    separate questions то два совершенно самостоятельных вопроса

    3) изолированный; уединённый

    4) сепаратный

  2. _n. [ˈseprɪt] отдельный оттиск (статьи)

  3. _v. [ˈsepəreɪt]

    1) отделять(ся), разделять(ся); разлучать(ся); расходиться

    2) сортировать, отсеивать; to separate chaff from grain очищать зерно
    от мякины

    3) разлагать (на части)

    4) _воен. увольнять, демобилизовывать

.
250 Command complete 
221 Closing connection''',
    "test29": '''151 "born" mueller_base "Mueller English-Russian Dictionary (base)": text follows
born

  [bɔ:n]

    1. _p-p. от bear II, 3

    2. _a. прирождённый; a poet born прирождённый поэт; in all one's born
    days за всю свою жизнь

.
250 Command complete
221 Closing connection''',
    "test30": '''''',

    "test1": '''151 "relative" mueller_base "Mueller English-Russian Dictionary (base)": text follows
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
    "test2": '''151 "obesity" mueller_base "Mueller English-Russian Dictionary (base)": text follows
obesity

  [?u?bi:s?t?] _n. тучность; ожирение

.
250 Command complete
221 Closing connection''',
    "test3": '''151 "recognize" mueller_base "Mueller English-Russian Dictionary (base)": text follows
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
    "test4": '''151 "forgive" mueller_base "Mueller English-Russian Dictionary (base)": text follows
forgive

  [f??g?v] _v. (forgave; forgiven)

    1) прощать

    2) не требовать, не взыскивать (долг)

.
250 Command complete
221 Closing connection''',
    "test5": '''151 "beautiful" mueller_base "Mueller English-Russian Dictionary (base)": text follows
beautiful

  [?bju:t?ful] _a.

    1) красивый, прекрасный,

    2) превосходный

.
250 Command complete
221 Closing connection''',
    "test6": '''152 16 matches found: list follows
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
    "test7": '''151 "less" mueller_base "Mueller English-Russian Dictionary (base)": text follows
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
    "test8": '''151 "took" mueller_base "Mueller English-Russian Dictionary (base)": text follows
took

  [tuk] _p. от take 1

.
250 Command complete
221 Closing connection''',
    "test9": '''151 "thou" mueller_base "Mueller English-Russian Dictionary (base)": text follows
thou

  [?au] _pron. _pers. (_obj. thee) _уст. _поэт. ты

.
250 Command complete
221 Closing connection''',
    "test10": '''151 "nevertheless" mueller_base "Mueller English-Russian Dictionary (base)": text follows
nevertheless

  [?nev????les]

    1. _adv. несмотря на, однако

    2. _cj. тем не менее

.
250 Command complete
221 Closing connection''',
    "test11": '''151 "plane" mueller_base "Mueller English-Russian Dictionary (base)": text follows
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
    "test12": '''151 "lean" mueller_base "Mueller English-Russian Dictionary (base)": text follows
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
    "test13": '''151 "hence" mueller_base "Mueller English-Russian Dictionary (base)": text follows
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
    "test14": '''151 "a" mueller_base "Mueller English-Russian Dictionary (base)": text follows
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
    "test15": '''151 "to" mueller_base "Mueller English-Russian Dictionary (base)": text follows
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

def main():
    p = Parser()
    #Parser.poses["NON"] = "_non"
    Parser.poses["PREP"] = "_prep"#предлоги не нужны в переводе но как образец для теста нужны
    #Parser.poses["P"] = "_p" # добавил к глаголам в список
    Parser.poses["NN"] = "_nn"
    Parser.poses["VV"] = "_vv"
    Parser.poses["NNN"] = "_nnn"


    test_set = {
        "test16" : [["NOUN","_n"],["NON","_non"]],
        "test17" : [["PRON","_pron"],["NON","_non"]],
        "test18" : [["ADJ","_a"],["NON","_non"]],
        "test19" : [["NOUN","_n"],["NON","_non"]],
        #"test20" : [["ADJ","_a"],["NON","_non"]],
        "test22" : [["VERB","_v"],["NON","_non"]],
        "test23" : [["NOUN","_n"],["NON","_non"]],
        "test24" : [["VERB","_v"],["NON","_non"]],
        "test25" : [["NOUN","_n"],["NON","_non"]],
        "test26" : [["PREP","_prep"],["NON","_non"]],
        "test27" : [["NOUN","_n"],["NON","_non"]],
        "test28" : [["ADJ","_a"],["NON","_non"]],
        "test29" : [["VERB","_v"],["NON","_non"]],


        "test1" : [["NOUN","_n"],["ADJ","_a"],["NON","_non"]],
        "test2": [["NOUN","_n"],["NON","_non"]],
        "test3": [["VERB","_v"],["NON","_non"]],
        "test4": [["VERB","_v"],["NON","_non"]],
        "test5": [["ADJ","_a"],["NON","_non"]],
        "test7": [["ADJ","_a"],["ADV","_adv"],["NOUN","_n"],["PREP","_prep"],["NON","_non"]],
        "test8": [["VERB","_p"],["NON","_non"]],# ["P","_p"]
        "test9": [["PRON","_pron"],["NON","_non"]],
        "test10": [["ADV","_adv"],["SCONJ","_cj"]],
        "test11": [["NOUN","_n"],["ADJ","_a"],["VERB","_v"],["NN","_nn"],["VV","_vv"],["NNN","_nnn"],["NON","_non"]],
        "test12": [["ADJ","_a"],["NOUN","_n"],["VERB","_v"],["NN","_nn"],["NON","_non"]],
        "test13": [["ADV","_adv"],["INTJ","_int"],["NON","_non"]],
        "test14": [["NOUN","_n"],["NON","_non"]],
        "test15": [["PREP","_prep"],["NON","_non"]]
    }

    for key, value in test_set.items():
        for i in range(0,len(value)):
            spacy_pos = value[i][0]

            p.recursion_protection = 0
            translation = p.parse_answer(test[key], spacy_pos)
            translation = p.resolve_linkanswer(translation, spacy_pos)
            a = 1
    a = 1

    """
    p.translation = ""
    p.multiline_begins = False
    p.pos_finded_above = False
    p.recursion_protection = 0
    translation = p.parse_answer(test["test6"], "spacy_pos1","seamlessly")
    p.translation = ""
    p.multiline_begins = False
    p.pos_finded_above = False
    p.recursion_protection = 0
    translation = p.parse_answer(test["test20"], 'ADJ',"transformative")
    p.translation = ""
    p.multiline_begins = False
    p.pos_finded_above = False
    p.recursion_protection = 0
    translation = p.parse_answer(test["test21"], 'VERB',"diminishe")
    """


if __name__ == '__main__':
    #find what possible POS can be in Spacy and correct my poses dictionary to map with possible POS in dictionary
    #https://spacy.io/api/annotation#pos-tagging
    #create sets of dictionary article - all possible POS in structure(lines where to search answer)
    #run my function parse_answer against every possible combination for testing

    #protect from several _POS _POS in one string
    #а) in the middle
    #token.lemma_ - always send this and I dont need to have to create code for #_p. и _p-p. от seek cases!
    main()



