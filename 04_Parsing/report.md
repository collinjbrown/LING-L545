# Dependency Parsing
 First tree

 ```
 # sent_id = test-s2
 # text = Luxenburgoko agintari politikoek ziurtatu zuten eskari hau onartzeko prest zeudela eta hegazkin txiki bat zain zegoela Findeleko aireportuan.
 1	Luxenburgoko	Luxenburgo	PROPN	_	Case=Loc|Definite=Def|Number=Sing	2	nmod	_	_
 2	agintari	agintari	NOUN	_	_	4	nsubj	_	_
 3	politikoek	politiko	ADJ	_	Case=Erg|Definite=Def|Number=Plur	2	amod	_	_
 4	ziurtatu	ziurtatu	VERB	_	Aspect=Perf|VerbForm=Part	0	root	_	_
 5	zuten	edun	AUX	_	Mood=Ind|Number[abs]=Sing|Number[erg]=Plur|Person[abs]=3|Person[erg]=3|VerbForm=Fin	4	aux	_	ReconstructedLemma=Yes
 6	eskari	eskari	NOUN	_	_	8	obj	_	_
 7	hau	hau	DET	_	Case=Abs|Definite=Def|Number=Sing	6	det	_	_
 8	onartzeko	onartu	VERB	_	Case=Loc|VerbForm=Fin	10	xcomp	_	_
 9	prest	prest	ADJ	_	Case=Abs|Definite=Ind	10	compound	_	_
 10	zeudela	egon	VERB	_	VerbForm=Fin	4	ccomp	_	_
 11	eta	eta	CCONJ	_	_	16	cc	_	_
 12	hegazkin	hegazkin	NOUN	_	_	16	nsubj	_	_
 13	txiki	txiki	ADJ	_	_	12	amod	_	_
 14	bat	bat	NUM	_	NumType=Card	12	nummod	_	_
 15	zain	zain	ADV	_	_	16	advmod	_	_
 16	zegoela	egon	VERB	_	Aspect=Prog|Mood=Ind|Number[abs]=Sing|Person[abs]=3|VerbForm=Fin	10	conj	_	_
 17	Findeleko	Findel	PROPN	_	Case=Loc|Definite=Def|Number=Sing	18	nmod	_	_
 18	aireportuan	aireportu	NOUN	_	Case=Ine|Definite=Def|Number=Sing	16	obl	_	SpaceAfter=No
 19	.	.	PUNCT	_	_	4	punct	_	_
 ```

 Second tree

 ```
 # sent_id = test-s3
 # text = Arazoa da ez daudela instituzioak arau horiek betetzen diren bermatzeko.
 1	Arazoa	arazo	NOUN	_	Animacy=Inan|Case=Abs|Definite=Def|Number=Sing	2	nsubj	_	_
 2	da	izan	VERB	_	Aspect=Prog|Mood=Ind|Number[abs]=Sing|Person[abs]=3|VerbForm=Fin	0	root	_	_
 3	ez	ez	PART	_	Polarity=Neg	4	advmod	_	_
 4	daudela	egon	VERB	_	Aspect=Prog|Mood=Ind|Number[abs]=Plur|Person[abs]=3|VerbForm=Fin	5	acl	_	_
 5	instituzioak	instituzio	NOUN	_	Animacy=Inan|Case=Abs|Definite=Def|Number=Plur	8	nsubj	_	_
 6	arau	arau	NOUN	_	_	8	nsubj	_	_
 7	horiek	horiek	DET	_	Case=Abs|Definite=Def|Number=Plur	6	det	_	_
 8	betetzen	bete	VERB	_	Aspect=Imp|VerbForm=Inf	10	ccomp	_	_
 9	diren	izan	AUX	_	Mood=Ind|Number[abs]=Plur|Person[abs]=3|VerbForm=Fin	8	aux	_	_
 10	bermatzeko	bermatu	VERB	_	Case=Abs|Definite=Ind|VerbForm=Fin	2	advcl	_	SpaceAfter=No
 11	.	.	PUNCT	_	_	2	punct	_	_
 ```

 Third tree

 ```
 # sent_id = test-s9
 # text = Lehendakari hautatu zutenetik, Djukanovicek aldaketa handia eman dio bere ildo politikoari.
 1	Lehendakari	lehendakari	NOUN	_	Case=Abs|Definite=Ind	2	obj	_	_
 2	hautatu	hautatu	VERB	_	Aspect=Perf|VerbForm=Part	8	advcl	_	_
 3	zutenetik	edun	AUX	_	Mood=Ind|Number[abs]=Sing|Number[erg]=Plur|Person[abs]=3|Person[erg]=3|VerbForm=Fin	2	aux	_	ReconstructedLemma=Yes|SpaceAfter=No
 4	,	,	PUNCT	_	_	2	punct	_	_
 5	Djukanovicek	Djukanovic	PROPN	_	Case=Erg|Definite=Def|Number=Sing	8	nsubj	_	_
 6	aldaketa	aldaketa	NOUN	_	_	8	obj	_	_
 7	handia	handi	ADJ	_	Case=Abs|Definite=Def|Number=Sing	6	amod	_	_
 8	eman	eman	VERB	_	Aspect=Perf|VerbForm=Part	0	root	_	_
 9	dio	edun	AUX	_	Mood=Ind|Number[abs]=Sing|Number[dat]=Sing|Number[erg]=Sing|Person[abs]=3|Person[dat]=3|Person[erg]=3|VerbForm=Fin	8	aux	_	ReconstructedLemma=Yes
 10	bere	bera	DET	_	Case=Gen|Number=Sing	11	nmod	_	_
 11	ildo	ildo	NOUN	_	_	8	iobj	_	_
 12	politikoari	politiko	ADJ	_	Case=Dat|Definite=Def|Number=Sing	11	amod	_	SpaceAfter=No
 13	.	.	PUNCT	_	_	8	punct	_	_
 ```

 Fourth tree

 ```
 # sent_id = test-s10
 # text = Gaur ere erremonte jaialdiak izango dira Galarretan eta Euskalen.
 1	Gaur	gaur	ADV	_	_	5	advmod	_	_
 2	ere	ere	CCONJ	_	_	1	fixed	_	_
 3	erremonte	erremonte	NOUN	_	_	4	nmod	_	_
 4	jaialdiak	jaialdi	NOUN	_	Animacy=Inan|Case=Abs|Definite=Def|Number=Plur	5	nsubj	_	_
 5	izango	izan	VERB	_	Aspect=Prosp|VerbForm=Part	0	root	_	_
 6	dira	izan	AUX	_	Mood=Ind|Number[abs]=Plur|Person[abs]=3|VerbForm=Fin	5	aux	_	_
 7	Galarretan	Galarreta	PROPN	_	Case=Ine|Definite=Def|Number=Sing	5	obl	_	_
 8	eta	eta	CCONJ	_	_	9	cc	_	_
 9	Euskalen	Euskal	PROPN	_	Case=Ine|Definite=Def|Number=Sing	7	conj	_	SpaceAfter=No
 10	.	.	PUNCT	_	_	5	punct	_	_
 ```

 Fifth tree

 ```
 # sent_id = test-s11
 # text = Esnatu orduko esan nuen:
 1	Esnatu	esnatu	VERB	_	VerbForm=Part	3	xcomp	_	_
 2	orduko	orduko	ADV	_	_	1	advmod	_	_
 3	esan	esan	VERB	_	Aspect=Perf|VerbForm=Part	0	root	_	_
 4	nuen	edun	AUX	_	Mood=Ind|Number[abs]=Sing|Number[erg]=Sing|Person[abs]=3|Person[erg]=1|VerbForm=Fin	3	aux	_	ReconstructedLemma=Yes|SpaceAfter=No
 5	:	:	PUNCT	_	_	3	punct	_	_
```

 Sixth tree

 ```
 # sent_id = test-s12
 # text = Eta aukera horretan denon parte hartzea, konpromezua eta ardura ezinbesteko izango dira.
 1	Eta	eta	CCONJ	_	_	12	cc	_	_
 2	aukera	aukera	NOUN	_	_	12	obl	_	_
 3	horretan	hori	DET	_	Case=Ine|Definite=Def|Number=Sing	2	det	_	_
 4	denon	dena	DET	_	Case=Gen|Definite=Def|Number=Plur	5	nmod	_	_
 5	parte	parte	NOUN	_	_	6	xcomp	_	_
 6	hartzea	hartu	VERB	_	Case=Abs|VerbForm=Fin	12	nsubj	_	SpaceAfter=No
 7	,	,	PUNCT	_	_	8	punct	_	_
 8	konpromezua	konpromiso	NOUN	_	Case=Abs|Definite=Def|Number=Sing	6	conj	_	_
 9	eta	eta	CCONJ	_	_	10	cc	_	_
 10	ardura	ardura	NOUN	_	Case=Abs|Definite=Def|Number=Sing	6	conj	_	_
 11	ezinbesteko	ezinbesteko	ADJ	_	Case=Abs|Definite=Ind	12	obl	_	_
 12	izango	izan	VERB	_	Aspect=Prosp|VerbForm=Part	0	root	_	_
 13	dira	izan	AUX	_	Mood=Ind|Number[abs]=Plur|Person[abs]=3|VerbForm=Fin	12	aux	_	SpaceAfter=No
 14	.	.	PUNCT	_	_	12	punct	_	_
 ```

 Seventh tree

 ```
 # sent_id = test-s15
 # text = - Gune ez hiritarretan bizi dira nagusiki.
 1	-	-	PUNCT	_	_	6	punct	_	_
 2	Gune	gune	NOUN	_	_	6	nsubj	_	_
 3	ez	ez	PART	_	Polarity=Neg	6	advmod	_	_
 4	hiritarretan	hiritar	ADJ	_	Case=Ine|Definite=Def|Number=Plur	6	obl	_	_
 5	bizi	bizi	ADJ	_	Case=Abs|Definite=Ind	6	compound	_	_
 6	dira	izan	VERB	_	Aspect=Prog|Mood=Ind|Number[abs]=Plur|Person[abs]=3|VerbForm=Fin	0	root	_	_
 7	nagusiki	nagusiki	ADV	_	_	6	advmod	_	SpaceAfter=No
 8	.	.	PUNCT	_	_	6	punct	_	_
 ```

 Eighth tree

 ```
 # sent_id = test-s19
 # text = Dakidan bakarra da taldeak bizi duen egoera puntuak aterata konpontzen dela.
 1	Dakidan	jakin	VERB	_	Aspect=Prog|Mood=Ind|Number[abs]=Sing|Number[erg]=Sing|Person[abs]=3|Person[erg]=1|VerbForm=Fin	2	acl	_	_
 2	bakarra	bakar	ADJ	_	Case=Abs|Definite=Def|Number=Sing	3	nsubj	_	_
 3	da	izan	VERB	_	Aspect=Prog|Mood=Ind|Number[abs]=Sing|Person[abs]=3|VerbForm=Fin	0	root	_	_
 4	taldeak	talde	NOUN	_	Animacy=Inan|Case=Erg|Definite=Def|Number=Sing	6	nsubj	_	_
 5	bizi	bizi	ADJ	_	Case=Abs|Definite=Ind	6	compound	_	_
 6	duen	ukan	VERB	_	VerbForm=Fin	7	acl	_	_
 7	egoera	egoera	NOUN	_	Animacy=Inan|Case=Abs|Definite=Def|Number=Sing	10	nsubj	_	_
 8	puntuak	puntu	NOUN	_	Animacy=Inan|Case=Abs|Definite=Def|Number=Plur	9	obj	_	_
 9	aterata	atera	VERB	_	VerbForm=Part	10	advcl	_	_
 10	konpontzen	konpondu	VERB	_	Aspect=Imp|VerbForm=Inf	3	ccomp	_	_
 11	dela	izan	AUX	_	Mood=Ind|Number[abs]=Sing|Person[abs]=3|VerbForm=Fin	10	aux	_	SpaceAfter=No
 12	.	.	PUNCT	_	_	3	punct	_	_
 ```

 Ninth tree

 ```
 # sent_id = test-s23
 # text = Ikuskizun makala eskaini zuten atzo Athleticek eta Feyenoordek San Mamesen, bazkidearen omenezko partiduan.
 1	Ikuskizun	ikuskizun	NOUN	_	_	3	obj	_	_
 2	makala	makal	ADJ	_	Case=Abs|Definite=Def|Number=Sing	1	amod	_	_
 3	eskaini	eskaini	VERB	_	Aspect=Perf|VerbForm=Part	0	root	_	_
 4	zuten	edun	AUX	_	Mood=Ind|Number[abs]=Sing|Number[erg]=Plur|Person[abs]=3|Person[erg]=3|VerbForm=Fin	3	aux	_	ReconstructedLemma=Yes
 5	atzo	atzo	ADV	_	_	3	advmod	_	_
 6	Athleticek	Athletic	PROPN	_	Case=Erg|Definite=Def|Number=Sing	3	nsubj	_	_
 7	eta	eta	CCONJ	_	_	8	cc	_	_
 8	Feyenoordek	Feyenoord	PROPN	_	Case=Erg|Definite=Def|Number=Sing	6	conj	_	_
 9	San	san	NOUN	_	_	10	compound	_	_
 10	Mamesen	Mames	PROPN	_	Case=Ine|Definite=Def|Number=Sing	3	obl	_	SpaceAfter=No
 11	,	,	PUNCT	_	_	14	punct	_	_
 12	bazkidearen	bazkide	NOUN	_	Case=Gen|Definite=Def|Number=Sing	13	nmod	_	_
 13	omenezko	omen	NOUN	_	Case=Loc|Definite=Ind	14	nmod	_	_
 14	partiduan	partidu	NOUN	_	Animacy=Inan|Case=Ine|Definite=Def|Number=Sing	3	obl	_	SpaceAfter=No
 15	.	.	PUNCT	_	_	3	punct	_	_
 ```

 Tenth tree

 ```
 # sent_id = test-s27
 # text = Hori diote futbolaz dakiten entrenatzaileek.
 1	Hori	hori	DET	_	Case=Abs|Definite=Def|Number=Sing	2	obj	_	_
 2	diote	esan	VERB	_	Aspect=Prog|Mood=Ind|Number[abs]=Sing|Number[erg]=Plur|Person[abs]=3|Person[erg]=3|VerbForm=Fin	4	advcl	_	_
 3	futbolaz	futbol	NOUN	_	Animacy=Inan|Case=Ins|Definite=Def|Number=Sing	4	obl	_	_
 4	dakiten	jakin	VERB	_	Aspect=Prog|Mood=Ind|Number[abs]=Sing|Number[erg]=Plur|Person[abs]=3|Person[erg]=3|VerbForm=Fin	0	root	_	_
 5	entrenatzaileek	entrenatzaile	NOUN	_	Case=Erg|Definite=Def|Number=Plur	4	nsubj	_	SpaceAfter=No
 6	.	.	PUNCT	_	_	4	punct	_	_
 ```