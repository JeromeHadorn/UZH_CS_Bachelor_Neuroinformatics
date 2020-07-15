# The signatures of this class and its public methods are required for the automated
# grading to work. You must not change the names or the list of parameters. You may
# introduce private/protected utility methods though.
class ProfanityFilter:

    def __init__(self, keywords, template):
        self.__template = template
        self.__keywords = []
        for key in keywords:
            self.__keywords.append(key.lower())
        self.__keywords.sort(key=len, reverse=True)
        #print(self.keywords)

    def filter(self, msg):
        self.__msg = msg
        for index, key in enumerate(self.__keywords):
            self.__recursively_replace_keyword(key, self.__msg)
        return self.__msg

    def __recursively_replace_keyword(self, key, msg):
        if key in msg.lower():
            index = msg.lower().index(key)
            end = index + len(key)
            msglist = list(msg)
            replacement = self.__generate_replacement(len(msg[index:end]))
            msglist[index:end] = replacement
            newmessage = "".join(msglist)
            self.__msg = newmessage
            self.__recursively_replace_keyword(key,newmessage)
        else:
            return msg

    def __generate_replacement(self,length):
        if length < len(self.__template):
            return self.__template[:length]
        else:
            multi = length // len(self.__template)
            left = length - len(self.__template) * multi
            #print(self.__template * multi + self.__template[:left],"replacement string for",length)
            return self.__template * multi + self.__template[:left]

# You can play around with your implementation in the body of the following 'if'.
# The contained state®ments will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "Batch", "mastard","MaBatch"], "?#$")
    offensive_msg = "abCdefghiMastardjklmBatchnoYMaBatchXXX"
    clean_msg = f.filter(offensive_msg)
    print("->",clean_msg)  # abc defghi ?#$?#$? jklmno