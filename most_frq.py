def most_frequent(string):
    d = {}
    for letter in string:
        d[letter] = d.get(letter,0)+1
    sorted_dict = dict(sorted(d.items(),key=lambda item:item[1],reverse=True))
    print(sorted_dict)

s='mississippi'
most_frequent(s)
