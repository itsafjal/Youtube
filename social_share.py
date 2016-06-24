#! /usr/bin/python

import socialshares


url = "https://www.youtube.com/watch?v=wPxqcq6Byq0"         #any url you want to use


counts = socialshares.fetch(url, ['facebook', 'linkedin'])
facebook = counts['facebook']
linkedin = counts['linkedin']


print "Total Facebook Share =  " + str(facebook)

print "Total Linkedin Share =  " + str(linkedin)


