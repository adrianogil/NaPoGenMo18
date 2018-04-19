from grammar import SimpleGrammar

poetry = SimpleGrammar() \
    .set_text("#main_structure#")\
    .add_tag("main_structure", [\
        "#1.feeling# #define_verb# mais do que #1.feeling#"\
        ])\
    .add_tag("feeling", [\
        "Amor", "Ódio", "Ciúmes", "Paixão", "Tristeza", "Raiva", "Fúria",\
        "Intensa luxúria"\
        ])\
    .add_tag("define_verb", [\
        "é", "significa", "quer dizer", "se define como",\
        "traça sua definição como", "se entrelaça no significado de",\
        "se traduz como" \
        ])\


print(str(poetry))