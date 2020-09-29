import sys
import pymongo

uri = 'mongodb+srv://admin:admin123@cluster0.f9acl.gcp.mongodb.net/labWeb?retryWrites=true'

def insertUserData(message, intent):
    client = pymongo.MongoClient(uri)
    db = client.get_default_database()

    database = db["data"]

    database.insert({"intent": intent, "question": message})

    client.close()


###############################################################################
# main
###############################################################################

def main(args):

    client = pymongo.MongoClient(uri)
    SEED_DATA = [
        {
            'decade': '1970s',
            'artist': 'Debby Boone',
            'song': 'You Light Up My Life',
            'weeksAtOne': 10
        },
        {
            'decade': '1980s',
            'artist': 'Olivia Newton-John',
            'song': 'Physical',
            'weeksAtOne': 10
        },
        {
            'decade': '1990s',
            'artist': 'Mariah Carey',
            'song': 'One Sweet Day',
            'weeksAtOne': 16
        }
    ]
          
    db = client.get_default_database()
    
    songs = db['songs']

    cursor = songs.find({'weeksAtOne': {'$gte': 10}}).sort('decade', 1)

    for doc in cursor:
        print ('In the %s, %s by %s topped the charts for %d straight weeks.' %
               (doc['decade'], doc['song'], doc['artist'], doc['weeksAtOne']))

    client.close()


if __name__ == '__main__':
    main(sys.argv[1:])