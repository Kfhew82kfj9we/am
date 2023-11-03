import scripts
if __name__ == '__main__':
    try:
        print(scripts.schedule_scripts({
            1: [2, 3, 4, 5],
            2: [4, 5, 6, 7],
            3: [2, 4, 5],
            4: [9, 10],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
            10: [],
        }))
    except Exception as e:
        print(e)
