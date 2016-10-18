from scipy import misc
import numpy as np 
import sys

#parse arguments
try:
    imgName = sys.argv[1]
    OPname = sys.argv[2]
except:
	print "Run like this : python medianFilter.py input.jpg output.jpg 3/5(filter size) \n"
	exit(0)
try:
	sFilter = int(sys.argv[3])
except:
	print "Filter size hasn't been mentioned. Using 3*3 by default."
	sFilter = 3


#read an image
try:
	img = misc.imread(imgName)
except:
	print "Can't find an image. Please check the name and path of supplied image\n"
	exit(0)


nRows = img.shape[0]
nCols = img.shape[1]
p_v = []

def CalculateFilter(i,j,n=3):
	if n == 3:
		try:
			p_v.append(img[i][j])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i][j+1])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i][j-1])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i-1][j])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i-1][j-1])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i-1][j+1])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i+1][j])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i+1][j-1])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i+1][j+1])
		except:
			p_v.append(0)
		return p_v

	if n == 5:
		try:
			p_v.append(img[i][j])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i][j+1])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i][j-1])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i][j-2])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i][j+2])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i-1][j])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i-1][j-1])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i-1][j+1])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i-1][j-2])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i-1][j+2])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i+1][j])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i+1][j-1])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i+1][j+1])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i+1][j-2])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i+1][j+2])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i+2][j])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i+2][j+1])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i+2][j+2])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i+2][j-1])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i+2][j-2])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i-2][j])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i-2][j+1])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i-2][j+2])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i-2][j-1])
		except:
			p_v.append(0)
		try:
			p_v.append(img[i-2][j-2])
		except:
			p_v.append(0)
		return p_v


#slide filter over an image
for i in range(nRows):
	for j in range(nCols):
		p_v = CalculateFilter(i,j,sFilter)
		print("[{0}][{1}] Pixel Value : {2}, Filter : {3} ".format(i,j,img[i][j],p_v))
		img[i][j] = np.median(p_v)
		del p_v[:]


misc.imsave(OPname,img)
print "\n Image has been saved as",OPname
