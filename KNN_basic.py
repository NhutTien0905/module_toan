from cProfile import label
import cv2
import numpy as np
import matplotlib.pyplot as plt

# .astype(<kiểu dữ liệu>) -> chuyển kiểu dữ liệu cho 1 mảng 
trainData = np.random.randint(0,100,(25,2)).astype(np.float32)
gr = np.random.randint(0,2,(25,1)).astype(np.float32)

# <array>.ravel() -> ra 1 boolean index các phần tử có giá trị cho trước
red = trainData[gr.ravel() == 1]
blue = trainData[gr.ravel() == 0]
obje = np.random.randint(0,100,(1,2)).astype(np.float32)

plt.scatter(red[:,0],red[:,1],100,'r','s',label = 'Group A')
plt.scatter(blue[:,0],blue[:,1],100,'b','^',label = 'Group B')
plt.scatter(obje[:,0],obje[:,1],100,'g','o',label = 'Object C')
plt.legend()

# khởi tạo thuật toán
knn = cv2.ml.KNearest_create()
# train dữ liệu
knn.train(trainData,0,gr)
# thu kết quả
family,mem_fam,resul,distance = knn.findNearest(obje,5)

print('Family: ',family)
print('Member of family: ',mem_fam)
print('Result: ',resul)
print('Distance: ',distance)

plt.show()
