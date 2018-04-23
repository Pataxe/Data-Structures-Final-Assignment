
import argparse #need this to get input files from the command line
import os #need this to check if the files, trains.dat & stations.dat, are present
import sys #to exit
#need to set a dictionary to hold arrival and departure times

class Node:
	#object constructor
	def __init__(self, station_name, station_number):
		#print('node called')
		#AKA the station number
		self.number = station_number
		#AKA the station name 
		self.name = station_name
		#
		#dictionary/array to store node adjacancies & weights-> need a method to add to this
		self.adjacentNodes = {}

	def addAdjacentNode(self, adjNode, weight):
		self.adjacentNodes[adjNode] = weight

	def get_Name(self):
		return self.name

	def get_Number(self):
		return self.number
	#def add_path():

	#def add

class Graph:
	def __init__(self):
		self.nodeList = {}
		self.nodeCount = 0

	def __iter__(self):
		return  iter(self.nodeList.values())
    	#return iter(self.nodeList.values())
    	#return x

	#def add_Node(self, s_name, n_number, arr_time, depart_time):
	def add_Node(self, s_name, n_number):
		new_node = Node(s_name, n_number)
		#print(new_node.get_Name())
		self.nodeList[n_number] = new_node
		self.nodeCount +=1
		return new_node

	def set_Edge(self, startNode, endNode, departTime, arrTime):
		weight = int(arrTime) - int(departTime) #have to cast this as an int since it is read in as a string 
		#assume that the nodes exist, skipping input validation
		#wighted directional graph, no need to add inverse 
		self.nodeList[startNode].addAdjacentNode(self.nodeList[endNode], weight)


def main():
	
	#declare variables
	trains_list = 'trains.dat'
	station_list = 'stations.dat'
	#create a graph object to store the graph in
	trainSchedule = Graph()

	#code to check if the two files are present -> tell the user and exit if not present
	if not os.path.exists(trains_list) or not os.path.exists(trains_list):
		print('The required files are not present, please run this in the same directory as trains.dat and stations.dat')
		#sys.exit()

	#create a node for each station from the station.dat file
	with open(station_list, 'r') as s_list:
		for station in s_list:
			#print(station)
			number, name = station.split()
			trainSchedule.add_Node(name, number)
			#print(number)
			#print(name)

	#get the edges from the trains.dat file
	with open(trains_list, 'r') as t_list:
		for train in t_list:
			#print(train)
			if train:  #make sure that any blank lines or line breaks are handled correctly
				dep_train, ar_train, dep_time, arr_time = train.split()
			trainSchedule.set_Edge(dep_train, ar_train, dep_time, arr_time)
	#print("train nodes = {}".format(trainSchedule.nodeCount))
	#print(trainSchedule.nodeList)

	for item in trainSchedule:
		print(item.get_Name()) #prints out the name of the node, ie Brooks, etc
		print(item.adjacentNodes)










if __name__ == "__main__":
	# parser = argparse.ArgumentParser(description='This is a script to process a userlist file')
	# parser.add_argument('-t', help='Name of the train list file, eg: trains.dat')
	# args = parser.parse_args()
	# input_file = args.f
	main()
























	# try:
 #    	f_in = open(input_file, 'r')
 #        #logger.info(input_file + ' exists')
 #    except:
 #        print('You must supply a valid filename to be processed, exiting now . . . . ')
 #        #logger.critical('No such file - ' + input_file )
 #        exit()

