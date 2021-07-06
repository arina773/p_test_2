from flask import Flask, render_template


app = Flask(__name__)
result = ''


@app.route("/")
def start():
    text = """1. You are totally exhausted because your week was endless and less than great. How are you going to spend 
    your weekend? """
    choices = [
        ('','second_q', 'E', """"I'll call my friends to ask about their plans. I heard that a new restaurant opened / 
        a nice comedy is playing in the cinemas / there are big discounts at the paintball club. We should all go out 
        together. """),
        ('','second_q', 'I', """I'll switch on the ''Don't disturb'' mode on my phone and stay at home. I'll watch a new
         episode of my avorite TV show, do a puzzle, and take a long bath with a book.""")
    ]
    return render_template('adventure.html',  text=text, choices=choices, result='')



@app.route("/second/<letter>")
def second_q(letter):
    text = """2. Which of these 2 descriptions suits you more?"""
    choices = [
        (letter, 'third_q', 'S', """The most important thing for me is what's happening here and now. I assess real 
        situations and pay attention to details."""),
        (letter, 'third_q', 'N', """Facts are boring. I love to dream and play over upcoming events in my mind. I rely 
        more on intuition than information. """)
    ]
    return render_template('adventure.html', text=text, choices=choices)


@app.route("/third/<letter>")
def third_q(letter):
    text = """3. A competitor of your current employer is trying to entice you. You have doubts because the salary is much 
    higher there, but the staff here is great. Moreover, the head of your department hinted that he will recommend you 
    to the bosses when he retires. How are you going to make a decision?"""
    choices = [
        (letter, 'forth_q', 'T', """I'll learn all the available information about the competitor, ask my HR manager for
         advice, and draw a chart with all the pros and cons. In such cases, it's important to weigh up all the 
         arguments and assess the situation with a cold mind. """),
        (letter, 'forth_q', 'F', "I'll listen to my feelings. I always try to follow my heart. ")
    ]
    return render_template('adventure.html', text=text, choices=choices)


@app.route("/forth/<letter>")
def forth_q(letter):
    text = """4. Only 2 weeks are left before your close friends' wedding. How are the preparations going?"""
    choices = [
        (letter, 'result_p', 'J', """One month ago, I chose the saxophonist who will play a medley of our school 
         songs / collected the couple's photo love story / composed a poem / pressed my suit / made appointments with 
         the stylist and makeup master. I prefer to be fully armed."""),
        (letter, 'result_p', 'P', """Why prepare? I'll be having fun and enjoying myself at the party. I'll 
         improvise my wedding speech. The best things happen spontaneously.""")
    ]

    return render_template('adventure.html', text=text, choices=choices)


@app.route("/result/<letter>")
def result_p(letter):
    title = "Congrats. You are all done!"

    text = f'Your result is'
    choices = []

    types = {
        # Analysts
        'intj': ('intj.png', 'Architect', 'imaginative and strategic thinkers, with a plan for everything'),
        'intp': ('intp.png', 'Logician', 'innovative inventors with an unquenchable thirst for knowledge'),
        'entj': ('entj.png', 'Commander', 'bold, imaginative and strong-willed leaders, always finding a way - or making one'),
        'entp': ('entp.png', 'Debater', 'smart and curious thinkers who cannot resist an intellectual challenge'),

        # Diplomats
        'infj': ('infj.png', 'Advocate', 'quiet and mystical, yet very inspiring and tireless idealists'),
        'infp': ('infp.png', 'Mediator', 'poetic, kind and altruistic people, always eager to help a good cause.'),
        'enfj': ('enfj.png', 'Protogonist', 'charismatic and inspiring leaders, able to mesmerize their listeners.'),
        'enfp': ('enfp.png', 'Campaigner', 'enthusiastic, creative and sociable free spirits, who can always find a reason to smile.'),

        # Sentinels
        'istj': ('istj.png', 'Logistican', 'practical and fact-minded individuals, whose reliability cannot be doubted.'),
        'isfj': ('isfj.png', 'Defender', 'very dedicated and warm protectors, always ready to defend their loved ones.'),
        'estj': ('estj.png', 'Executive', 'excellent administrators, unsurpassed at managing things – or people.'),
        'esfj': ('esfj.png', 'Consul', 'extraordinarily caring, social and popular people, always eager to help.'),

        # Explorers
        'istp': ('istp.png', 'Virtuoso', 'bold and practical experimenters, masters of all kinds of tools.'),
        'isfp': ('isfp.png', 'Adventurer', 'flexible and charming artists, always ready to explore and experience something new.'),
        'estp': ('estp.png', 'Enterprenuer', 'smart, energetic and very perceptive people, who truly enjoy living on the edge.'),
        'esfp': ('esfp.png', 'Entertainer', 'spontaneous, energetic and enthusiastic people – life is never boring around them.'),
    }
    type = types[letter.lower()]

    return render_template('adventure.html',type=type, letter=letter, title=title, text=text, choices=choices)


if __name__ == '__main__':
    app.run(debug=True)