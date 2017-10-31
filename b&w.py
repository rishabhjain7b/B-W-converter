from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

def threshold(imageArray):
    balanceAr=[]
    newAr= imageArray

    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = reduce(lambda x,y:x+y, eachPix[:2])/len(eachPix[:2])
            balanceAr.append(avgNum)
    balance = reduce(lambda x,y:x+y, balanceAr)/len(balanceAr)

    for eachRow in newAr:
        for eachPix in eachRow:
            if reduce(lambda x,y:x+y, eachPix[:2])/len(eachPix[:2])>balance:
                eachPix[0]=255
                eachPix[1]=255
                eachPix[2]=255
                #eachPix[3]=255

            else:
                eachPix[0]=0
                eachPix[1]=0
                eachPix[2]=0
                #eachPix[3]=255

    return newAr

j = Image.open('C:\Users\RISHABH JAIN\Desktop\IMG_20160823_072805.jpg')
jar = np.array(j)

fig = plt.figure()
ax1=plt.subplot2grid((8,6),(0,0), rowspan=5, colspan=3)
ax2=plt.subplot2grid((8,6),(0,3), rowspan=5, colspan=3)

ax1.imshow(jar)

threshold(jar)
ax2.imshow(jar)

plt.show()
