'''Objects/Classes Experiment'''

# Developed by Smit Rao



class Locker(object):
    '''A locker object.'''
    def __init__(self, status='Closed'):
        self.status = status
        
    def open(self):
        self.status = 'Open'
        
    def close(self):
        self.status = 'Closed'