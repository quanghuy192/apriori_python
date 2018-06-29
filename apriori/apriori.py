
class Apriori:

    min_support = 0.0
    min_confidence = 0.0

    def __init__(self):
        self.min_support = 1.0
        self.min_confidence = 1.0
        print('hello')

    def apriori_execute(self):
        with open('data', 'r') as fp:
            for cnt, line in enumerate(fp):

                if cnt == 1:
                    line1 = str(file.next()).split(' ')
                    self.min_support = line1[0]
                    self.min_confidence = line1[1]
                    print(self.min_support)
                    print(self.min_confidence)

                print("Line {}: {}".format(cnt, line))


def main():
    apriori = Apriori()
    apriori.apriori_execute()