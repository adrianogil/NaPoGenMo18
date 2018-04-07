from grammar import SimpleGrammar

poetry = SimpleGrammar() \
    .set_text("#main_structure#")\
    .add_tag("main_structure", [\
        "#simple_structure#\n\n#simple_structure#\n\n#simple_structure#"\
        ])\
    .add_tag("simple_structure", [\
        "#feeling_statement#\n#world_metaphore#\n#feeling_statement#"\
        ])\
    .add_tag("feeling_statement", [\
        "#feeling# #define_verb# #intense_comparation#" \
        ])\
    .add_tag("world_metaphore", [\
        "#world_object# que #intense_verb# #intense_comparation#"\
        ])\
    .add_tag("feeling", [\
        "Amor", "Ódio", "Ciúmes", "Paixão", "Tristeza", "Raiva", "Fúria",\
        "Intensa luxúria"\
        ])\
    .add_tag("world_object", [\
        "Casa", "Muralha", "Castelo", "Praia de #crazy_adjective#",\
        "Mar de #crazy_adjective#", "Murada", "Templo de #crazy_adjective#",\
        "Águas profundas de #crazy_adjective#"\
        ])\
    .add_tag("define_verb", [\
        "é", "significa", "quer dizer", "se define como"\
        ])\
    .add_tag("intense_verb", [\
        "trespassa o significado de", "se liquefaz como"\
        ])\
    .add_tag("intense_comparation", [\
        "nunca viver plenamente", "um animal perdido em sua insanidade"\
        ])\
    .add_tag("crazy_adjective", [\
        "tempestuosa alegria", "infinita tristeza", "efêmera contemplação"\
        ])


print(str(poetry))