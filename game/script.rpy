# Protagonista
define saviTortu = Character('[prota] [apellido]') # La variable del protagonista es saviTortu porque es una mezcla de las palabras en inglés '{cps=45}Savior' y '{cps=45}Torture', que son dos opciones {/cps}s plausibles para el jugador en el juego

label start:
    scene black
    stop music
    $ prota = renpy.input('Ingresa tu nombre en la aventura', length=32)
    $ prota = prota.strip()
    $ apellido = renpy.input('Ingresa un apellido', length = 32)
    $ apellido = apellido.strip()
    $ edad = ''
    while edad < '20' or not edad:
        $ edad = renpy.input('Ingresa tu edad en el juego (debe ser a partir de los 20 años)', length = 3)
        $ edad = edad.strip()

    if not prota and not apellido and not edad:
        $ prota = 'Jane'
        $ apellido = 'Doe'
        $ edad = '26'
        $ prota = prota.strip()
        $ apellido = apellido.strip()
        $ edad = edad.strip()
        
    'DISCLAIMER' '{cps=50}El contenido presentado puede contener temas relacionados a salud mental, bullying, suicidio, muerte e imágenes parpadeantes.{/cps}'
    'DISCLAIMER' '{cps=50}Se recomienda discreción y dejar de jugar si siente malestar o tiene un episodio de meltdown, epilepsia o similar. Se recomienda no pasar más de dos horas en el juego.{/cps}'

    menu:
        '{cps=50}¿Asumes que es tu responsabilidad lo que pase a partir de este punto?{/cps}'

        'Sí, es mi responsabilidad mantener mi seguridad personal ante este contenido':
            jump cap0
        'Necesito tiempo para pensarlo':
            return

label cap0:
    scene intro with fade
    play music '001.ClearAdventureDay.mp3'
    screen stats():
        if enPasado == True:
            text 'Día [diasPasado] | Pekins senlins: [monedas] | Reputación: [reputacionP]'
        else:
            text 'Pekins senlins: [monedas] | Reputación: [reputacionTra]'

    '{cps=45}Capítulo 0:{/cps} {cps=20}La reunión{/cps}'
    # Presentación de personajes y dinámicas actuales
    show screen stats
    # Cambiar narración a segunda persona en presente
    '{cps=45}8:00AM. Oficina de la policía de Senlín .Senlín Central, distrito de Senlín. 18 de Marzo, año 3046{/cps}'
    '{cps=45}Planeta: Mochu{/cps}'
    $ monedas += 1000
    '{cps=45}Nombre: {b}[prota] [apellido]{/b}{/cps}'
    '{cps=45}Habilidad de nacimiento: {b}{i}Brillo en la oscuridad{/i}{/b}.{/cps}'
    '{cps=45}Eres un agente ingresado a la policía de Senlín, con [edad] años, has logrado ganar la confianza de los tres sectores de la zona de Investigación.{/cps}'
    '{cps=45}Una reunión con los agentes te espera esta mañana.{/cps}'
    scene pasillo with fade
    show amigoAdam with moveinleft
    adam '{cps=45}Buenos días, agente [apellido]. ¿Cómo está para la reunión de hoy?{/cps}'
    hide amigoAdam
    show idleAdam
    '{cps=45}A tu lado, ves a Adam Carter, líder y detective principal del sector 970, uno de los primeros en acogerte en el entorno, aunque no lo conoces mucho.{/cps}'
    menu:
        '{cps=45}¿Cómo saludas?{/cps}'
        'Saludo amistoso, como a un amigo.':
            saviTortu '{cps=45}Buenos días, Adam.{/cps}'
            $ adamFeli +=2
            hide idleAdam
            show felizAdam
            adam '{cps=45}Buenos días, [prota], es un honor trabajar contigo.{/cps}'
            adam '{cps=45}Aunque no hablamos mucho, pareces ser una buena persona{/cps}'
            hide felizAdam
            show observadorAdam
            '{cps=45}Adam revisa brevemente el reloj, queda una hora para la reunión.{/cps}'
            '{cps=45}Una hora que tienes libre.{/cps}'
            hide observadorAdam
            show amigoAdam
            adam '{cps=45}Debo preparar las cosas para la reunión.{/cps}'
            hide amigoAdam
            show felizAdam
            menu:
                adam '{cps=45}¿Nos vemos luego?{/cps}'
                'Estaré allá':
                    hide felizAdam
                    show idleAdam
                    saviTortu '{cps=45}Me aseguraré de estar ahí, detective.{/cps}'
                    $ adamFeli += 1
                    hide idleAdam
                    show felizAdam
                    adam '{cps=45}Estoy seguro de ello.{/cps}'
                    hide felizAdam
                    '{cps=45}Adam se retira rápidamente hacia la sala de reuniones.{/cps}'
                    jump preReunion
                '¿Necesitas ayuda para preparar las cosas?':
                    hide felizAdam
                    show amigoAdam
                    adam '{cps=45}No te preocupes, [apellido]{/cps}'
                    adam '{cps=45}Solo estoy algo cansado, pero no es algo que no pueda manejar.{/cps}'
                    $ adamFeli += 2
                    hide amigoAdam
                    show felizAdam
                    adam '{cps=45}De todas formas, aprecio la preocupación{/cps}'
                    menu:
                        'Confiar en que podrá hacerlo':
                            hide felizAdam
                            show idleAdam
                            saviTortu '{cps=45}Bueno… espero que puedas lograrlo.{/cps}'
                            hide idleAdam
                            show amigoAdam
                            adam '{cps=45}Nos veremos más tarde, [prota].{/cps}'
                            '{cps=45}Ambos se van por su camino en silencio.{/cps}'
                            jump preReunion
                        'Ofrecer compañía':
                            $ reputacionTra += 5
                            hide felizAdam
                            show idleAdam
                            saviTortu '{cps=45}Podría ayudarte con eso, solo si quieres.{/cps}'
                            $ adamFeli += 2
                            hide idleAdam
                            show pensativoAdam
                            adam '{cps=45}¿En serio podrías?{/cps}'
                            hide pensativoAdam
                            show idleAdam
                            saviTortu '{cps=45}Claro, no es problema para mí. Tengo tiempo libre.{/cps}'
                            $ adamFeli += 4
                            hide idleAdam
                            show amigoAdam
                            adam '{cps=45}Claro, algo de compañía no haría mal.{/cps}'
                            adam '{cps=45}Sígueme, [prota].{/cps}'
                            jump ordenUnitario
        'Saludo formal':
            saviTortu '{cps=45}Buenos días, detective Carter{/cps}'
            $ adamFeli +=1
            hide idleAdam
            show felizAdam
            adam '{cps=45}Espero que te estés adaptando a la oficina, [apellido]. Todo va a su paso.{/cps}'
            hide felizAdam
            show amigoAdam
            adam '{cps=45}Quizás sea abrumador al inicio, pero estoy seguro de que puedes afrontarlo.{/cps}'
            adam '{cps=45}Nos veremos en la reunión, colega.{/cps}'
            menu:
                'Estaré allá':
                    hide amigoAdam
                    show idleAdam
                    saviTortu '{cps=45}Me aseguraré de estar ahí, detective.{/cps}'
                    $ adamFeli += 1
                    hide idleAdam
                    show felizAdam
                    adam '{cps=45}Estoy seguro de ello.{/cps}'
                    hide felizAdam
                    '{cps=45}Adam se retira rápidamente hacia la sala de reuniones.{/cps}'
                    jump preReunion
                '¿Necesitas ayuda para preparar las cosas?':
                    adam '{cps=45}No te preocupes, [apellido].{/cps}'
                    adam '{cps=45}Han pasado bastantes cosas, pero no es algo que no pueda manejar.{/cps}'
                    $ adamFeli += 2
                    hide amigoAdam
                    show felizAdam
                    adam '{cps=45}De todas formas, aprecio la preocupación.{/cps}'
                    menu:
                        'Confiar en que podrá hacerlo':
                            hide felizAdam
                            show idleAdam
                            saviTortu '{cps=45}Bueno… espero que puedas lograrlo.{/cps}'
                            adam '{cps=45}Nos veremos más tarde, [prota].{/cps}'
                            '{cps=45}Ambos se van por su camino en silencio.{/cps}'
                            jump preReunion
                        'Ofrecer compañía':
                            hide felizAdam
                            show idleAdam
                            saviTortu '{cps=45}Podría ayudar, tengo la hora libre.{/cps}'
                            $ adamFeli += 3
                            hide idleAdam
                            show amigoAdam
                            adam '{cps=45}Claro, algo de compañía no haría mal.{/cps}'
                            hide amigoAdam
                            show felizAdam
                            adam '{cps=45}Sígueme, [apellido].{/cps}'
                            jump ordenUnitario
    label preReunion:
        scene intro with dissolve
        '{cps=45}{b}{i}Una hora después…{/i}{/b}{/cps}'
        scene reunion with fade
        show idleAdam
        '{cps=45}Cuando entras a la reunión, ves a Adam terminando de ordenar la sala. Ves la sala limpia y ordenada, y sientes un aroma a panqueques y rollos de canela.{/cps}'
        hide idleAdam
        show felizAdam
        adam '{cps=45}Saludos, [apellido].{/cps}'
        menu:
            adam '{cps=45}Espera un poco ahí, ¿vale? El teniente va a llegar en breve.{/cps}'
            'Entendido':
                adam '{cps=45}Si alguien más aparece, los dejo entrar a ambos.{/cps}'
                pause(1.0)
                adam'{cps=45}Me sorprende haber terminado esto.{/cps}'
            '¿Arreglaste todo tú solo?':
                hide felizAdam
                show amigoAdam
                adam '{cps=45}Sí, todavía me sorprende haberlo logrado.{/cps}'
                hide amigoAdam
                show pensativoAdam
        menu:
            adam '{cps=45}Y me alcanzó tiempo para cocinar un poco.{/cps}'
            'Eso suena como un buen logro':
                $ adamFeli += 2
                hide pensativoAdam
                show felizAdam
                adam '{cps=45}Gracias, [apellido].{/cps}'
                adam '{cps=45}Aunque no es un logro como tal, me gusta considerarlo como tal.{/cps}'
            'Pero es una reunión, no tenías que hacer comida.':
                hide pensativoAdam
                show felizAdam
                adam '{cps=45}Buena pregunta, [apellido].{/cps}'
                hide felizAdam
                show amigoAdam
                adam '{cps=45}Para este tipo de reuniones, el teniente me da dado el permiso de preparar algo para aliviar el estrés una vez terminada la reunión.{/cps}'
                adam '{cps=45}Además, cocinar es terapéutico para mí, es divertido y puedo ir variando lo que hago.{/cps}'
                hide amigoAdam
                show observadorAdam
                pause(1.0)
                hide observadorAdam
                show pensativoAdam
                adam '{cps=45}…Eso no fue mucho detalle, ¿verdad?{/cps}'
                hide pensativoAdam
                show observadorAdam
                menu:
                    'No te preocupes, ahora entiendo más.':
                        $ adamFeli +=3
                        hide observadorAdam
                        show felizAdam
                        adam '{cps=45}Gracias, [apellido].{/cps}'
                        adam '{cps=45}Me alegra no estar alargando una explicación.{/cps}'
                        hide felizAdam
                        show amigoAdam
                        adam '{cps=45}Es que… normalmente no hablo tanto de mí mismo.{/cps}'
                    'Creo que explicaste demasiado':
                        $ adamFeli -=1
                        hide observadorAdam
                        show pensativoAdam
                        adam '{cps=45}Siento mucho haberme alargado.{/cps}'
                        hide pensativoAdam
                        show amigoAdam
                        adam '{cps=45}De todas formas, gracias por el comentario.{/cps}'
                adam '{cps=45}Como decía, esperemos al resto.{/cps}'
                menu:
                    'Parece que has cocinado algo bueno.':
                        $ adamFeli += 2
                        hide amigoAdam
                        show felizAdam
                        adam '{cps=45}Espero que te guste.{/cps}'
                        adam '{cps=45}Aunque es para después de la reunión, así que tienes que tener paciencia.{/cps}'
                        hide felizAdam
                        show idleAdam at right
                        brayan '{cps=45}Disculpa la demora, Adam.{/cps}'
                        '{cps=45}Ante ustedes, ves a {b}Brayan Orellana{/b}, agente especializado en misiones encubiertas del sector 970.{/cps}'
                        brayan '{cps=45}¿Te acaba de ayudar el nuevo?{/cps}'
                        hide idleAdam
                        show amigoAdam at right
                        adam '{cps=45}En realidad, [prota] acaba de llegar{/cps}'
                        hide amigoAdam
                        show idleAdam at right
                        brayan '{cps=45}Ah.{/cps}'
                        brayan '{cps=45}Eso es genial, supongo.{/cps}'
                        brayan '{cps=45}Entonces… [saviTortu], ¿no?{/cps}'
                        menu:
                            'Sí, soy yo.':
                                hide idleAdam
                                show amigoAdam at right
                                adam '{cps=45}[apellido], te presento al agente Orellana, experto en misiones encubiertas del sector 970.{/cps}'
                                adam '{cps=45}Brayan. creo que ya has escuchado de [prota], es de nuestros agentes recién graduados de… la escuela de criminalística.{/cps}'
                                brayan '{cps=45}Oh…{/cps}'
                                hide amigoAdam
                                show observadorAdam at right
                                '{cps=45}Notas una ligera tensión entre ambos agentes al mencionar la escuela de criminalística.{/cps}'
                                hide observadorAdam
                                show amigoAdam
                                adam '{cps=45}Bueno, como decía…{/cps}'
                                hide amigoAdam
                                show pensativoAdam
                                adam '{cps=45}Brayan, ya que estás aquí, ¿me puedes ayudar a ordenar la mesa?{/cps}'
                                adam '{cps=45}Tengo que prepararme para recibir al resto.{/cps}'
                                brayan '{cps=45}Claro que puedo.{/cps}'
                                hide amigoAdam
                                '{cps=45}Adam sale de la sala, observando en la puerta a la espera de los agentes.{/cps}'
                                '{cps=45}Mientras tanto,Brayan ordenaba la mesa, había un silencio incómodo entre ambos.{/cps}'
                                saviTortu '{cps=45}…{/cps}'
                                brayan '{cps=45}…{/cps}'
                                show pensativoAdam at left
                                adam '{cps=45}Disculpen…{/cps}'
                                adam '{cps=45}¿Está… todo bien?{/cps}'
                                hide pensativoAdam
                                show observadorAdam at left
                                brayan '{cps=45}No te preocupes, Carter.{/cps}'
                                brayan '{cps=45}Solo estoy ordenamos mientras [apellido] mira.{/cps}'
                                hide observadorAdam
                                show pensativoAdam at left
                                adam '{cps=45}Es raro que no hables, Orellana.{/cps}'
                                hide pensativoAdam
                                show observadorAdam at left
                                brayan '{cps=45}Estoy concentrado con la mesa.{/cps}'
                                hide observadorAdam
                                show amigoAdam at left
                                adam '{cps=45}Vale, vale.{/cps}'
                                hide amigoAdam
                                show felizAdam at left
                                menu:
                                    adam '{cps=45}¿Qué hay de ti, [prota]?{/cps}'
                                    'Yo suelo estar en silencio, detective':
                                        hide felizAdam
                                        show pensativoAdam at left
                                        adam '{cps=45}Comprendo.{/cps}'
                                        adam '{cps=45}Yo también era así a tu edad.{/cps}'
                                    'Estoy concentrado en algo':
                                        hide felizAdam
                                        show observadorAdam at left
                                        brayan '{cps=45}Somos dos, [apellido].{/cps}'
                                        brayan '{cps=45}Tranquilo, jefe, nadie se va a morir por no hablar{/cps}'
                                        saviTortu '{cps=45}...{/cps}'
                                        brayan '{cps=45}...{/cps}'
                                        adam '{cps=45}...{/cps}'
                jump reunion

    label ordenUnitario:
        scene reunion with fade
        '{cps=45}Adam y tú llegan a la sala de reuniones, la cual estaba presentable, pero no lo estaba para la reunión.{/cps}'
        show felizAdam with fade
        adam '{cps=45}Bien, [apellido], vamos a repartir los trabajos.{/cps}'
        menu:
            adam '{cps=45}¿Puedes limpiar la pizarra mientras preparo el desayuno?{/cps}'
            'Vale, yo veo la pizarra':
                hide felizAdam
                show amigoAdam
                adam '{cps=45}¡Genial! Creo que traje mis cosas para cocinar.{/cps}'
                hide amigoAdam
                show felizAdam
                adam '{cps=45}En la mesa tienes para limpiarlos.{/cps}'
            'Pero es una reunión, no tienes que hacer desayuno.':
                hide felizAdam
                show amigoAdam
                adam '{cps=45}Ese es un buen punto que olvidé explicar antes.{/cps}'
                hide amigoAdam
                show felizAdam
                adam '{cps=45}Para este tipo de reuniones, el teniente me da dado el permiso de preparar algo para… aliviar el estrés una vez terminada la reunión.{/cps}'
                adam '{cps=45}Además, cocinar es terapéutico para mí, es divertido y puedo ir variando lo que hago.{/cps}'
                hide amigoAdam
                show observadorAdam
                pause(1.0)
                hide observadorAdam
                show pensativoAdam
                adam '{cps=45}…Eso no fue mucho detalle, ¿verdad?{/cps}'
                hide pensativoAdam
                show observadorAdam
                menu:
                    'No te preocupes, ahora entiendo más.':
                        $ adamFeli +=3
                        hide observadorAdam
                        show felizAdam
                        adam '{cps=45}Gracias, [apellido].{/cps}'
                        adam '{cps=45}Me alegra no estar alargando una explicación.{/cps}'
                        hide felizAdam
                        show amigoAdam
                        adam '{cps=45}Es que… normalmente no hablo tanto de mí mismo.{/cps}'
                        jump OUR_PreReunion
                    'Creo que explicaste demasiado':
                        $ adamFeli -=1
                        hide observadorAdam
                        show pensativoAdam
                        adam '{cps=45}Siento mucho haberme alargado.{/cps}'
                        hide pensativoAdam
                        show amigoAdam
                        adam '{cps=45}De todas formas, gracias por el comentario.{/cps}'
                        adam '{cps=45}Como decía, sigamos con la {s}misión-{/s} digo, con la limpieza.{/cps}'
                        jump OUR_PreReunion
                    'Si quieres, puedes hablar mientras ordenamos':
                        $ adamFeli +=2
                        hide observadorAdam
                        show pensativoAdam
                        adam '{cps=45}¿No te molesta?{/cps}'
                        hide pensativoAdam
                        show observadorAdam
                        saviTortu '{cps=45}No, no me molesta.{/cps}'
                        $ adamFeli +=2
                        $ reputacionTra +=10
                        hide observadorAdam
                        show felizAdam
                        adam '{cps=45}Bien, aprovecha de limpiar la pizarra y yo cocinaré un poco.{/cps}'
                        adam '{cps=45}Y quizás te hable un poco de lo que estaré cocinando.{/cps}'
                        adam '{cps=45}En la mesa están las cosas para limpiar.{/cps}'
                        hide observadorAdam  
                        show idleAdam
                        '{cps=45}Por un largo rato, ambos trabajaron juntos. Adam estuvo cocinando y preparando el material mientras tú le ayudabas a limpiar la sala.{/cps}'
                        jump OUR_PreReunion
    label OUR_PreReunion:
        '{cps=45}{b}{i}47 minutos después…{/i}{/b}{/cps}'
        '{cps=45}Finalmente el lugar finalmente estaba ordenado, y Adam ya tenía el desayuno listo.{/cps}'
        show amigoAdam with fade
        adam '{cps=45}Finalmente hemos terminado.{/cps}'
        hide amigoAdam
        show felizAdam
        adam '{cps=45}Debo decir que sabes ordenar bastante bien.{/cps}'
        menu:
            'Gracias.':
                adam '{cps=45}Bien, ahora tenemos que esperar a los demás.{/cps}'
            'Parece que has cocinado algo bueno.':
                $ adamFeli += 2
                adam '{cps=45}Gracias, [prota].{/cps}'
                adam '{cps=45}Espero que te guste.{/cps}'
                adam '{cps=45}Aunque es para después de la reunión, así que tienes que tener paciencia.{/cps}'
        brayan '{cps=45}Disculpa la demora, Adam.{/cps}'
        '{cps=45}Ante ustedes, ves a {b}Brayan Orellana{/b}, agente especializado en misiones encubiertas del sector 970.{/cps}'
        brayan '{cps=45}¿Te acaba de ayudar el nuevo?{/cps}'
        adam '{cps=45}Yo lo veo aquí, ¿tú no?{/cps}'
        brayan '{cps=45}No me hables así, {i}\'Pichón\'{/i}, recuerda que soy mayor que tú.{/cps}'
        adam '{cps=45}Y yo soy el líder del 970.{/cps}'
        brayan '{cps=45}…Buen punto, Carter.{/cps}'
        adam '{cps=45}Pero sí, [prota] me ayudó a ordenar.{/cps}'
        brayan '{cps=45}Eso es genial.{/cps}'
        $ reputacionTra += 10
        brayan '{cps=45}Entonces… [saviTortu], ¿no?{/cps}'
        menu:
            'Sí, soy yo.':
                adam '{cps=45}[apellido], te presento al agente Orellana, experto en misiones encubiertas del sector 970.{/cps}'
                adam '{cps=45}Brayan. creo que ya has escuchado de [prota], es de nuestros agentes recién graduados de… la escuela de criminalística.{/cps}'
                brayan '{cps=45}Oh…{/cps}'
                '{cps=45}Notas una ligera tensión entre ambos agentes al mencionar la escuela de criminalística.{/cps}'
                adam '{cps=45}Bueno, como decía…{/cps}'
                adam '{cps=45}Brayan, ya que estás aquí, ¿puedes ayudar a [apellido] a ordenar la mesa?{/cps}'
                adam '{cps=45}Tengo que prepararme para recibir al resto.{/cps}'
                brayan '{cps=45}Claro que puedo.{/cps}'
                '{cps=45}Adam sale de la sala, observando en la puerta a la espera de los agentes.{/cps}'
                '{cps=45}Mientras tanto, tú y Brayan ordenaban la mesa, había un silencio incómodo entre ambos.{/cps}'
                saviTortu '{cps=45}…{/cps}'
                brayan '{cps=45}…{/cps}'
                adam '{cps=45}Disculpen…{/cps}'
                adam '{cps=45}¿Está… todo bien?{/cps}'
                brayan '{cps=45}No te preocupes, Carter.{/cps}'
                brayan '{cps=45}Solo estamos ordenamos con [apellido].{/cps}'
                adam '{cps=45}Es raro que no hables, Orellana.{/cps}'
                brayan '{cps=45}Estoy concentrado con la mesa.{/cps}'
                adam '{cps=45}Vale, vale.{/cps}'
                menu:
                    adam '{cps=45}¿Qué hay de ti, [prota]?{/cps}'

                    'Yo suelo estar en silencio, detective':
                        adam '{cps=45}Comprendo.{/cps}'
                        adam '{cps=45}Yo también era así a tu edad.{/cps}'
                    'También estoy concentrado':      
                        brayan '{cps=45}Somos dos, [apellido].{/cps}'
                        brayan '{cps=45}Tranquilo, jefe, nadie se va a morir por no hablar{/cps}'
                        saviTortu '{cps=45}...{/cps}'
                        brayan '{cps=45}...{/cps}'
                        adam '{cps=45}...{/cps}'
                        jump reunion
    label reunion:
        adam '{cps=45}Estoy vigilando la entrada, en caso de que el teniente pregunte.{/cps}'
        brayan '{cps=45}Como usted diga, jefe.{/cps}'
        gavya '{cps=45}Buenos días, ¿se puede entrar?{/cps}'
        '{cps=45}En la puerta, ven a {b}Gavya Meraki {/b}, encargada del relaciones exteriores del sector 1 (liderado por el agente {b}Orfeo Galloway{/b}).{/cps}'
        adam '{cps=45}Claro, pase, agente Meraki.{/cps}'
        gavya '{cps=45}¿Por qué me tratas así, Adam?{/cps}'
        gavya '{cps=45}Recuerda que nos conocemos desde la escuela.{/cps}'
        adam '{cps=45}Lo sé, Gavya…{/cps}'
        gavya '{cps=45}Saludos, Brayan.{/cps}'
        brayan '{cps=45}Hola, Gavya.{/cps}'
        brayan '{cps=45}¿Te toca venir en representación de Orfeo?{/cps}'
        gavya '{cps=45}Algo así.{/cps}'
        gavya '{cps=45}Anda en una misión con Eleanor en una colonia ilegal en Munho.{/cps}'
        adam '{cps=45}¿New Sydney?{/cps}'
        gavya '{cps=45}Esa misma, están investigando a la fábrica donde Palmer estuvo antes.{/cps}'
        gavya '{cps=45}Y tú…{/cps}'
        gavya '{cps=45}Debes ser [prota], ¿no?{/cps}'
        saviTortu '{cps=45}Sí, soy [saviTortu].{/cps}'
        $ reputacionTra +=10
        adam '{cps=45}Viene en nombre del sector 42.{/cps}'
        brayan '{cps=45}¿Cómo sabes eso?{/cps}'
        adam '{cps=45}Maryam me dijo. los demás están en algún caso o misión, que [apellido] fuera representante fue la mejor opción.{/cps}'
        gavya '{cps=45}¿Y Brayan?{/cps}'
        adam '{cps=45}En caso de que le pase algo a [apellido] que lo haga retirarse, uno de los dos representa al sector 42 y el otro se mantiene en nombre del sector 970.{/cps}'
        brayan '{cps=45}Tenemos asistencia casi completa desde nuestro sector, Adam.{/cps}'
        adam '{cps=45}Ciertamente, Brayan, porque estaremos Melissa, tú y yo.{/cps}'
        gavya '{cps=45}¿La agente Campbell en medio de una mision digital y el agente Rojas en una explosión?{/cps}'
        adam '{cps=45}Casi, porque Rojas está en una misión secreta con tus compañeros, Gavya.{/cps}'
        gavya '{cps=45}Creo que he escuchado de aquella misión.{/cps}'
        '{cps=45}En ese momento, aparece la agente {b}Melissa Torres{/b}, detective y agente del sector 970.{/cps}'
        melissa '{cps=45}¿Siguen esperando al Teniente?{/cps}'
        adam '{cps=45}¡Melissa! Que bueno que llegaste.{/cps}'
        adam '{cps=45}Antes que nada, te presento a…{/cps}'
        melissa '{cps=45}Ya leí el informe, Carter.{/cps}'
        melissa '{cps=45}[saviTortu], [edad] años, recién ingresado con habilidades de bioluminiscencia en entornos oscuros… ¿Ese?{/cps}'
        adam '{cps=45}Exacto…{/cps}'
        adam '{cps=45}Es representante del sector 42 por falta de personal.{/cps}'
        '{cps=45}Melissa hizo una mirada rápida a los presentes, entonces suspiró.{/cps}'
        melissa '{cps=45}Finalmente una reunión más calmada, al parecer.{/cps}'
        saviTortu '{cps=45}¿Las reuniones son caóticas aquí?{/cps}'
        melissa '{cps=45}Algo así.{/cps}'
        melissa '{cps=45}Cuando hay muchas personas en una reunión es difícil llegar a un acuerdo general.{/cps}'
        adam '{cps=45}Cuando piensas que está todo acordado, alguien cuestona de inmediato.{/cps}'
        brayan '{cps=45}Por suerte no hay peleas en esos momentos.{/cps}'
        brayan '{cps=45}Sería un desastre mágico.{/cps}'
        gavya '{cps=45}No creo que lleguemos a pelear, el Teniente no nos permitiría eso.{/cps}'
        adam '{cps=45}Eso es cierto, mejor evitemos las peleas.{/cps}'
        gavya '{cps=45}Entonces… ¿Dónde está el Teniente, detective?{/cps}'
        adam '{cps=45}¿Por qué la pregunta?{/cps}'
        gavya '{cps=45}Ya sabes la respuesta, Carter.{/cps}'
        adam '{cps=45}No tengo idea.{/cps}'
        melissa '{cps=45}Meraki, déjalo. El detective no sabe.{/cps}'
        adam '{cps=45}Además, el Teniente suele llegar a la hora exacta, y eso lo sabes.{/cps}'
        '{cps=45}El reloj suena, ya van a ser las 9AM.{/cps}'
        '{cps=45}Entonces escuchan pasos.{/cps}'
        adam '{cps=45}{i}{b}*Murmurando*{/b} Les dije que vendría justo a tiempo.{/i}{/cps}'
        erin '{cps=45}Buenos días, agentes.{/cps}'
        '{cps=45}Ante ustedes, se encontraba el Teniente Erin Miller, encargado de monitorear el sector de Investigación.{/cps}'
        'Unísono' '{cps=45}Buenos días, Teniente Miller.{/cps}'
        erin '{cps=45}Como habrán notado, en esta ocasión seremos menos de lo habitual.{/cps}'
        erin '{cps=45}Además de que contaremos con la presencia de nuestro agente en práctica, [saviTortu].{/cps}'
        erin '{cps=45}Entonces, con eso mencionado, vamos a empezar con la reunión.{/cps}'
        erin '{cps=45}Tenemos un caso.{/cps}'
        melissa '{cps=45}¿Tan rápido tenemos un caso? Recién llego [apellido] hace una semana desde el último caso.{/cps}'
        erin '{cps=45}Así es.{/cps}'
        erin '{cps=45}Recientemente algunos de los agentes ausentes enviaron la noticia de que habían descubierto un laboratorio ilegal cuyo objetivo sigue siendo desconocido.{/cps}'
        erin '{cps=45}Pero eso no hace que sea algo bueno.{/cps}'
        adam '{cps=45}Algunos informantes dicen que estarían trabajando en una… maquina del tiempo.{/cps}'
        menu:
            '¿Máquina del tiempo?':
                adam '{cps=45}Así es, [prota].{/cps}'
                adam '{cps=45}Tenemos un caso de máquina del tiempo.{/cps}'
            '¿La simple existencia y uso de la máquina no causaría una paradoja del tiempo?':
                adam '{cps=45}Sí, lo haría.{/cps}'
                adam '{cps=45}Sin embargo, la teoría del tiempo mochibria dice que es probable que en el proceso del viaje se esté creando una rama alterna para no afectar tu rama actual.{/cps}'
                brayan '{cps=45}En resumen, no se crea una paradoja.{/cps}'
                saviTortu '{cps=45}Entiendo, supongo.{/cps}' # Aquí quedé antes
        erin '{cps=45}El agente Orellana anoche logró rastrear la ubicación en las afueras de la ciudad.{/cps}'
        erin '{cps=45}Su misión será ir al laboratorio, destruir la máquina y traer a los que estén detrás de esto.{/cps}'
        erin '{cps=45}¿Puedo contar con ustedes?{/cps}'
        adam '{cps=45}Cuente conmigo como siempre, jefe.{/cps}'
        brayan '{cps=45}Estoy disponible para todo, cuénteme ahí.{/cps}'
        melissa '{cps=45}Afirmativo, Teniente.{/cps}'
        gavya '{cps=45}No soy mucho del trabajo en terreno, pero supongo que acepto la misión.{/cps}'
        menu:
            adam '{cps=45}¿Te unes, [apellido]?{/cps}'
            'Aceptar misión':
                $ reputacionTra += 10
                saviTortu '{cps=45}Cuenten conmigo.{/cps}'
                jump aceptar
            "Rechazar":
                saviTortu '{cps=45}No gracias, prefiero no asistir.{/cps}'
                $ rechazoDes += 1
                scene room_glitched2
                pause(0.2)
                scene reunion
                adam '{cps=45}¿Estás seguro?{/cps}'
                adam '{cps=45}A veces aprender en terreno es necesario.{/cps}'
                adam '{cps=45}Si pasa algo, estaremos ahí para asistiirte{/cps}'
                gavya '{cps=45}Considerando las implicaciones de esta misión, vamos a necesitar refuerzos probablemente, así que probablemente te llamemos mañana de ser necesario.{/cps}'
                menu:
                    'Asistir':
                        $ reputacionTra += 5
                        saviTortu '{cps=45}Pensándolo mejor, podría ir con ustedes.{/cps}'
                        jump aceptar
                    "Rechazar":
                        $ rechazoDes += 1
                        scene room_glitched3
                        pause(0.1)
                        scene room_glitched2
                        pause(0.07)
                        scene reunion
                        saviTortu '{cps=45}En ese caso, quizás vaya, pero por hoy paso.{/cps}'
                        adam '{cps=45}No te preocupes, [prota].{/cps}'
                        adam '{cps=45}De todas formas, necesitamos que estés atento si llegamos a necesitar ayuda.{/cps}'
                        '{cps=45}Asientes ante las palabras del detective.{/cps}'
                        pause(1.0)
                        '{cps=45}Hay un leve silencio incómodo, el cual se rompe cuando el teniente vuelve a tomar la palabra.{/cps}'
                        erin '{cps=45}¿Tienen algo que decir?{/cps}'
                        menu:
                            'No tengo nada que decir':
                                '{cps=45}Ante tu respuesta, Adam te mira con confianza a pesar de todo.{/cps}'
                                adam '{cps=45}Puedes decirnos cualquier cosa si lo necesitas.{/cps}'
                                saviTortu '{cps=45}…Gracias.{/cps}'
                        erin '{cps=45}¿…Alguien quiere decir algo más?{/cps}'
                        adam '{cps=45}Por mi parte, no hay nada.{/cps}'
                        melissa '{cps=45}No tengo nada que comentar.{/cps}'
                        brayan '{cps=45}Nada.{/cps}'
                        gavya '{cps=45}Hasta ahora, nada.{/cps}'
                        erin '{cps=45}Sin más que decir, pueden retirarse a sus turnos.{/cps}'
                        erin '{cps=45}Cuando terminen, directo a descansar.{/cps}'
                        'Al unísono' '{cps=45}Entendido.{/cps}'
                        jump desayuno
                    
    label aceptar:
        erin '{cps=45}Bien. Para mañana todos deben estar en las cordenadas que el detective Carter les va a mandar a sus comunicadores.{/cps}'
        erin '{cps=45}¿Tienen algo que decir?{/cps}'
        menu:
            'No tengo nada que decir':
                '{cps=45}Ante tu respuesta, Adam te mira con confianza.{/cps}'
                adam '{cps=45}Puedes decirnos cualquier cosa si lo necesitas.{/cps}'
                saviTortu '{cps=45}…Gracias.{/cps}'
            '¿Por qué me necesitan, exactamente?':
                erin '{cps=45}Hicimos cálculos con Adam y Wisteria anoche.{/cps}'
                adam '{cps=45}Para esta misión hubiera sido idea tener a todos por la cantidad de personas que habrán y por el peligro que conlleva.{/cps}'
                erin '{cps=45}Así que tu presencia será necesaria para nosotros.{/cps}'
                adam '{cps=45}No te preocupes, [prota], nosotros te protegeremos.{/cps}'
                adam '{cps=45}Por mi parte, mi prioridad será asegurar tu integridad.{/cps}'
        erin '{cps=45}¿…Alguien quiere decir algo más?{/cps}'
        adam '{cps=45}Por mi parte, no hay nada.{/cps}'
        melissa '{cps=45}No tengo nada que comentar.{/cps}'
        brayan '{cps=45}Nada.{/cps}'
        gavya '{cps=45}Hasta ahora, nada.{/cps}'
        erin '{cps=45}Sin más que decir, pueden retirarse a sus turnos.{/cps}'
        erin '{cps=45}Cuando terminen, directo a descansar.{/cps}'
        'Al unísono' '{cps=45}Entendido.{/cps}'
        jump desayuno

    label desayuno:
        adam '{cps=45}Antes de irse, ¿alguien quiere comer algo de desayuno?{/cps}'
        adam '{cps=45}Cociné algunas cosas para esta reunión.{/cps}'
        gavya '{cps=45}Adam, eres un sol.{/cps}'
        brayan '{cps=45}Nunca está de más algo de comer, ¡gracias, Adam!{/cps}'
        melissa '{cps=45}Supongo que no tengo problema.{/cps}'
        $ adamFeli += 10
        'Adam voltea a verte mientras ordena la mesa para desayunar.'
        menu:
            adam '{cps=45}¿Quieres comer algo? No temas de sacar cosas.{/cps}'
            'Sí, por favor.':
                $ reputacionTra += 5
                $ adamFeli += 10
            'No te preocupes, no tengo hambre.':
                adam '{cps=45}Entiendo.{/cps}'
                adam '{cps=45}Te voy a guardar algo para más tarde si llegas a tener hambre.{/cps}'
        'Después de comer un poco, todos se retiran mientras Adam y el teniente ordenan la mesa.'
        if(rechazoDes < 2):
            jump tarde
        else:
            jump tardeRechazo
    label tarde:
        stop music
        play music '006.Strings.mp3'
        scene introTarde with fade
        '{cps=45}Después de un rato, el día se vuelve tarde.{/cps}'
        
        scene paraderoTarde with dissolve
        'Sales de la oficina, mirando hacia el paradero para ir a casa hasta que ves a Adam saliendo.'
        adam '{cps=45}Hiciste un buen trabajo hoy, [prota].{/cps}'
        adam '{cps=45}Sé que hoy fue principalmente trabajo de oficina, pero normalmente solemos tener trabajos más arriesgados.{/cps}'
        adam '{cps=45}De hecho, creo que en muchas misiones pude haber muerto, pero seguimos vivos gracias a la Equilibria.{/cps}'
        adam '{cps=45}Eso, o el universo no quiere que me muera todavía.{/cps}'
        menu:
            '¿Crees que podré con la misión?':
                adam '{cps=45}Definitivamente podrás con eso.{/cps}'
                'Antes de responder, Adam mira el cielo un momento y suspira.'
                adam '{cps=45}Cuando era más joven y recién era ingresado a la policía como tú, también pensé lo mismo en mi primera misión en terreno.{/cps}'
                adam '{cps=45}Me tomó un largo tiempo tener confianza en mí mismo y llegar a se lo que soy ahora.{/cps}'
                adam '{cps=45}Eres fuerte, [apellido], más de lo que crees.{/cps}'
            'No sé qué suena más triste':
                adam '{cps=45}Prefiero no pensar en lo triste, no es divertido jugar con la suerte o el destino.{/cps}'
                adam '{cps=45}Mírame a mí, yo me alejé de mi destino y no sé cómo sigo vivo.{/cps}'
        '{cps=45}Cuando miras, tu bus llega.{/cps}'
        adam '{cps=45}Ese es tu transporte, ¿no?{/cps}'
        menu:
            'Sí, aquí me voy':
                adam '{cps=45}Vale.{/cps}'
                saviTortu '{cps=45}¿No te vas?{/cps}'
        menu:
            adam '{cps=45}No te preocupes, yo suelo irme caminando, mi casa no queda tan lejos.{/cps}'
            'Preguntar':
                saviTortu '{cps=45}¿No tienes a… alguien que te espere en casa?{/cps}'
                adam '{cps=45}¿Ah?{/cps}'
                saviTortu '{cps=45}Bueno, yo vivo en mi propia casa por decisión propia.{/cps}'
                saviTortu '{cps=45}Pero no pareces el tipo de persona que viviría solo.{/cps}'
                saviTortu '{cps=45}¿No tienes un familiar, o una macosta o algo así?{/cps}'
                adam '{cps=45}La verdad es que…{/cps}'
                adam '{cps=45}...{/cps}'
                saviTortu '{cps=45}No tienes que responder si no quieres.{/cps}'
                adam '{cps=45}La verdad es que no vivo con nadie, solo estamos el cetro y yo.{/cps}'
                saviTortu '{cps=45}…{/cps}'
                adam '{cps=45}…{/cps}'
            'Irse':
                saviTortu '{cps=45}Entiendo.{/cps}'
                saviTortu '{cps=45}Yo… ya me voy{/cps}'
        adam '{cps=45}Aprovecha de subirte al bus antes de que se vaya.{/cps}'
        saviTortu '{cps=45}Tienes razón{/cps}'
        '{cps=45}Subes al bus y ves la oficina alejarse mientras vas a casa a descansar para un nuevo día, y una nueva misión.{/cps}'
        saviTortu '{cps=45}{i}Hoy fue un buen día{/i}{/cps}'
        return
    label tardeRechazo:
        stop music
        play music '002.AdmadisFall.mp3' fadein 0.5 fadeout 0.1
        scene introTarde with fade
        '{cps=45}Después de horas, el día se vuelve tarde y luego se vuelve noche. Regresas rápidamente a casa para descansar un poco.{/cps}'
        '{cps=45}Entras rápidamente a tu cuarto para dormir.{/cps}'
        scene yourRoom with pixellate
        saviTortu '{cps=45}Finalmente en casa…{/cps}'
        '{cps=45}A pesar de estar en un entorno seguro, sientes algo raro.{/cps}'
        pause(1.0)
        stop music
        scene room_glitched1
        pause(0.5)
        scene yourRoom
        menu optional_name:
            '¿Qué fue eso?':
                scene room_glitched2
                pause(0.2)
                scene room_glitched2
                pause(0.1)
                scene yourRoom
                '{cps=45}Por un momento, sientes que todo vuelve a la normalidad.{/cps}'
                pause(2.0)
                scene room_glitched3
                pause(0.16)
                scene room_glitched2
                pause(0.14)
                scene room_glitched4
                pause(0.1)
                scene yourRoom
                saviTortu '{cps=45}Esto… esto no es normal…{/cps}'
                menu:
                    '{cps=45}Cuando revisas tus bolsillos, logras encontrar tu teléfono, es un buen momento para llamar ayuda.{/cps}'
                    '{cps=45}Llamar ayuda{/cps}':
                        scene room_glitched3
                        pause(0.05)
                        scene yourRoom
                        $ reputacionTra +=1
                        '{cps=45}Antes de poder hacer una llamada a la oficina, un cambio del entorno te hace soltar el teléfono.{/cps}'
                    '{cps=45}Esperar{/cps}':
                        '{cps=45}Te mantienes en tu posición, esperando a que se termine todo por sí solo.{/cps}'
                scene room_glitched3
                pause(0.16)
                scene room_glitched4
                pause(0.1)
                scene room_glitched5
                pause(0.12)
                scene room_glitched2
                pause(0.1)
                scene room_glitched1
                pause(0.14)
                scene room_glitched5
                pause(0.2)
                scene yourRoom
                '{cps=45}Sueltas un suspiro una vez sientes que todo volvió a la normalidad.{/cps}'
                scene black with dissolve
                '{cps=45}Te acuestas y apagas la luz para dormir, pero no puedes hacerlo sin sentir un pitido que te despierta.{/cps}'
                '{cps=45}Al final, no puedes descansar correctamente.{/cps}'
                '{cps=45}{i}Y quizás ese sea tu error.{/i}{/cps}'
    return # Con esto alcanza para la muestra
        
    # if rechazoDes = 3:
    #     jump cap1
    # else:
    #     jump altEmer
    
# label cap1:
#     '{cps=45}Capítulo 1:{/cps} {cps=20}La misión del reloj roto{/cps}'
#     # Desencadenante del conclicto, introducción de Lydia
#     '{cps=45}10:54AM. Laboratorios Chiraska. Senlín Central, distrito de Senlín. 18 de Marzo, año 3046{/cps}'
#     '{cps=45}llegas a tiempo a las afueras de un callejón.{/cps}'
#     saviTortu '{cps=45}Esto se supone que es el \'laboratorio\'…{/cps}'
#     adam '{cps=45}No lo digas tan alto o pueden oirte.{/cps}'
#     label altEmer:
#         '{cps=45}Capítulo 1:{/cps} {cps=20}La misión del reloj roto{/cps}'
#         '{cps=45}10:54AM. Casa de [saviTortu]. Senlín Central, distrito de Senlín. 18 de Marzo, año 3046{/cps}'
#         if(rechazoDes >= 3):
#             jump finalMaloSecuela
#         else:
#             'Rápidamente estás en las afueras de los laboratorios.'

#     hide screen stats
#     $ enPasado = True

# label cap2:
#     show screen stats
#     '{cps=45}Capítulo 2:{/cps} {cps=20}Aviones del pasado{/cps}'
#     # Conflicto, reintroducción de personajes en su forma pasada y sus dinámicas anteriores
#     '{cps=45}10:54AM. Escuela de criminalística. Senlín Central, distrito de Senlín. 18 de Marzo, año 3026{/cps}'
#     return

# label cap3: # Para la 2.0
#     '{cps=45}Capítulo 3:{/cps} {cps=20}Desastre a contrarreloj{/cps}'
#     # Aquí vemos la perpectiva de los personajes del presente, donde averiguan cómo traer al jugador de vuelta.

# label cap4: # Para la 3.0
#     '{cps=45}Capítulo 4:{/cps} {cps=20}La fiesta de la tortura{/cps}'
#     # Desarrollo de las dínamicas de la clase, vistazo a la soledad de Adam

# label cap5: # Para la 4.0
#     '{cps=45}Capítulo 5:{/cps} {cps=20}El descarrilado{/cps}'
#     # Desarrollo de Brayan

# label cap6:
#     '{cps=45}Capítulo 6:{/cps} {cps=20}La flautista del mazo{/cps}'
#     # Desarrollo de Gavya

# label cap7:
#     '{cps=45}Capítulo 7:{/cps} {cps=20}La heroína perdida y el admadis que no vuela{/cps}'
#     # Desarrollo de Adam y Maryam

# label cap8:
#     '{cps=45}Capítulo 8:{/cps} {cps=20}Competencia de compasión{/cps}'
#     # ???

# label cap9:
#     '{cps=45}Capítulo 9:{/cps} {cps=20}Ser el sol de la luna{/cps}'
#     # Aquí el jugador entiende que no puede cambiar el pasado de su línea original y que hizo una línea alternativa, pero puede cambiar el presente con lo que aprendió aquí

# label cap10:
#     '{cps=45}Capítulo 10{/cps}:{cps=20} El final de los tiempos{/cps}'
#     # Finalmente los del presentes logran abrir un portal para llegar al jugador de regreso (Adam fue la batería)

# label epílogo:
#     '{cps=45}Epílogo:{/cps} {cps=20}Recibiendo las consecuencias{/cps}'
#     # Final casi general donde calculamos el final del jugador

    # if(adamCFeli >= 80 and progresoRescate == 100 and estaEnPasado == False and adamFeli >= 80):
    #     jump finalExcelente
    #label finalMaloSecuela:
        # El personaje principal es mandado al pasado como castigo tras no asistir a la misión
    #    '{cps=45}.{/cps}'
    # label finalExcelente:
    #     # El personaje principal vuelve al presente y todo es perfecto
    #     '{cps=45}¡Felicidades, [prota]! Has conseguido el mejor final de todos.{/cps}'
    # label finalBully:
    #     # El personaje principal regresa y arruina la vida de Adam
    # label finalBullyPasado:
    #     # El personaje principal no regresa y arruina la vida de Adam niño
    # label finalPasado:
    #     # Acá el personaje principal no regresa al presente por decisión propia
    # label finalNormal:
    #     # El personaje principal regresa al presente
    return