from grammar import SimpleGrammar

poetry = SimpleGrammar() \
    .set_text("#main_structure#")\
    .add_tag("main_structure", [\
"""#capitalize.1.feeling# #define_verb# mais do que #1.feeling#
#capitalize.define_verb# #vague_feeling#."""
        ])\
    .add_tag("feeling", [\
        "amor", "ódio", "ciúmes", "paixão", "tristeza", "raiva", "fúria",\
        "intensa luxúria"\
        ])\
    .add_tag("define_verb", [\
        "é", "significa", "quer dizer", "se define como",\
        "traça sua definição como", "se entrelaça no significado de",\
        "se traduz como" \
        ])\
    .add_tag("vague_feeling", [
        "um sentimento inéfavel",
        "o silêncio de nossas indefinições",
        "a incerteza de #my_expression#"
        ])\
    .add_tag("my_expression", [
        "meus sorrisos",
        "meus suspiros",
        "meus bramidos"
        ])


print(str(poetry))