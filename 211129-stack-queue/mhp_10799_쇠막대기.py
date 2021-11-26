"""
1) 완전한 막대 수, 쪼개진 막대 수 설정
2) 레이저 만날 시에 쪼개진막대수 += 완전한 막대 수
3) 막대가 끝날 시 막대-1 
"""
import sys

comm = sys.stdin.readline().rstrip()

def get_nums(comm):

	nstick = 0
	tot = 0
	laser = '@'
	comm = comm.replace('()', laser)
	
	for c in comm:
		if c=='(':
			nstick+=1
			tot+=1
		elif c==laser:
			tot+=nstick
		elif c==')':
			nstick-=1
			#tot-=1
			
	return tot
	
print(get_nums(comm))