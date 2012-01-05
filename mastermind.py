#!/usr/bin/python

import random

def test_guess(correct, guess):
	black = len([1 for a, b in zip(correct, guess) if a == b])
	other = [(a, b) for a, b in zip(correct, guess) if a != b]
	sa = sorted(x[0] for x in other)
	sb = sorted(x[1] for x in other)
	ia, ib = 0, 0
        white = 0
        while ia < len(sa) and ib < len(sb):
		a = sa[ia]
		b = sb[ib]
		if a == b:
			white += 1
                        ia += 1
                        ib += 1
		elif a < b:
			ia += 1
		else:
			ib += 1

	return black, white


def autoguess(correct):
	options = [(a, b, c, d) for a in range(6) for b in range(6) for c in range(6) for d in range(6)]

	steps = 0

	while(len(options) > 1):
          steps += 1		
	  guess = options[1]
	  options2 = options[:]
	  guess_result = test_guess(correct, guess)

	  for i in range(len(options2)):
	    if guess_result[0] < test_guess(options2[i],guess)[0]:
	      options.remove(options2[i])
	      continue

	    if guess_result[1] < test_guess(options2[i],guess)[1]:
	      options.remove(options2[i])

	print 'Solution: {}, steps: {}'.format(options[0], steps)

if __name__ == "__main__":
	six_diseases = ['plague', 'gout', 'scurvy', 'cancer', 'gangrene', 'syphillis']
	correct = [random.choice(range(6)) for i in xrange(4)]
        print "Solution", correct

	enum_diseases = enumerate(six_diseases)
	print ''.join('{} {}\n'.format(i, d) for i, d in enum_diseases)	
	
	autoguess(correct)
	print '-' * 80
	print "Now you"
	print '-' * 80

	for x in xrange(10):
		print 'Guess {} out of 10. What is your guess?'.format(x+1)
		guess = [int(x) for x in raw_input()]
		if len(guess) != 4:
			print "invalid guess. try again"
			continue
		black, white =  test_guess(correct, guess)
		print "black {} white {}".format(black, white)
		if black == 4: 
			print "you win {} and {}".format(', '.join(six_diseases[i] for i in guess[:3]), six_diseases[guess[3]])
			break
	
	else:
		print "you lose"
			
		

