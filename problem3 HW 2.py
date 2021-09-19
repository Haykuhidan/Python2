import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--text",  help="text given by user", required=True)
parser.add_argument("--word1", help="text given by user", required=True)
parser.add_argument("--word2", help="text given by user", required=True)


args = parser.parse_args()
mytext = args.text
newtext = mytext.replace(args.word1, args.word2)

print("The given text: ", args.text)
print("First word: ", args.word1)
print("Second word: ", args.word2)
print("Output string: ", newtext)