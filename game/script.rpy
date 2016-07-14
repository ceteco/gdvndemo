# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.
image bg dibujando = "dibujando.png"
# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define c = Character('Carlos', color="#c8ffc8")
define d = Character('Desarrollador', color="ff8000")


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
    
    "Sí -Contestó el guía"
    
    c "Pero qué bestial está"
    c "¿Aquí hacen ese juego ustedes en el estudio?"
    "Así es Carlos"
    c "¿Cómo lo hacen?"
    "Desarrollar un videojuego involucra escribir guiones, programar, gráficos, economía, música y efectos de sonido"
    "Cómo verás son muchos los aspectos de crear un videojuego"
    "Por eso el trabajo en equipo es importante"
    c "No sabía que era tanto lo que involucraba"
    c "¿Cómo son los desarrolladores de videojuegos?"
    "Son creativos y además entienden cosas de tecnología, matemáticas, contar historias y arte"
    "... de repente..."
    scene black with vpunch
    "¡La tierra está temblando! ¡Es un terremoto!"
    scene black with vpunch
    "...tembló un poco más..."
    scene black with vpunch
    "Pero no duró mucho"
    c "¿Se vá a caer el edificio?"
    "Uf ¡Qué susto! No creo que se caiga. -Contestó el guía"
    c "Ajajaja -Dejé escapar una risa algo nerviosa, para fingir que no tenía miedo y todo seguía bien"
    c "Como sé mi poco desarrollar videojuegos no me dan miedo los terremotos"
    "¿ ?"
    "."
    ".."
    "..."
    "Vale, relájate y sigamos con..."
    d "¡Ey! ¿Adonde se fueron María y José?"
    "No lo sé -Contestó el guía"
    d "¡Ellos son quienes saben de gráficos y en este momento necesitamos cambiar los dibujos de la nave en cosa de 30 minutos!"
    "Chale ¿Qué pasó? ¿Se desaparecieron en el temblor?"
    d "¡No sé! ¡Sus escritorios simplemente están vacíos!"
    d "¡No están por ningún lado"
    c "¡Rayos! -Pensé para mí mismo"
    c "Oigan ustedes..."
    
menu:
    "... creo que mejor voy partiendo":
        jump ayudar
    "... ¿Puedo ayudar en algo?":
        jump ayudar
    
label ayudar:
    d "Oye Carlos, hace un rato parecías decir, el saber algo de videojuegos"
    c "Ah pues sí, un poquito"
    d "¿No sucederá que nos puedes ayudar?"
    d "En la computadora está la documentación, pero yo (ni nadie) somos muy buenos con los gráficos"
    d "Se necesita que dibujes una nueva nave en el juego que viste hace poco"
    d "Y la sustituyas dentro del juego"
    d "¿Podrás hacerlo?"
    
menu:
    "... he visto a María haciendo esto algunas veces, lo intentaré":
        jump dibujar
    "Solamente sí me invitan a una Paella para mí sólo":
        jump dibujar
    "¡De volada!":
        jump dibujar
        
label dibujar:
    d "¡Gracias! Por favor comienza dibujando la nave"
    d "Toma esta laptop, tiene instalado todo el software que necesitas"
    c "Copiado. Haré algo rápido ¿Está bien?"
    d "Sí, solamente necesitamos que sea diferente. No preguntes porqué. Tienes 20 minutos."
    c "ok"
    
    scene bg dibujando
    with fade    
    "Y así Carlos se sentó en la computadora y rápidamente dibujó una nave espacial"
    
        


    return
