from chatterbot import ChatBot
import pyttsx
#Initialize the corpus for taining
chatbot = ChatBot('Cortona',trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
#Train bot on english language words
chatbot.train('chatterbot.corpus.english')
while True:
	ip=raw_input("Ask question or type exit :")
	if 'exit' in ip:
		break
	response=chatbot.get_response(ip)
	print response

