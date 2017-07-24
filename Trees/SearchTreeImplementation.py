class TreeNode:
    def __init__(self, key, val, left = None, right = None, parent = None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc

        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self




class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def lenght(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    """
    Метод будет выполнять проверку на наличие корня дерева, а в случае отсутствия последнего
    создавать объект TreeNode и устанавливать его, как корневой узел.
    В противном случае put вызовет приватную рекурсивную вспомогательную функцию _put
    для поиска места в дереве по следующему алгоритму:
        Начиная от корня, проходим по двоичному дереву, сравнивая новый ключ с ключом текущего узла.
        Если первый меньше второго, то идём в левое поддерево. Наоборот - в правое.

        Когда не осталось левых или правых потомков для поиска - мы нашли позицию для установки нового узла.

        Чтобы добавить узел в дерево, создаём новый объект TreeNode и помещаем его на
        найденное за предыдущие шаги место.
    """

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)

        else:
            self.root = TreeNode(key, val)

        self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent = currentNode)

        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent = currentNode)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)

            if res:
                return res.payload

            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True

        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')

        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1

        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    """
    Если у узла есть правый потомок, то преемник - наименьший ключ в правом поддереве.

    Если у узла нет правого потомка и сам он - левый потомок родителя, то преемником будет родитель.

    Если узел - правый потомок своего родителя и сам правого потомка не имеет,
    то его преемником будет преемник родителя (исключая сам этот узел).
    """

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()

        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent

                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self

        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild

        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None

            else:
                self.parent.rightChild = None

        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild

                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent

            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild

                else:
                    self.parent.rightChild = self.rightChild

                self.rightChild.parent = self.parent

    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None

            else:
                currentNode.parent.rightChild = None

        elif currentNode.hasBothChildren(): #interior

            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

            """
            Если текущий узел - левый потомок, то нужно всего лишь обновить родительскую ссылку на него у предка,
            а затем обновить ссылку его потомка, чтобы она указывала на нового родителя.

            Если текущий узел - правый потомок, то мы обновляем родительскую ссылку его потомка,
            чтобы она указывала на предка текущего узла, а затем - ссылку на правого потомка у родителя текущего узла.

            Если текущий узел предка не имеет, то он должен быть корнем.
            В этом случае мы просто заменяем данные key, payload, leftChild и rightChild,
            вызвав для корня метод replaceNodeData."""

        else:           #This node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild

                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild

                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)

            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild

                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild

                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)

if __name__ == '__main__':
    myTree = BinarySearchTree()
    myTree[3] = "red"
    myTree[4] = "blue"
    myTree[6] = "yellow"
    myTree[2] = "at"

    print(myTree[6])
    print(myTree[2])




