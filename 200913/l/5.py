class Person:

    def __init__(self):
        self.hand = []

    def get_candi(self, n):
        candi = []

        for i in range(2**n):
            cur_res = 0
            for j in range(n):
                if i & (1 << j):
                    cur_res += 11
                else:
                    cur_res += 1
            candi.append(cur_res)
        return list(set(candi))

    
    def score(self):
        ### 여기 채우기
        if 1 in self.hand:
            candi = self.get_candi(self.hand.count(1))
            rest_sum = sum([0 if card == 1 else card for card in self.hand])

            candi_sum = [c + rest_sum for c in candi]

            res_num = -1

            for number in candi_sum:
                if number == 21:
                    res_num = 21
                    break
                elif number > 21:
                    continue
                else:
                    res_num = max(res_num, number)

            if res_num == -1:
                return 22
            else:
                return res_num
            
        else:
            return sum(self.hand)

    def get_length(self):
        return len(self.hand)

    def put(self, card):
        if card > 10:
            card = 10
        self.hand.append(card)
    
    def flush(self):
        self.hand = []


def solution(cards):

    card_index = 0

    # status 0 : step 0,1
    # status 1 : step 2,4
    # status 2 : question
    step = 0
    
    player = Person()
    dealer = Person()

    answer = 0

    while card_index < len(cards):
        print(answer, card_index, cards, 'step', step, 'hands' ,player.hand, player.score(), dealer.hand, dealer.score())
        cur_card = cards[card_index]
        if step == 0:
            player.put(cur_card)
            card_index += 1
            step += 1

        elif step == 1:
            dealer.put(cur_card)
            card_index += 1
            step += 1

        elif step == 2:
            player.put(cur_card)
            card_index += 1
            step += 1

        elif step == 3:
            dealer.put(cur_card)
            step = 3.5
        
        elif step == 3.5:
            if player.score() == 21:
                answer += 3
                step = 11
            elif dealer.score() == 21:
                answer -= 2
                step = 11
            elif player.score() == 21 and dealer.score() == 21:
                step = 11
            else:
                step = 4

        elif step == 4:
            # playing section
            next_step = 8
            for d_card in dealer.hand:
                if d_card in (2,3) and player.score() < 12:
                    next_step = 5
                    card_index += 1
                    break
                
            for d_card in dealer.hand:
                if d_card in (4,5,6):
                    next_step = 6
                    break

            for d_card in dealer.hand:
                if d_card in (1,7,8,9,10) and player.score() < 17:
                    next_step = 7
                    card_index += 1
                    break

            step = next_step

        # card = 2 or 3
        elif step == 5:
            player.put(cur_card)
            if player.score() < 12:
                card_index += 1
            else:
                step = 8
            

        # skip
        elif step == 6:
            step = 8

        # card = 1 or 7 up
        elif step == 7:
            player.put(cur_card)
            if player.score() < 17:
                card_index += 1
            else:
                step = 8

        elif step == 8:
            if dealer.score() < 17:
                card_index += 1
                step = 9

        elif step == 9:
            dealer.put(cur_card)
            if dealer.score() < 17:
                card_index += 1
            else:
                step = 10

        elif step == 10:
            if dealer.score() > 21:
                if player.score() > 21:
                    step = 11
                else:
                    answer += 2
                    step = 11
            elif player.score() > 21:
                if dealer.score() > 21:
                    step = 11
                else:
                    answer -= 2
                    step = 11
            
            elif player.score() == 21 and dealer.score() == 21:
                step = 11

            elif player.score() == 21:
                step = 11
                answer += 3

            elif dealer.score() == 21:
                step = 11
                answer -= 2
            
            elif dealer.score() > player.score():
                answer -= 2
                step = 11
            
            elif dealer.score() < player.score():
                answer += 2
                step = 11

            else:
                step = 11

        elif step == 11:
            player.flush()
            dealer.flush()
            step = 0
            card_index += 1

    return answer


print(solution([12, 7, 11, 6, 2, 12]))
print(solution([1, 4, 10, 6, 9, 1, 8, 13]))
print(solution([10, 13, 10, 1, 2, 3, 4, 5, 6, 2]))
print(solution([3, 3, 3, 3, 3, 3, 3, 3, 3, 3]))

    

