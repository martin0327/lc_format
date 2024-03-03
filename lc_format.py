while True:
    s = input()
    s = s.replace('Input: ', '')
    a = s.split(', ')
    for t in a:
        if '[[[' in t:
            t = "vector<vector<vector<int>>> " + t
        elif '[[' in t:
            t = "vector<vector<int>> " + t
        elif '[' in t:
            t = "vector<int> " + t
        else:
            t = "int " + t
        if '"' in t: 
            t = t.replace('int','string')
        t = t.replace('[', '{').replace(']', '}')
        t += ';'
        print(t)
