import cv2
import glob

# Bu kod input rakamlarını networke vermek için ön işlemeden geçirir.
# This script preprocesses the input digits before feeding them into neural network.

# path uygun olarak değşitirilmeli.
# paths must be changed accordingly.

path = "C:/.../*.*"

for bb, file in enumerate (glob.glob(path)):
    a = cv2.imread(file)
    print(a.shape)
    resized5 = cv2.resize(a, (28, 28))
    print(resized5.shape)
    gray_scale5 = cv2.cvtColor(resized5, cv2.COLOR_BGR2GRAY)
    print(gray_scale5.shape)
    image5 = cv2.bitwise_not(gray_scale5)

    #output pathi
    cv2.imwrite('C:/.../digit{}.png'.format(bb), image5)

    k = cv2.waitKey(1000)

    cv2.destroyAllWindows()
