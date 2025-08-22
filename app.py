from flask import Flask, render_template_string, request, redirect, url_for, session # type: ignore

app = Flask(__name__)
app.secret_key = 'CoC'  # Change this!
PASSWORD = "Auk04"  # Change this!

SCREENPLAY = """
<pre style="white-space: pre-wrap; font-family: monospace;">
FADE IN:

EXT. FLORENCE – NIGHT

SCENE 0 – PROLOGUE INTRO

NARRATION (V.O.)
Lanterns shimmer over the gallery’s marble floors. The Duomo’s bell tolls, and for a breath, all of Florence seems to hold still. In the hush, each of you finds your place—each with secrets, suspicions, and your own reasons for attending tonight’s unveiling.

            LORENZO BELLINI
    Florence puts on her finest dress for such nights… but the shadows still slip through the seams. What secrets will tonight reveal, I wonder?

            ISABELLA CONTI
    A gathering of this sort always carries more than art on its back. One must watch not just the paintings, but the people.

            FATHER MATTEO
    God grant this night be free of wickedness. Yet my heart whispers otherwise.

            SOFIA DA REGGIO
    If there’s magic tonight, I’ll be the one to spot it. Folk in masks and art with secrets—no better place for a mystery.

---

INT. GALLERIA BELLADONNA – NIGHT

A hush of anticipation settles. The MASTER OF CEREMONIES enters, cane tapping softly on marble. Hundreds of candles play across silk and gold, shadows moving with laughter and quiet intrigue. FLORENCE'S FINEST glide through the hall beneath painted ceilings.

Near a gilded pillar, Margherita MALFI gossips loudly.

                            Margherita
           (with relish)
        They say a real artist can see the soul inside a painting—careful, or it might look back!

ISABELLA CONTI, poised and elegant, turns to LORENZO BELLINI at a nearby table cluttered with glasses and sketches.

                            ISABELLA
        Margherita never tires of her tales. But tell me, Signore Bellini, is there truth in it? Can an artist paint what ought not be seen?

                            LORENZO
        Perhaps. Paint captures what words cannot. But sometimes, the cost is more than any patron can pay.
        You’ve seen how some stare at a canvas until it stares back.

                            ISABELLA
           (softening)
        I have. Once, I found myself weeping before a portrait of a child I’d never met. The artist was blind, but the eyes in that painting—Saints preserve me—were wide awake.

The music of a lute mingles with conversation. At an open window, SOFIA DA REGGIO stands, night air on her cheek, fidgeting with her sleeve. FATHER MATTEO joins her, quiet and steady.

                            FATHER MATTEO
        You look uneasy, child. First time among Florence’s finest?

                            SOFIA
        It’s not the people that unsettle me, Father. It’s the masks. Everyone’s wearing one—even when their faces are bare.

                            FATHER MATTEO
        In this city, masks protect more than they hide. But I find honesty survives in quiet corners.
        Tell me, do you work in the arts?

                            SOFIA
        My master makes carnival masks. I bring him deliveries—sometimes to the churches.
        I’ve seen you in the cloisters, reading in the shadows.

                            FATHER MATTEO
           (gentle, laughing)
        God’s house has many shadows, Sofia. Sometimes the best place to find light is by searching in the dark.

The four are drawn together by the music and distant bells.

                            ISABELLA
           (raising her glass)
        I see I’m not the only one drawn to the city’s mysteries tonight. Friends, will you join me for a toast before the unveiling?

                            LORENZO
        To new acquaintances, and the art that binds us.

                            SOFIA
           (softly)
        To masks, and to seeing what lies beneath them.

                            FATHER MATTEO
        To truth, in whatever form it finds us.

Laughter follows, until COSIMO THE PORTER nearly loses his tray. A quick clatter, quickly hushed.

                            COSIMO
           (apologetic)
        Beg your pardons, gentles! My hands are all thumbs tonight—blame the ghosts, not the wine.

                            ISABELLA
           (smiling)
        Careful, Cosimo, or you’ll have the gallery owner’s curses to haunt you as well.

LUCREZIA BELLADONNA approaches, step light and measured.

                            LUCREZIA
        Mother says fortune smiles on those who gather beneath new moonlight.
        I say, she hasn’t seen the Master’s scowl at spilled wine.
        Shall I save you all a seat by the dais?

If curiosity about the Master is voiced, Lucrezia glances down, reverent.

                            LUCREZIA
        They say he was once a great painter, until he stared too long at his own work and saw something he could never forget.

Margherita glides past, voice low.

                            Margherita
        Have you noticed the north wing tonight? I heard a rumor the new painting was brought in just before dusk. No one’s seen it unveiled, not even the gallery’s owner.

The lights dim. Conversation fades. The MASTER OF CEREMONIES  onto the dais, every whisper silenced.

                            THE MASTER
           (raising his cane)
        Signori, signore—welcome to a night of wonder, secrets, and revelations.
        Tonight, the walls of the Galleria Belladonna shall hold more than art—they shall cradle the whispers of fate itself.
        May your eyes be keen, your hearts steady, and your wits sharpened—for not every truth is gentle, nor every beauty safe.
        Tonight, we unveil more than canvas and paint.
        Tonight, Florence bares its soul.

Lucrezia leans in, voice barely a whisper.

                            LUCREZIA
        You see what I mean? He could sell thunder to the clouds…

                            Margherita
           (smiling)
        I wager even the saints are leaning in to listen.

In a quiet shadow by a marble column, a solitary figure stands motionless. Cloaked in black, he observes the proceedings with unseen intensity, features lost in half-light—more disturbance than form.

The room cools. A bell marks the hour. The Master lowers his cane.

                            THE MASTER
           (solemn)
        Let all gathered here bear witness—whatever the hour may bring.

The hush deepens. The serious figure’s eyes narrow. Somewhere, a whisper stirs the air. The painting’s cover shivers—not with wind, but as if something beneath is waking.

Suddenly, a noble near the dais gasps, clutching his chest. He staggers, collapses—veins darkening, eyes frozen wide with terror.

Panic blooms, shattering the stillness.

FADE OUT.

                                                                                                                                                        Property of Steve-Austin Alcis
</pre>
"""

LOGIN_PAGE = '''
<form method="POST">
    <input type="password" name="password" placeholder="Enter Password">
    <input type="submit" value="Login">
</form>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('screenplay'))
    return LOGIN_PAGE

@app.route('/screenplay')
def screenplay():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template_string(SCREENPLAY)

import os
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Render provides PORT; fallback for local use
    app.run(host='0.0.0.0', port=port)