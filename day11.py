def acyclic_dfs(src: str, target: str, graph: dict[str, list[str]]) -> int:
    if src == target:
        return 1
    children = graph[src]
    acc = 0
    for child in children:
        acc += acyclic_dfs(child, target, graph)
    return acc

def main():
    graph = dict[str, list[str]]()
    with open("reactor.txt") as file:
        while line := file.readline():
            line = line.split()
            node = line[0][:-1]
            children = line[1:]
            graph[node] = children
    print(acyclic_dfs("you", "out", graph))
    
if __name__=="__main__":
    main()