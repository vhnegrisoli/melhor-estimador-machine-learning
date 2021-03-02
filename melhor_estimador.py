SIM = 's'
NAO = 'n'
SAIR = 'x'

resposta = ''

while (resposta == SAIR or (resposta != SIM and resposta != NAO)):
	print('Início do estimador.')
	print('Para finalizar, basta apertar x em qualquer reposta')
	resposta = input('Você tem mais de 50 mil linhas no seu conjunto de dados?').lower()
	if (resposta == NAO):
		print('Será necessário obter mais dados.')
		resposta = SAIR
	if (resposta != SAIR):
		resposta = input('Está tentando prever uma categoria?').lower()
		if (resposta == NAO):
			## =============================== ALGORITMOS DE REGRESSÃO E REDUÇÃO DE DIMENSIONALIDADE ==========================
			resposta = input('É uma previsão quantitiva?').lower()
			if (resposta == SIM):
				print('Entraremos nos algoritmos de regressão.')
				resposta = input('Seu conjunto de dados possui menos de 100 mil linhas?').lower()
				if (resposta == NAO):
					print('O algoritmo selecionado é o Gradiente Descendente Estocástico (SGD Regressor)')
				elif (resposta == SIM):
					resposta = input('Poucos recursos são importantes?').lower()
					if (resposta == SIM):
						print('Utilize as técnicas Lasso (scikit-learn) ou Elastic Net Regularization')
					elif (resposta == NAO):
						print("""Os algoritmos selecionados foram: Regressão Ridge (ou Regularização de Tikhonov) ou também,\n
						Máquina de Vetores de Suporte SVR(com kernel = linear). Caso  não funcione, utilize SVR com kernel = rbf.""")
			elif (resposta == NAO):
				print('Entraremos nos algoritmos de redução de dimensionalidade.')
				resposta = input('Está apenas observando os dados?').lower()
				if (resposta == SIM):
					print('O algorimto selecionado é a Análise de Componentes Principais (PCA) randômico.')
					resposta = input('Está funcionando?').lower()
					if (resposta == NAO):
						resposta = input('Seu conjunto de dados possui menos de 10 mil linhas?').lower()
						if (resposta == SIM):
							print('O algoritmo selecionado foi o Isomap ou Spectral Embedding. Caso use Spectral Embedding e não funcione, utilize o algoritmo Incorporação Linear Local (LLE)')
						elif (resposta == NAO):
							print('O algoritmo selecionado foi a Aproximação de Kernel')
				elif (resposta == NAO):
					print('Poxa, que azar, por ser uma estrutura de predição, não há como avaliar.')
		elif (resposta == SIM):
			## =============================== ALGORITMOS DE CLASSIFICAÇÃO E AGRUPAMENTO ==========================			
			resposta = input('Seus dados são rotulados?').lower()
			if (resposta == SIM):
				resposta = input('Seu conjunto de dados possui menos de 100 mil linhas?').lower()
				if (resposta == NAO):
					print('O algoritmo selecionado foi o Classificador Gradiente Descendente Estocástico (SGD Regressor)')
				elif (resposta == SIM): 
					print('O algoritmo selecionado foi o SVC Linear')
					resposta = input('Está funcionando?').lower()
					if (resposta == NAO):
						resposta = input('Seus dados são textuais?').lower()
						if (resposta == SIM):
							print('O algoritmo selecionado foi Naive Bayes')
						elif (resposta == NAO):
							print('O algoritmo selecionado foi KNN para Classificação (KNeighbors Classifier). Caso não funcione, utilize SVC ou Ensemble Classifiers')
			elif (resposta == NAO):
				resposta = input('Você possui um número de categorias conhecidas?').lower()
				if (resposta == SIM):
					resposta = input('Seu conjunto de dados possui menos de 10 mil linhas?').lower()
					if (resposta == SIM):
						print('O algoritmo selecionado foi o K-Means. E, caso não funcione, utilize o Agrupamento Espectral (Spectral Clustering) ou o Modelo de Misturas de Gaussianas também conhecido como Gaussian Mixture Model (GMM).')
					elif (resposta ==NAO):
						print('O algoritmo selecionado foi o Mini Batch K-Means')
				elif (resposta == NAO):
					resposta = input('Seu conjunto de dados possui menos de 10 mil linhas?').lower()
					if (resposta == SIM):
						print('Que azar, não há como estimar além disso.')
					elif (resposta == NAO):
						print('O algoritmo selecionado foi o Mean-Shift ou o Variational Bayesian Gaussian Mixture Model (VBGMM)')
print('Finalizando...')
exit()