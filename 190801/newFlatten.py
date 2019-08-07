def getMinmax(boxes):
    if boxes[0] > boxes[1]:
        mIndex, mValue= [1,0], [boxes[1],boxes[0]]
    else:
        mIndex, mValue= [0,1], [boxes[0],boxes[1]]

    for e, box in enumerate(boxes):
        if box >= mValue[1]:
            mIndex[1], mValue[1] = e, box
        if box <= mValue[0]:
            mIndex[0], mValue[0] = e, box

    return [mIndex, mValue]

for t in range(10):
    dumpTotal = int(input())
    boxes = list(map(int, input().split()))
    count = 0

    while count < dumpTotal:
        
        minmax = getMinmax(boxes)
        diff = minmax[1][1] - minmax[1][0]
        
        #check Flat
        if diff == 0 or diff == 1:
            break

        #if not flat: dump
        boxes[minmax[0][0]] += 1
        boxes[minmax[0][1]] -= 1
        count += 1

        minmax = getMinmax(boxes)
        diff = minmax[1][1] - minmax[1][0]

    print('#{0} {1}'.format(t+1,diff))
    