states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kone"] = set(["id", "nv", "ut","wa","mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

#贪心算法:遍历所有的集合，从中选择覆盖了最多的未覆盖名称的集合。策略就是每次都选取剩余集合中包含最多个当前还未选择的名称的集合。
while states_needed:
    best_station = None
    states_covered = set()
    #从剩余集合中找到最优解
    for station,states in stations.items():
        #计算两个集合的交集
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)


print(final_stations)