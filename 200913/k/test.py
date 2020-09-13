
def solution(new_id):
    answer = []

    new_id = new_id.lower()

    step2 = 'abcdefghijklmnopqrstuvwxyz1234567890-_.'
    
    ans_step2 = []
    for ch in new_id:
        if ch in step2:
            ans_step2.append(ch)
    
    print(''.join(ans_step2))
    
    ans_step3 = [ans_step2[0]]

    for i in range(1, len(ans_step2)):
        cur_ch = ans_step2[i]

        if cur_ch == '.' and ans_step3[-1] == '.':
            continue
        else:
            ans_step3.append(cur_ch)
        
    ans_step4 = []

    ans_step4 = ans_step3[:]

    if len(ans_step4) != 0:
        if len(ans_step4) == 1:
            if ans_step4[0] == '.':
                ans_step5 = ['a']
            else:

                ans_step5 = ans_step4[:]
        else:
            if ans_step4[0] == '.':
                ans_step4 = ans_step4[1:]
            if ans_step4[-1] == '.':
                ans_step4 = ans_step4[:-1]

            ans_step5 = ans_step4[:]
    else:
        ans_step5 = ['a']

    if len(ans_step5) >= 16:
        ans_step6 = ans_step5[:15]
    else:
        ans_step6 = ans_step5[:] 
    
    if ans_step6[-1] == '.':
        ans_step6 = ans_step6[:-1]

    ans_step7 = ans_step6[:]

    while len(ans_step7) < 3:
        ans_step7.append(ans_step7[-1])

    print(ans_step7)
    

    return ('').join(ans_step7)
    

solution("...!@BaT#*..y.abcdefghijklm")
solution("abcdefghijklmn.p")

