#!/bin/python3
import re, sys, string
polymer = ""
rgx = [ 'aA', 'bB', 'cC', 'dD', 'eE', 'fF', 'gG', 'hH', 'iI', 'jJ', 'kK', 'lL', 'mM', 'nN', 'oO', 'pP', 'qQ', 'rR', 'sS', 'tT', 'uU', 'vV', 'wW', 'xX', 'yY', 'zZ', 'Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj', 'Kk', 'Ll', 'Mm', 'Nn', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt', 'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz' ]
with open('input.txt') as f:
	polymer = f.readline().strip()

def reaction(polymer):
	poly = polymer
	reactions = 0
	while any(reg in poly for reg in rgx):
		for reg in rgx:
			poly = re.sub(reg, '', poly)
			reactions +=1
		sys.stdout.write("\r%d reactions"% reactions)
		sys.stdout.flush()
	return(poly)

def prereact(polymer):
	fixed = {}
	for i in string.ascii_lowercase:
		reg = re.compile(i, re.IGNORECASE)
		fixed[i] = re.sub(reg, '', polymer)
	for pmer in fixed:
		print('\nReplacing %s: %d' % (pmer, len(reaction(fixed[pmer]))))

if __name__ == '__main__':
	prereact(polymer)
	polymer = reaction(polymer)
	print("\nCompleted! Final length: %d" % len(polymer))
