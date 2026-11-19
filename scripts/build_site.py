# Builds site/case.html, the RunDate case study served at wendelfreitas.com/cases/rundate-miami
# Mobile-first: on phones the live app launches full screen; on desktop it sits in a phone frame.
import json, pathlib
R = 'https://raw.githubusercontent.com/wendel-crypto/rundate/main/docs/'
C = {
'title': ['RunDate — Dating app for runners case study | Wendel Freitas', 'RunDate — Caso de estudio app de citas para corredores | Wendel Freitas', 'RunDate — Case de app de namoro para corredores | Wendel Freitas'],
'back': ['← Cases / App', '← Casos / App', '← Cases / App'],
'eyebrow': ['Mobile app design · iOS · Dating + fitness', 'Diseño de app móvil · iOS · Citas + fitness', 'Design de app mobile · iOS · Namoro + fitness'],
'h1a': ['Matches unlock', 'Los matches se desbloquean', 'Os matches desbloqueiam'],
'h1b': ['three hours', 'tres horas', 'três horas'],
'h1c': ['after you log a run.', 'después de registrar una carrera.', 'depois que você registra uma corrida.'],
'lede': ['Dating apps reward being on your phone. Training apps reward being outside. RunDate is built for people who would rather be outside: swipe mechanics on top of a real activity log, with a lock that makes the run the price of admission.',
         'Las apps de citas premian estar en el teléfono. Las de entrenamiento premian estar afuera. RunDate es para quienes prefieren estar afuera: swipe sobre un registro real de actividad, con un bloqueo que convierte la carrera en el precio de entrada.',
         'Apps de namoro recompensam ficar no celular. Apps de treino recompensam estar na rua. O RunDate é para quem prefere estar na rua: swipe em cima de um registro real de atividades, com uma trava que transforma a corrida no preço da entrada.'],
'b1': ['Try the live app', 'Prueba la app en vivo', 'Teste o app ao vivo'], 'b2': ['Open full screen ↗', 'Pantalla completa ↗', 'Tela cheia ↗'], 'b3': ['View the code ↗', 'Ver el código ↗', 'Ver o código ↗'],
'k1': ['Role', 'Rol', 'Papel'], 'k1v': ['Product design and build', 'Diseño y desarrollo de producto', 'Design e construção do produto'],
'k2': ['Category', 'Categoría', 'Categoria'], 'k2v': ['Consumer social, dating + fitness', 'Social, citas + fitness', 'Social, namoro + fitness'],
'k3': ['Market', 'Mercado', 'Mercado'], 'k3v': ['Miami, Brickell geofence', 'Miami, geocerca de Brickell', 'Miami, geocerca de Brickell'],
'k4': ['Platform', 'Plataforma', 'Plataforma'], 'k4v': ['iOS, mobile only', 'iOS, solo móvil', 'iOS, só mobile'],
'k5': ['Stage', 'Etapa', 'Estágio'], 'k5v': ['Interactive prototype', 'Prototipo interactivo', 'Protótipo interativo'],
'te': ['Try it', 'Pruébala', 'Teste'], 'th': ['Everything here is live.', 'Todo aquí funciona.', 'Tudo aqui funciona.'],
'tp': ['Swipe the cards, open a profile, log a run and watch the match lock count down. It is the actual prototype, not a video. Jump straight to a flow:',
       'Desliza las tarjetas, abre un perfil, registra una carrera y mira la cuenta regresiva del bloqueo. Es el prototipo real, no un video. Ve directo a un flujo:',
       'Arraste os cards, abra um perfil, registre uma corrida e veja a trava contar. É o protótipo de verdade, não um vídeo. Vá direto a um fluxo:'],
'launch': ['Launch the live app', 'Abrir la app en vivo', 'Abrir o app ao vivo'], 'launchs': ['Full screen · swipe with your thumb', 'Pantalla completa · desliza con el pulgar', 'Tela cheia · arraste com o polegar'],
'close': ['← Back to the case study', '← Volver al caso', '← Voltar ao case'],
'j1': ['Discover', 'Descubrir', 'Descobrir'], 'j1s': ['Swipe with drag physics, PACE and PASS', 'Swipe con física, PACE y PASS', 'Swipe com física, PACE e PASS'],
'j2': ['Hit the lock', 'Choca con el bloqueo', 'Bata na trava'], 'j2s': ['Like before unlock and get the warning', 'Da like antes de tiempo y recibe el aviso', 'Curta antes da hora e receba o aviso'],
'j3': ['Log a run', 'Registra una carrera', 'Registre uma corrida'], 'j3s': ['Distance, time, route, the rule, the confirmation', 'Distancia, tiempo, ruta, la regla y la confirmación', 'Distância, tempo, rota, a regra e a confirmação'],
'j4': ['Unlock and match', 'Desbloquea y haz match', 'Desbloqueie e dê match'], 'j4s': ['Skip the clock and swipe right', 'Adelanta el reloj y desliza a la derecha', 'Adiante o relógio e arraste para a direita'],
'j5': ['Profile', 'Perfil', 'Perfil'], 'j5s': ['About, stats, runs, gallery', 'Sobre mí, stats, carreras, galería', 'Sobre, stats, corridas, galeria'],
'j6': ['Feed & stories', 'Feed y stories', 'Feed e stories'], 'j6s': ['Run, Story and Milestone posts', 'Posts de carrera, story y logro', 'Posts de corrida, story e conquista'],
'j7': ['Matches & chat', 'Matches y chat', 'Matches e chat'], 'j7s': ['Countdown card, threads, quick replies', 'Cuenta regresiva, chats, respuestas rápidas', 'Contagem, conversas, respostas rápidas'],
'note': ['Prototype data · photos from Unsplash · nothing is saved', 'Datos de prototipo · fotos de Unsplash · nada se guarda', 'Dados de protótipo · fotos do Unsplash · nada é salvo'],
're': ['The read', 'La lectura', 'A leitura'], 'rh': ['Four observations that shaped the product.', 'Cuatro observaciones que dieron forma al producto.', 'Quatro observações que moldaram o produto.'],
'r1': ['Signal', 'Señal', 'Sinal'], 'r1p': ['Dating profiles optimise for photographs. Runners already generate better signal than a bio: pace, weekly mileage, personal records, the routes they actually run. The profile should be built out of training data.',
                                     'Los perfiles de citas se optimizan para fotos. Los corredores ya generan mejor señal que una bio: ritmo, millas semanales, récords y las rutas que realmente corren. El perfil debe construirse con datos de entrenamiento.',
                                     'Perfis de namoro são otimizados para fotos. Corredores já geram sinal melhor que uma bio: ritmo, quilometragem semanal, recordes e as rotas que realmente correm. O perfil deve ser feito de dados de treino.'],
'r2': ['Intent', 'Intención', 'Intenção'], 'r2p': ['A running app with dating bolted on attracts spectators. Gating matches behind a logged activity filters the pool down to people who actually run.',
                                       'Una app de running con citas pegadas atrae espectadores. Condicionar los matches a una actividad registrada filtra el grupo a gente que realmente corre.',
                                       'Um app de corrida com namoro colado atrai espectadores. Condicionar os matches a uma atividade registrada filtra o grupo para quem realmente corre.'],
'r3': ['Geography', 'Geografía', 'Geografia'], 'r3p': ['Running is local. Brickell is a 2.1 mile radius, not a city-wide pool. The geofence is quality control, not a limitation.',
                                         'Correr es local. Brickell es un radio de 2,1 millas, no toda la ciudad. La geocerca es control de calidad, no una limitación.',
                                         'Correr é local. Brickell é um raio de 2,1 milhas, não a cidade inteira. A geocerca é controle de qualidade, não limitação.'],
'r4': ['Proof', 'Prueba', 'Prova'], 'r4p': ['A photograph at a finish line beats a paragraph about loving the outdoors. The gallery and the activity feed carry the persuasion, so the interface gets out of their way.',
                                     'Una foto en la meta vale más que un párrafo sobre amar el aire libre. La galería y el feed de actividad persuaden, así que la interfaz se aparta.',
                                     'Uma foto na linha de chegada vale mais que um parágrafo sobre amar a natureza. A galeria e o feed fazem a persuasão, então a interface sai do caminho.'],
'me': ['The mechanic', 'La mecánica', 'A mecânica'], 'mh': ['The three-hour match lock.', 'El bloqueo de tres horas.', 'A trava de três horas.'],
'mp': ['This is the product. Everything else is a well-built dating app; the lock is the argument.', 'Este es el producto. Todo lo demás es una app de citas bien hecha; el bloqueo es el argumento.', 'Este é o produto. O resto é um app de namoro bem feito; a trava é o argumento.'],
'm1': ['The like button shows a padlock and stays disabled until three hours after the last logged activity.', 'El botón de like muestra un candado y sigue desactivado hasta tres horas después de la última actividad.', 'O botão de curtir mostra um cadeado e fica desativado até três horas depois da última atividade.'],
'm2': ['Swiping right before unlock raises a warning banner instead of producing a match.', 'Deslizar a la derecha antes de tiempo muestra un aviso en lugar de un match.', 'Arrastar para a direita antes da hora mostra um aviso em vez de um match.'],
'm3': ['The Matches tab dims every contact and shows a live countdown card.', 'La pestaña de Matches atenúa cada contacto y muestra una cuenta regresiva en vivo.', 'A aba Matches escurece cada contato e mostra uma contagem ao vivo.'],
'm4': ['The profile CTA reads “Unlock in Xh Xm” rather than Like.', 'El botón del perfil dice “Faltan Xh Xm” en vez de Like.', 'O botão do perfil diz “Faltam Xh Xm” em vez de Curtir.'],
'm5': ['Log Activity states the rule before you save, and the confirmation screen repeats it.', 'Registrar actividad explica la regla antes de guardar y la confirmación la repite.', 'Registrar atividade explica a regra antes de salvar e a confirmação repete.'],
'mc': ['It turns the app from a browsing habit into a reward for training, and it means everyone in the pool ran today.', 'Convierte la app de un hábito de scroll en una recompensa por entrenar, y garantiza que todos en el grupo corrieron hoy.', 'Transforma o app de um hábito de rolagem em recompensa pelo treino, e garante que todo mundo no grupo correu hoje.'],
'se': ['The screens', 'Las pantallas', 'As telas'], 'sh': ['Discover converts. Feed retains. Matches rewards. Profile persuades.', 'Descubrir convierte. Feed retiene. Matches premia. Perfil persuade.', 'Descobrir converte. Feed retém. Matches recompensa. Perfil persuade.'],
'swipeHint': ['Swipe →', 'Desliza →', 'Arraste →'],
'pe': ['The profile', 'El perfil', 'O perfil'], 'ph': ['Five tabs. One coherent person.', 'Cinco pestañas. Una persona coherente.', 'Cinco abas. Uma pessoa coerente.'],
'pp': ['The profile is not a biography. It is a training dossier with enough human signal to start a conversation.', 'El perfil no es una biografía. Es un expediente de entrenamiento con suficiente señal humana para empezar una conversación.', 'O perfil não é uma biografia. É um dossiê de treino com sinal humano suficiente para começar uma conversa.'],
'p1': ['About', 'Sobre mí', 'Sobre'], 'p1p': ['Bio, fun fact, Looking For, and a quick-info grid: preferred time, run days, next race, years running.', 'Bio, dato curioso, Busco y una grilla rápida: horario, días, próxima carrera y años corriendo.', 'Bio, curiosidade, Procuro e uma grade rápida: horário, dias, próxima prova e anos correndo.'],
'p2': ['Stats', 'Stats', 'Stats'], 'p2p': ['Personal records for 5K, half and full, physical stats and a weekly load chart. The signal a dating profile normally lacks.', 'Récords de 5K, media y maratón, datos físicos y un gráfico de carga semanal. La señal que a un perfil de citas le falta.', 'Recordes de 5K, meia e maratona, dados físicos e um gráfico de carga semanal. O sinal que falta num perfil de namoro.'],
'p3': ['Runs', 'Carreras', 'Corridas'], 'p3p': ['The recent activity log, doubling as proof the person actually trains.', 'El registro reciente de actividad, que también prueba que la persona entrena.', 'O histórico recente, que também prova que a pessoa treina.'],
'p4': ['Gallery', 'Galería', 'Galeria'], 'p4p': ['A three-column photo grid that opens into a full-screen lightbox with a thumbnail strip.', 'Una grilla de tres columnas que abre un visor a pantalla completa con miniaturas.', 'Uma grade de três colunas que abre um visualizador em tela cheia com miniaturas.'],
'p5': ['Settings', 'Ajustes', 'Ajustes'], 'p5p': ['Geofence radius and privacy sit at the top, because in this category they are product features, not admin.', 'El radio de geocerca y la privacidad van arriba, porque en esta categoría son producto, no administración.', 'Raio da geocerca e privacidade ficam no topo, porque nesta categoria são produto, não administração.'],
'de': ['Design decisions', 'Decisiones de diseño', 'Decisões de design'], 'dh': ['Four choices that define the experience.', 'Cuatro decisiones que definen la experiencia.', 'Quatro escolhas que definem a experiência.'],
'd1': ['Image first. Every piece of information sits on the photograph over a gradient. No white cards, no blank space under a picture.', 'Imagen primero. Toda la información va sobre la foto con un degradado. Sin tarjetas blancas ni espacio vacío.', 'Imagem primeiro. Toda informação fica sobre a foto com um degradê. Sem cards brancos, sem espaço vazio.'],
'd2': ['Match count removed from the profile. A visible total turns a dating app into a scoreboard and changes who feels welcome.', 'Sin contador de matches en el perfil. Un total visible convierte la app en un marcador y cambia quién se siente bienvenido.', 'Sem contador de matches no perfil. Um total visível transforma o app num placar e muda quem se sente bem-vindo.'],
'd3': ['The geofence is shown, not hidden. “Brickell · 2.1 mi” sits in the header so the size of the pool is never a surprise.', 'La geocerca se muestra. “Brickell · 2.1 mi” está en el encabezado, así el tamaño del grupo nunca sorprende.', 'A geocerca aparece. “Brickell · 2.1 mi” fica no topo, então o tamanho do grupo nunca surpreende.'],
'd4': ['Verification badges and online status ride on every card, because trust is the scarce thing in this category.', 'Insignias de verificación y estado en línea en cada tarjeta, porque la confianza es lo escaso en esta categoría.', 'Selos de verificação e status online em cada card, porque confiança é o que falta nesta categoria.'],
'xe': ['What I would measure', 'Qué mediría', 'O que eu mediria'], 'xh': ['Six metrics. No vanity numbers.', 'Seis métricas. Sin números de vanidad.', 'Seis métricas. Sem números de vaidade.'],
'x1': ['Logged runs per active user per week', 'Carreras registradas por usuario activo por semana', 'Corridas registradas por usuário ativo por semana'], 'x1p': ['The lock only earns its place if it actually drives training.', 'El bloqueo solo se justifica si realmente impulsa el entrenamiento.', 'A trava só se justifica se realmente gera treino.'],
'x2': ['Run to swipe conversion', 'Conversión de carrera a swipe', 'Conversão de corrida para swipe'], 'x2p': ['Share of users who open Discover within an hour of unlock. Measures whether the delayed reward lands.', 'Usuarios que abren Descubrir en la primera hora tras desbloquear. Mide si la recompensa diferida funciona.', 'Usuários que abrem Descobrir na primeira hora após desbloquear. Mede se a recompensa adiada funciona.'],
'x3': ['Match to first message', 'Del match al primer mensaje', 'Do match à primeira mensagem'], 'x3p': ['Whether shared training context makes the opening line easier to write.', 'Si el contexto de entrenamiento compartido facilita la primera frase.', 'Se o contexto de treino em comum facilita a primeira frase.'],
'x4': ['Profile completion depth', 'Profundidad del perfil', 'Profundidade do perfil'], 'x4p': ['Photos uploaded and tabs filled. The product is only as good as its profiles.', 'Fotos subidas y pestañas completas. El producto vale lo que valen sus perfiles.', 'Fotos enviadas e abas preenchidas. O produto vale o que valem seus perfis.'],
'x5': ['Geofence density', 'Densidad de la geocerca', 'Densidade da geocerca'], 'x5p': ['Active runners per square mile in Brickell. Below a threshold the pool feels empty and nothing else matters.', 'Corredores activos por milla cuadrada en Brickell. Por debajo de un umbral el grupo se siente vacío.', 'Corredores ativos por milha quadrada em Brickell. Abaixo de um limite o grupo parece vazio.'],
'x6': ['30-day retention', 'Retención a 30 días', 'Retenção em 30 dias'], 'x6p': ['The honest read on whether the lock builds a habit or just adds friction.', 'La lectura honesta de si el bloqueo crea hábito o solo agrega fricción.', 'A leitura honesta se a trava cria hábito ou só adiciona atrito.'],
'ce': ['Built with Claude', 'Construido con Claude', 'Construído com Claude'], 'cp': ['The prototype is a single HTML file with no framework or build step: real drag physics, a live lock clock, stories, chat and run logging, in English, Spanish and Portuguese.',
                                       'El prototipo es un solo archivo HTML sin framework ni compilación: física de arrastre real, reloj de bloqueo en vivo, stories, chat y registro de carreras, en inglés, español y portugués.',
                                       'O protótipo é um único arquivo HTML sem framework nem build: física de arrasto real, relógio da trava ao vivo, stories, chat e registro de corridas, em inglês, espanhol e português.'],
'fh': ['Building a consumer app with a real mechanic?', '¿Construyendo una app de consumo con una mecánica real?', 'Construindo um app de consumo com uma mecânica de verdade?'],
'fp': ['WRGB designs products around the one decision that makes them different, then builds outward from there.', 'WRGB diseña productos alrededor de la decisión que los hace distintos y construye desde ahí.', 'A WRGB desenha produtos em torno da decisão que os torna diferentes e constrói a partir dela.'],
'fb': ['Start a project →', 'Empecemos un proyecto →', 'Vamos começar →'],
}
S = [('01-discover', ['Discover', 'Descubrir', 'Descobrir'], ['Full-bleed photos, tap zones to cycle them, pace and PRs on a gradient strip.', 'Fotos a sangre, zonas táctiles para pasarlas, ritmo y récords sobre el degradado.', 'Fotos sangradas, toques para trocar, ritmo e recordes sobre o degradê.']),
     ('02-locked', ['The lock', 'El bloqueo', 'A trava'], ['Swipe right too early and the banner explains the rule instead of matching.', 'Desliza antes de tiempo y el aviso explica la regla en vez del match.', 'Arraste cedo demais e o aviso explica a regra em vez do match.']),
     ('03-profile', ['Profile · About', 'Perfil · Sobre mí', 'Perfil · Sobre'], ['Bio, fun fact and a colour-coded Looking For card. The CTA counts down.', 'Bio, dato curioso y tarjeta Busco por colores. El botón cuenta hacia atrás.', 'Bio, curiosidade e card Procuro por cores. O botão faz contagem.']),
     ('04-stats', ['Profile · Stats', 'Perfil · Stats', 'Perfil · Stats'], ['5K, half and full PRs plus an eight-week load chart.', 'Récords de 5K, media y maratón y carga de ocho semanas.', 'Recordes de 5K, meia e maratona e carga de oito semanas.']),
     ('05-feed', ['Feed', 'Feed', 'Feed'], ['Stories on top, then Run, Story and Milestone posts with a stats bar.', 'Stories arriba y luego posts de carrera, story y logro con barra de stats.', 'Stories no topo e posts de corrida, story e conquista com barra de stats.']),
     ('06-matches', ['Matches', 'Matches', 'Matches'], ['Every contact dims behind a live countdown until the clock hits zero.', 'Cada contacto se atenúa tras una cuenta regresiva hasta llegar a cero.', 'Cada contato escurece atrás de uma contagem até zerar.']),
     ('07-chat', ['Chat', 'Chat', 'Chat'], ['History, quick replies and a working send input.', 'Historial, respuestas rápidas y envío funcional.', 'Histórico, respostas rápidas e envio funcionando.']),
     ('08-log', ['Log activity', 'Registrar', 'Registrar'], ['Type, distance, time, route and photo. The rule is stated before you save.', 'Tipo, distancia, tiempo, ruta y foto. La regla aparece antes de guardar.', 'Tipo, distância, tempo, rota e foto. A regra aparece antes de salvar.']),
     ('09-match', ["It's a match", 'Es un match', 'Deu match'], ['Both of you ran today. That is the whole point.', 'Los dos corrieron hoy. Ese es el punto.', 'Os dois correram hoje. Esse é o ponto.'])]
JUMP = ['discover', 'lock', 'log', 'unlock', 'card', 'story', 'chat']

def t(k, tag='span', cls=''):
    return f'<{tag} data-t="{k}"{(" class=" + chr(34) + cls + chr(34)) if cls else ""}>{C[k][0]}</{tag}>'

meta = ''.join(f'<div><span data-t="k{i}">{C[f"k{i}"][0]}</span><b data-t="k{i}v">{C[f"k{i}v"][0]}</b></div>' for i in range(1, 6))
jumps = ''.join(f'<button data-go="{g}"><span class="n">0{i+1}</span><span><b data-t="j{i+1}">{C[f"j{i+1}"][0]}</b><small data-t="j{i+1}s">{C[f"j{i+1}s"][0]}</small></span></button>' for i, g in enumerate(JUMP))
reads = ''.join(f'<div class="card"><span class="num">0{i}</span><h3 data-t="r{i}">{C[f"r{i}"][0]}</h3><p data-t="r{i}p">{C[f"r{i}p"][0]}</p></div>' for i in range(1, 5))
mech = ''.join(f'<li><span>→</span><p data-t="m{i}">{C[f"m{i}"][0]}</p></li>' for i in range(1, 6))
shots = ''.join(f'<figure class="shot"><img src="{R}screens/{s[0]}.jpg" alt="" loading="lazy" width="390" height="844"><figcaption><b data-s="{i}">{s[1][0]}</b><span data-sp="{i}">{s[2][0]}</span></figcaption></figure>' for i, s in enumerate(S))
ptabs = ''.join(f'<div class="card"><h3 data-t="p{i}">{C[f"p{i}"][0]}</h3><p data-t="p{i}p">{C[f"p{i}p"][0]}</p></div>' for i in range(1, 6))
decs = ''.join(f'<div class="card"><span class="num">0{i}</span><p data-t="d{i}">{C[f"d{i}"][0]}</p></div>' for i in range(1, 5))
mets = ''.join(f'<div class="card"><h3 data-t="x{i}">{C[f"x{i}"][0]}</h3><p data-t="x{i}p">{C[f"x{i}p"][0]}</p></div>' for i in range(1, 7))

CSS = r'''
:root{--bg:#080808;--panel:#111;--line:#232323;--ink:#f4f4f1;--mute:#9a9a94;--lime:#c8f135;--pink:#FF3D6E;--pink2:#FF7A59}
*{box-sizing:border-box}html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:400 16px/1.6 Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit}button{font:inherit;color:inherit;cursor:pointer;background:none;border:0;padding:0}img{max-width:100%}
.wrap{max-width:1120px;margin:0 auto;padding:0 20px}
header{position:sticky;top:0;z-index:20;background:rgba(8,8,8,.88);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
header .wrap{display:flex;align-items:center;gap:16px;min-height:58px}
.logo{font:800 21px Syne,sans-serif;text-decoration:none;letter-spacing:-.02em}.logo span{color:var(--lime)}
nav{display:flex;gap:18px;margin-left:auto;align-items:center}nav a{font:500 11.5px 'JetBrains Mono',monospace;letter-spacing:.12em;text-transform:uppercase;text-decoration:none;color:var(--mute)}nav a[aria-current]{color:var(--ink)}
nav .hide-m{display:none}
.cta{background:var(--lime);color:#080808!important;padding:9px 14px;border-radius:6px;font:600 13px Inter,sans-serif!important;letter-spacing:0!important;text-transform:none!important}
.eyebrow{font:500 11.5px 'JetBrains Mono',monospace;letter-spacing:.16em;text-transform:uppercase;color:var(--lime);margin:0 0 10px}
h1{font:800 clamp(36px,10.5vw,82px)/1.02 Syne,sans-serif;letter-spacing:-.03em;margin:12px 0 18px;text-wrap:balance}h1 em{font-style:normal;background:linear-gradient(90deg,var(--pink),var(--pink2));-webkit-background-clip:text;background-clip:text;color:transparent}
h2{font:700 clamp(25px,6.4vw,38px)/1.12 Syne,sans-serif;letter-spacing:-.02em;margin:0 0 14px;text-wrap:balance}
h3{font:700 17px/1.25 Syne,sans-serif;margin:6px 0 6px}
.hero{padding-top:36px;padding-bottom:28px}.lede{color:#c9c9c3;font-size:17px;max-width:660px;margin:0}
.back{font:500 11.5px 'JetBrains Mono',monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--mute);text-decoration:none}
.btns{display:grid;gap:10px;margin-top:22px}.btn{display:block;text-align:center;padding:14px 18px;border-radius:8px;border:1px solid #3a3a3a;text-decoration:none;font-weight:600;font-size:15px}
.btn.p{background:var(--lime);color:#080808;border-color:var(--lime)}
.cover{margin:26px -20px 0;overflow:hidden;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.cover img{display:block;width:100%;height:auto}
.meta{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--line);border:1px solid var(--line);border-radius:12px;overflow:hidden;margin-top:22px}
.meta div{background:var(--panel);padding:14px 16px}.meta div:last-child{grid-column:1/-1}.meta span{display:block;font:500 10.5px 'JetBrains Mono',monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--lime);margin-bottom:4px}.meta b{font-weight:500;font-size:14px;color:#dcdcd6}
section{padding:46px 0;border-top:1px solid var(--line)}
p{color:#c9c9c3}
/* live app: mobile launcher */
.launcher{display:flex;gap:16px;align-items:center;margin:20px 0 6px;padding:14px;border-radius:18px;background:linear-gradient(135deg,#2a0b16,#140a0c);border:1px solid rgba(255,61,110,.4);width:100%;text-align:left}
.launcher img{width:86px;height:186px;object-fit:cover;border-radius:16px;border:1px solid #333;flex:none}
.launcher b{display:block;font:800 21px/1.15 Syne,sans-serif;margin-bottom:6px}.launcher small{display:block;color:#f2b8c8;font-size:13.5px}
.launcher .go{display:inline-flex;margin-top:12px;align-items:center;gap:8px;background:linear-gradient(135deg,var(--pink),var(--pink2));color:#fff;font-weight:700;font-size:14px;padding:10px 14px;border-radius:10px}
.launcher .live{display:inline-flex;align-items:center;gap:6px;font:500 10.5px 'JetBrains Mono',monospace;letter-spacing:.12em;text-transform:uppercase;color:#7ef3b5;margin-bottom:8px}.launcher .live i{width:7px;height:7px;border-radius:50%;background:#34D399;box-shadow:0 0 0 0 rgba(52,211,153,.6);animation:pl 1.6s infinite}
@keyframes pl{70%{box-shadow:0 0 0 7px rgba(52,211,153,0)}100%{box-shadow:0 0 0 0 rgba(52,211,153,0)}}
.jump{display:grid;gap:8px;margin-top:16px}
.jump button{display:flex;align-items:center;gap:14px;text-align:left;padding:13px 14px;border-radius:12px;background:var(--panel);border:1px solid var(--line);min-height:56px}
.jump button.on,.jump button:active{border-color:var(--pink)}.jump b{font:700 15px Syne,sans-serif;display:block}.jump small{color:var(--mute);font-size:13px;line-height:1.35;display:block}
.jump .n{font:500 12px 'JetBrains Mono',monospace;color:var(--pink);min-width:20px}
.note{font:500 10.5px 'JetBrains Mono',monospace;letter-spacing:.1em;text-transform:uppercase;color:var(--mute);margin-top:14px}
.device{display:none}
/* full-screen overlay on phones */
.ov{position:fixed;inset:0;z-index:100;background:#0B0B10;display:none;flex-direction:column}.ov.on{display:flex}
.ov .bar{height:calc(46px + env(safe-area-inset-top));padding-top:env(safe-area-inset-top);display:flex;align-items:center;padding-left:14px;padding-right:14px;border-bottom:1px solid #1f1f28;background:#08080b}
.ov .bar button{font:600 14px Inter;color:#f2b8c8}
.ov iframe{flex:1;width:100%;border:0;background:#0B0B10}
body.lock{overflow:hidden}
/* cards & lists */
.grid{display:grid;gap:10px;margin-top:20px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:18px}.card p{margin:0;font-size:15px}
.num{font:500 12px 'JetBrains Mono',monospace;color:var(--pink)}
.mech{list-style:none;padding:0;margin:20px 0}.mech li{display:flex;gap:14px;padding:14px 0;border-bottom:1px solid var(--line)}.mech li span{color:var(--pink);font:700 18px Syne}.mech p{margin:0}
.pull{font:700 clamp(19px,4.8vw,24px)/1.35 Syne,sans-serif;color:var(--ink);border-left:3px solid var(--pink);padding-left:16px;margin:22px 0 0}
/* screens: swipeable strip on every size */
.strip{display:flex;gap:14px;overflow-x:auto;scroll-snap-type:x mandatory;margin:22px -20px 0;padding:0 20px 8px;scrollbar-width:none}.strip::-webkit-scrollbar{display:none}
.shot{flex:none;width:72vw;max-width:300px;margin:0;scroll-snap-align:start}.shot img{width:100%;height:auto;aspect-ratio:390/844;object-fit:cover;border-radius:28px;border:1px solid #2a2a2a;display:block;background:#111}
.shot figcaption{padding:10px 4px 0}.shot b{display:block;font:700 16px Syne,sans-serif}.shot span{color:var(--mute);font-size:13.5px;line-height:1.4;display:block}
.sh-top{display:flex;align-items:flex-end;justify-content:space-between;gap:12px}.hint{font:500 11px 'JetBrains Mono',monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--pink);white-space:nowrap}
.sw{display:flex;gap:8px;flex-wrap:wrap;margin:18px 0}.sw div{width:72px}.sw i{display:block;height:46px;border-radius:8px;border:1px solid #2a2a2a}.sw span{font:500 10.5px 'JetBrains Mono',monospace;color:var(--mute);display:block;margin-top:5px}
.tags{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px}.tags span{font:500 12px 'JetBrains Mono',monospace;border:1px solid #333;border-radius:999px;padding:6px 11px;color:#c9c9c3}
.final{text-align:center}.final p{max-width:520px;margin:0 auto 22px}
footer{border-top:1px solid var(--line);padding:30px 0 calc(40px + env(safe-area-inset-bottom));color:var(--mute);font-size:14px}footer .wrap{display:flex;gap:14px;flex-wrap:wrap;justify-content:space-between}
/* tablet */
@media(min-width:640px){.wrap{padding:0 28px}.btns{display:flex;flex-wrap:wrap}.btn{display:inline-block}.meta{grid-template-columns:repeat(5,minmax(0,1fr))}.meta div:last-child{grid-column:auto}
 .grid.g2{grid-template-columns:1fr 1fr}.grid.g3{grid-template-columns:repeat(3,minmax(0,1fr))}.cover{margin:30px 0 0;border:1px solid var(--line);border-radius:16px}.strip{margin:22px -28px 0;padding:0 28px 8px}.shot{width:260px}nav .hide-m{display:inline}}
/* desktop: phone frame inline */
@media(min-width:980px){body{font-size:17px}.hero{padding-top:70px;padding-bottom:40px}.lede{font-size:19px}section{padding:72px 0}
 .play{display:grid;grid-template-columns:minmax(0,1fr) 410px;gap:56px;align-items:center}.launcher{display:none}
 .device{display:block;width:410px;height:864px;border-radius:54px;background:#1a1a22;padding:10px;box-shadow:0 0 0 1px #2a2a35,0 40px 120px rgba(255,61,110,.16)}
 .device iframe{width:390px;height:844px;border:0;border-radius:44px;display:block;background:#0B0B10}
 .two{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:56px}.two .grid{margin-top:0}
 .grid.g4{grid-template-columns:repeat(4,minmax(0,1fr))}.grid.g5{grid-template-columns:repeat(5,minmax(0,1fr))}.shot{width:280px}.jump button:hover{border-color:var(--pink)}}
'''

html = f'''<!doctype html><html lang="en" data-rd-static="1"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{C['title'][0]}</title>
<meta name="description" content="RunDate is a dating app for runners in Brickell, Miami: matches unlock three hours after you log a run. Interactive iOS prototype and product case study.">
<meta property="og:title" content="RunDate — Matches unlock three hours after you log a run"><meta property="og:description" content="A dating app for runners with a three-hour match lock. Live interactive prototype."><meta property="og:image" content="{R}cover.jpg">
<meta name="theme-color" content="#080808"><link rel="canonical" href="https://www.wendelfreitas.com/cases/rundate-miami">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<header><div class="wrap"><a class="logo" href="/">W<span>F</span></a><nav><a class="hide-m" href="/">Home</a><a class="hide-m" href="/services">Services</a><a href="/cases" aria-current="page">Cases</a><a class="hide-m" href="/about">About</a><a class="cta" href="/contact">Get Free Audit →</a></nav></div></header>
<main translate="no">
<div class="wrap hero">
<a class="back" href="/cases">{t('back')}</a>
<p class="eyebrow" style="margin-top:22px">{t('eyebrow')}</p>
<h1>{t('h1a')} <em data-t="h1b">{C['h1b'][0]}</em> {t('h1c')}</h1>
<p class="lede">{t('lede')}</p>
<div class="btns"><a class="btn p" href="#try" data-launch>{t('b1')}</a><a class="btn" href="/rundate/app/" target="_blank" rel="noopener">{t('b2')}</a><a class="btn" href="https://github.com/wendel-crypto/rundate" target="_blank" rel="noopener">{t('b3')}</a></div>
<div class="cover"><img src="{R}cover.jpg" alt="RunDate app screens: feed, discover, profile and matches" width="2240" height="990"></div>
<div class="meta">{meta}</div>
</div>
<section id="try"><div class="wrap play"><div>
<p class="eyebrow">{t('te')}</p><h2>{t('th')}</h2>
<p>{t('tp')}</p>
<button class="launcher" data-launch><img src="{R}thumbs/01-discover.jpg" alt=""><span><span class="live"><i></i>Live</span><b data-t="launch">{C['launch'][0]}</b><small data-t="launchs">{C['launchs'][0]}</small><span class="go">▶ <span data-t="b1">{C['b1'][0]}</span></span></span></button>
<div class="jump" id="jump">{jumps}</div>
<p class="note">{t('note')}</p>
</div>
<div class="device"><iframe id="app" data-src="/rundate/app/?embed" title="RunDate interactive prototype" loading="lazy"></iframe></div>
</div></section>
<section><div class="wrap"><p class="eyebrow">{t('re')}</p><h2>{t('rh')}</h2><div class="grid g2 g4">{reads}</div></div></section>
<section><div class="wrap two"><div><p class="eyebrow">{t('me')}</p><h2>{t('mh')}</h2><p>{t('mp')}</p></div><div><ul class="mech">{mech}</ul><p class="pull">{t('mc')}</p></div></div></section>
<section><div class="wrap"><div class="sh-top"><div><p class="eyebrow">{t('se')}</p><h2>{t('sh')}</h2></div><span class="hint" data-t="swipeHint">{C['swipeHint'][0]}</span></div>
<div class="strip" id="strip">{shots}</div></div></section>
<section><div class="wrap"><p class="eyebrow">{t('pe')}</p><h2>{t('ph')}</h2><p>{t('pp')}</p><div class="grid g2 g5">{ptabs}</div></div></section>
<section><div class="wrap"><p class="eyebrow">{t('de')}</p><h2>{t('dh')}</h2><div class="grid g2 g4">{decs}</div>
<div class="sw"><div><i style="background:#0B0B10"></i><span>#0B0B10</span></div><div><i style="background:#17171F"></i><span>#17171F</span></div><div><i style="background:linear-gradient(135deg,#FF3D6E,#FF7A59)"></i><span>Pace</span></div><div><i style="background:#FBBF24"></i><span>Lock</span></div><div><i style="background:#34D399"></i><span>Unlock</span></div><div><i style="background:#60A5FA"></i><span>Verified</span></div></div></div></section>
<section><div class="wrap"><p class="eyebrow">{t('xe')}</p><h2>{t('xh')}</h2><div class="grid g2 g3">{mets}</div></div></section>
<section><div class="wrap"><p class="eyebrow">{t('ce')}</p><p style="max-width:720px">{t('cp')}</p><div class="tags"><span>Product design</span><span>iOS UX</span><span>Mechanic design</span><span>HTML · CSS · JS</span><span>Claude</span></div></div></section>
<section class="final"><div class="wrap"><h2>{t('fh')}</h2><p>{t('fp')}</p><a class="btn p" style="display:inline-block" href="/contact">{t('fb')}</a></div></section>
</main>
<footer><div class="wrap"><span>© 2026 Wendel Freitas · Miami</span><span><a href="/cases">All cases</a> · <a href="https://linkedin.com/in/wendel-de-freitas">LinkedIn</a> · <a href="https://github.com/wendel-crypto">GitHub</a></span></div></footer>
<div class="ov" id="ov" translate="no"><div class="bar"><button id="ovClose" data-t="close">{C['close'][0]}</button></div><iframe id="ovf" title="RunDate live app"></iframe></div>
<script>
const C={json.dumps(C, ensure_ascii=False)},S={json.dumps([[s[1], s[2]] for s in S], ensure_ascii=False)};
const LI=()=>{{const l=(document.documentElement.lang||'en').slice(0,2);return l==='es'?1:l==='pt'?2:0}};
const LC=()=>['en','es','pt'][LI()];
const desk=matchMedia('(min-width:980px)');
const app=document.getElementById('app'),ov=document.getElementById('ov'),ovf=document.getElementById('ovf');
function send(f,msg){{try{{f.contentWindow.postMessage(msg,'*')}}catch(e){{}}}}
function loadDesk(){{if(desk.matches&&!app.src)app.src=app.dataset.src+'&lang='+LC()}}
const io='IntersectionObserver' in window?new IntersectionObserver(e=>{{if(e.some(x=>x.isIntersecting)){{loadDesk();io.disconnect()}}}},{{rootMargin:'400px'}}):null;
io?io.observe(document.getElementById('try')):loadDesk();desk.addEventListener('change',loadDesk);
function openOv(go){{const src='/rundate/app/?embed&lang='+LC()+(go?'&screen='+go:'');if(ovf.dataset.loaded&&ovf.src){{if(go)send(ovf,{{rd:'go',v:go}})}}else{{ovf.src=src;ovf.dataset.loaded=1}}ov.classList.add('on');document.body.classList.add('lock');history.pushState({{rd:1}},'')}}
function closeOv(){{ov.classList.remove('on');document.body.classList.remove('lock')}}
document.getElementById('ovClose').onclick=()=>{{history.state&&history.state.rd?history.back():closeOv()}};
addEventListener('popstate',()=>{{if(ov.classList.contains('on'))closeOv()}});
document.querySelectorAll('[data-launch]').forEach(b=>b.addEventListener('click',e=>{{if(desk.matches)return;e.preventDefault();openOv()}}));
document.querySelectorAll('#jump button').forEach(b=>b.onclick=()=>{{document.querySelectorAll('#jump button').forEach(x=>x.classList.toggle('on',x===b));const g=b.dataset.go;if(desk.matches){{loadDesk();send(app,{{rd:'go',v:g}})}}else openOv(g)}});
function applyLang(){{const l=LI();document.querySelectorAll('[data-t]').forEach(e=>{{const v=C[e.dataset.t];if(v)e.textContent=v[l]}});document.querySelectorAll('[data-s]').forEach(e=>e.textContent=S[+e.dataset.s][0][l]);document.querySelectorAll('[data-sp]').forEach(e=>e.textContent=S[+e.dataset.sp][1][l]);document.title=C.title[l];[app,ovf].forEach(f=>f.src&&send(f,{{rd:'lang',v:LC()}}))}}
new MutationObserver(applyLang).observe(document.documentElement,{{attributes:true,attributeFilter:['lang']}});
applyLang();
</script>
<script src="/wf-site.v10.js" defer></script></body></html>'''
pathlib.Path('/home/claude/rundate/site/case.html').write_text(html, encoding='utf-8')
print(len(html))
