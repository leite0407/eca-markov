import pickle
import pandas as pd

print('Bem vindo ao eca_corretor! Escreve texto como se fosses o Eça de Queirós\n')

markov_file = open('markov.pkl', 'rb')
markov = pickle.load(markov_file)

input_map = {
	
	'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6,
}

inverse_map = ['a)', 'b)', 'c)', 'd)', 'e)']

last_token = '.'

text = ''

while(True):

	top = pd.Series(markov[tuple([last_token])]).value_counts()
	
	for i in range(5):
		print(inverse_map[i], top.index[i], end = ' ')

	print('\nf) [Outra palavra]  g) [Sair]')

	escolha = input_map[input('\nEscolhe opção (a, b, ...): \n')]

	if 0 <= escolha <= 4:

		text = text + ' ' + top.index[escolha]
		print('\n\n', text)

		last_token = top.index[escolha]

	elif escolha == 5:

		palavra = input('Palavra: ')
		
		text = text + ' ' + palavra
		print(text)

		last_token = palavra

	else:
		break