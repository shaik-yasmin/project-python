import numpy as np
data_from_text_file = np.genfromtxt('E:\\Num_data.txt', delimiter=',')
print(data_from_text_file)
data_from_text_file=data_from_text_file.astype('int32')
print(data_from_text_file)
print(data_from_text_file>10)
print(data_from_text_file[data_from_text_file>0])


def numpy_function(x,y,z):
    return 10*x+y-z
b=np.fromfunction(numpy_function,(4,5,3),dtype=int)
print(b)

