class PropertyTest(object):
    def __init__(self, name, *args, **kw):
        super(PropertyTest, self).__init__(*args, **kw)
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

if __name__ == '__main__':
    p = PropertyTest('ken')
    print p.name
    p.name = 'fu'
    print p.name

