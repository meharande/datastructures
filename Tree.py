class EcommerceFiltersTree:
    def __init__(self, category):
        self.category = category
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        return self.children[len(self.children) - 1]

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def treeTraverse(self):
        value = self.category
        spaces = ' ' * self.get_level() * 2
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.treeTraverse()

def prepareTree():
    gorceries = EcommerceFiltersTree('Groceries')
    dailyNeeds = gorceries.add_child(EcommerceFiltersTree('Daily needs'))
    vegetables = gorceries.add_child(EcommerceFiltersTree('Vegetables'))
    milkProducts = gorceries.add_child(EcommerceFiltersTree('Milk products'))

    dailyNeeds.add_child(EcommerceFiltersTree('Tea'))
    dailyNeeds.add_child(EcommerceFiltersTree('Sugar'))
    dailyNeeds.add_child(EcommerceFiltersTree('Salt'))

    vegetables.add_child(EcommerceFiltersTree('Onion'))
    vegetables.add_child(EcommerceFiltersTree('Lady finger'))
    vegetables.add_child(EcommerceFiltersTree('Carrot'))

    milkProducts.add_child(EcommerceFiltersTree('Milk'))
    milkProducts.add_child(EcommerceFiltersTree('Curd'))
    milkProducts.add_child(EcommerceFiltersTree('Butter'))

    return gorceries

if __name__ == '__main__':
    groceries = prepareTree()
    groceries.treeTraverse()
