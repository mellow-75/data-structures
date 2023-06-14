class TreeNode:
    def __init__(self, data):
        self.data=data
        self.children=[]
        self.parent=None


    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent

        return level



    def print_tree(self):
        spaces=" " * self.get_level()*3
        prefix=spaces+"|__" if self.parent else ""


        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()



def build_product_tree():
    root=TreeNode("electronics")

    laptop=TreeNode("laptop")
    laptop.add_child(TreeNode("MAC"))
    laptop.add_child(TreeNode("surface"))
    laptop.add_child(TreeNode("thinkpad"))


    cellphone=TreeNode("cellphone")
    cellphone.add_child(TreeNode("iphone"))
    cellphone.add_child(TreeNode("google pixel"))
    cellphone.add_child(TreeNode("vivo"))


    tv=TreeNode("TV")
    tv.add_child(TreeNode("samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root



root=build_product_tree()
print(root.get_level())
root.print_tree()
pass