class Shiritori:

    def __init__(self):
        self.words=[]
        self.game_over=False

    def play(self,w):

        if self.game_over!=True:
            if len(self.words)==0:
                self.words.append(w)
                print(self.words)
                return
            else:
                for i in range(len(self.words)):
                    if w == self.words[i]:
                        self.game_over=True
                        print("Game over!")
                        print("Zborovite ne smeat da se povtoruvat!")
                        return

                golemina=len(self.words[len(self.words)-1])-1
                posleden_karakter=self.words[len(self.words)-1][golemina]

                if posleden_karakter!=w[0]:
                    self.game_over=True
                    print("Game over!")
                    print(w+" ne zapocnuva na "+posleden_karakter)
                    return

            self.words.append(w)
            print(self.words)


    def restart(self):
        self.words=[]
        self.game_over=False
        print("game restarted!")
        return


if __name__=="__main__":
    my_shiritori = Shiritori()
    my_shiritori.play("apple")
    my_shiritori.play("ear")
    my_shiritori.play("rhino")
    my_shiritori.play("corn")
    my_shiritori.play("corn")
    my_shiritori.restart()
    print(my_shiritori.words)
    my_shiritori.play("hostess")
    my_shiritori.play("stash")
    my_shiritori.play("hostess")