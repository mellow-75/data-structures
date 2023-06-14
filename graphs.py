class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        for start , end in self.edges:
            if start in self.graph_dict:
                pass
            else:
                self.graph_dict[start]=[end]

        print("graph dict :",self.graph_dict)






    def get_paths(self,start, end,path=[]):
        path= path +[start]
        if start ==end:
            return [path]

        if start not in self.graph_dict[start]:
            return []
        paths=[]

        for node in self.graph_dict[start]:
            if node not in path:
                new_paths=self.get_paths(node,end,path)
                for p in new_paths:
                    paths.append(p)

        return paths


    def get_shortest_path(self,start,end,path=[]):
        path=path+[start]

        if start ==end:
            return path

        if start not in self.graph_dict:
            return None

        








routes = [
    ("mumbai", "paris"),
    ("mumbai", "dubai"),
    ("paris", "dubai"),
    ("paris", "new york"),
    ("dubai", "new york"),
    ("new york", "toronto")
]


route_graph=Graph(routes)
start ="mumbai"
end="new york"

print(f"paths between(start) and (end): ", route_graph.get_paths(start,end))