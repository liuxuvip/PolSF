# PolSF
# PolSAR dataset on San Francisco
The original PolSAR data is downloaded from https://ietr-lab.univ-rennes1.fr/polsarpro-bio/san-francisco/
For the same region, San Francisco, images come from five different satellites and times.
Courtesy of CNSA, CSA, ESA, IECAS, ISRO, JAXA, MDA, NASA-JPL, NSOAS. 
Courtesy of Dr. Jili SUN, Dr. Bing HAN (IECAS), Dr. Xinzhe YUAN (NSOAS), Tao YAO (CNSA)

#the files SF-XXX include the ground truth (label2d), PauliRGB image, and the colored ground truth (label3d). Which is labeled by our team IPIU.(https://pan.baidu.com/s/1k_zAiThTSxgdzdln0_XK9Q)

![image](https://github.com/liuxuvip/PolSF/blob/master/PolSF.png)


#The color code, the class number and name are shown as follows:
# SF-ALOS2
 https://ietr-lab.univ-rennes1.fr/polsarpro-bio/san-francisco/dataset/SAN_FRANCISCO_ALOS2.zip

The cut region from the original image(736, 2832, 3520, 7888)% (x1,y1,x2,y2)

color = [[0,0,0],[132,112,255],[0,0,255],[0,255,0],[192,0,0],[0,255,255],[255,255,0]]

0, unlabel, 1,Montain,2,Water,3,Vegetation,4,High-Density Urban,5,Low-Density Urban,6,Developd
# SF-GF3
 https://ietr-lab.univ-rennes1.fr/polsarpro-bio/san-francisco/dataset/SAN_FRANCISCO_GF3.zip

The cut region from the original image (1144, 3464, 3447, 6375)% (x1,y1,x2,y2)

color = [[0,0,0],[132,112,255],[0,0,255],[0,255,0],[192,0,0],[0,255,255],[255,255,0]]

0, unlabel, 1,Montain,2,Water,3,Vegetation,4,High-Density Urban,5,Low-Density Urban,6,Developd
# SF-RISAT
 https://ietr-lab.univ-rennes1.fr/polsarpro-bio/san-francisco/dataset/SAN_FRANCISCO_RISAT.zip

The cut region from the original image (2486, 4257, 7414, 10648)% (x1,y1,x2,y2)

color = [[0,0,0],[132,112,255],[0,0,255],[0,255,0],[192,0,0],[0,255,255],[255,255,0]]

0, unlabel, 1,Montain,2,Water,3,Vegetation,4,High-Density Urban,5,Low-Density Urban,6,Developd

# SF-RS2
 https://ietr-lab.univ-rennes1.fr/polsarpro-bio/san-francisco/dataset/SAN_FRANCISCO_RS2.zip

The cut region from the original image (7326,661,9125,2040)% (x1,y1,x2,y2)

color = [[0,0,0], [0,0,255],[0,255,0],[255,0,0],[255,255,0],[255,0,255]]

0, unlabel, 1,Water,2,Vegetation,3,High-Density Urban,4,Low-Density Urban,5,Developd

# SF-AIRSAR

 https://ietr-lab.univ-rennes1.fr/polsarpro-bio/san-francisco/dataset/SAN_FRANCISCO_AIRSAR.zip

color = [[0,0,0], [0,255,255],[255,255,0],[0,0,255],[255,0,0],[0,255,0]]

0, unlabel, 1,Montain,2,Water,3,Urban,4,Vegetation ,5, Bare soil

# The file 'label2dto3d.py' shows the process of coloring.

If you are interested, please refer to the article:

Xu Liu, Licheng Jiao, Fang Liu, Dan Zhang, Xu Tang. PolSF: PolSAR image datasets on san Francisco[C]//International Conference on Intelligence Science. Cham: Springer International Publishing, 2022: 214-219.

@inproceedings{liu2022polsf,
  title={PolSF: PolSAR image datasets on san Francisco},
  author={Liu, Xu and Jiao, Licheng and Liu, Fang and Zhang, Dan and Tang, Xu},
  booktitle={International Conference on Intelligence Science},
  pages={214--219},
  year={2022},
  organization={Springer}
}
