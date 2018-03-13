
import numpy as np
import csv

def learn_load_csv(str):
    output_nodes=1
    input_nodes=2
    training_data_file=open(str,'r')
    training_data_list=training_data_file.readlines()
    training_data_file.close()
    x_train=np.empty((0,input_nodes),int)
    t_train=np.empty((0,output_nodes),int)
    for recode in training_data_list:
        all_values=recode.split(',')
        inputs=(np.asfarray(all_values[1:]))
        targets=(np.asfarray(all_values[0:1]))
        x_train=np.append(x_train,np.array([inputs]),axis=0)
        t_train=np.append(t_train,np.array([targets]),axis=0)
    return (x_train,t_train)#x_train:開花日 t_train:年度




def load_csv():
    (x,y)=learn_load_csv("../dataset/Flowering_date.csv")#桜開花日データ
    return(x,y)

x,y=load_csv()
print(x[0])
print(y[0])
