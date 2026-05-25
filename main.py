def main():
    
    print("Enter box size")
    box = int(input())

    print("Enter sum")
    target = int(input())

    print (counting(box, target, 1))


def counting(box, target, min_part):
    if box == 1:
        possib = []
        targets = [target]
        possib.append(targets)
        return possib

    possible_range = target//box

    answer = []

    for f in range (min_part, possible_range +1):
        subs = counting (box-1, target-f, f)
        for sub in subs:
            sub.insert(0, f)
            answer.append(sub)

    return answer

main()