from collections import deque
import json


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

print("GRAPH: ", json.dumps(graph, indent=1))

def people_is_seller(people):
    return people[-1] == "m"

def search(name):
    queue_search = deque()
    queue_search += graph[name]
    verified = []

    while queue_search:
        people = queue_search.popleft()
        if not people in verified:

            if people_is_seller(people):
                print(people + " is seller")
                return True
            else:
                queue_search += graph[people]
                verified.append(people)

    return False

search("you")
