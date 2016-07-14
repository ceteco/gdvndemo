# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define c = Character('Carlos', color="#c8ffc8")


# The game starts here.
# - El juego comienza aquí.
label start:
    
    scene black with dissolve

    show text "Capítulo 3 \nNaves Espaciales" with Pause(2.0)

    scene black with dissolve

# scene your_scene_title

    "Hoy es día de tour por el estudio de desarrollo"
    "No tenía previsto que ese mismo día se me presentase la opción de contribuír en el desarrollo de un videojuego"
    "Ahora la historia en realidad comienza."    
    
    #Este código inserta un video en medio de la novela visual
    $ renpy.movie_cutscene("movie.ogv")

    c "¡Wow!" 
    c "¿Eso es un juego de naves espaciales?"
    
    "Sí" -Contestó el guía
    
    c "Pero qué bestial está"
    c "¿Aquí hacen ese juego ustedes en el estudio?"
    "Así es Carlos"
    c "¿Quienes lo hacen"
    "Desarrollar un videojuego involucra escribir guiones, programar, gráficos, economía, música y efectos de sonido"
    "Cómo verás son muchos los aspectos de crear un videojuego"
    "Por eso el trabajo en equipo es importante"
    c "No sabía que era tanto lo que involucraba"
    c "¿Cómo son los desarrolladores de videojuegos?
    "Son creativos y además entienden cosas de tecnología, matemáticas, contar historias y arte"
    "... de repente..."


    return
