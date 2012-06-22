# the store must use dictionaries because it allows you to map one item of a particular type to another item of another type

#printing items and price
market={'Apples':  '5GHC','Bananas':  '2GHC','Bread':'1GHC','Carrot':'2GHC','Champaigne':'4GHC','strawberies':'16GHC'}
for key,value in market.iteritems():
    print key, '    ',   value

    # manipulating the dictionary

'''market['strawberies']='20GHC'
market['chicken']='30GHC'
print pairs'''
