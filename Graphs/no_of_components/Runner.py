
import no_of_components as noc


ver= input("list down all vertices of the graph as a string: ")
vlist=list(ver)
print("No of vertices in the graph is "+str(len(vlist)))
# print("\nEnter type of graph",end="")
# type=input("d for directed un for undirected: ")
print("\nList down edges of the graph")
print("eg. 12 5,23 2,31 5 and so on..",end="")
ed=input("where 12 5 shows if there is edge to edge 1 to 2 with edgeweight: ")
print("No. of edges  in the graph is "+str(len(ed.split(','))))

c=noc.no_of_components(vlist, ed)
print("No. of connected components is: ",end="")
print(c)