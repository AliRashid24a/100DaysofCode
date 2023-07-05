# Make a choose your adventure game which uses conditionals and logic to guide a player through a series of choices.

def start_game():
    print('''
                _ ___                /^^\ /^\  /^^\_
    _          _@)@) \            ,,/ '` ~ `'~~ ', `\.
  _/o\_ _ _ _/~`.`...'~\        ./~~..,'`','',.,' '  ~:
 / `,'.~,~.~  .   , . , ~|,   ,/ .,' , ,. .. ,,.   `,  ~\_
( ' _' _ '_` _  '  .    , `\_/ .' ..' '  `  `   `..  `,   \_
 ~V~ V~ V~ V~ ~\ `   ' .  '    , ' .,.,''`.,.''`.,.``. ',   \_
  _/\ /\ /\ /\_/, . ' ,   `_/~\_ .' .,. ,, , _/~\_ `. `. '.,  \_
 < ~ ~ '~`'~'`, .,  .   `_: ::: \_ '      `_/ ::: \_ `.,' . ',  \_
  \ ' `_  '`_    _    ',/ _::_::_ \ _    _/ _::_::_ \   `.,'.,`., \-,-,-,_,_,
   `'~~ `'~~ `'~~ `'~~  \(_)(_)(_)/  `~~' \(_)(_)(_)/ ~'`\_.._,._,'_;_;_;_;_;
Once upon a time in the mystical land of Argoth, there lived a dragon named Earl. Earl was not like other dragons.
While his fiery breath and large wings made him a formidable creature, Earl had a unique obsession: buttons.
Yes, you heard it right, buttons!

Earl had a collection of buttons from all over the kingdom, big and small, colorful and plain. 
But there was one button he treasured above all others. It was a golden button with a delicate carving of a dragon, 
a perfect match for his majestic scales.

However, one dreadful evening as Earl was getting ready for bed, he noticed that his favorite button was missing!
He fears that his twin brother, Grey, stole his button out of jealousy! Anguished, Earl pleads for your help. 
    ''')
    start_input = str(input("Will you help Earl find his button? Yes or No"))
    if start_input.lower() == "yes":
        print("Earl bows his head in gratitude. You swiftly leave his cave and arrive at the crossroads outisde.")
        begin_quest()
    else:
        print("Oh my! How dare you sit idly while Earl is in such a state of sorrow! You have been executed by the"
              "people of the kingdom. GAME OVER")

def begin_quest():
    quest1 = str(input('''You have 4 options: 
1. Search Grey's Lair
2. Seek Clues in the nearby village
3. Investigate the Enchanted Forest
4. Go fishing
'''))
    if quest1 == "1":
        grey_lair()
    elif quest1 == "2":
        village()
    elif quest1 == "3":
        enchanted_forest()
    elif quest1 == "4":
        print("You notice that it is an excellently swell day outside and think to yourself,'Man I'd rather be fishin."
              "As you settle down on a nice peaceful lake with your favorite bait and reel, you slip into the lake"
              "and get mauled by a swarm piranhas. Unfortunately, you failed to notice that you were fishing at "
              "piranha lake. GAME OVER ")
    else:
        print("Please input a number to decide where to go")
        begin_quest()

def grey_lair():
    print('''
You gather your courage and agree to help Earl search Grey's lair. The dragon brothers' lairs are situated on
opposite ends of the kingdom, and it takes you a while to reach Grey's territory. As you enter the dimly lit cave, 
you notice various treasures scattered around. It seems that Grey has a fondness for shiny objects.
''')
    explore = str(input("Do you wish to continue or try another location? Yes or No."))
    if explore.lower() == "yes":
        print('''
You begin your search, carefulily inspecting every nook and cranny. Just as you're about to give up, a glint of gold 
catches your eye. It's Earl's golden button! Relief washes over you, and you quickly snatch it up. 
As you make your way back to Earl, you wonder if there's more to this story than meets the eye.
''')
        end_game(ending="grey")
    else:
        print("Deciding that Grey seems a bit spooky. You make your way back to the crossroads.")
        begin_quest()


def village():
    print('''
You decide to investigate the village to find clues about Earl's missing button. The villagers are kind and eager to
help. They tell you about a shady character named Oswald, known for his mischievous deeds. Rumor has it that Oswald has 
been pilfering valuables around the kingdom lately.

You track down Oswald's hideout, a small shack hidden deep within the village. Cautiously, you enter and start searching
for any signs of Earl's button. Amongst piles of stolen trinkets, you find a golden glimmer tucked away.

With the button in hand, you make your way back to Earl. He is overjoyed to have his treasure back but still wonders how
Oswald managed to get hold of it. Earl asks if you can confront Oswald and find out the truth.
    ''')
    oswald = str(input("Do you choose to confront Oswald? Yes or No "))
    if oswald.lower() == "yes":
        end_game(ending="oswald")
    else:
        print("Deciding that it simply ain't that deep you statisfy yourself knowing that Earl has his button and"
              "all is well in the world.\nThe End :)")

def enchanted_forest():
    print('''
You trip on a branch and smash your squishy little head. GAME OVER
    ''')

def end_game(ending):
    if ending == "grey":
        print('''
You return to Earl with the recovered button. He greets you with immense gratitude and joy. Earl's scales shimmer as he 
proudly fastens the golden button onto his shirt, completing his majestic appearance.

Overwhelmed with relief and happiness, Earl offers you a generous reward for your help. He also expresses his heartfelt 
gratitude and assures you of his everlasting friendship. As you bid farewell to Earl, you feel a sense of fulfillment for 
being part of his extraordinary button adventure.

The End :)
''')
    if ending == "oswald":
        print('''
With Earl's button safely returned, you decide to confront Oswald to uncover the truth behind his involvement. 
You locate Oswald in a dimly lit tavern on the outskirts of the village. As you approach him, he eyes you suspiciously.

You present the recovered golden button and ask Oswald about its origin. He hesitates for a moment, then a sly smile 
spreads across his face. Oswald confesses that he did indeed steal the button from Earl's lair, driven by envy of his 
brother's prized possession.

However, Oswald reveals that his intentions were not to keep the button for himself but to teach Earl a lesson about 
humility. He felt that Earl's obsession with buttons had made him arrogant and distant from others.

Deeply remorseful, Oswald promises to return the stolen button to Earl personally and apologize for his actions. 
You accompany Oswald back to Earl's lair, where he expresses his sincere remorse and asks for forgiveness.

Earl, touched by Oswald's honesty and repentance, forgives his brother. The two dragon brothers reconcile, realizing the
importance of their bond over material possessions.

As a token of gratitude for your involvement, both Earl and Oswald offer you a small gift from their treasure hoard. 
You graciously accept their presents, feeling honored to have played a part in their reconciliation.

From that day forward, Earl and Oswald learn to appreciate each other's unique qualities and share their button 
collections with joy, reminding everyone in the kingdom of Argoth that true happiness lies in friendship and forgiveness.

The End.
''')

start_game()