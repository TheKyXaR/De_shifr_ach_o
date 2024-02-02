sumvols = {
	".-":    "а",
	"-...":  "б",
	".--":   "в",
	"....":  "г",
	"--.":   "ґ",
	"-..":   "д",
	".":     "е",
	"..-..": "є",
	"...-":  "ж",
	"--..":  "з",
	"-.--":  "и",
	"..":    "ї",
	".---.": "і",
	".---":  "й",
	"-.-":   "к",
	".-..":  "л",
	"--":    "м",
	"-.":    "н",
	"---":   "о",
	".--.":  "п",
	".-.":   "р",
	"...":   "с",
	"-":     "т",
	"..-":   "у",
	"..-.":  "ф",
	"----":  "х",
	"-.-.":  "ц",
	"---.":  "ч",
	"--.-":  "ш",
	"--.--": "щ",
	"-..-":  "ь",
	"..--":  "ю",
	".-.-":  "я",
	" ": "",
	"   ": " "
}

val, key = list(sumvols.values()), list(sumvols.keys())

while True:
	input_ = input("\nenter text or - . -.- ... -\n").lower()
	try :
		print(" ".join([key[val.index(x)] for x in input_]))
	except ValueError :
		block = input_.split('     ')
		words = [x.split(" ") for x in block]
		print(" ".join(["".join([sumvols[y] for y in x]) for x in words]))

	