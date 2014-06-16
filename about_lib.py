def tablify(L,heading=False):
    T = '<table>'
    start = 0
    if heading:
        T += '<tr><th>'
        T += '</th><th>'.join(L[0])
        T += '</th></tr>'
        start = 1
    for row in L[start:]:
        T += '<tr><td>'
        T += '</td><td>'.join(row)
        T += '</td></tr>'
    return T + '</table>'

def get_data(line):
    return line.split(",")[-2:]

m = open("memory.csv")
memory = m.read()   
m.close()
memory = memory.split("\n")

def get_games():
    
    games = []

    gen = ''
    for line in memory[:-2]:
        line = get_data(line)
        #print line
        if len(games) == 0:
            games += [line]
        elif line[1] != games[-1][1] and line[1] != gen:
            # add line to games if it is a new game
            games += [line]
        else:
            if line[1] == games[-1][1] and line[0] != games[-1][0]:
                # previous game doesn't count if move outcomes are alternating
                games = games[:-1]
                # means it is a gen.py game
                gen = line[1]
        #print games

    return games

def stats(games):
    # [games,L,T,W]
    s = [0,0,0,0]
    for game in games:
        s[0] += 1
        s[ int(game[0])+2 ] += 1
    # [games,L,T,W,rate]
    s += [round(float((0.5*s[2]+s[3])/s[0]),3)]
    s = [str(stat) for stat in s]
    s[-1] = '<font color="#CC66FF">' + s[-1] + '</font>'
    return s

headings = ["Number of Games","Losses","Ties","Wins",'<font color="#CC66FF">Success Rate</font>']

def current():
    return tablify([headings]+[stats(get_games())],True)

def date(game):
    return game[1][:10]

def find(d):
    return tablify([headings]+[stats([game for game in get_games() if date(game) == d])],True)

def show_all():
    game = 0
    game_sets = []
    while game + 100 < len(get_games()):
        game_sets += [stats([get_games()[g] for g in range(game,game+100)])]
        game_sets[-1][0] = str(game + 1) + " - " + str(game + 100)
        game += 100
    game_sets += [stats([get_games()[g] for g in range(game,len(get_games()))])]
    game_sets[-1][0] = str(game + 1) + " - " + str(len(get_games()))
    return tablify([headings]+game_sets,True)

def yearOptions():
    D = []
    for game in get_games():
        if date(game)[:4] not in D:
            D += [date(game)[:4]]
    return D

def options(L,name,selected):
    O = '<select name="' + name + '" size="1"><option>'
    O += '</option><option>'.join(L)
    ' selected'.join(O.split('>'+selected))
    O += '</option></select>'
    return O
