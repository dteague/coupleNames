class TreeABC:
    def __init__(self,_current):
        self.values = [0.] * 26
        self.current = _current
        self.end = False
        
    def add_letter(self, _letter):
        if self.let_exists(_letter):
            return
        else:
            _tree_letter = TreeABC(_letter)
            _val_let = ord(_letter) - ord('a')
            self.values[_val_let] = _tree_letter

    def let_exists(self, _letter):
        _tmp = ord(_letter) - ord('a')
        return self.values[_tmp] != 0.
        
    def return_let(self):
        return self.current

    def add_phrase(self, _phrase):
        if _phrase != '':
            self.add_letter(_phrase[0])
            _tmp = ord(_phrase[0]) - ord('a')
            self.values[_tmp].add_phrase(_phrase[1:])
        else:
            self.end = True
            
    def print_phrases(self, _previous):
        if self.end:
            print _previous
            
        if self.values == [0.] * 26:
            return
        else:
            for _next in self.values:
                if _next != 0.:
                    _tmp = _previous + _next.current
                    _next.print_phrases(_tmp)


    def phrase_exist(self, _phrase):
        if _phrase !='' and self.let_exists(_phrase[0]):
            _tmp = ord(_phrase[0]) - ord('a')
            if self.values[_tmp].end and len(_phrase) == 1:
                return True
            else:
                return self.values[_tmp].phrase_exist(_phrase[1:])
        else:
            return False
                      
class Dictionary:
    def __init__(self):
        self.dic = TreeABC('1')

    def add_word(self, word):
        self.dic.add_phrase(word)

    def print_words(self):
        self.dic.print_phrases("")

    def word_exists(self, word):
        return self.dic.phrase_exist(word)

