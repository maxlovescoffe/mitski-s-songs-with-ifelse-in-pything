print('\033[1;31mWHICH MISKI SONG ARE YOU? \033[m')
print('\033[1;31mDISPONIBLE ALBUMNS: ')
print('\033[4;32m 1 = PUBERTY2')
print('\033[4;32m 2 = RETIRED FROM SAD NEW CAREER IN BUSINESS')
print('\033[4;32m 3 = BURRY ME AT A MAKE OUT CREAK')
print('\033[4;32m 4 = BE THE COWBOY')

album=input('{} type the number of your favorite album {}'.format('\033[1;35;43m','\033[m'))
if album == '1': #puberty2
    print('\033[1;35m repressed, gentleness, exhaustion, agony, nothing \033[m') 
    #repressed = dna the dancer// fireworks = melancholy // gentleness = i bet on losing dogs 
    question = str(input('which of the upper  words describe you the best? (only one!!) '))
    print('\033[1;31;45mYOU ARE.... \033[m')
    if question == 'repressed': 
        print('\033[1;35m DAN THE DANCER!  \033[m')
        print('" cause dan would never dance, outside of his room, when no one was "')
        print("you have learn from a very young age that i couln't be the way you are")
    elif question == 'gentleness':
        print('\033[1;35m I BET ON LOSING DOGS \033[m')
        print('" my baby my baby, you are my baby, say it to me "')
        print('please put yourself first')
    elif question == 'exhaustion':
        print('\033[1;35m a burning hill \033[m')
        print("'im tired of wanting more, i think i'm finally worn'")
        print("you don't feel like yourself it's been along time.")
    elif question == 'agony':
        print(" \033[1;35m MY BODY'S MADE OF CRUSHED LITTLE STARS \033[m ")
        print("I'M NOT DOING ANYTHING // I WANT TO SEE THE WHOLE WORLD")
        print(" I DON'T KNOW HOW I'M GOING TO PAY RENT")
        print("you are growing older, everything is getting more complex and complicated")
        print("and here's something you may have realized, but you don't want to face it: you are desesperate and alone")
        print("so, i must tell you: every human being feels like this too. but it's sharing this pain and rage that we learn stuff and feel seen")
        print("i promise that, someday, the capitalism and all of your pain and rage will end")
        print('because, mostly, you wish to be kind, despite all that rage')
    elif question == 'nothing':
        print("")
if album == '2': #retired from sad
    print('{}desire, loneliness, exhaustion, self-destructive{}'.format('\033[1;32m', '\033[m'))
    question = str(input('which of the upper  words describe you the best? (only one!!) '))
    print('\033[1;31;45mYOU ARE.... \033[m')
    if question == 'desire': 
        print('\033[1;32m I WANT YOU \033[m')
        print('"i just need a quiet place, where i can scream how i love you"')
        print("you see love as this giant and soul-and-body-consuming monster")
    elif question == 'loneliness':
        print('\033[1;32m SQUARE \033[m')
        print("God is very simple, and love shouldn't burn")
        print('please put yourself first')
    elif question == 'exhaustion':
        print('\033[1;32m CLASS OF 2013 \033[m')
        print("YOU SAW THIS COMING")
        print('"mom / im tired"')
        print("you don't feel like yourself it's been along time.")
    elif question == 'self-destructive':
        print('\033[1;32m HUMPTY \033[m')
        print('"all the eggshells are on the ground and i try, im trying to pick them up"')
        print('but they crack and crumble and its all too much, too frail for me to touch')
        print('no matter what you do, you always feel like you come back to this miserable and cold and lonely bathtub')
if album == '3':
    print('')
if album == '4':
