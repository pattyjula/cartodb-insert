#import modules
import urllib
import urllib2


username =  'pattyjula' #Do not include @email.com
apikey ='yourkey' # let's get this value from our account on cartodb.com
url = "https://%s.cartodb.com/api/v1/sql" % username # create the URL

# these are the rows being added to CartoDB table
rows = [
    "(CDB_LatLng(34.051559, -118.243184), 'Owl', '110 Main St', 'Los Angeles', 'CA')",
    "(CDB_LatLng(34.139544, -118.207939), 'Squirrel', '5105 Hermosa Ave', 'Los Angeles', 'CA')",
    "(CDB_LatLng(33.974055, -118.277816), 'Horse', '7218 S Broadway', 'Los Angeles', 'CA')",
    "(CDB_LatLng(33.745817, -118.296934), 'Lizard', '906 W Sepulveda St', 'San Pedro', 'CA')"
]

# Create your SQL statement, matching values with existing field names in table
insert = "INSERT INTO newtable(the_geom, name, street, city, state) (VALUES %s)" % ','.join(rows)
print insert
params = {
    'api_key' : apikey, # your CartoDB api key
    'q'       : insert  # insert statement above
}

req = urllib2.Request(url, urllib.urlencode(params)) # prepare the URL
response = urllib2.urlopen(req) # open URL

print "Made it"


