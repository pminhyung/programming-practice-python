def solution(numbers, hand):
    g = [(3, 1),
         (0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2),
         (3, 0), (3, 2)]

    def get_dist(n, hand):
        curr_r, curr_c = g[hand][0], g[hand][1]
        nr, nc = g[n][0], g[n][1]
        return abs(curr_r - nr) + abs(curr_c - nc)  # l1 norm

    hand_short = 'R' if hand == 'right' else 'L'
    answer = ''
    left_hand, right_hand = -2, -1

    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            left_hand = n
        elif n in [3, 6, 9]:
            answer += 'R'
            right_hand = n
        else:
            if get_dist(n, left_hand) > get_dist(n, right_hand):
                answer += 'R'
                right_hand = n
            elif get_dist(n, left_hand) < get_dist(n, right_hand):
                answer += 'L'
                left_hand = n
            else:
                answer += hand_short
                if hand == 'right':
                    right_hand = n
                else:
                    left_hand = n
    return answer