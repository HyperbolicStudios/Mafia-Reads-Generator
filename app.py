from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, RadioField

import random

hardTownReads = ["""I read PLAYER_NAME as a strong town for several reasons.
1. They're not afraid to defend their stances, and push for them, even if I disagree with them
2. They do not seem to have any coordination with any other player, scumread or otherwise.
3. They don't feel too pressured when they are pushed on.""" ,

"""PLAYER_NAME has been contributing all game and has led the lynch of multiple scum players.
Their reads have been extremely well thought out and have zero flaws.""" ,

"""PLAYER_NAME seems scummy, but I always read them wrong so I'm going to townread them for the whole game. Sorry but I'm bad at mafia.""" ,

"PLAYER_NAME is a strong town read for me because of their pushes to move out of the RVS stage and I agree with most of their posts. They are consistiently pushing for discussion instead of attempting to slow it."]

leanTownReads = ["""For PLAYER_NAME, Lean town for now, they don't really have any strong reads, but i'm not noticing any coordination with other players rn, and I don't disagree with them much.""" ,

"""I’m leaning town on PLAYER_NAME because they’ve been active and contributing to the game, asking good questions and making good points.""" ,

"""Probably town for meme quality""" ,

"PLAYER_NAME strikes me as kinda meh. I wouldn't lynch them" ,

"I’ve got a hesitant town read on PLAYER_NAME . They seem to be actively contributing to the discussion, and I agree with most of the points they have made so far."]


neutralReads = ["""I think PLAYER_NAME is neutral. Their actions don't seem like they're from someone who is scumhunting, but rather to seem helpful and stay alive. But they also seem completely uncoordinated, and aren't gravitating to, defending, or hard attacking any player in a weird way. Can't see them as part of a scum team, but also can't see them as part of town.""" ,

"I dont like how PLAYER_NAME actually plays the game. PLAYER_NAME is too aggresive for my taste and I don't like authority in this game. Hard to tell their true intentions." ,

"I’m just not able to get a good read on PLAYER_NAME. Seeing a lot of conflicting stuff. They’re generally towny by role but their actions in thread haven’t been super good. Probably a good one to wait on." ,

"I can’t make up my mind on PLAYER_NAME . A lot of their posts seem pretty towny, but some of them scream scum to me. I can’t seem to form a proper read on PLAYER."]


leanScumReads = ["for PLAYER_NAME, Leaning scum here. They're mostly piggybacking on other people, and not really posting much reads of their own. I feel like their scumteam is using them as a bridge that can agree with both their own agenda and a strong town's reads." ,

"For PLAYER_NAME, They post alot and argue. thats not good. We should probably lynch them if they don't claim." ,

"PLAYER_NAME had some interactions with dead scum that feel fake and forced. Haven’t seen much else relating to them so I’ve put them as lean scum for now, but this is good to look into" ,

"I have a scum lean on PLAYER_NAME . They seem more inactive than usual, and they seem intent on bantering instead of contributing to discussion."]


hardScumReads = ["Strong scum. Their play at EoD especially showed how they were very clearly gravitating toward certain players, defending and attacking players without directly interacting with them, etc. Scum players will forget to make fake interactions with their scummates in times of stress, so the fact that they're not speaking to the person they're defending or attacking says a lot. PLAYER_NAME also scumslipped several times, and have also been seemingly not coherent in their standards for reads, instead pushing for an agenda first, and basing their reads off that." ,

"PLAYER_NAME has a terrible claim and hasn’t been very helpful either. This is my lynch target for today" ,

"I have a hard scum read on PLAYER_NAME . Their aversion to certain questions pointed towards them is sus, and their interactions with other mafia members seem forced and fake. Their play differs from last game, in which they were town."
]
inactiveReads = ["Inactive. Their posts are either fluff or tell me little." ,

"PLAYER_NAME hasn’t done anything all game. Hoping they get replaced out soon so we can read them, but right now they’re null for me." ,

"Has PLAYER_NAME even posted today? I don’t think they have posted at all yet this phase, I want to see more from them."]



app = Flask(__name__)

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.DataRequired()])




@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)


    if request.method == 'POST':
        name=request.form['name']
        read = request.form['read']


        if form.validate():
            # Save the comment here.
            print(name)
            print(read)


            if read=="hardTown":
                maxValue = len(hardTownReads)-1
                output = hardTownReads[random.randint(0,maxValue)]
                output = output.replace("PLAYER_NAME", name)

            elif read=="leanTown":
                maxValue = len(leanTownReads)-1
                output = leanTownReads[random.randint(0,maxValue)]
                output = output.replace("PLAYER_NAME", name)

            elif read=="neutral":
                maxValue = len(neutralReads)-1
                output = neutralReads[random.randint(0,maxValue)]
                output = output.replace("PLAYER_NAME", name)

            elif read=="leanScum":
                maxValue = len(leanScumReads)-1
                output = leanScumReads[random.randint(0,maxValue)]
                output = output.replace("PLAYER_NAME", name)

            elif read=="hardScum":
                maxValue = len(hardScumReads)-1
                output = hardScumReads[random.randint(0,maxValue)]
                output = output.replace("PLAYER_NAME", name)

            elif read=="inactive":
                maxValue = len(inactiveReads)-1
                output = inactiveReads[random.randint(0,maxValue)]
                output = output.replace("PLAYER_NAME", name)

            else:

                output = "Error - read not found."
            flash(output)



        else:
            flash('Error: All the form fields are required. ')
            print("ERROR")

    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()
