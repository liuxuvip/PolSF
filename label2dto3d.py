import numpy as np
from skimage import io
from scipy import misc

### The original PolSAR data is downloaded from www.ietr.fr/polsarpro-bio/sanfrancisco.
### Courtesy of CNSA, CSA, ESA, IECAS, ISRO, JAXA, MDA, NASA-JPL, NSOAS.
### The color code and the class are shown as follows:
# SF-ALOS2
# https://www.ietr.fr/polsarpro-bio/san-francisco/dataset/SAN_FRANCISCO_ALOS2.zip
# color = [[0,0,0],[132,112,255],[0,0,255],[0,255,0],[192,0,0],[0,255,255],[255,255,0]]
## 0, unlabel, 1,Montain,2,Water,3,Vegetation,4,High-Density Urban,5,Low-Density Urban,6,Developd
# SF-GF3
# https://www.ietr.fr/polsarpro-bio/san-francisco/dataset/SAN_FRANCISCO_GF3.zip
# color = [[0,0,0],[132,112,255],[0,0,255],[0,255,0],[192,0,0],[0,255,255],[255,255,0]]
## 0, unlabel, 1,Montain,2,Water,3,Vegetation,4,High-Density Urban,5,Low-Density Urban,6,Developd
# SF-RISAT
# https://www.ietr.fr/polsarpro-bio/san-francisco/dataset/SAN_FRANCISCO_RISAT.zip
# color = [[0,0,0],[132,112,255],[0,0,255],[0,255,0],[192,0,0],[0,255,255],[255,255,0]]
## 0, unlabel, 1,Montain,2,Water,3,Vegetation,4,High-Density Urban,5,Low-Density Urban,6,Developd

# SF-RS2
# https://www.ietr.fr/polsarpro-bio/san-francisco/dataset/SAN_FRANCISCO_RS2.zip
# color = [[0,0,0], [0,0,255],[0,255,0],[255,0,0],[255,255,0],[255,0,255]]
## 0, unlabel, 1,Water,2,Vegetation,3,High-Density Urban,4,Low-Density Urban,5,Developd

# SF-AIRSAR
# https://www.ietr.fr/polsarpro-bio/san-francisco/dataset/SAN_FRANCISCO_AIRSAR.zip
color = [[0,0,0], [0,255,255],[255,255,0],[0,0,255],[255,0,0],[0,255,0]]
## 0, unlabel, 1,Montain,2,Water,3,Urban,4,Vegetation ,5, Bare soil

# label_files = '/home/bidlc/labelposar/PolSF/SF-AIRSAR/SF-AIRSAR-label2d.png'
datanameall = ['SF-AIRSAR','SF-AIRSAR','SF-AIRSAR','SF-AIRSAR','SF-AIRSAR']
dataname = datanameall[4]
label_files = './'+dataname+'/'+dataname+'-label2d.png'

label = io.imread(label_files)
mm = label.shape[0]
nn = label.shape[1]

label3d = np.zeros([mm, nn, 3])

for j in range(mm):
    for k in range(nn):
        print(j,k)
        label3d[j][k]=color[int(label[j][k])]
misc.imsave('/home/bidlc/labelposar/PolSF/'+dataname+'/'+dataname+'-label3d-test.png', label3d)