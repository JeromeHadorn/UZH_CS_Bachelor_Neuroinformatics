# This signature is required for the automated grading to work. You must not
# rename the function or change its list of parameters.
def analyze(posts):
    hashtagDictionary = {}

    for post in posts:
        words = post.split()
        for extractedWord in words:

            word = extractedWord
            if word[0] == "#":
                print(word)
                noDoubleHashtags = False
                notEmptyHashtag = False

                hastagDidntStartedWithNonLetter = False


                # Strip execisve #
                startIndexofPound = 0
                endIndexofPound = 0
                if len(word) > 2:
                    if word[1] == "#":
                        for index, character in enumerate(word):
                            if character == "#":
                                endIndexofPound = index
                            else:
                                break
               # print(endIndexofPound)
                if endIndexofPound != 0:
                    word = word[endIndexofPound:]
                   # print(extractedWord,word,"REMOVED EXECISSVE POUNDS")




                if len(word[1:]) > 0:
                    notEmptyHashtag = True
                else:
                    #print("word to short")
                    continue

                #Checks the hashtag starts with a letter
                if  (64 < ord(word[1]) < 91 or 96 < ord(word[1]) < 123):
                    hastagDidntStartedWithNonLetter = True
                else:
                  #  print("First letter of hashtag not a letter")
                    continue



                possibleSubWords = []

                # Checks for limiting characters that end the hashtag
                for index, character in enumerate(word[1:]):
                    if  (not 64 < ord(character) < 91 and  not 96 < ord(character) < 123 and not 47 < ord(character) < 58):
                        #print("found some bad characters: ",character)
                        WordToContinueWith = word[:index+1]
                        #print(WordToContinueWith,"word to continue with")
                        #print(word[index+1:])
                        if "#" in word[index:]:
                            rest = word[index+1:]
                            nextPount = rest.index("#")
                            words.append(rest[nextPount:])
                            #print(words,"appended word")
                            #print("appended possible substring",rest[nextPount:])

                        word = WordToContinueWith
                        break




                #print("CLEANED: ",word)

                if word[1:] in hashtagDictionary.keys():
                    oldValue = hashtagDictionary[word[1:]]
                    hashtagDictionary[word[1:]] = oldValue + 1
                else:
                    hashtagDictionary[word[1:]] = 1

    return hashtagDictionary


# You can play around with your solution from within this block.
if __name__ == '__main__':
    posts = [
        "hi #weeken.d #weekend3",
        "good morning #### #zurich #limmat",
        "spend my #wee.kend #1aaaa #ñaa in #zurich.",
        "#Zurich <3"]
    print(analyze(posts))
