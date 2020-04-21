import scipy
import nltk
import allennlp
dir(allennlp)
elmo=allennlp
from allennlp.commands.elmo import ElmoEmbedder
elmo = ElmoEmbedder(options_file='elmo_2x4096_512_2048cnn_2xhighway_options.json',weight_file='elmo_2x4096_512_2048cnn_2xhighway_weights.hdf5')


print("\nBank,Break,Address,Bar,Harbour,Pass,Date,Kingdom,Rock,Hit,Light,Catch,Dark,Cut,Bark,Force,Score,\nService,Crash,Blow,Beat,Head,Shade,Model,Cover,Balance,Clear,Rule,Flat,Point,Cabinet,Bulb,\nToast,Post,Act,Sense,Tap,Press,Flesh,Bow,Race,Star,Deck,Pipe,Note,Pirate,Bat,Play,Moniter,Story")
while True:
	ifile=open("wordnet_glosses.txt","r")
	word=input("Enter Wsd Word:")
	stri=" "
	c=0
	while stri:
		r=ifile.readline()
		if (r==""):
			break
		a=r.split("~")
		if (word==a[0]):

			print ("First gloss is:"+a[1])
			sentence1=a[1]
			tokens1 = nltk.word_tokenize(sentence1)
			vector1 = elmo.embed_sentence(tokens1)
			for i in tokens1:
				if(word.upper()==i.upper()):
					wsd1=i
					break

			print ("Second gloss is:"+a[2])
			sentence2=a[2]
			tokens2 = nltk.word_tokenize(sentence2) 
			vector2 = elmo.embed_sentence(tokens2)
			for j in tokens2:
				if(word.upper()==j.upper()):
					wsd2=j
					break

			sentence3=input("Enter user sentence:")
			tokens3 = nltk.word_tokenize(sentence3)
			vector3 = elmo.embed_sentence(tokens3)
			for k in tokens3:
				if(word.upper()==k.upper()):
					wsd3=k
					break

			similarity_distance1=scipy.spatial.distance.cosine(vector1[2][tokens1.index(i)], vector3[2][tokens3.index(k)])
			similarity_distance2=scipy.spatial.distance.cosine(vector2[2][tokens2.index(j)], vector3[2][tokens3.index(k)])

			ofile=open("hindi.txt","r")
			stri1=" "
			while stri1:
				h=ofile.readline()
				if (h==""):
					break
				b=h.split("~")
				if (word==b[0]):
					if(similarity_distance1 > similarity_distance2):
						print("Hindi Translation of Wsd Word in this case is :"+b[2])
					if(similarity_distance1 < similarity_distance2):
						print("Hindi Translation of Wsd Word in this case is :"+b[1])

			print("%16s %16s %16s" %("Word","WSD from gloss1","WSD from gloss2"))
			print("--------------------------------------------------------")
			print("%32s %16s" %(wsd1,wsd2))
			print("--------------------------------------------------------")
			print("%16s %16.5f %16.5f" %(wsd3,similarity_distance1,similarity_distance2))       
			c+=1
			break
	if(c==0):
		print("Not Present")
	choice=input("Want to enter more words(yes/no):")
	if(choice=="yes"):
		continue
	elif(choice=="no"):
		break
ifile.close()
ofile.close()


