from collections import deque
"""
Здесь реализован поиск в ширину напримере поиска продавца манго среди
друзей и их друзей, в функции person_is_seller продавцом является тот,
у кого последняя буква в имени 'm'
"""

def person_is_seller(name):
    return name[-1] == 'm'


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
print(graph)


def search_mango_seller(name):
    search_queque = deque()
    search_queque += graph[name]
    searched = []

    while search_queque:
        person = search_queque.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is mango seller!")
                return True
            else:
                search_queque += graph[person]
                searched.append(person)
    return False


search_mango_seller("you")
