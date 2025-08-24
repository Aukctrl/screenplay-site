from flask import Flask, render_template_string, request, redirect, url_for, session # type: ignore

app = Flask(__name__)
app.secret_key = 'CoC'  # Change this!
PASSWORD = "Auk04"  # Change this!

SCREENPLAY = """
<pre style="white-space: pre-wrap; font-family: monospace;">
FADE IN:

EXT. FLORENCE – NIGHT

		SCENE 0 

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
		Scene 1

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
		Scene 2
NARRATION (V.O.)
A tremor of panic ripples across the marble, voices rising and falling like waves against stone. The noble’s lifeless form lies sprawled at the base of the dais, his elegant clothes twisted, the light in his eyes already gone. Servants shout for help. Glass breaks somewhere in the darkness.

Most guests press back, clutching loved ones or searching for the nearest exit—but some stand frozen, struck not just by fear, but by a sense that something has gone terribly, invisibly wrong.

For a heartbeat, the Master’s voice tries to steady the room, but uncertainty lingers like a cold draft through ancient halls. In the swirl of confusion, those with sharper senses—those who have seen too much, or perhaps not enough—find themselves on the edge of a decision.

Is there a threat still lurking in the crowd?  
A shadow slipping away, unseen by all but the most watchful?  
Or are the answers waiting here, hidden among faces painted with terror and masks of civility?

The choice hangs in the air—chase a fleeing phantom, tend to the dying, or search for truth before it slips through trembling fingers.

The chaos erupts. Panic and confusion swirl through the crowd.

For a brief second, the movement parts—REVEALING a BLACK-CLOAKED FIGURE slipping through a side entrance, glancing back only once before vanishing into darkness. The heavy door groans shut behind them.

		scene 3

INT. GALLERIA BELLADONNA – NIGHT

A jolt of shared understanding passes through the group. The air turns thin, tense with anticipation.

For one breathless instant, the gallery’s chaos recedes. The cries and clatter seem to echo from a distant world as your attention converges—each of you, by instinct or dread, fixated on the retreating silhouette. The black-cloaked stranger glances back once, just long enough for candlelight to gleam along a pale cheek and the hint of something strange in their eyes. Then they slip through the side entrance, the door’s heavy hinges groaning shut behind them.
                            ISABELLA
           (urgent and firm)
        We cannot let them vanish. With me—quickly!

Father Matteo murmurs a prayer, hands trembling but steadying.

                            FATHER MATTEO
           (soft, wavering then firmer)
        We don’t know who—or what—we’re following. Everyone, keep your wits. If you feel anything strange, speak up.

                            LORENZO
           (quiet, just above a whisper)
        I’ve got a bad feeling… If you see anything, say so. I’ll try to keep us on track.

Isabella looks to Sofia, who clutches her amulet, trying to sound brave.

                            ISABELLA
        Sofia, stay close, all right? We can’t afford to get separated now.

                            SOFIA
           (a tremor in her voice, nodding)
        I’m not going anywhere, Isabella. Not alone.

The group cuts through the edge of the crowd—past pale faces, trembling hands, servants frozen with shock.

They slip BEYOND THE DOOR into shadowy, stone corridors. Flickering lanterns throw uncertain shadows on the walls. Every footfall echoes with possibility.

The corridor branches. A faint footstep echoes from above. The black cloak flutters on a stairwell, vanishing upward.

                            ISABELLA
           (soft, determined)
        There—stairs. Let’s keep together. No heroes, no splitting up.

                            LORENZO
           (halfhearted humor, tight)
        Promise me someone’s watching my back, at least.

                            FATHER MATTEO
           (reassuring)
        You’re not alone, Lorenzo. We go as one.

                            SOFIA
           (almost a whisper, more to herself)
        I hope we don’t find what we’re looking for…

They ascend, steps echoing with dread. At the landing, a shaft of moonlight illuminates the far end. The figure pauses—white-faced, posture tense—then bolts for a side room. The door rattles open and shut.

For a moment, only the group's own shivering shadows remain.

                            ISABELLA
           (low, almost pleading)
        Do we follow? Or wait—what if this is what they want?

                            LORENZO
           (uncertain, but resolved)
        If we don’t go, we’ll never know. But we don’t go blind.

                            FATHER MATTEO
           (breathing deep, steadying)
        Whatever happens, we face it together.

                            SOFIA
           (trying to smile)
        Together, then.

They gather themselves, sharing a silent look of mutual protection, then step forward—into the unknown.

CUT TO BLACK.



                                                                                                                                                        Property of Steve-Austin Alcis

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