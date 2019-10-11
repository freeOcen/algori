from collections import deque
#将图抽象成散列表
graph = {}
#将你映射到一个数组，数组中包含了你的所有邻居
graph["you"] = ["alice","bob","claire"]
#依次按层级将其他节点和其邻居映射到散列表
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["peggy"] = []
graph["anuj"] = []
graph["thom"] = []
graph["jonny"] =[]


def person_is_seller(name):
    return name[-1] == 'm'

#假设我们要查找你的邻居中是否有姓名是m结尾的人（类似查找从是否有从A-B的路径）。下面是实现过程。
#增加一个数组用来记录已经检查过的人，防止重复检查和死循环

def search(name):
    #创建一个队列
    search_queue = deque() 
    #将你的邻居都加入到这个搜索队列
    search_queue += graph[name]
    searched = []
    while search_queue: #只有队列不为空
        person = search_queue.popleft() #取出其中的第一个人
        if person not in searched:
            if(person_is_seller(person)):
                print(person + "is a seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)        
    return False

search("you")
search("alice")