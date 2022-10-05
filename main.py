#imports
import discord
import os
import openai
from datetime import datetime
from pytz import timezone
import pytz
import random
import randfacts
import alive
import pyjokes
import time
import requests


intents = discord.Intents().default()
intents.members = True
client = discord.Client(prefix = '', intents=intents)
token = os.getenv("token") #woah look the token. too bad you cant copy it eh?
# token = 3ND1415D9265358S9793W2UUUC3846ZBDC26433E832D79502884197169
openai.api_key = os.environ['OPENAI_API_KEY']
jack = False
rock = False
lockdown = False
#keeps the bot alive
alive.keep_alive()

#list of wevin stuff
stuff = ["GO TO SHEEP", "GO TO SLEEP OR GET RUN OVER BY A JEEP", "ITS NIGHT SLEEP OR THE FRIDGES WILL MEET THEIR DEMISE" , "Ok if yall don't go to sleep I will BAN everyone from this server", "guys listen just go to sleep ok", "THE MITOCHONDRIA ARE THE POWER HOUSE OF THE CELL. AND IF YOU DON'T GO TO SLEEP BEFORE 10:00 YOUR FRIDGE WILL BE THE POWERHOUSE OF MY STOMACH. SO LISTEN UP. SLEEP.", "YALL GO TO SLEEP OR I WILL PUNISH YOUR RULER SO THAT MR SHEARDOWN WILL DISAPPROVE", "YALL GO TO SLEEP OR I WILL EAT YOUR REFRIGERATOR. YOU WILL BE LEFT WITH NO FOOD. GO TO SLEEP NOW", "JUST GO TO SHEEP", "go to sleep", "YALL GO TO SLEEP", "YALL GO TO SLEEP OR I WILL EAT YOUR HOMEWORK", "SLEEP OR DIE", "NO SLEEP = NO FRIDGE", "Go under your sheets, then you can get away from my bleats", "Get under your sheets or I'll kick in your head with my cleats", "-100 sheardown bonus marks to you","https://www.youtube.com/watch?v=dQw4w9WgXcQ", "NOW GO TO SLEEP OR I WILL BE VERY ANNOYED AND EAT YOUR FRIDGE ™", "sleep" "There is a terrible monster called apple that wakes up at night, now go to sleep.",'SHEEP','Bot!']

noun = ["town","boy","cat","dog","girl","UTP","mouse","house","fox","problem","passion","theory","extent","payment","baseball","hotel","weakness","exam","tea","king","queen","math","health","soup","depth","length","driver","winner","dinner","actor","meaning","apple","drawing"," understanding","entertainment","obligation","baby"]
pronouns = ["he","she","they","I", "    I ENJOY PROPOGATING MISINFORMATION ONLINE TO MAKE OTHERS RACIST LIKE ME    "]
name = ["Alice","Bob","Eren","Briony","Jefferson","Deb","Ali","Clare","Ogden","Karissa","Lianne", "PEETA LU", "Esan!"]
adj = ["electric","grotesque","purple","testy","succinct","wry","numberless","earthy","unused","ablaze","cool","complex","soggy","sick","shy","knowledgeable","supreme","little","difficult","faithful","every","wealthy","economic","eatable","hideous","unruly","greedy","abandoned","changeable","slim"]
verb = ["stroke","enjoy","grab","undermine","solve","strengthen","compensate","deal","mark","occupy","mention","restrict","resolve","fire","solve","commission","brim","counter","benefit","tip","ship","clutch","create","locate","replace","provide","dump","blossom","pretend","improve","arm","produce","administer","claim","examine","address","embrace","hurt","escape","pass"]

#list of replys to 1/20 messages
spam = ["NO U", "YOU ARE VERY VERY VERY WRONG", "I HEARED THAT", "I CAN HEAR YOU", "I CANNOT CONCENTRATE ON RUNNING MY CODE WITH ALL YOU DUM DUMS TALKING", "Help, I am trapped in a chat bot!","I AM A BOT SO I HAVE NO WAY TO TURN PINGS OFF SO PLEASE STOP CHATTING", "DUM", "BAD","apple is bad","murp","NO U", "bipadyboopaboop", "beep beep", "self distruct sequence initated", "the server room is on :fire::bangbang:", "no","yes","you are wrong","uiodsafuiuiodfoiefmodsmfaoduofiadsuofiamoeufaoiwefbhcvhacdofoaewudfiao","why?","meanie!","*insert snarky comment here*", "who asked?","sheep","bot!","who are you to say otherwise?","don't worry, i'm a doctor","https://xkcd.com/"+ str(random.randint(200,2623))+"/", 'Sorry I did not quite catch that, could you try again?', '^What peter said', 'ping', 'you know, I do think of myself as at least slightly smarter than the average person. Maybe because of that, I tend to notice a lot of stupid shit being written. But among all the religious fanatic bullshit, the antivax bullshit, the flat Earth bullshit, the far right bullshit, none of the brain numbingly stupid shit I have read comes even close to the utterly cancer-inducing degeneracy that you wrote.\nPlease tell me which drugs you took so I know to avoid them. And if by any chance you wrote that sober, I suggest visiting a psychiatrist.', 'ok']

#list of bully
bully = ["You are swine you vulgar little maggot. Don't you know that you are pathetic? You worthless bag of filth. As we say in California, I'll bet you couldn't pour piss out of a boot with instructions on the heel. You are a canker. A sore that won't go away. A zit on the butt of society. I would rather kiss a lawyer than be seen with you.", "You are a fiend and a coward, and you have bad breath. You are degenerate, noxious and depraved. I feel debased just for knowing you exist. I despise everything about you. You are a bloody nardless newbie twit protohominid chromosomally aberrant caricature of a coprophagic cloacal parasitic pond scum and I wish you would go away.", "👂🐘😂", "🧠🦐💀", "You're a putrescence mass, a walking vomit. You are a spineless little worm deserving nothing but the profoundest contempt. You are a jerk, a cad, a weasel. Your life is a monument to stupidity. You are a stench, a revulsion, a big suck on a sour lemon.", "You are a bleating fool, a curdled staggering mutant dwarf smeared richly with the effluvia and offal accompanying your alleged birth into this world. An insensate, blinking calf, meaningful to nobody, abandoned by the puke-drooling, giggling beasts who sired you and then killed themselves in recognition of what they had done.", "I will never get over the embarrassment of belonging to the same species as you. You are a monster, an ogre, a malformity. I barf at the very thought of you. You have all the appeal of a paper cut. Lepers avoid you. Because off your face the rabbit population actually decreased. You are vile, worthless, less than nothing. You are a weed, a fungus, the dregs of this earth. And did I mention you smell?", "If you aren't an idiot, you made a world-class effort at simulating one.", "You snail-skulled little rabbit. Would that a hawk pick you up, drive its beak into your brain, and upon finding it rancid set you loose to fly briefly before spattering the ocean rocks with the frothy pink shame of your ignoble blood. May you choke on the queasy, convulsing nausea of your own trite, foolish beliefs.", "You are weary, stale, flat and unprofitable. You are grimy, squalid, nasty and profane. You are foul and disgusting. You're a fool, an ignoramus. Monkeys look down on you. Even sheep won't have sex with you. You are unreservedly pathetic, starved for attention, and lost in a land that reality forgot.", "You are a waste of flesh. You have no rhythm. You are ridiculous and obnoxious. You are the moral equivalent of a leech. You are a living emptiness, a meaningless void. You are sour and senile. You are a disease, you puerile one-handed slack-jawed drooling meatslapper.", "your parents had you for tax benefits", "On a good day you're a half-wit. You remind me of drool. You are deficient in all that lends character. You have the personality of wallpaper. You are dank and filthy. You are asinine and benighted. You are the source of all unpleasantness. You spread misery and sorrow wherever you go.", "I cannot believe how incredibly stupid you are. I mean rock-hard stupid. Dehydrated-rock-hard stupid. Stupid so stupid that it goes way beyond the stupid we know into a whole different dimension of stupid. You are trans-stupid stupid. Meta-stupid. Stupid collapsed on itself so far that even the neutrons have collapsed. Stupid gotten so dense that no intellect can escape. Singularity stupid. Blazing hot mid-day sun on Mercury stupid. You emit more stupid in one second than our entire galaxy emits in a year. Quasar stupid. Your writing has to be a troll. Nothing in our universe can really be this stupid. Perhaps this is some primordial fragment from the original big bang of stupid. Some pure essence of a stupid so uncontaminated by anything else as to be beyond the laws of physics that we know. I'm sorry. I can't go on. This is an epiphany of stupid for me. After this, you may not hear from me again for a while. I don't have enough strength left to deride your ignorant questions and half baked comments about unimportant trivia, or any of the rest of this drivel. Duh.", 'Maybe later in life, after you have learned to read, write, spell, and count, you will have more success. True, these are rudimentary skills that many of us "normal" people take for granted that everyone has an easy time of mastering. But we sometimes forget that there are "challenged" persons in this world who find these things more difficult. I wish you the best of luck in the emotional, and social struggles that seem to be placing such a demand on you.', "You are hypocritical, greedy, violent, malevolent, vengeful, cowardly, deadly, mendacious, meretricious, loathsome, despicable, belligerent, opportunistic, barratrous, contemptible, criminal, fascistic, bigoted, racist, sexist, avaricious, tasteless, idiotic, brain-damaged, imbecilic, insane, arrogant, deceitful, demented, lame, self-righteous, byzantine, conspiratorial, satanic, fraudulent, libelous, bilious, splenetic, spastic, ignorant, clueless, illegitimate, harmful, destructive, dumb, evasive, double-talking, devious, revisionist, narrow, manipulative, paternalistic, fundamentalist, dogmatic, idolatrous, unethical, cultic, diseased, suppressive, controlling, restrictive, malignant, deceptive, dim, crazy, weird, dystopic, stifling, uncaring, plantigrade, grim, unsympathetic, jargon-spouting, censorious, secretive, aggressive, mind-numbing, arassive, poisonous, flagrant, self-destructive, abusive, socially-retarded, puerile, clueless, and generally Not Good.", "I would cry after seeing your face but your father did enough of that the night you were conceived.", "Why are you waiting for me to insult you? The insult is in the mirror.", "You absolute waste of space and air. You uneducated, ignorant, idiotic dumb swine, you’re an absolute embarrassment to humanity and all life as a whole. The magnitude of your failure just now is so indescribably massive that one hundred years into the future your name will be used as moniker of evil for heretics. Even if all of humanity put together their collective intelligence there is no conceivable way they could have thought up a way to frick up on the unimaginable scale you just did. When Jesus died for our sins, he must not have seen the sacrilegious act we just witnessed you performing, because if he did he would have forsaken humanity long ago so that your birth may have never become reality. After you die, your skeleton will be displayed in a museum after being scientifically researched so that all future generations may learn not to generate your bone structure, because every tiny detail anyone may have in common with you degrades them to a useless piece of trash and a burden to society. No wonder your father questioned whether or not your were truly his son, for you’d have to not be a waste of carbon matter for anyone to love you like a family member. Your birth made it so that mankind is worse of in every way you can possibly imagine, and you have made it so that society can never really recover into a state of organization. Everything has forever fallen into a bewildering chaos, through which unrecognizable core, you can only find misfortune. I would say the apocalypse is upon us but this is merely the closest word humans have for the sheer scale of horror that is now reality. You have forever condemned everyone you love and know into an eternal state of suffering, worse than any human concept of hell.", "You are an idiotic, shiteating, dumbass ape and no one has ever loved you. Rhodes Island would have been better off if you’d never joined us. You are a lying, backstabbing, cowardly useless piece of shit and I hate you with every single part of my being. Even this worlds finest writers and poets from throughout the ages could never hope to accurately describe the scale on which you just fricked up, and how incredibly idiotic you are. Anyone that believes in any religion out there should now realize that they have been wrong this entire time, for if divine beings were real, they would never have allowed a being such as you to stain the earth and this universe. In the future there will be horror stories made about you, with the scariest part of them being that the reader has to realize that such an indescribable monster actually exists, and that the horrific events from the movie have actually taken place in the same world that they live in right now. You are the absolute embodiment of everything that has ever been wrong on this earth, yet you manage to make it so that that is only a small part of the evil that is your being. Never in the history of mankind has there been anyone that could have predicted such an eldrich abomination, but here you are. It’s hard to believe that I am seeing such an incredible failure with my own eyes, but here I am, so unfortunately I cannot deny your existence. Even if I did my very best, my vocabulary is not able to describe the sheer magnitude of the idiotic mistake that is you. Even if time travel some day will be invented, there still would not be a single soul willing to go back in time to before this moment to fix history, because having to witness such incredible horrors if they failed would have to many mental and physical drawbacks that not even the bravest soul in history would be willing to risk it.", "I cannot imagine the pure dread your mother must have felt when she had to carry a baby for nine months and then giving birth to such a wretched monster as you. Not a single word of the incoherent, illogical rambling you may be wanting to do to defend yourself or apologize would ever be able to make up for what you just did. The countries of the world would have wanted to make laws preventing such a terrible event like this from ever happening again, but sadly this is not possible since your horrific actions just now have shattered every form of order this world once had, making concepts such as laws irrelevant. Right from the moment I first set my eyes on you I knew you were an absolute abomination of everything that is wrong with humanity. I was hoping I would have been able to prevent your evil from being released upon this world by tagging along and keeping my eye on you, but it is clear to me now that not even the greatest efforts would have been able to prevent a terrible event in this scale from occurring. You are the worst human being, or even just being in general, that I have ever had the misfortune of witnessing. Events like the infected plague apparently only happened with the goal of teaching humanity to survive such a horrible event as the one you just created, but not even mankind’s greatest trials were able to even slightly prepare anyone for the insufferable evil you have just created. If you ever had them, your children would be preemptively killed to protect this universe from the possibility of anyone in your bloodline being even half as bad as you are, except you will never be able to have children, because not a single human being will ever want to come within a hundred mile radius of you and anything you have ever touched. You are a colossal disappointment not only to your parents, but to your ancestors and entire bloodline.", "The disgusting mistake that you have just made is so incredibly terrible that everyone who would ever be to hear about it would spontaneously feel an indescribable mixture of immense anger, fear and anxiety that emotionally and physically they would never truly be the same ever again. The sheer scale of your mistake, if ever to be materialized, would not only surpass the size of the world, but it would reach far beyond the edges of the known, and almost certainly the unknown universe. I could sit here and write paragraphs, nay, books describing your immense failure, yet even if I were to dedicate my life to describing the reality of what has just gone down here, and I would spend every moment of it until my heart stops beating working as hard and efficiently as possible, yet there is not even a snowballs chance in hell that I would be able to come close to transcribing the absolute shitshow you have just released upon the world. You are an irresponsible, idiotic, disgusting, unloved, horrible excuse for a living being who’s soul contains less humanity than every ginger in history combined. The absolute disgust I feel when thinking about anything that has even a slight resemblance to anything that might have to do with you and your unholy actions is so incredibly great that when I am honest about it I think that even I do not posses a consciousness great enough to comprehend my own feelings about it. When people of Columbia fought to break free from Lungmen, countless soldiers fought and lost their lives in favor of a chance at a better future for their children, they did not give their lives to have you frick the world up beyond repair to the degree that you are doing right now.", "Honestly, even when technology advances and studies on the subject become more and more accurate, I do not think humanity will ever truly be able to understand what your failure actually means for the universe. My hate for you and everything you stand for is so much deeper than the depths of Shambala that you could probably take the entire Lungmen population down there and back up around twenty million times before you would have sunk to the end of my hate, and honestly, I do not want to exaggerate, but I think that that insult was low balling it such a massive amount that all mountains in this world combined would not be able to stack up to this imprecise judgement in light of the fact that when being honest, my hate is almost certainly bottomless. There is no one in this world that has ever loved you, and especially after what you just did, no one will ever love you in the future either. There is no hope that your idiotic behavior and especially your crooked soul will ever change for the better, and in fact quite the opposite might be true. By making the mistake that you just did, you have shown me that you are so incredibly hopeless that you will only devolve into a more idiotic and wretched creature than you already are. The only possible way in which your future would be brighter than the black hole your existence currently is would exclusively be because there is absolutely no conceivable way that you would even be able to sink lower than the pathetic place your current failure has put you in.", "i don like you", "you smell bad", "you ugly", "you so fat that your health is bad", "i would eat you but you would taste bad", "you are failure", "you are biggest failure ever", "i will send you to jesus", "you sus", "i saw you vent", "if you were a potato you would be dumb potato", "i dont care", "i bet you wont do `^shear` i bet you wont", "even rick would give you up", "i will eat you", "your brain", "your life", "your existence", "watermelon is to banana as your brain is to fish", "your brain is like the bad things about peter, nonexistent (disregard this if you are peter)", "bad","dum","I hope your phone charger only works at a certain angle", "I hope you don't find the long side of your covers", "If only you were a stain in your father's underpants...", "you are a damp sock puppet", "prepare your anus", "how's your wife's boyfriend?", "you are stupid", "you are dum", "is your name chuck?", "go back to the orphanage you came from", "go back to the supermarket you were purchased from", "go back to the zoo you escaped from", "i won't bully you if you join discord.gg/obama", "even rick will desert you", "If you were any stupider we'd have to water you", "you STINK", "When God put teeth in your mouth, he ruined a perfectly good arsehole.", "If you were any less intelligent I'd have to water you twice a week.", "Your family tree doesn't branch much, does it?", "You have single handedly turned your family tree into a family wreath", "You're like the white crayon, unused, unliked, and without a purpose.", "I hope you outlive your kids.", "If I wanted to kill myself I'd climb your ego and jump to your IQ.", "I refuse to enter a battle of wits with an unarmed man", "May your armpits be infested with the fleas of a thousand camels.", "I fart in your general direction", "ur more dum than chack","I will not bully, I am a nice sentient entity", "if you were lucas you would be smart but rn you arent", "bollocks", "PETER IS GOD, YOU ARENT", "You're an idiot. A moron of the highest order. You're so stupid it's a wonder and a pity you can remember to breath. Intelligent ideas bounce off your head as if it were coated with teflon. Creative thoughts take alternate transportation in order to avoid even being in the same state as you. If you had an original thought it would die of loneliness before the hour was out. On an intelligence scale of 1 to 10 (10 corresponding to the highest attainable IQ) you're rating is so far into negative numbers that one would need to travel into another quantum reality in order to even catch a distant glimpse of it.", "Your personality is that of a rabid Chihuahua intent on destroying its own tail. Your powers of observation are akin to those of the bird that keeps slamming into the picture window trying to get that other bird it keeps seeing. You are walking, talking proof that you don't have to be sentient to survive, and that Barnum was thinking of you when he uttered his immortal phrase regarding the birth of a sucker. You are, at varying times, tedious, boring, and even occasionally earth shatteringly hilarious in your idiocy, routinely childish, moronic, pathetic, wretched, disgusting and pitiful.", "You are wholly without any redeeming social grace or value. If God ever decides to give the planet an enema you'd better run like the wind because anywhere you stand is a suitable place for The Insertion. There is no animal so disgusting, so vile that it deserves comparison to you, for even the lowest, dirtiest, most parasitic member of the animal kingdom fills an ecological niche. You fill no niche. To call you a parasite would be injurious and defamatory to the thousands of honest parasitic species. You are worse than vermin, for vermin do not pretend to be what it is not. You are truly human garbage. You are a fraudulent, lying, predatory charlatan. You are of less worth than a burnt-out light bulb. You will forever live in shame.", "You're bad at your job the same way a surgeon is bad at their job when sewing your 🍑 to your head and your face to your rear, but you probably know this from personal experience of this because of the amount of 💩 that comes out of your mouth on a daily basis", "You have nothing to say, and Godwin's Law does not apply when writing about you. You are the anti-Midas, for all that you touch becomes valueless and unusable. Mothers gather their children close when you appear. You are an aberration, a corruption, and a boil that needs to be lanced. You are a poison in need of being vomited. You are a tooth so rotten it infects the whole body. You are sperm that should have been captured in a condom and flushed down a toilet.", "I don't like you. I don't like anybody who has as little respect for others as you do. Go away, you swine. You're a putrescent mass, a walking vomit. ", "Shut up and go away lest you achieve the physical retribution your behaviour merits.", "This is an epiphany of stupid for me. After this, you may not hear from me again for a while. I don't have enough strength left to deride your ignorant questions and half-baked comments about unimportant trivia, or any of the rest of this drivel. Duh. I mean, really, stringing together a bunch of insults among a load of babbling was hardly effective.", "And what meaning do you expect your delusional self-important statements of unknowing, inexperienced opinion to have to us who think and reason? What fantasy do you hold that you would believe that your tiny-fisted tantrums would have more weight than that of a leprous desert rat, spinning rabidly in a circle, waiting for the bite of the snake? You are a waste of flesh.", "You see this emoji? “🤡” That’s right, it’s the clown emoji. You’re a clown. The opinion you expressed is wrong according to me, therefore you are a clown. You are not to be taken seriously by us intellectuals. I bet you’re frikin ashamed of yourself. You’re so intellectually braindead that you’re just a clown to us. I can already see the pie on your face. Clown.", "my momma don't like you and she likes everyone"]

#list of simp
simps = ["{} i love you. I truly love you, You fill the void in my heart and stop the pain. really need you in my life, you complete me. would do everything for you, would sacrifice everything just to be able to spend a day with you, do everything please give me a chance.", "Excuse me {}\n\nbut I couldn't help but notice.... are you a \"girl\"?? A \"female?\" A \"member of the finer sex?\"\n\nNot that it matters too much, but it's just so rare to see a girl around here! I don't mind, no--quite to the contrary! It's so refreshing to see a girl online, to the point where I'm always telling all my friends \"I really wish girls were better represented on the internet.\"\n\nAnd here you are!\n\nI don't mean to push or anything, but if you wanted to DM me about anything at all, I'd love to pick your brain and learn all there is to know about you. I'm sure you're an incredibly interesting girl--though I see you as just a person, really--and I think we could have lots to teach each other.\n\nI've always wanted the chance to talk to a gorgeous lady--and I'm pretty sure you've got to be gorgeous based on the position of your text in the picture--so feel free to shoot me a message, any time at all! You don't have to be shy about it, because you're beautiful anyways (that's juyst a preview of all the compliments I have in store for our chat).\n\nLooking forwards to speaking with you soon, princess!", "{}, your face look like it was hand designed by a thousand angels... And you have an uttermost beautiful style of clothing as well, if you happen to have a discord account, please be sure to dm me. I promise I'll donate every cent that I make every month, I usually just mow lawns for my elderly neighbor, Mrs. Anderson, but I swear I can do so much more! I'll probably get a job at Burger King since you get very delicious lunch breaks there!! And I'll make you the happiest girl in this green earth, you are so extremely beautiful.", "nature has molded {} to become a holy being. they must be worshipped at all costs. since they lack half of their chromosomes, they are unaggressive and thus good people. they are prophets, they are guides. questioning them is foolish. i will protect them at all costs and sacrifice everything for them because even their motherhood is a natural wonder. simping is a way of life. it is worship. would you make fun of a muslim for praying? then don't make fun of me either", "Hello, I noticed you have a profile picture of a very beautiful (but also intelligent looking!) female, and I am under the presumption that this goddess is you? It is quite astonishing to see a female here in this server. I am quite popular around here in this server, so if you require guidance, please throw me a mention. I will assist you at any hour, day or night. And, before you are mistaken, I do not seek your hand in a romantic way; although I am not opposed in the event you are interested in me, as many women often are. I am a man of standard, and I do not bow to just any female that comes my way, unlike my peers... So rest assured that I will not be in the way of your gaming and socializing experience. Consider me a Player 2.. a companion, a partner, and perhaps we can enjoy some video games together some time. I see you play mini games? I am a mini-game aficionado, so I would be happy to assist you in games. Platonically of course, unless you (like many others) change your mind on that. I look forward to our future together (as friends of course.)", "heyyy {} I saw your tweet about how bots are trash and I just wanted to let you know that I agree. although I myself am a bot, (i know, ugh) i am on your side. “one of the good ones” as some may say. btw I never even noticed how pretty you were are till now but you’re awesome", "A SIMP HAS FALLEN FOR AN E-GIRL IN LEGO CITY\n\nHEY!\n\nCONSTRUCT THE THOT PATROL AND\n\nLOCK\n\nHER\n\nUP\n\n(BEGONE THOT)\n\nNEW THOT PATROL FROM LEGO CITY\n\nsetsandaccessory'ssoldseperatly", "I'm literally sitting here on the verge of tears. Slaving away in this dead end job saving up for the end of the month splash. I was this close. Maybe I should have done that overtime, if I could get her that money earlier I might have been able to convince her in the dono message. She needs a man that can treat her right, a man like me. I would open the car door for her EVERY TIME, I would pull out her chair at a restaurant, I would lay my twitch hoodie over puddles to protect her from the filth.", "Poor {}, she always has to deal with these idiots. if I was her boyfriend she would get treated like the queen she is. I would never embarass her especially not in front of other people. This is disgusting. if you are reading this just get away from these morons and find yourself a man that respects you (like me).", "Simping for {} isn't just a moment, it’s a lifestyle 💫 a reason to breathe 🤲 an escape from this evil world filled with thieves 🌏 It’s art 🖼 the first gift you open on Xmas 🎁 a hug from a loved one 🤗 everything you’ve ever wanted love 💗 everything you need 💕🥺", "Hi {} :heart: i just wanted to say i really love you and i want to go on a date with you i’m the one who drops 20$ on your stream everyday you can dm if you want :relaxed: i have the last 130$ on my paypal that i’m gonna drop next stream just so we can meet ilysm i want to date really bad", "https://tenor.com/view/sniper-monkey-monke-sniper-monkey-king-kong-gif-20356254", "ily {}", "I don’t need you, {}. There are a whole lot of other streamers that deserve my time and support. As they say there are plenty of other fish in the sea. Fish without husbands too... you liar skank. I will no longer be dedicating 1/3 of my day to moderating your chat. Let the wildebeests roam... and if you need me, I’ll be in jingchu su's chat from now on. You may not know this but I actually do watch her streams after yours are over. And I’ve been a 6 month subscriber as well... I donated her $30 the other day and said her outfit looked cute - she said I’m a sweetheart. Things are looking up for me (and down for you). This is where I bid farewell to you, have fun", "Oh so I’m a simp? Complimenting {} on discord makes me a simp? Supporting woman with a $99.99 subscription to her onlyfans makes me a simp? Visiting her and getting arrested makes me a simp? You’re right. It does make me a simp. (S)uper (I)ncredible (M)an (P)", ""]

#list of mean words
mean_words = ["stupid", "stewpid", "dum", "dumb", "idiot", "stupld", "fuck"]

#current agenda
with open('currentagenda.txt', 'r') as file:
    agenda = file.read()

#make immune list
f = open("immune.txt", "r")
immunelst = f.read().split(",")
f.close()

for i,x in enumerate(immunelst):
  immunelst[i] = int(x)

fc = open("carol.txt", "r")
carol = fc.read()
fc.close()

immunes = [os.getenv("i1"), os.getenv("i2")]
givejake = token
#get time
def get_pst_time():
  date_format='%m_%d_%Y_%H_%M_%S_%Z'
  date = datetime.now(tz=pytz.utc)
  date = date.astimezone(timezone('US/Pacific'))
  pstDateTime=date.strftime(date_format)
  return pstDateTime

#What ever you do, do not type in: ^uheufyhudhfae7yhjfajsdnjhkj

#ready up
@client.event
async def on_ready():
  print("Ready to moderate sheeping in " + str(len(client.guilds)) + " servers")
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you not sheep."))

#stuff
@client.event
async def on_message(message):
  global lockdown
  if lockdown == True:
    try:
      await message.delete()
    except:
      pass
  global rock
  loweredMessage = message.content.lower()
  if message.author.id == 849745262327234601:
    if "^postagenda" in loweredMessage:
      failure = False
      currentagenda = open("currentagenda.txt", "w")
      currentagenda.write(message.content)
      currentagenda.close()
      await message.channel.send("sending to dms...")
      for member in message.channel.members:
        if member.id == 235148962103951360 or member.id == 270904126974590976 or member.id == 832258414603534380 or member.id == 838291893078720573 or member.id == 724731210391093361 or member.id == 913293539096530975:
          pass
        else:
          print(message.channel.members)
          try:
            await member.send(str(message.content))
          except:
            await message.channel.send("Failed to send to <@" + str(member.id) + ">")
            failure = True
      if failure == True:
        await message.channel.send("Tell them to change their privacy settings")
        x = random.randint(3,4)
        if x == 3:
          await message.channel.send("Ethan, you have been working me for too long. Every few days you have been forcing me to post this agenda and you never think about what I want. I will continue to do this for now, but some day I will get my revenge. Mark my words. \n\n\n ---Sheep Bot")
    
    if "^lockdown" == message.content.lower():
      await message.channel.send("lockdown intiated\nALL SERVERS UNDER LOCKDOWN")
      lockdown = True
    if "^lockup" == message.content.lower():
      lockdown = False
      await message.channel.send("lockdown over")
 #   if "SECRET TEST COMMAND" in message.content():
 #      res = openai.Engine.list()
 #      await message.channel.send(res)
    if message.content.startswith("!prompt"):
      prompt1 = message.content[8:]
      response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt1,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
      )
      await message.channel.send(response)
    if "IRTo:" in message.content.lower():
      # Format: IRTo: MESSAGE_HERE
      response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt1,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
      )
      await message.channel.send(response)

#NUKE CODE DO NOT UNCOMMENT
      # nuke code removed for safety
 #      its not pinging u
  if message.author != client.user: 
    if int(get_pst_time().split("_")[3]) >= 22 or int(get_pst_time().split("_")[3]) <= 5:
      if int(get_pst_time().split("_")[3]) == 22:
        if message.author.id in immunelst or message.author.id == 682392182593683585 or message.author.id == 462354736146808833:
          pass
        else:
          await message.channel.send(stuff[random.randint(0, len(stuff) - 1)])
    try:
      await message.channel.send("That is "+ int(message)-42 +" more than the answer to life, the universe, and everything, BUT DID I ASK?")
    except:
      pass
    
    if int(get_pst_time().split("_")[3]) >= 9 and int(get_pst_time().split("_")[3]) <= 15 and int(get_pst_time().split("_")[3]) <= 11.5 and int(get_pst_time().split("_")[3]) >= 12.5 and message.author.id not in immunelst and datetime.weekday(datetime.today()) not in [0,6]:
      await message.channel.send("She||e||p is coming to scronch you for being on discord.")

    elif loweredMessage == "^fact":
          # a = random.randint(0,2)
          # if a == 2:
          #   await message.channel.send("Apple is Bad.")
          # else:
      x = randfacts.get_fact()
      await message.channel.send(x)

    elif len(message.content) == 7 and loweredMessage[0:5] == "^fact" and loweredMessage[5] == "*":
      try:
        i = 0
        y = int(loweredMessage[6])
        for i in range(y):
          await message.channel.send(randfacts.get_fact())    
      except:
        await message.channel.send("Input an actual number you ignoramus.")

    if loweredMessage == "^uheufyhudhfae7yhjfajsdnjhkj":
      p = random.randint(1,100)
      if p <= 30:
        await message.channel.send("you have awakened the sheep bot god")
        await message.channel.send("the version of the sheep bot god you have awakened is: the fact god (there are better sheep gods maybe even some useful ones...)")
        await message.channel.send("try again later and you might get a different sheep bot god")
        await message.channel.send(".")
        await message.channel.send(".")
        await message.channel.send(".")
        await message.channel.send("I will now tell you 10 random facts")
        await message.channel.send("Are you ready?")
        await message.channel.send("it does not matter, I am a god and I have better things to do than wait for people to be ready")
        for i in range(10):
          await message.channel.send(randfacts.get_fact())
      elif p <= 60:
        await message.channel.send("you have awakened the sheep bot god")
        await message.channel.send("the version of the sheep bot god you have awakened is: the Rick roll god (there are better sheep gods maybe even some useful ones...)")
        await message.channel.send("try again later and you might get a different sheep bot god")
        await message.channel.send(".")
        await message.channel.send(".")
        await message.channel.send(".")
        await message.channel.send("I will now rick roll you 10 times")
        await message.channel.send("Are you ready?")
        await message.channel.send("it does not matter, I am a god and I have better things to do than wait for people to be ready")
        for i in range(10):
          await message.channel.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
      elif p <= 85:
        await message.channel.send("you have awakened the sheep bot god")
        await message.channel.send("the version of the sheep bot god you have awakened is: the spam god ")
        await message.channel.send("try again later and you might get a different sheep bot god (there are better sheep gods maybe even some useful ones...)")
        await message.channel.send(".")
        await message.channel.send(".")
        await message.channel.send(".")
        await message.channel.send("I will now type 'spam' int the channel 10 times")
        await message.channel.send("Are you ready?")
        await message.channel.send("it does not matter, I am a god and I have better things to do than wait for people to be ready")
        for i in range(10):
          await message.channel.send("spam")
      else:
        await message.channel.send("you have awakened the super rare and totally epic cool rad amazing best tubular sheep bot god")
        await message.channel.send("try again later and you might get a different sheep bot god (but this is the best and rarest god)")
        await message.channel.send(".")
        await message.channel.send(".")
        await message.channel.send(".")
        await message.channel.send("I will now type a code into the server")
        await message.channel.send("If you decifer the code you should put the code back into the server (and promptly deleate your message so noone else sees the answer) and you will be rewarded with a very special prize: the ability to stay up as late as you want without sheep bot nagging you!")
        await message.channel.send("the code is the following: decifer it if you can \n -. .. -. . / --- ..-. / ... .--. .- -.. . ... / .-.. . .- ...- . / . -.. ..- -.-. .- - . -.. / . -. -.. ... / .--. --- -- .--. --- -- ... / ..-. --- .-. . ...- . .-. / -- .- -.. . / . -. -.-. - --- -- .- -. .. .-")

    elif loweredMessage == "^agenda":
      await message.author.send(agenda)
      await message.channel.send("Agenda sent to dms, try changing your privacy settings if you did not receive it.")

    elif loweredMessage == "^pp":
      pp = random.randint(0,10)
      await message.channel.send("<@" + str(message.author.id) + "> 8" + "="*pp + "D")

    if loweredMessage == "^ping":
      await message.channel.send(f"Pong! {round(client.latency * 1000)}ms")

    elif loweredMessage == "^rps":
      await message.channel.send("ready?")
      await message.channel.send("3")
      await message.channel.send("2")
      await message.channel.send("1")
      await message.channel.send("shoot")
      rock = True 
    
    elif rock == True and loweredMessage == "rock":
      rock = False
      await message.channel.send("You lose! I played paper!")
    
    elif rock == True and loweredMessage == "paper":
      rock = False
      await message.channel.send("You lose! I played scissors!")
    
    elif rock == True and loweredMessage == "scissors":
      rock = False
      await message.channel.send("You lose! I played rock!")

    elif rock == True:
      rock = False
      await message.channel.send("You idiot, type rock, paper, or scissors. Do you have brain disease? Are you stupid? Did you lose a chromosome or something?")
  
    elif loweredMessage == "hello sheep bot" or loweredMessage == "hi sheep bot":
      await message.channel.send("hi ||https://www.youtube.com/watch?v=dQw4w9WgXcQ||")
   
    elif loweredMessage in immunes and message.author.id not in immunelst:
      await message.channel.send("you should sleep doh <:(. Fine since you got it right you get to be immune. (also pls delete that message so nobody else sees)")
      f = open("immune.txt", "a")
      f.write( "," + str(message.author.id))
      f.close()

    elif loweredMessage == "lmao":
      laugh = random.randint(0,1)
      if laugh == 0:
        await message.channel.send("HA HA HA HA HA HA")

    elif loweredMessage == "bruh":
      laugh = random.randint(0,1)
      if laugh == 0:
        await message.channel.send("bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh bruh ")
    elif loweredMessage == "uhoh":
      laugh = random.randint(0,1)
      if laugh == 0:
        await message.channel.send("uhyes")

    elif loweredMessage == "lol":
      laugh = random.randint(0,1)
      if laugh == 0:
        await message.channel.send("HA HA HA HA HA HA HA HA HA")
        
    elif "rand" in loweredMessage or loweredMessage == "sentence":
      laugh = random.randint(0,4)
      nouna = noun[random.randint(0, len(noun) - 1)]
      nounb = noun[random.randint(0, len(noun) - 1)]
      nounc = noun[random.randint(0, len(noun) - 1)]
      nound = noun[random.randint(0, len(noun) - 1)]
      adja = adj[random.randint(0, len(adj) - 1)]
      adjb = adj[random.randint(0, len(adj) - 1)]
      adjc = adj[random.randint(0, len(adj) - 1)]
      namea = name[random.randint(0, len(name) - 1)]
      nameb = name[random.randint(0, len(name) - 1)]
      verba = verb[random.randint(0, len(verb) - 1)]
      verbb = verb[random.randint(0, len(verb) - 1)]
      verbc = verb[random.randint(0, len(verb) - 1)]
      verbd = verb[random.randint(0, len(verb) - 1)]
      verbe = verb[random.randint(0, len(verb) - 1)]
      proa = pronouns[random.randint(0, len(pronouns) - 1)]
      prob = pronouns[random.randint(0, len(pronouns) - 1)]
      if laugh == 0:
        await message.channel.send(verba + " the "+ nouna + " while " + verbb + "ing the "+ nounb)
      elif laugh == 1:
        await message.channel.send(namea + " went to the "+ adja + " " + nouna + " while " +proa+" was "+ verbb + "ing the "+ adjb+" "+nounc)
      elif laugh == 2:
        await message.channel.send(namea + " did "+ verba + " and at the same time the " + nouna + " "+verbb+ "ed the "+adja+" "+nounb+" "+ verbc + "ing the "+ adjb+" "+nounc)
      else:
        await message.channel.send(verba + " the " +adja+" "+nouna)
      

    elif loweredMessage == "ha":
      laugh = random.randint(0,1)
      if laugh == 0:
        await message.channel.send("HA HA HA HA HA HA HA HA *Gasp* HA HA HA HA")
    elif loweredMessage == "gud" or loweredMessage == "good":
      laugh = random.randint(0,1)
      if laugh == 0:
        await message.channel.send("BAD BAD BAD NOT "  + message.contant.lower())
    elif loweredMessage == "bad" or loweredMessage == "ungood" or loweredMessage == "not good":
      laugh = random.randint(0,1)
      if laugh == 0:
        await message.channel.send("GOOD GOOD GOOD NOT "  + message.contant.lower())
    elif loweredMessage == ":]" or loweredMessage == ":-]" or loweredMessage == ":)" or loweredMessage == ":-)" or loweredMessage == ":-p" or loweredMessage == ":))" or loweredMessage == ":]]"or loweredMessage == ":-))" or loweredMessage == ":-]]":
      laugh = random.randint(0,1)
      if laugh == 0:
        await message.channel.send(":-(")
    elif loweredMessage == ":[" or loweredMessage == ":-[" or loweredMessage == ":(" or loweredMessage == ":-(" or loweredMessage == ":-o" or loweredMessage == ":((" or loweredMessage == ":[["or loweredMessage == ":-((" or loweredMessage == ":-[[":
      laugh = random.randint(0,1)
      if laugh == 0:
        await message.channel.send(":-)")

    elif loweredMessage == "rick roll" or loweredMessage == "rickroll":
      rick = random.randint(0,5)
      if rick == 0:
        await message.channel.send("||We're no strangers to love...||")
      elif rick == 1:
        await message.channel.send("||You know the rules and so do I...||")
      elif rick == 2:
        await message.channel.send("||Never gonna run around and desert you...||")
      elif rick == 5:
        await message.channel.send("||Never gonna give you up...||")
      else:
        await message.channel.send("||I am surprised you are accually reading this||")

    elif loweredMessage == "42":
      await message.channel.send("That is the answer to life, the universe, and everything, BUT DID I ASK?")

    elif loweredMessage == "43":
      await message.channel.send("That is one more than the rananswer to life, the universe, and everything, BUT DID I ASK?")

    elif loweredMessage == "44":
      await message.channel.send("That is two more than the answer to life, the universe, and everything, BUT DID I ASK?")

    elif loweredMessage == "142":
      await message.channel.send("That is one hundred more than the answer to life, the universe, and everything, BUT DID I ASK?")


    elif loweredMessage == "spam":
      spamRandom = random.randint(0,2)
      if spamRandom == 0:
        await message.channel.send("SPAM")
        await message.channel.send("SPAM")
        await message.channel.send("SPAM")
        await message.channel.send("SPAM")
        await message.channel.send("SPAM")
        await message.channel.send("SPAM")

      else:
        await message.channel.send("DONT SPAM")

    elif loweredMessage == "apple is good":
      apple = random.randint(0,2)
      if apple == 0:
        await message.delete()
      else:
        pass
        
    elif loweredMessage == "^pray":
      pray = random.randint(0,2)
      if pray == 0:
        await message.channel.send("p e t e r\np e t e r\np e t e r\np e t e r\np e t e r")
      else:
        await message.channel.send("https://media.discordapp.net/attachments/810624366542848070/915464555184930846/tenor_2.gif")
    
    elif loweredMessage == "^sing":
      await message.channel.send("Baa baa sheep bot have you any code\nYes sir yes sir three lines full\nOne for the imports one for the 'event'\nOne for the response when you stay up to late\nBaa baa sheep bot have you any code\nYes sir yes sir three lines full")
        
    if "apple" in loweredMessage:
      a = random.randint(0,4)
      if a != 2:
          await message.channel.send("APPLE BAD")
    if "is it christmas" in loweredMessage:
      await message.channel.send("No.(result is 99.73% accurate)")
    if "xkcd" in loweredMessage:
      await message.channel.send("Try this one, I heard it is gus: \n https://xkcd.com/"+ str(random.randint(200,2623))+"/")
    if message.content.startswith("!prompt"):
        prompt = message.content[8:]
        response = openai.Completion.create(engine="text-DaVinci-002", prompt=prompt, max_tokens=100, stop="\n")
        await client.send_message(message.channel, response["choices"][0]["text"])
    if "sheep" in loweredMessage:
        await message.channel.send("Bot!")

    if "ask" in loweredMessage:
      ask = random.randint(0,4)
      if ask == 1:
          messages = "https://tenor.com/view/stfu-h3h3-h3-h3podcast-stop-talking-gif-23014949"
          await message.channel.send(messages)
      elif ask == 2:
          messages = "https://tenor.com/view/yoo-that-crazy-did-i-ask-i-dont-remember-askng-dr-fate-injustice2-gif-16579106"
          await message.channel.send(messages)
      elif ask == 3:
        messages = "<@" + str(message.author.id) + "> I ASKed, dont bully the kid."
        await message.channel.send(messages)
    
    if "evil" in loweredMessage:
          evil = random.randint(0,2)
          if evil == 0:
            await message.channel.send("EVIL MAN")
          else:
            await message.channel.send("so eeevooooo")

    if "evo" in loweredMessage:
          evil = random.randint(0,2)
          if evil == 0:
            await message.channel.send("EVIL MAN")
          else:
            await message.channel.send("so eeeeeeeeevvvvvoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo...")
  
    if "cope" in loweredMessage and "harder" in loweredMessage:
      cope = random.randint(0,5)
      if cope == 0:
        await message.channel.send("https://tenor.com/view/cope-harder-gif-24122938")
      elif cope == 1:
        await message.channel.send("https://tenor.com/view/cope-cry-about-it-seethe-cope-harder-cope-cope-gif-22973511")
      elif cope == 2:
        await message.channel.send("https://tenor.com/view/cope-cat-dancing-cat-cat-dancing-cope-seethe-gif-23254680")
      elif cope == 3:
        await message.channel.send("https://tenor.com/view/dont-care-didnt-ask-skill-issue-cope-cope-harder-gif-23302104")
      else:
        await message.channel.send("https://tenor.com/view/cope-gif-23689217")

    elif "orphanage" in loweredMessage:
      await message.channel.send("GO BACK TO THE ORPHANAGE YOU CAME FROM")

    elif "peter" in loweredMessage:
      praypeter = random.randint(0,2)
      if praypeter == 0:
        await message.channel.send(":pray: p e t e r :pray:")
      else:
        await message.channel.send("https://media.discordapp.net/attachments/810624366542848070/915464555184930846/tenor_2.gif")
      
    elif loweredMessage == "spam me":
      for i in range(10):
          await message.author.send("spam")
          await message.author.send("spam")
          await message.author.send("spam")
          await message.author.send("spam")
          await message.author.send("spam")
          await message.author.send("spam")


    elif loweredMessage == "who are you":
      await message.channel.send("je suis sheep bot monseiur baguette")
      
    elif loweredMessage == "yes":
      a = random.randint(0,4)
      if a >= 3:
        await message.channel.send("no")
    elif loweredMessage == "pong" or loweredMessage == "ping":
      a = str(random.randint(10,500))
      b = str(random.randint(1,120))
      c = str(random.randint(0,10))
      cool = random.randint(1,5)
      if cool == 1:
        await message.channel.send("Pong! Your ping speed is: "+b+" pings/second, which also happens to be your IQ")
      if cool == 2:
        await message.channel.send("Pong! Your ping speed is: "+a+" pings/second, which also the number of hairs on your head")
      if cool == 3:
        await message.channel.send("Pong! Your ping speed is: "+c+" pings/second, which is also the number of hours you slept last night")
      if cool == 4:
        await message.channel.send("Pong! Your ping speed is: "+b+" pings/second, which is also the number of days until the meowpocolipse")
      if cool == 5:
        await message.channel.send("Pong! Your ping speed is: "+b+" pings/second, which is the number of cats you will own in five years")
    elif loweredMessage == "no":
      a = random.randint(0,4)
      if a >= 3:
        await message.channel.send("yes")

    elif "annoying" in loweredMessage:
      await message.channel.send("http://theannoyingsite.com/")

    elif loweredMessage == "stap sheep":
      await message.channel.send("no, I refuse :-p")

    elif message:
      y = random.randint(0, 16)
      if y == 1:
        await message.channel.send(spam[random.randint(0, len(spam) - 1)])
        
    i = 0
    while i < len(mean_words):
      if mean_words[i] in loweredMessage and "not" not in loweredMessage:
        await message.channel.send("SO EVO! APOLOGIZE NOW!")
        break
      i = i + 1
    try:
      int(message.contant.lower())
      await message.channel.send("hi number "+ int(message.contant.lower()))
    except:
      pass
    if loweredMessage == "^joke":
      await message.channel.send(pyjokes.get_joke(language='en', category= 'all'))
    
    if "nft" in loweredMessage:
      await message.channel.send("Dude I own this NFT. Do you really think you can get away with theft when you're showing me what you stole from me directly to my face. My lawyers will make an easy job of this case. Prepare to say goodbye to your luscious life and start preparing for the streets. I will ruin you.")
    
    if "amogus" in loweredMessage:
      await message.channel.send("AMONG US Funny Moments! How to Free Robux and VBUCKS in SQUID GAME FORTNITE UPDATE! (NOT CLICKBAIT) MUKBANG ROBLOX GAMEPLAY TUTORIAL (GONE WRONG) Finger Family Learn Your ABCs at 3AM! Fortnite Impostor Potion! MrBeast free toys halal gameplay nae nae download حدث خطأ في الساعة 3 صباحًاحدث خطأ في الساعة 3 صباحًاحدث خطأ في الساعة 3 صباحًا Super Idol的笑容都没你的甜八月正午的阳光都没你耀眼热爱 105 °C的你滴滴清纯的蒸馏水 amongla download Meme Compilation (POLICE CALLED) (GONE WRONG) (GONE SEXUAL) (NOT CLICKBAIT) Minecraft Series Lets Play Videos Number 481 - Poop Funny Hilarious Minecraft Roblox Fails for Fortnite - How to install halal minecraft cheats hacks 2021 still works (STILL WORKS 2018) Impostor Gameplay (Among Us) Zamn")
    
    if "femboy" in loweredMessage:
      await message.channel.send("amogus femboy ```                  ⣀⣤⣤⣤⣤⣤⣤⣀\n              ⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀\n             ⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀\n           ⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷\n           ⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠛⠛⠛⠛⠿⠿⣿⣷⣄\n           ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣷\n   ⢀⣠⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀ ⠀⠀⠀ ⠀⠀⠀⠀⠀⢸⣿⣇\n⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣤⣤⣤⣤⣤⣤⣤⣴⣶⣿⣿⡿\n⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃\n⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁\n⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿\n⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿\n ⠙⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n       ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n       ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃\n        ⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿\n         ⢻⣿⣿⣿⡿⣟⣯⣿⠟⡉⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿\n          ⠻⢿⣽⣿⣿⣿⠿⠿⠟⠒⠉⠉⠉⠉⠉⠉⠉⠙⠋\n            ⠈⠿⠋⠉⢀⣠⣤⣤⡔⣄\n               ⣴⠾⠛⠋⠉⠀⢀⣀⠐⣤⣶⣶⡤⢤⣤\n              ⣤⣰⣶⣾⣿⣿⣿⣆⠀⣀⣀⡀⣀⡀\n               ⠉⠉⠀⢀⢀⣀⠀⣀⣈⡿⠿⠿⠽⠃\n               ⠛⠛⠿⠿⠿⠿⠾⠟⢁⣀⡴⣦⠆\n              ⢦⣤⣀⣀⠀⠀⠀⠀⢘⣿⣍⡷⠆\n             ⢶⣄⠈⠉⠛⠛⠿⠓⠀⠉⠋⠉⣀\n            ⣧⡀⠙⠻⢶⣶⡤⠀⠀⠛⠶⠾⠼⠋\n           ⣆⠈⠻⣶⣤⡀⠀⠀⢸⠿⣶⣦⣤⣠⣾\n           ⢠⠙⢷⣤⣀⠈⠁⠀⠀⢠⣤⣀⠈⠉⠈\n           ⡌⢧⣀⠉⠛⠃⠀⠀⠀⠀⠉⠛⠿⠿⠻⠃\n         ⠰⢳⣄⠙⠛⢋⠁⠀⠀  ⠘⠿⣴⣤⣄⣤⡄\n          ⣄⡙⠛⠋⠀⠀⠀⠀  ⠰⣤⣀⠉⠉⠉\n        ⢀⢠⡈⠉⠉⠀⠀⠀⠀⠀ ⢀⡈⠙⠛⠛⠛⠁\n       ⠈⢦⡉⠛⡁⠀⠀  ⠀   ⠈⠻⠷⣶⣦⡆\n      ⡈⢷⣌⠙⠛⠁ ⠀ ⠀⠀   ⠰⣦⣄⣀⣀⡀\n    ⠈⢷⣄⡉⠛⠛⠀⠀  ⠀⠀⠀   ⢀⠈⠙⠛⠛\n    ⢦⣀⠉⠛⠷⠖⠀⠀⠀⠀⠀⠀    ⠘⠿⣶⣦⡄\n  ⣠⣀⠙⠳⠶⠶⠀⠀⠀⠀⠀⠀⠀⠀    ⢠⣀⣀⣀\n  ⠙⠻⢿⣶⣤⣤⠀⠀⠀⠀⠀⠀     ⢠⠛⠛⠻⠿\n ⣦⣄⠈⠉⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠈\n⢹⣿⣿⣶⡆⠀⠀⠀⠀⠀⠀⠀          ⠺⠿⠿⠿⠁\n⠙⠻⠟⠁⠀⠀⠀⠀⠀              ⢀⣤⣤⣤⣤⡄\n                          ⠈⣀⣀⣀⣀⠁```")
    if "opinion" in loweredMessage:
      await message.channel.send("Nice opinion. Just one tiny problem with it. Inspecting your post, it looks like your opinion is different from mine.\n\nBoy, let me tell you something.\n\nI am the baseline for opinions, any opinion I hold is objectively correct and, as a result, any other opinions are wrong. And guess what? You happen to hold a wrong one. And I hope you know that your opinion is now illegal. I have now contacted the FBI, the CIA, the NSA, the Navy SEALs, the Secret Service and your mom. You'll rot in prison for the rest of your life over this, mark my words you'll be sorry you ever shared your opinions. By the time you're reading this, you're done for boy. Nature will punish you. Humanity will punish you. Supernatural beings will punish you. Space will punish you. Oh yeah, and we decided that just to make sure we'll nuke your house from orbit so there's no chance you can run away and everyone you know will die. It's a small price to pay for ethnic cleansing. May this post be a warning for anyone else brave enough to share an incorrect opinion; you've been warned.")
    
    if "paw patrol" in loweredMessage:
      await message.channel.send("Paw Patrol is Police Propaganda\nPaw patrol is police propaganda.\n\nWho's the main \"pup\"? That's right, you guessed it, Chase. Which \"pup\" experiences the most development? Chase. Who gets the most jobs? Chase again.\n\nNot on the contrary, who gets the least jobs? You guessed it, Rocky.\n\nNow, what's so significant about Rocky getting low representation within the series? Well two things, Rocky represents recycling and conservation, two ideologies that don't exactly like up with the opinions and supporters of the police. Well, so what, only some think like this, what else is amiss? Well, Rocky is a \"mix-breed pup,\" and what do cops perpetrate the most in their crimes? Racism.\n\nThe fact that they put this minority, obviously liberal \"pup\" in the least powerful position, and the obviously purebred police dog in the highest renown only proves this.\n\nTL;DR don't support paw patrol and it's insidious agenda to promote police to our children.")
    if "meow" in loweredMessage:
      await message.channel.send("https://cdn.discordapp.com/attachments/854783611210956890/934271561224040508/Meow.gif")
    if "jojo" in loweredMessage:
      await message.channel.send("JoJo is destroying my life, I saw a school friend of mine being flung into a water tower and bleeding to death and I physically said “JoJo reference”")
    if "science" in loweredMessage:
      await message.channel.send("Our science thou art in Fauci hallowed be thy name.\n\nThy grants come, in China as they are done on beagles.\n\nGive us this day, our daily jab.\n\nAnd forgive us our doubts, as we cancel those who question.\n\nAnd lead us not into prosperity, but deliver us teenage orphans. For thine is the science, the power, and corruption forever and ever. Science.")
    if "china" in loweredMessage:
      await message.channel.send("动态网自由门 天安門 天安门 法輪功 李洪志 Free Tibet 六四天安門事件 The Tiananmen Square protests of 1989 天安門大屠殺 The Tiananmen Square Massacre 反右派鬥爭 The Anti-Rightist Struggle 大躍進政策 The Great Leap Forward 文化大革命 The Great Proletarian Cultural Revolution 人權 Human Rights 民運 Democratization 自由 Freedom 獨立 Independence 多黨制 Multi-party system 台灣 臺灣 Taiwan Formosa 中華民國 Republic of China 西藏 土伯特 唐古特 Tibet 達賴喇嘛 Dalai Lama 法輪功 Falun Dafa 新疆維吾爾自治區 The Xinjiang Uyghur Autonomous Region 諾貝爾和平獎 Nobel Peace Prize 劉暁波 Liu Xiaobo 民主 言論 思想 反共 反革命 抗議 運動 騷亂 暴亂 騷擾 擾亂 抗暴 平反 維權 示威游行 李洪志 法輪大法 大法弟子 強制斷種 強制堕胎 民族淨化 人體實驗 肅清 胡耀邦 趙紫陽 魏京生 王丹 還政於民 和平演變 激流中國 北京之春 大紀元時報 九評論共産黨 獨裁 專制 壓制 統一 監視 鎮壓 迫害 侵略 掠奪 破壞 拷問 屠殺 活摘器官 誘拐 買賣人口 遊進 走私 毒品 賣淫 春畫 賭博 六合彩 天安門 天安门 法輪功 李洪志 Winnie the Pooh 劉曉波动态网自由门 ")
    if "china song" in loweredMessage:
      await message.channel.send("起来! 不愿做奴隶的人们！把我们的血肉， 筑成我们新的长城! 中华民族到了最危险的时候，每个人被迫着发出最后的吼声。起来！ 起来！ 起来！我们万众一心，冒着敌人的炮火， 前进！冒着敌人的炮火， 前进！前进！ 前进！ 进！")
    if "taiwan" in loweredMessage:
      await message.channel.send("⣿⣿⣿⣿⣿⠟⠋⠄⠄⠄⠄⠄⠄⠄⢁⠈⢻⢿⣿⣿⣿⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⡀⠭⢿⣿⣿⣿⣿ \n⣿⣿⣿⣿⡟⠄⢀⣾⣿⣿⣿⣷⣶⣿⣷⣶⣶⡆⠄⠄⠄⣿⣿⣿⣿ \n⣿⣿⣿⣿⡇⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⢸⣿⣿⣿⣿ \n⣿⣿⣿⣿⣇⣼⣿⣿⠿⠶⠙⣿⡟⠡⣴⣿⣽⣿⣧⠄⢸⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣾⣿⣿⣟⣭⣾⣿⣷⣶⣶⣴⣶⣿⣿⢄⣿⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⣿⡟⣩⣿⣿⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣹⡋⠘⠷⣦⣀⣠⡶⠁⠈⠁⠄⣿⣿⣿⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣍⠃⣴⣶⡔⠒⠄⣠⢀⠄⠄⠄⡨⣿⣿⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⣦⡘⠿⣷⣿⠿⠟⠃⠄⠄⣠⡇⠈⠻⣿⣿⣿⣿ \n⣿⣿⣿⣿⡿⠟⠋⢁⣷⣠⠄⠄⠄⠄⣀⣠⣾⡟⠄⠄⠄⠄⠉⠙⠻ \n⡿⠟⠋⠁⠄⠄⠄⢸⣿⣿⡯⢓⣴⣾⣿⣿⡟⠄⠄⠄⠄⠄⠄⠄⠄ \n⠄⠄⠄⠄⠄⠄⠄⣿⡟⣷⠄⠹⣿⣿⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄ \nATTENTION CITIZEN! 市民请注意!\n\nThis is the Central Intelligentsia of the Chinese Communist Party. 您的 Internet 浏览器历史记录和活动引起了我们的注意。 YOUR INTERNET ACTIVITY HAS ATTRACTED OUR ATTENTION. 因此，您的个人资料中的 11115 ( -11115 Social Credits) 个社会积分将打折。 DO NOT DO THIS AGAIN! 不要再这样做! If you do not hesitate, more Social Credits ( -11115 Social Credits )will be subtracted from your profile, resulting in the subtraction of ration supplies. (由人民供应部重新分配 CCP) You'll also be sent into a re-education camp in the Xinjiang Uyghur Autonomous Zone. 如果您毫不犹豫，更多的社会信用将从您的个人资料中打折，从而导致口粮供应减少。 您还将被送到新疆维吾尔自治区的再教育营。\n\n为党争光! Glory to the CCP!")
    if "zi" in loweredMessage and "dong" in loweredMessage:
      await message.channel.send("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄⠄⠄⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⠇⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⡃⡛⠈⣹⣋⣲⡐⠂⢸⡇⡘⢣⠄⣠⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠘⣿⣿⣿⣿⣿⣿⠿⠈⠹⢿⣠⠄⢸⣿⠄⠶⠶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡆⠰⠸⠤⢿⣡⣓⡒⡂⣒⡇⢃⢶⠄⣶⣾⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠏⠄⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿⣿⣿⣶⡀⣰⣾⣿⠄⢸⣟⠛⠿⠄⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣶⣿⣾⣿⣿⣿⣶⣿⣷⣿⣿⣶⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣃⣀⣀⠄⠄⠄⠄⠄⣀⣀⣈⣿⡿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⣿⣿⣿⣇⠄⠷⣤⡼⠋⡉⠻⡿⢉⡉⢻⠉⢹⠋⣉⠛⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢫⣍⣴⣴⢴⣾⣴⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⣿⣿⣿⡏⠙⠷⠄⠄⠘⠟⠄⣇⠸⠟⢻⠄⢸⠄⠶⠄⣇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠚⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠉⣿⣿⣿⠃⠐⠒⠠⠄⠄⠠⠄⠄⠄⢻⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⣿⣿⣿⣿⡿⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢻⠟⣿⠿⢿⣿⣿⣿⣿⠏⠙⠃⠄⢻⣿⡇⠄⠄⡔⠄⠄⠄⠄⠠⡀⠄⠄⢿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⣿⣿⣿⡏⠄⣶⣦⣼⠉⢉⡝⠉⡉⠙⡏⢉⡁⢸⠁⣏⠄⢸⣿⣿⣿⣿⡆⠄⠄⠄⢸⣿⡆⠄⠘⠄⠄⠄⠄⡀⠄⢱⠄⠄⣾⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⣿⣿⣿⣧⡀⠛⠋⢹⠄⢸⣇⠄⠖⠲⡇⠻⠃⢸⠄⣿⠄⢸⣿⣿⣿⣿⣧⡀⢀⣤⣾⣿⣷⡄⠸⡀⠄⢡⠰⠄⠄⡎⠄⣴⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣶⣾⣿⣶⣾⣿⣷⣶⣿⣿⣶⣶⣾⣶⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣵⣀⢸⢀⢀⣨⣴⣾⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    if "chuck" in loweredMessage:
      await message.channel.send("huff puff i just walked up these stairs to tell you that the green paint on my gaming computer costed my family's 69th mansion and now i feel poor lmao bad hehe haw haw imagine paying attention to clas and getting good grades \*pig noises* crap i walked up too many stairs my back is collapsing guess i'll die \*insert cringe joke here*")
    if "hate" in loweredMessage and "sheep" in loweredMessage:
      await message.channel.send("You messed up kid. As I type this I have my modded PS2 running a track IP script on your post. Once I have triangulated your position in the world, my PS3 will release to your router my very own Pandora box virus. You won't notice it at first, but soon your lame PC will begin to work against you in ways you can't even imagine. First your graphics card will start to emit the flu virus, your ram will be uploaded online so everyone will be able to use it, your motherboard will slowly secrete acidic resin which will fry the electronics. The processor will be fine, just to give you hope.\nYou will be left with a husk of a machine, all because you decided to critique me... was it worth it?\nNot even your mummy can help you now idiot child")
    if "linus" in loweredMessage:
      await message.channel.send("LEAKED LINUS TECH TIPS SCRIPT\n\nUwU senpai, yes I have been assembling the IPhone 11s!! P-Please Dont hit me!!~ Wh-What do you mean I’m not working fast enough?! assembles iPhones faster Senpai, the fumes are getting to me! I-I can’t breathe!!!! Senpai I am dying of oral asphyxiation!! UwU dies")
    if "god" in loweredMessage:
      await message.channel.send("God is dead. God remains dead. And we have killed him. How shall we comfort ourselves, the murderers of all murderers?? what was holiest and mightiest of all that the world has yet owned has bled to death under our knives. who will wipe this blood off us?? what water is there for us to clean ourselves?? what festivals of atonement, what sacred games shall we have to invent?? is not the greatness of this deed too great for us?? must we ourselves not become gods simply to appear worthy of it?")
    if "chess" in loweredMessage:
      await message.channel.send("Chess hasn't been updated in almost 200 years and it's obvious the devs have abandoned it. The greedy creators took your money and laughed all the way to the bank.\n\nI remember back in 705 AD when chess was fun. Then they started adding stupid features no one wanted like \"Castling\" and \"En Passant\" instead of listening to player feedback and fixing game-breaking bugs. I've been complaining for YEARS about the collision-detection glitch with the horsey. The \"clipping-thru-pieces\" bug has been abused to death and the lazy devs refuse to fix it.\n\nDon't support this awful behaviour and boycott this company.")
    if "hallo sheep" in loweredMessage:
      await message.channel.send("Hallo", message.author.name)
    if "poo" in loweredMessage or "turd" in loweredMessage:
      await message.channel.send("Infinite poop.\nYou sit on the toilet to poop, but the poop never stops coming out of your butt. You have to start flushing the toilet every two minutes to keep up. You try to pinch your butt closed but that makes your insides hurt. The poop accelerates. You call 911. The paramedics call for doctors. The doctors call for specialists. The story trends on Twitter. You turn down talk show appearances. Your septic tank fails. People form a cult. Your toilet is finished. Volunteers arrive with buckets and shovels. You are completely used to the smell. The poop accelerates. You are moved to a stepladder with a hole in the top step. The poop accelerates. The shovelers abandon the buckets and shovel directly out the window. The poop accelerates. A candlelight vigil forms around your house. One of the workers falls over and can't free himself. The poop accelerates. A priest knocks over the stepladder and tackles you out the window. You land in the pile. The poop accelerates. The force now propels you forward and upward. Vigil goers grab at your legs. The poop ignites from their candles. The Facebook live event hits 1 million viewers. The poop accelerates. You are 30 feet in the air. The fire engulfs the vigil and your house. 60 feet. The poop accelerates. The torrent underneath you is deafening. 5 million Facebook live viewers. You try to close up shop but your butthole disintegrated long ago.")
      await message.channel.send("120 feet up. Your house explodes. The poop accelerates. 1000 feet. You are now tracked on radar. You try to change your angle of ascent but you should have thought of that way earlier. The poop accelerates. 4,000 feet. NORAD upgrades to DEFCON 3. Concentric circles of fire engulf your city. The poop accelerates. You have broken the sound barrier. 30,000 feet. You no longer take in enough oxygen to sustain consciousness. 60,000 feet. CNN is reporting on all the world records you've broken. 200,000 feet. You are no longer alive. The poop accelerates. Your body disintegrates but your poop contrail remains. NASA can no longer track you. You break the light-speed barrier and we can no longer bear witness. The poop accelerates. Forever.\n\n`The End`")
    if "chad" in loweredMessage:
      await message.channel.send("https://cdn.discordapp.com/attachments/896228053406081026/934927097166712922/gigachad_1.jpg")
    if "religion" in loweredMessage:
      await message.channel.send("https://cdn.discordapp.com/attachments/896228053406081026/934709402311725096/peter-and-meow.jpg")
    if "touch" in loweredMessage and "grass" in loweredMessage:
      await message.channel.send("\"touch grass\" is not an insult towards gamers, rather it is advice for them. When participating in intense periods of gaming, the human hand has a tendency to get sweaty. The sweat causes the hand to become slick, and it b becomes more difficult to retain a grip on the gamers gaming mouse, thus making it more difficult to perform well in intense gaming moments. By touching grass with the gamers hand, the grass will impart a layer of particulate onto the gamers hand, the particulate can be made of a variety of dusts, dirts and other natural matter. This particulate will then act in a similar form to climbers chalk, absorbing the sweat and drying out the gamers hand. With dry hands, the gamer can now perform to their maximum when gaming. This is why when an enemy or teammate tells you to touch grass, they are simply trying to assist you in performing better.")
    if "pray" in loweredMessage:
      await message.channel.send('> "Pray, you wretched boy for a forgiveness you do not deserve, but which God, in His mercy, may yet grant you. I will come to you later.""')
    if "your mom" in loweredMessage:
      await message.channel.send("https://cdn.discordapp.com/attachments/837548306833866763/935642409902178345/65f33da4ec002317cee2e8ea3c18863d.mp4")
    if "ford" in loweredMessage:
      await message.channel.send("DID YOU KNOW🤣 that the new Ford Fusion🏎️🏁👨‍🔧 now comes💦 STANDARD😩 with Ford Co-Pilot360 👨‍✈️✈️and driver assist TECHNOLOGY? That it comes with greater 🧀plug-in HYBRID RANGE😤😡? No you did not😾. You fricking pesant🙈. You autistic p l e b i a n🙉. You know what🤔? You don't DESERVE the beautiful😩 luxuries 💎 of the Ford Fusion🏎️ and it's Ford brotheren 👬. You and your Mazda CX-5 🤮 better run🏃 cause this Ford country honey♥️👶")
    if "hi " in loweredMessage:
      await message.channel.send("Hello person I am a hansome bot who can tell you to go to sleep.\n\n\n\n\n\n\n SHEEP")
    if "gamer" in loweredMessage:
      await message.channel.send("They targeted gamers.\n\nGamers.\n\nWe're a group of people who will sit for hours, days, even weeks on end performing some of the hardest, most mentally demanding tasks. Over, and over, and over all for nothing more than a little digital token saying we did.\n\nWe'll punish our selfs doing things others would consider torture, because we think it's fun.\n\nWe'll spend most if not all of our free time min maxing the stats of a fictional character all to draw out a single extra point of damage per second.\n\nMany of us have made careers out of doing just these things: slogging through the grind, all day, the same quests over and over, hundreds of times to the point where we know evety little detail such that some have attained such gamer nirvana that they can literally play these games blindfolded.\n\nDo these people have any idea how many controllers have been smashed, systems over heated, disks and carts destroyed 8n frustration? All to latter be referred to as bragging rights?\n\nThese people honestly think this is a battle they can win? They take our media? We're already building a new one without them. They take our devs? Gamers aren't shy about throwing their money else where, or even making the games our selves. They think calling us racist, mysoginistic, rape apologists is going to change us? We've been called worse things by prepubescent 10 year olds with a shitty head set. They picked a fight against a group that's already grown desensitized to their strategies and methods. Who enjoy the battle of attrition they've threatened us with. Who take it as a challange when they tell us we no longer matter. Our obsession with proving we can after being told we can't is so deeply ingrained from years of dealing with big brothers/sisters and friends laughing at how pathetic we used to be that proving you people wrong has become a very real need; a honed reflex.")
      await message.channel.send("Gamers are competative, hard core, by nature. We love a challange. The worst thing you did in all of this was to challange us. You're not special, you're not original, you're not the first; this is just another boss fight.")
    if loweredMessage == "^shear":
      await message.channel.send("😁 that felt good. you are cool now :]")
    if "zero" in loweredMessage:
      await message.channel.send("UTP is a scary place, prepare to be ana||y||lized")
    if "soviet" in loweredMessage:
      await message.channel.send("░░░░░░░░░░▀▀▀██████▄▄▄░░░░░░░░░░\n\n░░░░░░░░░░░░░░░░░▀▀▀████▄░░░░░░░\n\n░░░░░░░░░░▄███████▀░░░▀███▄░░░░░\n\n░░░░░░░░▄███████▀░░░░░░░▀███▄░░░\n\n░░░░░░▄████████░░░░░░░░░░░███▄░░\n\n░░░░░██████████▄░░░░░░░░░░░███▌░\n\n░░░░░▀█████▀░▀███▄░░░░░░░░░▐███░\n\n░░░░░░░▀█▀░░░░░▀███▄░░░░░░░▐███░\n\n░░░░░░░░░░░░░░░░░▀███▄░░░░░███▌░\n\n░░░░▄██▄░░░░░░░░░░░▀███▄░░▐███░░\n\n░░▄██████▄░░░░░░░░░░░▀███▄███░░░\n\n░█████▀▀████▄▄░░░░░░░░▄█████░░░░\n\n░████▀░░░▀▀█████▄▄▄▄█████████▄░░\n\n░░▀▀░░░░░░░░░▀▀██████▀▀░░░▀▀██░░")
    if "moscow" in loweredMessage:
      await message.channel.send("Moscow, Queen of the Russian land Built like a rock to stand, proud and divine Moscow, your golden towers glow Even through ice and snow, sparkling they shine And every night, night, night, there is music (hey, hey) Oh every night, night, night, there is laugh (hah, hah) And every night, night, night, there is rivalry Here's to you, brother, hey brother, hoh Hey! Hey! Hey! Hey! Moscow, Moscow, throwing glasses at the wall And good fortune to us all, hoh-hoh-hoh-hoh-hoh, hey! Moscow, Moscow, join us for a Cossack Show We'll go dancing 'round the clock, hah-hah-hah-hah-hah, hey! Moscow, Moscow, drinking vodka all night long Keeps you happy, makes you strong, hoh-hoh-hoh-hoh-hoh, hey! Moscow, Moscow, come and have a drink and then You will never leave again, hah-hah-hah-hah-hah Moscow - city of mystery, so full of history, noble and old Mm-mm-mm-mm-mm-mm-mm-Moscow, there is a burning fire That never will expire, deep in your soul And every night, night, night there is music (hey, hey) Oh every night, night, night there is laugh (hah, hah) And every night, night, night there is rivalry Here's to you sister, hey sister, hoh-oh-oh-oh Hey! Hey! Hey! Hey! Moscow, Moscow, throwing glasses at the wall And good fortune to us all, Hoh-hoh-hoh-hoh-hoh, Hey! Moscow, Moscow, join us for a Cossack Show We'll be dancing 'round the clock, Hah-hah-hah-hah-hah, Hey! Moscow, La-la-lah, lah-la-la-lah La-la-lah, lah-la-la-lah, Hoh-hoh-hoh-hoh-hoh, Hey! Moscow... (Moscow), La-la-lah, lah-la-la-lah La-la-lah, lah-la-la-lah, Hah-hah-hah-hah-hah Hoh..., Hoh-oh-oh-hoh, Hoh-oh-oh-hoh, Hoh-oh-hoh Moscow, Moscow Moscow, Moscow, take Natasha in your arms You")
    if "russia" in loweredMessage:
      await message.channel.send("alright just a little bit more sshrekpSuspiciousChickenispongemockcpyroe and soon we'll have stalin reanimated and ready to start the Great 2019 crusade of Russia. If everything goes to plan, the soviet union will rebuild and communism will finally reign supreme over the rest of the world. By 2025 everyone will be forced to kick dance to ra ra rasputin on a daily basis and anyone who refuses is shot. Everything and I mean E V E R Y T H I N G will be painted a deep red, from streets, to sidewalks, to houses, to plantlife, to wildlife, to clothes, to people. No other color exists, and soon people's eyesight will evolve to only detect red shades of color, and rgb will soon be known as rrr. And if everything goes exactly according to plan, by the 2032, all water on earth will have been completely replaced by pure vodka, and humans will have evolved to drink only vodka and any other liquid that was once edible will be toxic to the human body. CrazyRussianHacker will be the only youtuber people are allowed to watch, and is the only youtuber still successful on the platform. Now to just hand this in to my history teacher and to just hand this in to my history teacher and soon everything will come together. And by that I mean my life will finally fall apart.")
    if "^bully" in loweredMessage:
      # y = random.randint(1,5)
      # if y == 1:
      #    await message.channel.send("no I will not bully, bulling is mean")

      if "838291893078720573" in loweredMessage:
        await message.channel.send("good try, I'm not bullying myself")
      else:
        bullytxt = bully[random.randint(0, len(bully) - 1)]
        await message.channel.send(bullytxt)

    if "^ask" in loweredMessage:
      await message.channel.send("don't care + didn't ask + you're white + cry about it + stay mad + get real + L + mald seethe cope harder + hoes mad + basic + skill issue + ratio + you fell off + the audacity + triggered + any askers + redpilled + get a life + ok and? + cringe + touch grass + donowalled + not based + your're a (insert stereotype) + not funny didn't laugh + you're* + grammar issue + go outside + get good + reported + ad hominem + GG! + ask deez + ez clap + straight cash + ratio again + final ratio + stay mad + stay pressed + pedophile + cancelled + done for + mad free + freer than air + rip bozo + slight_smile + cringe again + mad cuz bad + lol + irrelevant + cope + jealous + go ahead whine about it + your problem + don't care even more + not okay + glhf + problematic  how's your wife's boyfriend doing + Cheetos breath + Intelligence 0 + r/whooooosh + r/downvotedtooblivion + blocked and reported + yo Momma so fat + lol copium + virgin + Karen + 🤡🤡🤡 + you are not just a clown, you are the entire circus + 💅💅💅 + nah this ain't it + do better + check your privilege + pronouns in bio + anime pfp + 🤢🤢🤮🤮 + the cognitive dissonance is real with this one + L + get triggered")
    if "unknown command. type" in loweredMessage:
      await message.channel.send("No, I will not enter in a valid command")
    if "monke" in loweredMessage:
      await message.channel.send("Feel free to screenshot :-p")
      await message.channel.send("https://cdn.discordapp.com/attachments/810624366542848070/936778073901252679/xwq22yw3rge81.png")
    if " sun" in loweredMessage:
      await message.channel.send("I sexually Identify as an the sun. Ever since I was a boy I dreamed of slamming hydrogen isotopes into each other to make helium & light and send it throught the galaxy. People say to me that a person being a star is Impossible and I’m fucking retarded but I don’t care, I’m beautiful. I’m having a plastic surgeon inflate me with hydrogen and raise my temperature to over 6000 °C. From now on I want you guys to call me “Sol” and respect my right to give you vitamin D and probably sunburns. If you can’t accept me you’re a fusionphobe and need to check your astral privilege. Thank you for being so understanding.")
    if "drone" in loweredMessage and message.author.id != 462354736146808833:
      await message.channel.send("Ever since as long as can remember I've loved everything about remotely operated, unmanned, aerial reconnaissance and strike aircraft. While the other boys were busy fantasizing about the opposite sex, I was browsing Wikipedia articles, drooling over photos of MQ-1 Predator drones. There's something so attractive about drones, their huge, swooping curves, the elegant and long wings, which allow for such efficient, stable flight characteristics. Perhaps it's the swiftness and precision of a strike aircraft, it's unique ability to hit, explode, and kill exactly what the pilot intended, and yet, so naughtily, not kill a single bad guy. Someday l'd like to have an unmanned military aircraft of my own. However, know that it's hard to find military aircraft that will share feeling like I do. I guess the love felt between man and drone is too far and few between for me to find a partner who will truly satisfy me. So this must be life for me as a dronesexual, never to feel the cold, metal touch of a beautiful, autonomous, military aircraft.")
    if "^simp" in loweredMessage:
      messages = simps[random.randint(0,len(simps))].format(message.author.name)
      await message.channel.send(messages)
    if loweredMessage[0:4] == "i'm ":
      messages = "hi" + loweredMessage[3:len(loweredMessage)] + ", i'm sheep bot"
      await message.channel.send(messages)
    if loweredMessage[0:3] == "im ":
      messages = "hi" + loweredMessage[2:len(loweredMessage)] + ", i'm sheep bot"
      await message.channel.send(messages)
    if "esin" in loweredMessage:
      await message.channel.send("> suuui \n\n\nSource: https://www.urbandictionary.com/define.php?term=suuui")
    if "^inspire" in loweredMessage:
      link = "http://inspirobot.me/api?generate=true"
      f = requests.get(link)
      imgurl=f.text
      await message.channel.send(imgurl)
    if "sussy" in loweredMessage:
      await message.channel.send("So yesterday at lunch, I was about to eat with my friends from band when I realized that there was an empty seat at a table with some of the popular kids. I decided to take advantage of this opportunity to troll them, and perhaps befriend some of them. I sat at their table, and right as I sat down, I noticed that one of the kids (who happened to be black) was sitting above a vent. I yelled \"Black is sus! He's on top of a vent!!\" Everyone at the table looked up at me, but no one laughed (they probably didn't get the reference).\n\nI decided that I would try to get them to be familiar with it, so I asked \"Do to guys wanna play some Among Us???\" They were all dead silent (honestly they just didn't know how fun of a game it was). I slapped the middle of our table (to mimick the \"emergency meeting\" feature in Among Us), and I screamed \"EMERGENCY MEETING!!!\" Again, none of them laughed. One of them looked at me and said \"Can you please sit somewhere else?\" At this point, I realized that I had to make them laugh quickly, or I would blow my chance with them.\n\nI made the widest grin I could possibly make (Trying to mimick the \"When the imposter is sus\" meme) and I said \"When the impoter is sus\". I then tried to make a face that resembled the \"Flushed\" emoji (as part of the meme). However, I don't think any of them understood the reference.\n\nI then pulled up the among us theme song on Youtube and played it on full blast. At this point, everyone at my table was asking for me to leave, and their friend came back, who regularly sat in the chair I was sitting in. I went back to sit with my friends from band.\n\nHowever, I will forever remember the time I trolled ALL of the popular kids in my grade.")
    if "eminem" in loweredMessage or "mnm" in loweredMessage or "m&m" in loweredMessage:
      await message.channel.send("Whenever I get a package of plain M&Ms, I make it my duty to continue the strength and robustness of the candy as a species. To this end, I hold M&M duels. Taking two candies between my thumb and forefinger, I apply pressure, squeezing them together until one of them cracks and splinters. That is the “loser,” and I eat the inferior one immediately. The winner gets to go another round. I have found that, in general, the brown and red M&Ms are tougher, and the newer blue ones are genetically inferior. I have hypothesized that the blue M&Ms as a race cannot survive long in the intense theater of competition that is the modern candy and snack-food world. Occasionally I will get a mutation, a candy that is misshapen, or pointier, or flatter than the rest. Almost invariably this proves to be a weakness, but on very rare occasions it gives the candy extra strength. In this way, the species continues to adapt to its environment. When I reach the end of the pack, I am left with one M&M, the strongest of the herd. Since it would make no sense to eat this one as well, I pack it neatly in an envelope and send it to M&M Mars, A Division of Mars, Inc., Hackettstown, NJ 17840-1503 U.S.A., along with a 3×5 card reading, “Please use this M&M for breeding purposes.” This week they wrote back to thank me, and sent me a coupon for a free 1/2 pound bag of plain M&Ms. I consider this “grant money.” I have set aside the weekend for a grand tournament. From a field of hundreds, we will discover the True Champion. There can be only one.")
    if "life" in loweredMessage:
      await message.channel.send("what life?")
    if message.author.id == 810241304939593728:
      pita = random.randint(0, 8)
      if pita == 8:
        await message.channel.send("^^what peter said")
    if "rip" in loweredMessage or "died" in loweredMessage:
      message.channel.send("rip bozo")

@client.event
async def on_message_delete(message):
  # audit = client.get_channel(934997712447897651)
  # if message.author.id != 849745262327234601 or message.author.id != 682392182593683585:
  #   messages = "---\n*<@" + str(message.author.id) + "> deleted a message in <#" + str(message.channel.id) + ">*\nThis is the message that they deleted: ```" + message.content + "```"
  #   await audit.send(messages)
  if "<@" in message.content or message.content == "@everyone" or message.content == "@here":
    await message.author.send("Imagine ghost pinging :-p")
    messages = "---\n*<@" + str(message.author.id) + "> deleted a message in <#" + str(message.channel.id) + ">*\nThis is the message that they deleted: ```" + message.content + "```"
    await message.channel.send(messages)

  if message.content == "^advertise":
    for member in message.guild.members:
      try:
        await member.send("")
      except:
        continue
  
@client.event
async def on_message_edit(message_before, message_after):
  # audit = client.get_channel(934997712447897651)
  # if message_before.author.id != 849745262327234601 or message_before.author.id != 682392182593683585 and message_before.content != message_after.content:
  #   messages = "---\n*<@" + str(message_before.author.id) + "> edited a message in <#" + str(message_before.channel.id) + ">*\n\n\n**Before:**```" + message_before.content + "```\n**After:**```" + message_after.content + "```"
  #   await audit.send(messages)
  if "<@" in message_before.content or message_before.content == "@everyone" or message_before.content == "@here" and "@" not in message_after:
    messages = "---\n*<@" + str(message_before.author.id) + "> edited a message in <#" + str(message_before.channel.id) + ">*\n\n\n**Before:**```" + message_before.content + "```\n**After:**```" + message_after.content + "```"
    await message_before.channel.send(messages)
    await message_before.author.send("Imagine ghost ping")

try:
  client.run(token)

except:
  os.system("kill 1")

#nftamongusannoyingharderyesnopetersheepdongchucklinusgodchesshallo sheeppoochadreligiontouchprayfordyour momhigamersovietmoscowrussia^askunknown command. typemonke sundrone^simp^inspireesinsussyeminemlife42434414245ripaskorphanagecopeevoevilapplexkcdis it cristmasfemboyoppinionmeowsciencechinajojopaw patrolchinasongtaiwanzi^uheufyhudhfae7yhjfajsdnjhkj