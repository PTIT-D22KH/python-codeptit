# pykt083.py

def main():
    # Write your code here
    d = {}
    a = []
    topic = ""
    isTopic = True
    for _ in range(int(input())):
        s = input()
        if (s.strip() == ""):
            topic = ""
            isTopic = True
        else:
            if not isTopic:
                d[topic].append(s)
            else:
                topic = s
                d[topic] = []
                isTopic = False
            if len(d) == 0:
                topic = s
                isTopic = False
    for key,value in d.items():
        print(f"{key}: {len(value)}")
    
        
if __name__ == '__main__':
    main()
