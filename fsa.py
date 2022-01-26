class State:
    def __init__(self):
        self.ins = {}
        self.outs = {}
        self.ends = {}
    
    def add_link(self, type):
        pass

    def has_out(self, out):
        if out in self.outs.keys():
            return True
        return False
    
    def add_gram(self, state, gram):
        if gram in state.ends.keys():
            state.ends[gram] += 1
        else:
            state.ends[gram] = 1

class FSA:
    def __init__(self):
        self.states = [State()]
        
    def parse(self, word):
        pass

    def add_word(self, word, lemma, gramemma):
        """:param word word_lemma_gramemma
        """
        path = self.generate_path(word, lemma)
        current_state = self.states[0]
        
        print(f"WORD:\t {word}")
        print(f"PATH:\t {path}", end='\n\n')

        for elem in path:
            """
                1) Есть ли из текущего состоянии нужный выход (линк)
                    1.1) Есть. перейти по нему в след. состояние  
                    1.2) Нет. создать новую связь и ищем подходящий узел (с выходом равным следующей букве)
                        1.2.1) Узел есть. проложить связь к нему. Переключить current_state на него
                        1.2.2) Узла нет. создать новый. Переключить current_state на него
            """
            
            # target_state = self.find_state_by_out(elem)
            # if target_state is None:
            #     create_state()
            
            if current_state.has_out(elem):
                current_state = current_state.outs[elem]
                print(f'{elem} in states outs')
            else:
                target_state = self.get_state_by_out(elem)
                if target_state:
                    print(f'{elem}: next state is already exists')
                else:
                    print(f"{elem}: create new state")
                    target_state = self.create_state()
                    current_state.outs[elem] = target_state
                
                target_state.ins[elem] = current_state
                current_state = target_state

            # current_state.add_gram(gram)


    def unpack(self):
        for i, val in enumerate(self.states):
            print(f'element {i}')
            print('ins', [i for i in val.ins.keys()])
            print('outs', [i for i in val.outs.keys()])
            print('\n')


    def create_state(self):
        new_state = State()
        self.states.append(new_state)

        return new_state         

    def get_state_by_out(self, out):
        for state in self.states:
            if out in state.outs.keys():
                return state
        return None

    # @staticmethod
    # def generate_path(word, lemma):
    # вариант со строкой
    #     if len(word) < len(lemma):
    #         word += '_' * (len(lemma) - len(word))
    #     path = [f'{w}:{l}' for l, w in zip(lemma, word)]

    #     return path
    
    @staticmethod
    def generate_path(word, lemma):
    # вариант с туплем
        diff = len(word) - len(lemma)
        word += '_' * -diff
        lemma += '_' * diff
        path = [(w, l.upper()) for l, w in zip(lemma, word)]

        return path


    def find_state_by_out(self, link):
        for state in self.states:
            if link in state.outs.keys():
                return state





if __name__ == '__main__':
    # tested fsa
    test_fsa = FSA()
    # test_fsa.states[0].outs[('н','Н')] = State()
    print('\n\n')
    #
    test_fsa.add_word('ножом', 'нож', 'S')
    test_fsa.add_word('ножом', 'нож', 'S')
    test_fsa.add_word('боком', 'бок', 'S')
    test_fsa.add_word('ножом', 'нож', 'S')
    print('\n\n')
    test_fsa.unpack()
    for i, val in enumerate(test_fsa.states):
        print(i, val.ins, val.outs)

