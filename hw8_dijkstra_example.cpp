#void GRAPH::dijkstra(int source)
def dijkstra(self, )
{

	//array to hold 'the value at this node is finalized'
	//int finalized[];
	//array to track weights from source to all other nodes - holds actual costs
	//int weights[];
	//array to hold distances
	int distance[nodeCount];  //set distances to infinity? Still not 100% sure why
	//vector<bool> visited;
	int visited[nodeCount];  
	stack<int> s;
	int dist_val = INT_MAX;
	int v = 0;
	int min;

	//initialize the vector like an array
	for (int i=0; i < nodeCount; i++)
	{
		visited[i] = 0; //0 for false 1 for true
	}

	//create the distance matrix from the adjacency matrix -> REMEMBER i =0 which is actually node 1
	for(int i=0; i < nodeCount; i++)
		//distance[i] = -1;
		distance[i] = matrix[0][i];  //set the distance really large for the line below that compares

	
	//set the source distance to itself to zero
	distance[0] = 0;
	//set the source node to visited
	visited[0] = 1;
	//for(;;)
	for(int i = 0; i < nodeCount; i++)
	{
		// //printing out the distance list each itertation since i do not knwo why 0 is getting any distance added
		// for (int i = 1; i < nodeCount; i++)
		// 	{cout << "1 -> "<< i << " / " << distance[i] << endl;
		// 	}

		// cout << "===========" << endl;

			//v = smallest unknown distance vertex
		//get the smallest unknown distance -> unknown being 999999999999 here
		//**************OLD SELECTOR*********************************
		// for(int x = 0; x < nodeCount; x++)
		// {
		// 	if( !visited[x] && dist_val > distance[x])  //the node was not visited yet and its min value is greater 
		// 		dist_val = distance[x]; //set the new distance value to check against
		// 		v = x; 
		// }

		min = dist_val;
		//check the visited array and if they have not been visited find the smallest distance if smaller then our current one
		for(int x = 0; x < nodeCount; x++)
		{
			//cout << x << " : " << visited[x] << endl;
			//if(visited[x] == false && min > distance[x])
			//if(min > distance[x] && visited[x] == 0)  //this never executes!!!!!!!! WWWHHHHYYYYYYYYYYYY!!!!!!!!!!!!!!
			if(visited[x] == 0)
			{
				//cout << "Visited #" << x << endl;
				if(distance[x] < min)
				{
					//cout << "new min set: " <<  distance[x] << endl;
					min = distance[x];
					v = x; 
					//cout << "v: is " << v << endl;
				}
			}
		}

		//if no v -> //break
		//cout << "v is " << v << endl;
		if(visited[v] == 0)  //why is this executing on 0??????
		{
			//cout << "v: isssss " << v << endl;
			//v.known = true -> set the visited array to true so that we do not go through this again
			visited[v] = 1;
				//for each w adajacent to v
				for(int w = 0; w < nodeCount; w++)
				{
					//if !w.known
					if(matrix[v][w] != 0) // adjacency exists 
						//the value is not equal to zero so there is an adjacency 
						//if(v.distance + cvw) < w.dist
						//if((min + matrix[v][w] ) < distance[w])  //this never fires so it never changes the distance 
						if(distance[w] == 0 ) //distance for the node not calculated
							distance[w] = min + matrix[v][w];
						else if(distance[w] > distance[v] + matrix[v][w] ) 
							distance[w] = min + matrix[v][w];
							//cout << "this ever go off? " << endl;
							//decrease w.dist to v.dist + cvw
							//distance[w] = min + matrix[v][w];
				}
		}
	}

	// print out our results
	cout << "\nDijkstra\n========\n";
	for (int i = 1; i < nodeCount; i++)
	{
		cout << "1 -> "<< i << " / " << distance[i];
		cout << endl;
	}
}