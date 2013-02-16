def count(n):
    mapper = {
        0:0,
        1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4,
        10:3, 11:6, 12:6, 13:8, 14:7, 15:7, 16:7, 17:9, 18:9, 19:8,
        20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6
    }
    char_count = 0
    for i in range(1,n+1):
        if i == 1000:
            char_count += len("onethousand")
            break
        if i >= 100:
            x,i = hundies(i)
            char_count += mapper[x] + len("hundred")
            if i != 0:
                char_count += 3
        if i > 20 and i < 100:
            t = tens(i)
            char_count += mapper[t[0]] + mapper[t[1]]
        else:
            char_count += mapper[i]
    return char_count

def tens(n):
    s = str(n)
    tenner = int(s[0]) * 10
    digit = int(s[1])
    return (tenner, digit)

def hundies(n):
    s = str(n)
    return (int(s[0]), int(s[1:]))

if __name__=="__main__":
    print(count(1000))