# 1 get min max and dump

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

# ================================================

# 2 sort and dump
for t in range(10):
    dumpTotal = int(input())
    boxes = list(map(int, input().split()))
    count = 0

    # sort first
    for i in range(len(boxes),-1,-1):
        for j in range(i-1):
            if boxes[j] > boxes[j+1]:
                boxes[j], boxes[j+1] = boxes[j+1], boxes[j]
                
    while count < dumpTotal:
        # get difference / check flat
        diff = boxes[-1] - boxes[0]
        if diff == 0 or diff == 1:
            break

        # dump / count
        boxes[0] += 1
        boxes[-1] -= 1
        count += 1

        # rearrange
            # 1) sort again
        # for i in range(len(boxes),-1,-1):
        #     for j in range(i-1):
        #         if boxes[j] > boxes[j+1]:
        #             boxes[j], boxes[j+1] = boxes[j+1], boxes[j]
            # 2) sort changed items
        # boxes[0]
        for i in range(99):
            while boxes[i] > boxes[i+1]:
                boxes[i], boxes[i+1] = boxes[i+1], boxes[i]
        for i in range(99,0,-1):
            while boxes[i] < boxes[i-1]:
                boxes[i], boxes[i-1] = boxes[i-1], boxes[i]

        # get difference
        diff = boxes[-1] - boxes[0]

    print('#{0} {1}'.format(t+1,diff))