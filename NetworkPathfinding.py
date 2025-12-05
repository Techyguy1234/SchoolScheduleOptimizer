import networkx as nx

G = nx.Graph() 

# Hallway Points
G.add_node("H0")
G.add_node("H1")
G.add_node("H2")
G.add_node("H3")
G.add_node("H4")
G.add_node("H5")
G.add_node("H6")
G.add_node("H7")
G.add_node("H8")
G.add_node("H9")
G.add_node("H10")
G.add_node("H11")
# Hallway Connections
G.add_edge("H0", "H1", weight=10)
G.add_edge("H1", "H2", weight=10)
G.add_edge("H2", "H3", weight=10)
G.add_edge("H2", "H4", weight=10)
G.add_edge("H3", "H5", weight=10)
G.add_edge("H4", "H6", weight=10)
G.add_edge("H5", "H7", weight=10)
G.add_edge("H6", "H9", weight=10)
G.add_edge("H7", "H8", weight=10)
G.add_edge("H8", "H9", weight=10)
G.add_edge("H7", "H10", weight=10)
G.add_edge("H9", "H11", weight=10)

# Add Classes
G.add_node("AUD")
G.add_edge("AUD", "H1", weight=10)
G.add_node("GYM")
G.add_edge("GYM", "H1", weight=10)
G.add_node("CAFE")
G.add_edge("CAFE", "H1", weight=10)

G.add_node("120")
G.add_edge("120", "H3", weight=10)
G.add_node("122")
G.add_edge("122", "H3", weight=10)

G.add_node("121")
G.add_edge("121", "H4", weight=10)
G.add_node("123")
G.add_edge("123", "H4", weight=10)

G.add_node("124")
G.add_edge("124", "H5", weight=10)
G.add_node("126")
G.add_edge("126", "H5", weight=10)

G.add_node("127")
G.add_edge("127", "H6", weight=10)
G.add_node("125")
G.add_edge("125", "H6", weight=10)

G.add_node("LIB")
G.add_edge("LIB", "H5", weight=25)
G.add_node("LIB")
G.add_edge("LIB", "H3", weight=25)
G.add_node("LIB")
G.add_edge("LIB", "H4", weight=25)
G.add_node("LIB")
G.add_edge("LIB", "H6", weight=25)

G.add_node("128")
G.add_edge("128", "H7", weight=10)

G.add_node("130")
G.add_edge("130", "H10", weight=10)
G.add_node("136")
G.add_edge("136", "H10", weight=10)
G.add_node("134")
G.add_edge("134", "H10", weight=10)
G.add_node("132")
G.add_edge("132", "H10", weight=10)

G.add_node("133")
G.add_edge("133", "H11", weight=10)
G.add_node("131")
G.add_edge("131", "H11", weight=10)
G.add_node("129")
G.add_edge("129", "H11", weight=10)

G.add_node("MUS")
G.add_edge("MUS", "H0", weight=10)
G.add_node("ART")
G.add_edge("ART", "H0", weight=10)

G.add_node("BSMT")
G.add_edge("BSMT", "H0", weight=10)



#targetlocation="CAFE"
#currentlocation="134"
## Find the shortest path between "A" and "D" based on 'weight'
#shortest_path = nx.shortest_path(G, source=currentlocation, target=targetlocation, weight="weight")
#shortest_path_length = nx.shortest_path_length(G, source=currentlocation, target=targetlocation, weight="weight")

#print(f"Shortest path from CAFE to 134: {shortest_path}")
#print(f"Length of the shortest path: {shortest_path_length}")

def get_path(sourceloc,targetloc):
    bestPath=nx.shortest_path(G, source=sourceloc, target=targetloc, weight="weight")
    return bestPath