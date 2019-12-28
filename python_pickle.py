import pickle
#Pickling
'''example_dict={1:"Suraj",2:"Pranshu",3:"Piyush"}
pickle_out=open("dict.pickle","wb")
pickle.dump(example_dict,pickle_out)
pickle_out.close()'''

#unpickling
pickle_in=open("dict.pickle","rb")
example_dcit=pickle.load(pickle_in)
print(example_dcit)
print(example_dcit[2])