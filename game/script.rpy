# Protagonista
define saviTortu = Character("[prota] [apellido]") # La variable del protagonista es saviTortu porque es una mezcla de las palabras en inglés "{cps=18}Savior" y "{cps=18}Torture", que son dos opciones {/cps}s plausibles para el jugador en el juego

label start:
    stop music
    $ prota = renpy.input("Ingresa tu nombre en la aventura", length=32)
    $ prota = prota.strip()
    $ apellido = renpy.input("Ingresa un apellido", length = 32)
    $ apellido = apellido.strip()
    $ edad = ""
    while edad < "20" or not edad:
        $ edad = renpy.input("Ingresa tu edad en el juego (debe ser a partir de los 20 años)", length = 3)
        $ edad = edad.strip()

    if not prota and not apellido and not edad:
        $ prota = "Jane"
        $ apellido = "Doe"
        $ edad = "26"
        
    "DISCLAIMER" "{cps=24}El contenido presentado puede contener temas relacionados a salud mental, bullying, suicidio, muerte e imágenes parpadeantes.{/cps}"
    "DISCLAIMER" "{cps=24}Se recomienda discreción y dejar de jugar si siente malestar o tiene un episodio de meltdown, epilepsia o similar. Se recomienda no pasar más de dos horas en el juego.{/cps}"

    menu:
        "{cps=24}¿Asumes que es tu responsabilidad lo que pase a partir de este punto?{/cps}"

        "Sí, es mi responsabilidad mantener mi seguridad personal ante este contenido":
            jump cap0
        "Necesito tiempo para pensarlo":
            return

label cap0:
    play music "001.ClearAdventureDay.mp3"
    screen stats():
        if enPasado == True:
            text "Día [diasPasado] | Pekins senlins: [monedas] | Adam Miller (felicidad): [adamCFeli]/100 | Rescate [progresoRescate]% | Reputación: [reputacionP]"
        else:
            text "Pekins senlins: [monedas] | Adam Carter (felicidad): [adamFeli]/100 | Reputación: [reputacionTra]"

    "{cps=18}Capítulo 0:{/cps} {cps=3}La reunión{/cps}"
    # Presentación de personajes y dinámicas actuales
    show screen stats
    # Cambiar narración a segunda persona en presente
    "{cps=18}8:00AM. Oficina de la policía de Senlín .Senlín Central, distrito de Senlín. 18 de Marzo, año 3046{/cps}"
    "{cps=18}Planeta: Mochu{/cps}"
    $ monedas += 1000
    "{cps=18}Nombre: {b}[prota] [apellido]{/b}{/cps}"
    "{cps=18}Habilidad de nacimiento: {b}{i}Brillo en la oscuridad{/i}{/b}.{/cps}"
    "{cps=18}Eres un agente ingresado a la policía de Senlín, con [edad] años, has logrado ganar la confianza de los tres sectores de la zona de Investigación.{/cps}"
    "{cps=18}Una reunión con los agentes te espera esta mañana.{/cps}"
    adam "{cps=18}Buenos días, agente [apellido]. ¿Cómo está para la reunión de hoy?{/cps}"
    "{cps=18}A tu lado, ves a Adam Carter, líder y detective principal del sector 970, uno de los primeros en acogerte en el entorno, aunque no lo conoces mucho.{/cps}"
    menu:
        "{cps=18}¿Cómo saludas?{/cps}"

        "Saludo amistoso, como a un amigo.":
            saviTortu "{cps=18}Buenos días, Adam.{/cps}"
            $ adamFeli +=2
            adam "{cps=18}Buenos días, [prota], es un honor trabajar contigo.{/cps}"
            adam "{cps=18}Aunque no hablamos mucho, pareces ser una buena persona{/cps}"
            "{cps=18}Adam revisa brevemente el reloj, queda una hora para la reunión.{/cps}"
            "{cps=18}Una hora que tienes libre.{/cps}"
            adam "{cps=18}Debo preparar las cosas para la reunión.{/cps}"
            adam "{cps=18}¿Nos vemos luego?{/cps}"
            menu:
                "Estaré allá":
                    saviTortu "{cps=18}Me aseguraré de estar ahí, detective.{/cps}"
                    $ adamFeli += 1
                    adam "{cps=18}Estoy seguro de ello.{/cps}"
                    "{cps=18}Adam se retira rápidamente hacia la sala de reuniones.{/cps}"
                    jump reunion
                "¿Necesitas ayuda para preparar las cosas?":
                    adam "{cps=18}No te preocupes, [apellido]{/cps}"
                    adam "{cps=18}Solo estoy algo cansado, pero no es algo que no pueda manejar.{/cps}"
                    $ adamFeli += 2
                    adam "{cps=18}De todas formas, aprecio la preocupación{/cps}"
                    menu:
                        "Confiar en que podrá hacerlo":
                            saviTortu "{cps=18}Bueno… espero que puedas lograrlo.{/cps}"
                            adam "{cps=18}Nos veremos más tarde, [prota].{/cps}"
                            "{cps=18}Ambos se van por su camino en silencio.{/cps}"
                            jump reunion
                        "Ofrecer compañía":
                            saviTortu "{cps=18}Podría ayudarte con eso, solo si quieres.{/cps}"
                            $ adamFeli += 2
                            adam "{cps=18}¿En serio podrías?{/cps}"
                            saviTortu "{cps=18}Claro, no es problema para mí. Tengo tiempo libre.{/cps}"
                            $ adamFeli += 4
                            adam "{cps=18}Claro, algo de compañía no haría mal.{/cps}"
                            adam "{cps=18}Sígueme, [prota].{/cps}"
                            jump ordenUnitario
        "Saludo formal":
            saviTortu "{cps=18}Buenos días, detective Carter{/cps}"
            $ adamFeli +=1
            adam "{cps=18}Espero que te estés adaptando a la oficina, [apellido]. Todo va a su paso.{/cps}"
            adam "{cps=18}Quizás sea abrumador al inicio, pero estoy seguro de que puedes afrontarlo.{/cps}"
            adam "{cps=18}Nos veremos en la reunión, colega.{/cps}"
            menu:
                "Estaré allá":
                    saviTortu "{cps=18}Me aseguraré de estar ahí, detective.{/cps}"
                    $ adamFeli += 1
                    adam "{cps=18}Estoy seguro de ello.{/cps}"
                    "{cps=18}Adam se retira rápidamente hacia la sala de reuniones.{/cps}"
                    jump reunion
                "¿Necesitas ayuda para preparar las cosas?":
                    adam "{cps=18}No te preocupes, [apellido].{/cps}"
                    adam "{cps=18}Han pasado bastantes cosas, pero no es algo que no pueda manejar.{/cps}"
                    $ adamFeli += 2
                    adam "{cps=18}De todas formas, aprecio la preocupación.{/cps}"
                    menu:
                        "Confiar en que podrá hacerlo":
                            saviTortu "{cps=18}Bueno… espero que puedas lograrlo.{/cps}"
                            adam "{cps=18}Nos veremos más tarde, [prota].{/cps}"
                            "{cps=18}Ambos se van por su camino en silencio.{/cps}"
                            jump reunion
                        "Ofrecer compañía":
                            saviTortu "{cps=18}Podría ayudar, tengo la hora libre.{/cps}"
                            $ adamFeli += 3
                            adam "{cps=18}Claro, algo de compañía no haría mal.{/cps}"
                            adam "{cps=18}Sígueme, [apellido].{/cps}"
                            jump ordenUnitario
        "Desconocer":
            saviTortu "{cps=18}Disculpe la pregunta, señor.{/cps}"
            saviTortu "{cps=18}Pero ¿quién es usted?{/cps}"
            adam "{cps=18}…{/cps}"
            "{cps=18}El detective mira a la ventana un momento, entonces suspira y vuelve a verte.{/cps}"
            adam "{cps=18}En caso de cualquier problema, soy Adam Carter, detective principal y líder del sector 970 de la zona de Investigación.{/cps}"
            adam "{cps=18}Si necesitas ayuda, estoy aquí para todo.{/cps}"
            adam "{cps=18}Supongo que nos veremos en la reunión.{/cps}"
            "{cps=18}Te retiras y vas a buscar algunos papeles antes de ir a la sala de reuniones.{/cps}"
            jump desconocer
        "Ignoras y sigues tu camino":
            "{cps=18}Pasas de largo el saludo de Adam, como si no hubieras notado su presencia.{/cps}"
            saviTortu "{cps=18}{i}\"Es un tipo raro…\"{/i}.{/cps}"
            $ adamFeli -=2
            jump ignorar
    label reunion:
        "{cps=18}{b}{i}Una hora después…{/i}{/b}{/cps}"
        "{cps=18}Cuando entras a la reunión, ves a Adam terminando de ordenar la sala. Ves la sala limpia y ordenada, y sientes un aroma a panqueques y rollos de canela.{/cps}"
        adam "{cps=18}Saludos, [apellido].{/cps}"
        menu:
            adam "{cps=18}Espera un poco ahí, ¿vale? El teniente va a llegar en breve.{/cps}"
            "Entendido":
                adam "{cps=18}Si alguien más aparece, los dejo entrar a ambos.{/cps}"
            "¿Arreglaste todo tú solo?":
                adam "{cps=18}Sí, todavía me sorprende haberlo logrado.{/cps}"
                menu:
                    adam "{cps=18}Y me alcanzó tiempo para cocinar un poco.{/cps}"
                    "Eso suena como un buen logro":
                        $ adamFeli += 2
                        adam "{cps=18}Gracias, [apellido].{/cps}"
                        adam "{cps=18}Aunque no es un logro como tal, me gusta considerarlo como tal.{/cps}"
                    "Pero es una reunión, no tenías que hacer desayuno.":
                        adam "{cps=18}Buena pregunta, [apellido].{/cps}"
                        adam "{cps=18}Para este tipo de reuniones, el teniente me da dado el permiso de preparar algo para aliviar el estrés una vez terminada la reunión.{/cps}"
                        adam "{cps=18}Además, cocinar es terapéutico para mí, es divertido y puedo ir variando lo que hago.{/cps}"
                        adam "{cps=18}…Eso no fue mucho detalle, ¿verdad?{/cps}"
                        menu:
                            "No te preocupes, ahora entiendo más.":
                                $ adamFeli +=3
                                adam "{cps=18}Gracias, [apellido].{/cps}"
                                adam "{cps=18}Me alegra no estar alargando una explicación.{/cps}"
                                adam "{cps=18}Es que… normalmente no hablo tanto de mí mismo.{/cps}"
                            "Creo que explicaste demasiado":
                                $ adamFeli -=1
                                adam "{cps=18}Siento mucho haberme alargado.{/cps}"
                                adam "{cps=18}De todas formas, gracias por el comentario.{/cps}"
                                adam "{cps=18}Como decía, esperemos al resto.{/cps}"
                                "{cps=18}{/cps}"
            
    label desconocer:
        "{cps=18}{b}{i}Una hora después…{/i}{/b}{/cps}"
        "{cps=18}Una vez llegas a la sala de reuniones, ves a Adam ordenando las sillas, dejando un espacio simétrico entre ellas.{/cps}"
    label ignorar:
        "{cps=18}Vas a la sala común a recoger unos papeles.{/cps}"
        brayan "{cps=18}¿Sabes que ignorar un saludo es de mala educación?{/cps}"
        $ reputacionTra -= 10
        "{cps=18}Antes de darte cuenta, divisas a {b}Brayan Orellana{/b}, agente especializado en misiones encubiertas del sector 970, el cual se estaba sirviendo un té.{/cps}"
        brayan "{cps=18}Especialmente si es uno de los superiores.{/cps}"
        menu:
            "Al ver que te tenía entre la espada y la pared, decides…"
            "Disculparte":
                saviTortu "{cps=18}No me había dado cuenta de que estaba ahí.{/cps}"
                saviTortu "{cps=18}Lo siento.{/cps}"
                brayan "{cps=18}No te preocupes, [apellido], llevas poco tiempo aquí.{/cps}"
                brayan "{cps=18}Pero recuerda que en Senlín es una falta de respeto ignorar el saludo.{/cps}"
                brayan "{cps=18}Debes tenerlo en cuenta para la próxima, ¿vale?{/cps}"
                saviTortu "{cps=18}Entendido…{/cps}"
                $ reputacionTra += 5
                brayan "{cps=18}¿Estás libre? Voy a ayudar a Carter a arreglar las cosas para la reunión.{/cps}"
                menu:
                    brayan "{cps=18}¿Me acompañas?{/cps}"
                    "Claro, no me molesta ayudarlos":
                        $ reputacionTra += 10
                        brayan "{cps=18}Bien, sígueme.{/cps}"
                        jump colaboracionRemor
                    "Tengo trabajo pendiente que hacer":
                        brayan "{cps=18}Es algo de papelería, ¿verdad?{/cps}"
                        brayan "{cps=18}Pregúntale a {b}Gavya Meraki{/b} para que te ayude con eso. Ella sabe de papelería.{/cps}"
                        brayan "{cps=18}Solo si quieres, claro.{/cps}"
            "Hacer una excusa":
                saviTortu "{cps=18}¿De qué hablas? Yo no vi a nadie.{/cps}"
                brayan "{cps=18}¿En serio?{/cps}"
                brayan "{cps=18}Porque yo reconozco cuando alguien ignora a una persona.{/cps}"
                gavya "{cps=18}¿Pasa algo, Orellana y [apellido]?{/cps}"
                "{cps=18}Ante ti, ves a {b}Gavya Meraki{/b}, encargada de relaciones exteriores del sector 1 (liderado por {b}Orfeo Galloway{/b}).{/cps}"
                brayan "{cps=18}Son cosas del sector, Meraki.{/cps}"
                gavya "{cps=18}¿Seguro? Sentí que pasaron cosas en el pasillo.{/cps}"
                $ reputacionTra -= 10
                brayan "{cps=18}Algunos problemas con [apellido].{/cps}"
                gavya "{cps=18}Oh.{/cps}"
                gavya "{cps=18}¿Solo eso van a decir?{/cps}"
                brayan "{cps=18}Te explicaré más tarde, Gavya.{/cps}"
    label colaboracionRemor:
        "{cps=18}Después de un largo rato, llegaron a la sala de reuniones, donde Adam estaba ordenando.{/cps}"
        brayan "{cps=18}Jefe.{/cps}"
        adam "{cps=18}¡Hola, Brayan{/cps}!"
        adam "{cps=18}Veo que has traído a alguien.{/cps}"
        brayan "{cps=18}Así es. [saviTortu] quiso venir a ayudar.{/cps}"
        adam "{cps=18}¡Eso está perfecto! Si los tres trabajamos de buena forma, tendremos todo listo en poco tiempo.{/cps}"
    label ordenUnitario:
        "{cps=18}Adam y tú llegan a la sala de reuniones, la cual estaba presentable, pero no lo estaba para la reunión.{/cps}"
        adam "{cps=18}Bien, [apellido], vamos a repartir los trabajos.{/cps}"
        menu:
            adam "{cps=18}¿Puedes limpiar la pizarra mientras preparo el desayuno?{/cps}"
            "Vale, yo veo la pizarra":
                adam "{cps=18}¡Genial! Creo que traje mis cosas para cocinar.{/cps}"
                adam "{cps=18}En la mesa tienes para limpiarlos.{/cps}"
            "Pero es una reunión, no tienes que hacer desayuno.":
                adam "{cps=18}Ese es un buen punto que olvidé explicar antes.{/cps}"
                adam "{cps=18}Para este tipo de reuniones, el teniente me da dado el permiso de preparar algo para… aliviar el estrés una vez terminada la reunión.{/cps}"
                adam "{cps=18}Además, cocinar es terapéutico para mí, es divertido y puedo ir variando lo que hago.{/cps}"
                adam "{cps=18}…Eso no fue mucho detalle, ¿verdad?{/cps}"
                menu:
                    "No te preocupes, ahora entiendo más.":
                        $ adamFeli +=3
                        adam "{cps=18}Gracias, [apellido].{/cps}"
                        adam "{cps=18}Me alegra no estar alargando una explicación.{/cps}"
                        adam "{cps=18}Es que… normalmente no hablo tanto de mí mismo.{/cps}"
                        jump OUR_PreReunion
                    "Creo que explicaste demasiado":
                        $ adamFeli -=1
                        adam "{cps=18}Siento mucho haberme alargado.{/cps}"
                        adam "{cps=18}De todas formas, gracias por el comentario.{/cps}"
                        adam "{cps=18}Como decía, sigamos con la {s}misión-{/s} digo, con la limpieza.{/cps}"
                        jump OUR_PreReunion
                    "Si quieres, puedes hablar mientras ordenamos":
                        $ adamFeli +=2
                        adam "{cps=18}¿No te molesta?{/cps}"
                        saviTortu "{cps=18}No, no me molesta.{/cps}"
                        $ adamFeli +=2
                        $ reputacionTra +=10
                        adam "{cps=18}Bien, aprovecha de limpiar la pizarra y yo cocinaré un poco.{/cps}"
                        adam "{cps=18}Y quizás te hable un poco de lo que estaré cocinando.{/cps}"
                        adam "{cps=18}En la mesa están las cosas para limpiar.{/cps}"
                        "{cps=18}Por un largo rato, ambos trabajaron juntos. Adam estuvo cocinando y preparando el material mientras tú le ayudabas a limpiar la sala.{/cps}"
    label OUR_PreReunion:
        "{cps=18}{b}{i}47 minutos después…{/i}{/b}{/cps}"
        "{cps=18}Después de largos minutos, el lugar finalmente estaba ordenado, y Adam ya tenía el desayuno listo.{/cps}"
        adam "{cps=18}Finalmente hemos terminado.{/cps}"
        adam "{cps=18}Debo decir que sabes ordenar bastante bien.{/cps}"
        menu:
            "Gracias.":
                adam "{cps=18}Bien, ahora tenemos que esperar a los demás.{/cps}"
            "Parece que has cocinado algo bueno.":
                $ adamFeli += 2
                adam "{cps=18}Gracias, [prota].{/cps}"
                adam "{cps=18}Espero que te guste.{/cps}"
                adam "{cps=18}Aunque es para después de la reunión, así que tienes que tener paciencia.{/cps}"
                brayan "{cps=18}Disculpa la demora, Adam.{/cps}"
                "{cps=18}Ante ustedes, ves a {b}Brayan Orellana{/b}, agente especializado en misiones encubiertas del sector 970.{/cps}"
                brayan "{cps=18}¿Te acaba de ayudar el nuevo?{/cps}"
                adam "{cps=18}Yo lo veo aquí, ¿tú no?{/cps}"
                brayan "{cps=18}No me hables así, {i}\"Pichón\"{/i}, recuerda que soy mayor que tú.{/cps}"
                adam "{cps=18}Y yo soy el líder del 970.{/cps}"
                brayan "{cps=18}…Buen punto, Carter.{/cps}"
                adam "{cps=18}Pero sí, [prota] me ayudó a ordenar.{/cps}"
                brayan "{cps=18}Eso es genial.{/cps}"
                $ reputacionTra += 10
                brayan "{cps=18}Entonces… [saviTortu], ¿no?{/cps}"
                menu:
                    "Sí, soy yo.":
                        adam "{cps=18}[apellido], te presento al agente Orellana, experto en misiones encubiertas del sector 970.{/cps}"
                        adam "{cps=18}Brayan. creo que ya has escuchado de [prota], es de nuestros agentes recién graduados de… la escuela de criminalística.{/cps}"
                        brayan "{cps=18}Oh…{/cps}"
                        "{cps=18}Notas una ligera tensión entre ambos agentes al mencionar la escuela de criminalística.{/cps}"
                        adam "{cps=18}Bueno, como decía.{/cps}"
                        adam "{cps=18}Brayan, ya que estás aquí, ¿puedes ayudar a [apellido] a ordenar la mesa?{/cps}"
                        adam "{cps=18}Tengo que prepararme para recibir al resto.{/cps}"
                        brayan "{cps=18}Claro que puedo.{/cps}"
                        "{cps=18}Adam sale de la sala, observando en la puerta a la espera de los agentes.{/cps}"
                        "{cps=18}Mientras tanto, tú y Brayan ordenaban la mesa, había un silencio incómodo entre ambos.{/cps}"
                        saviTortu "{cps=18}…{/cps}"
                        brayan "{cps=18}…{/cps}"
                        adam "{cps=18}Disculpen…{/cps}"
                        adam "{cps=18}¿Está… todo bien?{/cps}"
                        brayan "{cps=18}No te preocupes, Carter.{/cps}"
                        brayan "{cps=18}Solo estamos ordenamos con [apellido].{/cps}"
                        adam "{cps=18}Es raro que no hables, Orellana.{/cps}"
                        brayan "{cps=18}Estoy concentrado con la mesa.{/cps}"
                        adam "{cps=18}Vale, vale.{/cps}"
                        menu:
                            adam "{cps=18}¿Qué hay de ti, [prota]?{/cps}"

                            "Yo suelo estar en silencio, detective":
                                adam "{cps=18}Comprendo.{/cps}"
                                adam "{cps=18}Yo también era así a tu edad.{/cps}"
                            "También estoy concentrado":      
                                brayan "{cps=18}Somos dos, [apellido].{/cps}"
                                brayan "{cps=18}Tranquilo, jefe, nadie se va a morir por no hablar{/cps}"
                            "Se siente tenso estar en silencio, ¿puedo poner música?":
                                brayan "{cps=18}¿Quieres poner un poco de música?{/cps}"
                                "{cps=18}Brayan saca un parlante y lo deja en una silla.{/cps}"
                                brayan "{cps=18}Reclamo esta silla, y deja que encienda el parlante para que pongas música, [apellido].{/cps}"
                                adam "{cps=18}Solo puede ser una, porque estamos en la hora.{/cps}"
                                "{cps=18}Revisas en tu celular las canciones que tienes, te pones audífonos para elegir una canción mientras Adam y Brayan terminan de ordenar.{/cps}"
                                "{cps=18}Solo tienes {b}cinco{/b} canciones disponibles{/cps}"
                                "{cps=18}…{/cps}"
                                "{cps=18}…{/cps}"
                                "{cps=18}…{/cps}"
                                "{cps=18}…{/cps}"
                                "{cps=18}…{/cps}"
                                adam "{cps=18}Un poco más a la derecha… Ya está listo{/cps}"
                                menu:
                                    adam "{cps=18}¿Encontraste algo, [apellido]?{/cps}"

                                    "Quiero escuchar (nombreC)":
                                        "{cps=18}…{/cps}"
                                        adam "{cps=18}…{/cps}"
                                        jump OUR_Reunion
                                    "Quiero escuchar (nombreC)":
                                        "{cps=18}…{/cps}"
                                        jump OUR_Reunion
                                    "Quiero escuchar (nombreC)":
                                        "{cps=18}…{/cps}"
                                        jump OUR_Reunion
                                    "Quiero escuchar (nombreC)":
                                        "{cps=18}…{/cps}"
                                        jump OUR_Reunion
                                    "Quiero escuchar (nombreC)":
                                        "{cps=18}…{/cps}"
                                        jump OUR_Reunion
    label OUR_Reunion:
        adam "{cps=18}Estoy vigilando la entrada, en caso de que el teniente pregunte.{/cps}"
        brayan "{cps=18}Como usted diga, jefe.{/cps}"
        gavya "{cps=18}Buenos días, ¿se puede entrar?{/cps}"
        "{cps=18}En la puerta, ven a {b}Gavya Meraki {/b}, encargada del relaciones exteriores del sector 1 (liderado por el agente {b}Orfeo Galloway{/b}).{/cps}"
        adam "{cps=18}Claro, pase, agente Meraki.{/cps}"
        gavya "{cps=18}¿Por qué me tratas así, Adam?{/cps}"
        gavya "{cps=18}Recuerda que nos conocemos desde la escuela.{/cps}"
        adam "{cps=18}Lo sé, Gavya…{/cps}"
        gavya "{cps=18}Saludos, Brayan.{/cps}"
        brayan "{cps=18}Hola, Gavya.{/cps}"
        brayan "{cps=18}¿Te toca venir en representación de Orfeo?{/cps}"
        gavya "{cps=18}Algo así.{/cps}"
        gavya "{cps=18}Anda en una misión con Eleanor en una colonia ilegal en Munho.{/cps}"
        adam "{cps=18}¿New Sydney?{/cps}"
        gavya "{cps=18}Esa misma, están investigando a la fábrica donde Jadyn estuvo antes.{/cps}"
        gavya "{cps=18}Y tú…{/cps}"
        gavya "{cps=18}Debes ser [prota], ¿no?{/cps}"
        saviTortu "{cps=18}Sí, soy [saviTortu].{/cps}"
        $ reputacionTra +=10
        adam "{cps=18}Viene en nombre del sector 42.{/cps}"
        brayan "{cps=18}¿Cómo sabes eso?{/cps}"
        adam "{cps=18}Maryam me dijo. los demás están en algún caso o misión, que [apellido] fuera representante fue la mejor opción.{/cps}"
        gavya "{cps=18}¿Y Brayan?{/cps}"
        adam "{cps=18}En caso de que le pase algo a [apellido] que lo haga retirarse, uno de los dos representa al sector 42 y el otro se mantiene en nombre del sector 970.{/cps}"
        brayan "{cps=18}Tenemos asistencia casi completa desde nuestro sector, Adam.{/cps}"
        adam "{cps=18}Ciertamente, Brayan, porque estaremos Melissa, tú y yo.{/cps}"
        gavya "{cps=18}¿La agente Campbell en medio de una mision digital y el agente Rojas en una explosión?{/cps}"
        adam "{cps=18}Casi, porque Rojas está en una misión secreta con tus compañeros, Gavya.{/cps}"
        gavya "{cps=18}Creo que he escuchado de aquella misión.{/cps}"
        "{cps=18}En ese momento, aparece la agente {b}Melissa Torres{/b}, detective y agente del sector 970.{/cps}"
        melissa "{cps=18}¿Siguen esperando al Teniente?{/cps}"
        adam "{cps=18}¡Melissa! Que bueno que llegaste.{/cps}"
        adam "{cps=18}Antes que nada, te presento a…{/cps}"
        melissa "{cps=18}Ya leí el informe, Carter.{/cps}"
        melissa "{cps=18}[saviTortu], [edad] años, recién ingresado con habilidades de bioluminiscencia en entornos oscuros… ¿Ese?{/cps}"
        adam "{cps=18}Exacto…{/cps}"
        adam "{cps=18}Es representante del sector 42 por falta de personal.{/cps}"
        "{cps=18}Melissa hizo una mirada rápida a los presentes, entonces suspiró.{/cps}"
        melissa "{cps=18}Finalmente una reunión más calmada, al parecer.{/cps}"
        saviTortu "{cps=18}¿Las reuniones son caóticas aquí?{/cps}"
        melissa "{cps=18}Algo así.{/cps}"
        melissa "{cps=18}Cuando hay muchas personas en una reunión es difícil llegar a un acuerdo general.{/cps}"
        adam "{cps=18}Cuando piensas que está todo acordado, alguien cuestona de inmediato.{/cps}"
        brayan "{cps=18}Por suerte no hay peleas en esos momentos.{/cps}"
        brayan "{cps=18}Sería un desastre mágico.{/cps}"
        gavya "{cps=18}No creo que lleguemos a pelear, el Teniente no nos permitiría eso.{/cps}"
        adam "{cps=18}Eso es cierto, mejor evitemos las peleas.{/cps}"
        gavya "{cps=18}Entonces… ¿Dónde está el Teniente, detective?{/cps}"
        adam "{cps=18}¿Por qué la pregunta?{/cps}"
        gavya "{cps=18}Ya sabes la respuesta, Carter.{/cps}"
        adam "{cps=18}No tengo idea.{/cps}"
        melissa "{cps=18}Meraki, déjalo. El detective no sabe.{/cps}"
        adam "{cps=18}Además, el Teniente suele llegar a la hora exacta, y eso lo sabes.{/cps}"
        "{cps=18}El reloj suena, ya van a ser las 9AM.{/cps}"
        "{cps=18}Entonces escuchan pasos.{/cps}"
        adam "{cps=18}{i}{b}*Murmurando*{/b} Les dije que vendría justo a tiempo.{/i}{/cps}"
        erin "{cps=18}Buenos días, agentes.{/cps}"
        "{cps=18}Ante ustedes, se entontraba el Teniente{/cps}"
        "Unísono" "{cps=18}Buenos días, Teniente Miller.{/cps}"
        erin "{cps=18}Como habrán notado, en esta ocasión seremos menos de lo habitual.{/cps}"
        erin "{cps=18}Además de que contaremos con la presencia de nuestro agente en práctica, [saviTortu].{/cps}"
        "{cps=18}…{/cps}"
        erin "{cps=18}Entonces, con eso mencionado, vamos a empezar con la reunión.{/cps}"
        erin "{cps=18}Tenemos un caso.{/cps}"
        melissa "{cps=18}¿Tan rápido tenemos unn caso? Recién llego [apellido] hace una semana desde el último caso.{/cps}"
        erin "{cps=18}Así es.{/cps}"
        erin "{cps=18}Recientemente algunos de los agentes ausentes enviaron la noticia de que habían descubierto un laboratorio ilegal cuyo objetivo sigue siendo desconocido.{/cps}"
        erin "{cps=18}Pero eso no hace que sea algo bueno.{/cps}"
        adam "{cps=18}Algunos informantes dicen que estarían trabajando en una… maquina del tiempo.{/cps}"
        menu:
            "¿Máquina del tiempo?":
                adam "{cps=18}Así es, [prota].{/cps}"
            "¿La simple existencia y uso de la máquina no causaría una paradoja?":
                adam "{cps=18}Sí, lo haría.{/cps}"
                adam "{cps=18}Sin embargo, la teoría del tiempo mochibria dice que es probable que en el proceso del viaje se esté creando una rama alterna para no afectar tu rama actual.{/cps}"
                brayan "{cps=18}En resumen, no se crea una paradoja.{/cps}"
                saviTortu "{cps=18}Entiendo.{/cps}"
    if rechazoDes > 3:
        jump cap1
    else:
        jump altEmer
    
label cap1:
    "{cps=18}Capítulo 1:{/cps} {cps=3}La misión del reloj roto{/cps}"
    # Desencadenante del conclicto, introducción de Ringi
    "{cps=18}10:54AM. Laboratorios Chiraska. Senlín Central, distrito de Senlín. 18 de Marzo, año 3046{/cps}"
    "{cps=18}llegas a tiempo a las afueras de un callejón.{/cps}"
    saviTortu "{cps=18}Esto se supone que es el \"laboratorio\"…{/cps}"
    adam "{cps=18}No lo digas tan alto o pueden oirte.{/cps}"
    label altEmer:
        "{cps=18}Capítulo 1:{/cps} {cps=3}La misión del reloj roto{/cps}"
        "{cps=18}10:54AM. Casa de [saviTortu]. Senlín Central, distrito de Senlín. 18 de Marzo, año 3046{/cps}"
        if(rechazoDes >= 3):
            jump finalMaloSecuela
        else:
            "Rápidamente estás en las afueras de los laboratorios."

    hide screen stats
    $ enPasado = True

label cap2:
    show screen stats
    "{cps=18}Capítulo 2:{/cps} {cps=3}Aviones del pasado{/cps}"
    # Conflicto, reintroducción de personajes en su forma pasada y sus dinámicas anteriores
    "{cps=18}10:54AM. Escuela de criminalística. Senlín Central, distrito de Senlín. 18 de Marzo, año 3026{/cps}"
    return

# label cap3: # Para la 2.0
#     "{cps=18}Capítulo 3:{/cps} {cps=3}Desastre a contrarreloj{/cps}"
#     # Aquí vemos la perpectiva de los personajes del presente, donde averiguan cómo traer al jugador de vuelta. Introducción de Lydia.

# label cap4: # Para la 3.0
#     "{cps=18}Capítulo 4:{/cps} {cps=3}La fiesta de la tortura{/cps}"
#     # Desarrollo de las dínamicas de la clase, vistazo a la soledad de Adam

# label cap5: # Para la 4.0
#     "{cps=18}Capítulo 5:{/cps} {cps=3}El descarrilado{/cps}"
#     # Desarrollo de Brayan

# label cap6:
#     "{cps=18}Capítulo 6:{/cps} {cps=3}La flautista del mazo{/cps}"
#     # Desarrollo de Gavya

# label cap7:
#     "{cps=18}Capítulo 7:{/cps} {cps=3}La heroína perdida y el admadis que no vuela{/cps}"
#     # Desarrollo de Adam y Maryam

# label cap8:
#     "{cps=18}Capítulo 8:{/cps} {cps=3}Competencia de compasión{/cps}"
#     # ???

# label cap9:
#     "{cps=18}Capítulo 9:{/cps} {cps=3}Ser el sol de la luna{/cps}"
#     # Aquí el jugador entiende que no puede cambiar el pasado de su línea original y que hizo una línea alternativa, pero puede cambiar el presente con lo que aprendió aquí

# label cap10:
#     "{cps=18}Capítulo 10{/cps}:{cps=3} El final de los tiempos{/cps}"
#     # Finalmente los del presentes logran abrir un portal para llegar al jugador de regreso (Adam fue la batería)

# label epílogo:
#     "{cps=18}Epílogo:{/cps} {cps=3}Recibiendo las consecuencias{/cps}"
#     # Final casi general donde calculamos el final del jugador

    # if(adamCFeli >= 80 and progresoRescate == 100 and estaEnPasado == False and adamFeli >= 80):
    #     jump finalExcelente
    label finalMaloSecuela:
        # El personaje principal es mandado al pasado como castigo tras no asistir a la misión
        "{cps=18}.{/cps}"
    # label finalExcelente:
    #     # El personaje principal vuelve al presente y todo es perfecto
    #     "{cps=18}¡Felicidades, [prota]! Has conseguido el mejor final de todos.{/cps}"
    # label finalBully:
    #     # El personaje principal regresa y arruina la vida de Adam
    # label finalBullyPasado:
    #     # El personaje principal no regresa y arruina la vida de Adam niño
    # label finalPasado:
    #     # Acá el personaje principal no regresa al presente por decisión propia
    # label finalNormal:
    #     # El personaje principal regresa al presente
    return