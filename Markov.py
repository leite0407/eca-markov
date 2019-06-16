import random

class Markov:
    
    def __init__(self, n=1, markov_dict={}):
        
        self.n = n
        self.markov_dict = markov_dict
    
    def train(self, tokens):
        ''' Conta quantas vezes cada token aparece à frente de cada conjunto de n tokens'''

        # Itera sobre tokens
        for i in range(self.n, len(tokens)):
            
            # Tuple com últimos n tokens
            past_tokens = tuple(tokens[i - self.n : i])
            
            # Verifica se past_tokens já existe no markov_dict
            if past_tokens not in self.markov_dict.keys():
                # Se não, incializa-o como sendo uma lista cujo único elemento é o token atual
                self.markov_dict[past_tokens] = [tokens[i]]
                
            else:
                # Se sim, apende o token atual à lista
                self.markov_dict[past_tokens].append(tokens[i])
    
    
    def generate_next_token(self, past_tokens):
        ''' Escolhe aleatoriamente um token de markov_dict[token_set] '''
        
        random_index = random.randint(0, len(self.markov_dict[past_tokens])-1)
        
        return self.markov_dict[past_tokens][random_index]
    
    def generate_sequence(self, start_tuple='random', length=20):
        
        if start_tuple == 'random':
            start_tuple =  list(self.markov_dict.keys())[random.randint(0, len(self.markov_dict.keys()) - 1)]
        
        results = list(start_tuple)
        
        for i in range(self.n, length):
            
            results.append(self.generate_next_token(tuple(results[i - self.n : i])))
        
        return results