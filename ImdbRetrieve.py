#!/usr/bin/env python
"""
get_top_bottom_movies.py

Usage: get_top_bottom_movies

Return top and bottom 10 movies, by ratings.
"""

import sys

# Import the IMDbPY package.
import imdb




i = imdb.IMDb()
out_encoding = sys.stdout.encoding or sys.getdefaultencoding()

def testIMDB():
    top250 = i.get_top250_movies()
    bottom100 = i.get_bottom100_movies()


    for label, ml in [('top 10', top250[:10]), ('bottom 10', bottom100[:10])]:
        print ''
        print '%s movies' % label
        print 'rating\tvotes\ttitle'
        for movie in ml:
            outl = u'%s\t%s\t%s' % (movie.get('rating'), movie.get('votes'),
                                        movie['long imdb title'])
            print outl.encode(out_encoding, 'replace')

def writeTop250(path):
    fichier = open(path, "w")
    top250 = i.get_top250_movies()
    bottom100 = i.get_bottom100_movies()

    for label, ml in [('top 10', top250), ('bottom 10', bottom100)]:
        print ''
        print '%s movies' % label
        print 'rating\tvotes\ttitle'
        for movie in ml:
            outl = u'%s\t%s\t%s' % (movie.get('rating'), movie.get('votes'),
                                    movie['long imdb title'])
            print outl.encode(out_encoding, 'replace')
            fichier.write(outl.encode(out_encoding, 'replace'))
            fichier.write("\n")
            #fichier.write(movie.summary().encode(out_encoding, 'replace'))
    fichier.close()
movie_list = i.search_movie('the passion')
first_match = movie_list[0]
print first_match.summary()
i.update(first_match)

print("-----DEBUT DE NOTRE PARTIE -------")
def retrieveNmovie(n, path):
    fichier = open(path, "w")

    for movieID in range (3000, 3000+n):

        movie = i.get_movie(str(movieID))
        outl = u'%s\t%s\t%s' % (movie.get('rating'), movie.get('votes'),
                                movie['long imdb title'])
        fichier.write(outl.encode(out_encoding, 'replace'))
        fichier.write("\n")
    fichier.close()

#writeTop250("textFile.txt")
retrieveNmovie(2000, "Retrieved.txt")