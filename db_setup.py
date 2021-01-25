'''
Setup for adding the data to the database
It is the process_files.py code but rewritten
to work with the postgressql db
Edlee Ducay
'''
class Babynames(db.Model):
    '''
    Table object extends the sqlalchemy db model
    '''

    __tablename__ = 'babynames'
    name = db.Column(db.String(100), primary_key = True)
    year = db.Column(db.Integer, primary_key = True)
    rank_boy = db.Column(db.Integer)
    rank_girl = db.Column(db.Integer)
    freq_boy = db.Column(db.Integer)
    freq_girl = db.Column(db.Integer)

    def __init__(self, name, year, rank_boy=0, rank_girl=0, freq_boy=0, freq_girl=0):
        self.name = name
        self.year = year
        self.rank_boy = rank_boy
        self.rank_girl = rank_girl
        self.freq_boy = freq_boy
        self.freq_girl = freq_girl

def load_file(db, filename = 'baby-names-frequency-2017.txt'):
    '''
    This function will load the file and create/return dictionaries for the names
    
    Parameters:
    string
        filename of the list of names
    Return:
    dictionary
        a dictionary for the top ten lists and the names
        
    '''
    
    # Error Checking the files
    print('HELLO')
    try:
        file = open(filename, 'r', encoding = 'utf-16')
        data = file.read()
        file.close()
    except:
        print('File does not exist')
        return None
    
    # Splitting data and removing unnecessary lines
    data = data.split('\n')
    for i in range(5):
        data.pop(0)
    
    # Processing data
    add_data(db, data)

    return
    
def add_data(db, text):
    '''
    Adds the data to the db
    '''
    base_table = db.session.query(Babynames)
    for line in text:
        name = line.split('\t')
        if base_table.filter(Babynames.name != name[1] and Babynames.year != name[4]):
            data = Babynames(name[1], name[4])
            db.session.add(data)
            db.session.commit()
        query = base_table.filter(Babynames.name == name[1] and Babynames.year == name[4])
        if name[3] == 'Boy':
            query.rank_boy = name[0]
            query.freq_boy = name[2]
        elif name[3] == 'Girl':
            query.rank_girl = name[0]
            query.freq_girl = name[2]
        db.session.commit()

        return


def create_topTen_dict(data):
    
    # Creating the dictionary
    topTen_dict = {'boys': {}, 'girls': {}}
    data.pop()
    
    for line in data:
        name = line.split('\t')

        if 'Boy' in name and int(name[0]) <= 10:
            topTen_dict['boys'].setdefault(int(name[4]))
            if topTen_dict['boys'][int(name[4])] == None:
                topTen_dict['boys'][int(name[4])] = []
            topTen_dict['boys'][int(name[4])].append([int(name[0]), name[1], int(name[2])])
        elif 'Girl' in name and int(name[0]) <= 10:
            topTen_dict['girls'].setdefault(int(name[4]))
            if topTen_dict['girls'][int(name[4])] == None:
                topTen_dict['girls'][int(name[4])] = []
            topTen_dict['girls'][int(name[4])].append([int(name[0]), name[1], int(name[2])])

    return topTen_dict

def create_names_dict(data):
    '''
    This function creates the names dictionary
    
    Parameters:
    list
        data of names in form of a list
    Return
    dictionary
        the names dictionary
        
    '''
    
    # Creating the dictionary
    names_dict = {}
    for line in data:
        name = line.split('\t')
        names_dict.setdefault(name[1])
        if names_dict[name[1]] == None:
            names_dict[name[1]] = []
        names_dict[name[1]].append([int(name[2]), name[3], int(name[4])])

    return names_dict
