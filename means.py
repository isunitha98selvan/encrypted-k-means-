from datapoint import DataPoint
import os
verbose = False

class KMeans:

	def __init__(self, k, inputFile):
		self.dataPoints = []
		if verbose:
			print inputFile
		f = open(inputFile, 'r')
		for line in f:
			val = eval(line)
			self.d = len(val)
			self.dataPoints.append(DataPoint(len(val), val))
		self.k = k
		self.means = self.dataPoints[:k]

	def getClusterCentroids(self):
		centroids = [[DataPoint(self.d),0] for i in range(self.k)]
		for point in self.dataPoints:
			closestCluster =min([(self.means[i].distanceTo(point), i) for i in range(self.k)])[1]
			point.setCluster(self.means[closestCluster])
			centroids[closestCluster][0].addVector(point)
			centroids[closestCluster][1]+=1
		return centroids

	def updateMeans(self, means):
		self.means = means

	def allPoints(self, numClusters):
		final_data = [[] for i in range(numClusters)]
		for point in self.dataPoints:
    		# print point.getCluster()
			#final_data[point.getCluster()].append(point)
			print "Helloo"
			print point.getCluster().val

		count = 0
		# datafile = "result/clusters/" + str(count)+".in"
		# if os.path.exists(datafile):
		# 	os.remove(datafile)
		# f = open(datafile, 'w')
		for data in final_data:
			count +=1
			datafile = "result/clusters/"+str(count)+".in"
			f = open(datafile, 'a')
			f.write("%s\n" % data)
			f.close()

	def __str__(self):
		return str([mean.getVector() for mean in self.means])

	def getDims(self):
		return self.d






