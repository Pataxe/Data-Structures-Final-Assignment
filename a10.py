
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
		#dictionary/array to store node adjacancies & weights-> need a method to add to this
		self.adjacentNodes = {}

	def getPathWeight(self, node_number):
		if node_number in self.adjacentNodes:
			return self.adjacentNodes[node_number]

	def addAdjacentNode(self, adjNode, weight):
		self.adjacentNodes[adjNode] = weight

	def get_Name(self):
		return self.name

	def get_Number(self):
		return self.number
	
	def getAdjacentNodesList(self):
		return self.adjacentNodes


class Graph:
	def __init__(self):
		self.nodeList = {}
		self.nodeCount = 0
		self.schedule=[]

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
		#print(self.nodeList[startNode].adjacentNodes)

	def set_schedule(self, startNode, endNode, departTime, arrTime):
		#declare a temp dictionary to store the schedule entry in 
		temp_dict = {}
		#this will create a dictionary that is in the format of {depart_station:number, arr_station:number, depart_time:time, arr_time:time}
		temp_dict['d_station'] = startNode
		temp_dict['a_station'] = endNode
		temp_dict['d_time'] = departTime
		temp_dict['a_time'] = arrTime
		#add the dictionary to the list
		self.schedule.append(temp_dict)
		#to access the list use self.schedule[]

	def getNodeCount(self):
		#return self.nodeCount
		return len(self.nodeList)

def dijkstra(train_sched, source):
	#ADAPTED THIS FROM MY LAST ASSIGNMENT
	#array to hold finalized value
	finalized = []
	#array to track weights from source to all other nodes - holds actual costs
	#weights = []
	#array to hold distances
	distance = [train_sched.getNodeCount()]
	#array to hold the visited nodes
	visited = []
	#visited = [train_sched.getNodeCount()]
	#python lists can act as a stack with the append and pop list methods
	stack = []
	#value to fill in array with
	dist_val = float('inf')
	# i cant remember what this variable is for, will update when I do
	v = 0

	#create a matrix from the graph because I cannot figure out how to implement Dijkstra for a list
	matrix_bounds = train_sched.getNodeCount() + 1 #because of the array starting at zero
	matrix = [[0 for x in range(matrix_bounds)] for y in range(matrix_bounds)] 
	#add the values to the matrix
	for i in train_sched.nodeList:
		nlist = train_sched.nodeList[i].getAdjacentNodesList()
		for key, value in nlist.items():
			matrix[int(i)][int(key.get_Number())]= int(value)

	#initialize the visited array & create the distance array from the matrix
	ctr = 0
	while ctr < train_sched.getNodeCount(): #0 for false and 1 for true
		visited.append(0)
		distance.append(matrix[source][ctr+1]) 
		ctr+=1

	#create the distance array from the adjacency array
	for j in distance:
		print(j)
		#distance[j] = 0  #just for debugging
		#distance[j] = matrix[0][i]; 
	
	distance[0] = 0
	visited[source] = 1


def printSchedule(train_sched):
	print('Full Train Schedule')
	for item in train_sched.schedule:
		print("Departure to " + train_sched.nodeList[item.get('a_station')].get_Name() + ' at ' + item.get('d_time') + ', arriving at ' + item.get('a_time'))
	print('\n')

def printStationSchedule(train_sched):
	stationID = input("Enter the station ID: ")
	print("Schedule for " + train_sched.nodeList[stationID].get_Name() + ":")
	for item in train_sched.schedule:
		if item.get('d_station') == stationID:
			print("Departure to " + train_sched.nodeList[item.get('a_station')].get_Name() + ' at ' + item.get('d_time') + ', arriving at ' + item.get('a_time'))		
	print('\n')

def getStationName(train_sched):
	s_number = input('Enter the station number: ')
	if train_sched.nodeList[s_number]:
		print(train_sched.nodeList[s_number].get_Name())
		return None                                             #return none to exit the if statement
	print('Station #{} not found'.format(s_number))

def getStationID(train_sched):
	s_name = input('Enter the station name: ')
	for d_item in train_sched.nodeList:                                        #loop through the node list for each node 
		if s_name.lower() in train_sched.nodeList[d_item].get_Name().lower():  #use the lower case to normalize getting the name from the nodelist
			print(train_sched.nodeList[d_item].get_Name() + ' is Station number '  + str(train_sched.nodeList[d_item].get_Number())) 
			return None				#return none to exit the if statement
	print('Station {} not found'.format(s_name))
	#print('ran getStationID')

def serviceAvailable(train_sched):
	print('ran service available')

def nonstopService(train_sched):
	print('ran nonstop service')

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
			trainSchedule.set_schedule(dep_train, ar_train, dep_time, arr_time)
	#print("train nodes = {}".format(trainSchedule.nodeCount))
	#print(trainSchedule.nodeList)

	#initialize user selection otherwise it errors out because of 
	user_selection=''
	#prnt the menu
	
	print('\n')
	print("========================================================================")
	print("                    READING RAILWAYS SCHEDULER")
	print("========================================================================")
	print("Options - (Enter the number of your selected option)")
	print("(1) - Print full schedule")
	print("(2) - Print station schedule")
	print("(3) - Look up stationd id")
	print("(4) - Look up station name")
	print("(5) - Service available")
	print("(6) - Nonstop service available")
	print("(7) - Find route (Shortest riding time)")
	print("(8) - Find route (Shortest overall travel time)")
	print("(9) - Exit")

	while user_selection != 9:
		#get the user's selection
		try:
			user_selection = int(input("Enter Option: "))
		except:
			print('Please enter a number')

		#call the function based on the user input
		if user_selection == 1:
			printSchedule(trainSchedule)
		elif user_selection == 2:
			printStationSchedule(trainSchedule)
		elif user_selection == 3:
			getStationID(trainSchedule)
		elif user_selection == 4:
			getStationName(trainSchedule)
		elif user_selection == 5:
			serviceAvailable(trainSchedule)
		elif user_selection == 6:
			nonstopService(trainSchedule)
		elif user_selection == 7:
			print('need ')
		elif user_selection == 8:
			dijkstra(trainSchedule, 3)
			#print('need')
		elif user_selection == 9:
			print('Goodbye!')
			sys.exit()
		else:
			print('Invalid selection, please try again')

	#this just prints out the things below for troubleshooting
	for item in trainSchedule:
		print(item.get_Name()) #prints out the name of the node, ie Brooks, etc
		print(item.adjacentNodes)



if __name__ == "__main__":
	# parser = argparse.ArgumentParser(description='This is a script to process a userlist file')
	# parser.add_argument('-t', help='Name of the train list file, eg: trains.dat')
	# args = parser.parse_args()
	# input_file = args.f
	main()



			#print(matrix[row][val])
			#print(str(i) + ' ' + str(key.get_Number()) + ' ' +  str(value))
		#print(train_sched.nodeList[i].getAdjacentNodesList())
		#ctr = 1
		#while ctr < (train_sched.getNodeCount() + 1):
			#print('I: ' + str(i) + ' node: ' + str(ctr))
			#ctr+=1


			#print(train_sched.nodeList[i].getPathWeight(node))
			#ctr+=1
		#print(train_sched.nodeList[i].getPathWeight(i))
		#print(train_sched.nodeList[i].get_adjacentNode(i))
		#for key in i.adjacentNodes:
			#print (i[key])
		#for node in  i.adjacentNodes:
			#print(node)


		
		#def getPathWeight(self, node_number):
		#return self.adjacentNodes[node_number]


	# try:
 #    	f_in = open(input_file, 'r')
 #        #logger.info(input_file + ' exists')
 #    except:
 #        print('You must supply a valid filename to be processed, exiting now . . . . ')
 #        #logger.critical('No such file - ' + input_file )
 #        exit()

	# for row in matrix:
	# 	print(row)
	#  	for val in row:
	#  		print(val)
