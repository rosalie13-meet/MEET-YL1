Ze_dict={}
Ze_list=[]
age_list=[]
for i in range(0,3):
    x=raw_input('Give me a name')
    y=int(raw_input('Give me an age'))
   
    Ze_list.append(x)
    age_list.append(y)
    Ze_dict['names']=Ze_list
    Ze_dict['ages']=age_list
print Ze_dict
