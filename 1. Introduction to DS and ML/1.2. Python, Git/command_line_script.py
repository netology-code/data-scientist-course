# -*- coding: utf-8 -*-
# Построчная обработка файлов с помощью командной строки
# Про Argparse https://docs.python.org/3/howto/argparse.html

import sys
import argparse

parser = argparse.ArgumentParser( description = 'Get user id' )
parser.add_argument( '--ids', help = 'Enter user ids list like --ids "1 5 44"' )
args = parser.parse_args()

idsList = args.ids.split(' ')

firstLine = True
started = True

for line in sys.stdin:
	if firstLine:
		firstLine = False

	else:
		line = line.strip().split(',')

		if line[0] in idsList:

			currentUser = line[0]
			currentRating = float( line[2] )

			if started:
				previousUser = currentUser
				previousRating = currentRating

				userSumRatings = currentRating
				nUserRatings = 1

				started = False

			else:
				if previousUser == currentUser:
					userSumRatings += currentRating
					nUserRatings += 1

					previousRating = currentRating

				else:
					print( previousUser, userSumRatings / nUserRatings )

					previousUser = currentUser
					previousRating = currentRating

					userSumRatings = currentRating
					nUserRatings = 1

print( previousUser, userSumRatings / nUserRatings )