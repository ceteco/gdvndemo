# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.
image bg dibujando = "dibujando.png"
image bg extra = "folder_extra.png"
image bg exito = "exito.png"
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
    
    scene bg extra
    with fade
    c "¡Excelente! Ya terminé de dibujar la nave espacial y la guardé en el lugar correcto!"
    "Dijo Carlos mientras admiraba su obra"
    c "Pero esto aún no termina ¡Caracoles!"
    c "¿Cómo haré para sustituír la nave espacial que trae el juego por la mía?"
    "Mientras Carlos se preguntaba, se topó con algunas capturas de pantalla de María, en las cuáles explicaba el proceso"
    "Las fué viendo en la computadora"
    "¡AHORA TÚ QUE ESTÁS DEL OTRO LADO DE LA PANTALLA!"
    "Es tu momento de brillar y hacer que el juego cobre vida con el nuevo dibujo de nave espacial de Carlos"
    "Lógralo para pasar al siguiente nivel"
    "Mira bien la nave original que incluye el juego, es un triángulo blanco, ejécutalo en tu computadora para observarlo"
    "Ahora copia de el folder -extra- el archivo spaceship.png"
    "Copialo en el folder anterior, -sprites-. Cuando pregunte sí quieres sobre-escribir responde que sí"
    "Ahora corre de nuevo el juego"
    scene bg extra
    with fade
    d "¡Excelente trabajo Carlos!"
    d "¡Con tu habilidad salvaste el día!"
    c "ajaja, no es para tanto (Sí supiera como me costó)"
    d "No digas tonterías, este trabajo ya nos saca del apuro"
    c "Gracias"
    d "Ven, te invito a una pizza..."
    "Buen final"
    
    
    
    
    
        


    return
