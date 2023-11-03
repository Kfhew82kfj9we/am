def schedule_scripts(scripts):
    scripts_data = scripts.copy()
    ordered = []
    temp_set = []
    for k in list(scripts_data.keys()):
        scripts_data[k] = list(set(scripts_data[k]))
        if not scripts_data[k]:
            temp_set.append(k)
            del scripts_data[k]

    while temp_set:
        n = temp_set.pop()
        ordered.append(n)
        for m in list(scripts_data.keys()):
            if n in scripts_data[m]:
                scripts_data[m].remove(n)
            if not scripts_data[m]:
                temp_set.insert(0, m)
                del scripts_data[m]
    if scripts_data:
        raise Exception("Cycle or unlisted dependency detected")
    else:
        return ordered
