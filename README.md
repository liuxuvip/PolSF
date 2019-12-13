# PolSF
# PolSAR dataset
The original PolSAR data is downloaded from www.ietr.fr/polsarpro-bio/sanfrancisco. For the same region, San Francisco, images come from five different satellites and times

Courtesy of CNSA, CSA, ESA, IECAS, ISRO, JAXA, MDA, NASA-JPL, NSOAS.

#the files SF-XXX include the ground truth (label2d), PauliRGB image, and the colored ground truth (label3d). Which is labeled by our team IPIU

![image](https://github.com/liuxuvip/PolSF/blob/master/PolSF.png)


#The color code, the class number and name are shown as follows:
# SF-ALOS2
https://www.ietr.fr/polsarpro-bio/san-francisco/dataset/SAN_FRANCISCO_ALOS2.zip

The cut region from the original image(736, 2832, 3520, 7888)

color = [[0,0,0],[132,112,255],[0,0,255],[0,255,0],[192,0,0],[0,255,255],[255,255,0]]

0, unlabel, 1,Montain,2,Water,3,Vegetation,4,High-Density Urban,5,Low-Density Urban,6,Developd
# SF-GF3
https://www.ietr.fr/polsarpro-bio/san-francisco/dataset/SAN_FRANCISCO_GF3.zip

The cut region from the original image (1144, 3464, 3448, 6376)

color = [[0,0,0],[132,112,255],[0,0,255],[0,255,0],[192,0,0],[0,255,255],[255,255,0]]

0, unlabel, 1,Montain,2,Water,3,Vegetation,4,High-Density Urban,5,Low-Density Urban,6,Developd
# SF-RISAT
https://www.ietr.fr/polsarpro-bio/san-francisco/dataset/SAN_FRANCISCO_RISAT.zip

The cut region from the original image (2486, 4257, 7414, 10648)

color = [[0,0,0],[132,112,255],[0,0,255],[0,255,0],[192,0,0],[0,255,255],[255,255,0]]

0, unlabel, 1,Montain,2,Water,3,Vegetation,4,High-Density Urban,5,Low-Density Urban,6,Developd

# SF-RS2
https://www.ietr.fr/polsarpro-bio/san-francisco/dataset/SAN_FRANCISCO_RS2.zip

The cut region from the original image (7326:9125,661,2040)

color = [[0,0,0], [0,0,255],[0,255,0],[255,0,0],[255,255,0],[255,0,255]]

0, unlabel, 1,Water,2,Vegetation,3,High-Density Urban,4,Low-Density Urban,5,Developd

# SF-AIRSAR

https://www.ietr.fr/polsarpro-bio/san-francisco/dataset/SAN_FRANCISCO_AIRSAR.zip

color = [[0,0,0], [0,255,255],[255,255,0],[0,0,255],[255,0,0],[0,255,0]]

0, unlabel, 1,Montain,2,Water,3,Urban,4,Vegetation ,5, Bare soil

# The file 'label2dto3d.py' shows the process of coloring.
