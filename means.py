from datapoint import DataPoint
import sys
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
		points = []
		centroids = []
		for point in self.dataPoints:
			if point.getCluster().val not in centroids:
				centroids.append(point.getCluster().val)
		temp = []
		print 'Centroids:'
		print centroids
		for point in self.dataPoints:
			temp.append(point.getCluster().val)
			clusterNum = centroids.index(point.getCluster().val)
			datafile = "result/clusters/"+str(clusterNum)+".in"
		 	f = open(datafile, 'a')
		 	f.write("%s\n" % point.val)
		 	f.close()
		print '---------'
		# print '[[443L, 947L, 683L], [718L, 293L, 793L], [713L, 321L, 769L], [530L, 892L, 910L]]'
		# final_data = [[] for i in range(numClusters)]
		# for point in points:
		# 	final_data[point.getCluster().val].append(point.val)
		# datafile = "result/clusters/"
		# if os.path.exists(datafile):
		# 	os.remove(datafile)
		# f = open(datafile, 'w')
		# count = 0
		# for data in final_data:
		# 	count +=1
		# 	datafile = "result/clusters/"+str(count)+".in"
		# 	f = open(datafile, 'a')
		# 	f.write("%s\n" % data)
		# 	f.close()

	def __str__(self):
		return str([mean.getVector() for mean in self.means])

	def getDims(self):
		return self.d






