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
    
    "De casualidad pasaba por el estudio de desarrollo de videojuegos"
    "Disfrutaba mucho de ver todas las actividades, pero jamás pude haber previsto"
    "Que ese mismo día yo llegaría a aprender algo relacionado a desarrollo de videojuegos"
    
    c "BALEADAS."
    
    c "Ren'Py CORREEEEEALDASLJDLASJDLASJDLSAJDLASJDLSAJDLSAD."
    
    #Este código inserta un video en medio de la novela visual
    $ renpy.movie_cutscene("movie.ogv")



    return
