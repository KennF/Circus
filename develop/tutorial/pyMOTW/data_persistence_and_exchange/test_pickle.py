try:
    import cPickle as pickle
except:
    import pickle

import pprint
from StringIO import StringIO

def simple_pickle():
    data = [{'a':'A', 'b':2, 'c':3.0}]
    print 'data:'
    pprint.pprint(data)
    data_string = pickle.dumps(data)
    pprint.pprint(data_string)

    data1 = pickle.loads(data_string)
    pprint.pprint(data1)
    print "same?", data is data1
    print "equal?", data==data1

class simple_object(object):
    def __init__(self, name):
        self.name = name;
        self.name_reversed = self.name[::-1]

def pickle_stringio():
    '''
    It's quite easy to replace StringIO in the this example with file or socket
    the object definition(class definition) should be exist in both side of server(dump)/client(load) side

    For object can't be pickled, can define some magic mathod help to serialize, refer to SL doc.
    '''
    l = []
    l.append(simple_object('test'))
    l.append(simple_object('pickle'))
    l.append(simple_object('cPickle'))

    out_s = StringIO()
    for i in l:
        print "Write %s:%s" % (i.name, i.name_reversed)
        pickle.dump(i, out_s)
        out_s.flush()

    pprint.pprint(out_s.getvalue())


    in_s = StringIO(out_s.getvalue())

    while(True):
        try:
            o = pickle.load(in_s)
        except EOFError:
            break
        else:
            print "Read %s:%s"% (o.name, o.name_reversed)

class Node(object):
    def __init__(self, name):
        self.name = name;
        self.connections = []
        return

    def add_edge(self, node):
        self.connections.append(node)
        return

    def __iter__(self):
        return iter(self.connections)

def preorder_traverasl(root, )



if __name__ == '__main__':
    simple_pickle()
    pickle_stringio()