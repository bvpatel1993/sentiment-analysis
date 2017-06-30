
import Orange

# cities sequence Austin, Berkely, Boston, Chicago, San Jose, Washington D.C
album_artist_data = ["Taylor Swift, Backstreet Boys, Rihanna",
                     "Lady Gaga, Rihanna, Adele",
                     "Lady Gaga, Backstreet, Rihanna",
                     "Taylor Swift, Rihanna, Adele",
                     "Taylor Swift, Lady Gaga, Backstreet Boys"]



# write data to the text file: data.basket
f = open('artist.basket', 'w')
for item in album_artist_data:
    f.write(item + '\n')
f.close()

# Load data from the text file: data.basket
data = Orange.data.Table("artist.basket")


# Identify association rules with supports at least 0.4
statements = Orange.associate.AssociationRulesSparseInducer(data, support = 0.4)


# print out rules
print "%4s %4s  %s" % ("Supp", "Conf", "Rule")
for r in statements[:]:
    print "%4.1f %4.1f  %s" % (r.support, r.confidence, r)

rule = statements[0]
for idx, d in enumerate(data):
    print '\nCity {0}: {1}'.format(idx, album_artist_data[idx])
    for r in statements:
        if r.applies_left(d) and not r.applies_right(d):
            print "%4.1f %4.1f  %s" % (r.support, r.confidence, r)

