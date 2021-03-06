class PhraseTree:
    def __init__(self, phrases):
        self.tree = {}
        self.construct(phrases)

    def construct(self, phrases):
        for phrase in phrases:
            self.add_phrase(self.tree, phrase.lower().split(' '))

    def add_phrase(self, tree, phrase):
        """
            Recorsively adds a phrase to the phrase tree
        """
        if not phrase:
            tree['_M'] = True # indicates a match
            return True
        elif (phrase[0] in tree):
            word = phrase.pop(0)
            return self.add_phrase(tree[word], phrase)
        else:
            word = intern(phrase.pop(0))
            tree[word] = {}
            return self.add_phrase(tree[word], phrase)

    def _has(self, tree, phrase):
        """
            Returns:
                a) 1 if the tree matches a phrase
                b) 0 if the tree has the phrase so far but it's not complete
                c) -1 if the tree does not have the phrase 
        """
        if not phrase:
            if '_M' in tree and tree['_M']:
                return 1
            else:
                return 0
        else:
            word = phrase.pop(0)
            if word in tree:
                return self._has(tree[word], phrase)
            else: return -1

    def has(self, phrase):
        return self._has(self.tree, phrase[:])
