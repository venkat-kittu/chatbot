from chatterbot import ChatBot
import pyttsx

#chatbot=ChatBot('Ron Obvious',trainer='chatterbot.trainer.ChatterBotCorpusTrainer')
chatbot = ChatBot('Ron Obvious',trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
chatbot.train('chatterbot.corpus.english')
while True:
	ip=raw_input("Ask question or type exit :")
	if 'exit' in ip:
		break
	response=chatbot.get_response(ip)
	print response

