import unittest

from xid import Xid

TestXids = [
    # taken from https://github.com/rs/xid/blob/master/id_test.go
    {
        'xid': Xid([0x4d, 0x88, 0xe1, 0x5b, 0x60, 0xf4, 0x86, 0xe4, 0x28, 0x41, 0x2d, 0xc9]),
        'ts': 1300816219,
        'machine': ''.join(map(chr, [0x60, 0xf4, 0x86])),
        'pid': 0xe428,
        'counter': 4271561
    },
    {
        'xid': Xid([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
        'ts': 0,
        'machine': ''.join(map(chr, [0x00, 0x00, 0x00])),
        'pid': 0x0000,
        'counter': 0
    },
    {
        'xid': Xid([0x00, 0x00, 0x00, 0x00, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0x00, 0x00, 0x01]),
        'ts': 0,
        'machine': ''.join(map(chr, [0xaa, 0xbb, 0xcc])),
        'pid': 0xddee,
        'counter': 1
    }
]

class TestXid(unittest.TestCase):
    def test_no_duplicates(self):
        collect = []
        for i in range(0, 1000):
            collect.append(Xid())

        ids = [i.string() for i in collect]
        self.assertEqual(len(set(ids)), 1000)

    def test_from_string(self):
        x = Xid()
        y = Xid.from_string(x.string())

        self.assertEqual(x.value, y.value)
        self.assertEqual(x.bytes(), y.bytes())
        self.assertEqual(x.string(), y.string())

    def test_timestamp(self):
        for x in TestXids:
            self.assertEqual(x.get('xid').time(), x.get('ts'))

    def test_machine(self):
        for x in TestXids:
            self.assertEqual(x.get('xid').machine(), x.get('machine'))
            
    def test_pid(self):
        for x in TestXids:
            self.assertEqual(x.get('xid').pid(), x.get('pid'))

    def test_counter(self):
        for x in TestXids:
            self.assertEqual(x.get('xid').counter(), x.get('counter'))

    def test_copy_array_from_golang(self):
        x = Xid([0x4d, 0x88, 0xe1, 0x5b, 0x60, 0xf4,
                 0x86, 0xe4, 0x28, 0x41, 0x2d, 0xc9])
        self.assertEqual('9m4e2mr0ui3e8a215n4g', x.string())

    def test_copy_string_from_golang(self):
        x = Xid.from_string('9m4e2mr0ui3e8a215n4g')
        self.assertEqual(x.value, [0x4d, 0x88, 0xe1, 0x5b, 0x60, 0xf4,
                                   0x86, 0xe4, 0x28, 0x41, 0x2d, 0xc9])

if __name__ == '__main__':
    unittest.main()

