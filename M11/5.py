# MODULE 11: FUNCTIONS
# 5: Text censorer
# Diff: Intermediate

# list stolen from one of my previous studio works lol
# pls dont question me, i did not made this list
# our ex-lead wanted to censor text sent from the user, resulting in this list
blockedWords = (
    "2g1c",
    "acrotomophilia", "anal", "anilingus", "anus", "apeshit", "arse", "arsehole", "ass", "asses", "asshole", "assmunch", "autoerotic", "aweonado",
    "babeland", "bangbros", "bangbus", "bareback", "barenaked", "bastard", "bastardo", "bastinado", "bbw", "bdsm", "beaner", "beaners", "beastiality", "bestiality", "bimbos", "birdlock", "bitch", "bitches", "bitchy", "blowjob", "blumpkin", "blyat", "bollocks", "bondage", "boner", "boob", "boobs", "breast", "breasts", "bukkake", "bulldyke", "bunghole", "busty", "butt", "buttcheeks", "butthole",
    "camgirl", "camslut", "camwhore", "carpetmuncher", "chupamedias", "cialis", "circlejerk", "clit", "clitoris", "clusterfuck", "cock", "cocks", "coprolagnia", "coprophilia", "cornhole", "coon", "coons", "creampie", "cum", "cumming", "cumshot", "cumshots", "cunnilingus", "cunt", "cunts",
    "darkie", "daterape", "deepthroat", "dendrophilia", "dick", "dickhead", "dicks", "dildo", "dingleberry", "dingleberries", "doggiestyle", "doggystyle", "dogshit", "dolcett", "domination", "dominatrix", "dommes", "dumbass", "dumbfuck", "dvda",
    "ecchi", "ejaculation", "erotic", "erotism", "escort", "eunuch",
    "fag", "faggot", "faggots", "fatass", "fecal", "felch", "fellatio", "feltch", "femdom", "figging", "fingerbang", "fingering", "fisting", "footjob", "frotting", "fuck", "fucker", "fuckin", "fucking", "fucks", "fucktards", "fudgepacker", "fukc", "futanari",
    "gago", "gangbang", "genitals", "goatcx", "goatse", "gokkun", "goodpoop", "goregasm", "grope", "g-spot",
    "handjob", "hardcore", "hentai", "homoerotic", "honkey", "hooker", "horny", "horseshit", "humping",
    "incest", "intercourse",
    "jailbait", "jigaboo", "jiggaboo", "jiggerboo", "jizz", "juggs",
    "kike", "kinbaku", "kinkster", "kinky", "knobbing",
    "livesex", "lolita", "lovemaking",
    "masturbate", "masturbating", "masturbation", "milf", "mong", "motherfucker", "muffdiving",
    "nambla", "nawashi", "negro", "neonazi", "nigga", "nigger", "niggas", "nimphomania", "nipple", "nipples", "nsfw", "nude", "nudity", "nutten", "nympho", "nymphomania",
    "octopussy", "omorashi", "orgasm", "orgy",
    "paedophile", "paki", "panties", "panty", "pedobear", "pedophile", "pedophilia", "pegging", "pendeja", "pendejo", "penis", "penises", "pikey", "pissing", "pisspig", "playboy", "ponyplay", "poof", "poon", "poontang", "punany", "pussies", "pussy", "poopchute", "porn", "porno", "pornography", "pthc", "pubes", "pussy", "puta", "puto",
    "queaf", "queef", "quim",
    "raghead", "rape", "raping", "rapist", "ratshit", "rectum", "retard", "retarded", "retardedbitch",  "retards", "rimjob", "rimming",
    "sadism", "santorum", "scat", "schlong", "scissoring", "semen", "sex", "sexcam", "sexo", "sexy", "sexual", "sexually", "sexuality", "shemale", "shibari", "shit", "shitass", "shitblimp", "shits", "shitter", "shitting", "shitty", "shota", "shrimping", "skeet", "slanteye", "slut", "s&m", "smartass", "smut", "snatch", "snowballing", "sodomize", "sodomy", "spastic", "spic", "splooge", "spooge", "spunk", "strapon", "strappado", "suck", "sucks", "swastika", "swinger",
    "tanga", "tangina", "tarantado", "threesome", "throating", "thumbzilla", "tit", "tits", "titties", "titty", "topless", "tosser", "towelhead", "tranny", "tribadism", "tubgirl", "tushy", "twat", "twink", "twinkie",
    "undressing", "upskirt", "urophilia",
    "vagina", "vaginas", "viagra", "vibrator", "vorarephilia", "voyeur", "voyeurweb", "voyuer", "vulva",
    "wank", "wetback", "whore", "worldsex",
    "xx", "xxx",
    "yaoi", "yiffy",
    "zoophilia",
    "🖕"
)
wordBreakers = " \n\t.,_=:;+`~!#@$%^*(){}[]|\\'\"<>?/"

def processWord (word: str, censorChar: str):
    output = word

    for blockedWord in blockedWords:
        if word.lower() != blockedWord.lower():
            continue

        output = ""

        for char in word: output += censorChar
        break
    
    return output

def censor (text: str, censorChar: str = "*"):
    currentWord = ""
    words = []

    for i in range(len(text)):
        char = text[i]
    
        if char in wordBreakers:
            words.append(f"{processWord(currentWord, censorChar)}{char}")
            currentWord = ""
            continue
        
        currentWord += char

        if i == len(text) - 1: words.append(processWord(currentWord, censorChar))
    
    return "".join(words)

print("Insert text that you wanna censor:\n\t", end = "")
inDat = input()
print()
print("Censored:")
print(f"\t{censor(inDat)}")
print()