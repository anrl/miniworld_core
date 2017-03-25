import json
import numbers
from UserDict import UserDict

import re
from collections import OrderedDict


class ConnectionEncoder(json.JSONEncoder):
    def default(self, obj):
        return self.my_encode(obj)

    def encode(self, o):
        return super(ConnectionEncoder, self).encode(self.my_encode(o))

    def my_encode(self, obj, escape_keys=True):
        from miniworld.model.emulation.nodes.EmulationNode import EmulationNode
        from miniworld.model.network.connections.ConnectionDetails import ConnectionDetails
        from miniworld.model.network.interface.Interface import Interface

        def p(obj2):
            return '%s => %s' % (obj, obj2)

        if isinstance(obj, (dict, UserDict)):
            items = map(self.default, obj.items())
                # escape keys -> string
            if escape_keys:
                items = map(lambda (x,y) : (str(x), y), items)
            res = OrderedDict( items )
            # print p(res)
            return res

        elif isinstance(obj, EmulationNode):
            res = str(obj.id)
            # print p(res)
            return res

        elif isinstance(obj, Interface):
            res = obj.node_class_name
            # print p(res)
            return res

        elif isinstance(obj, ConnectionDetails):
            res = obj.link_quality
            # print p(res)
            return res

        elif isinstance(obj, str):
            res = str(obj)
            # print p(res)
            return res

        elif isinstance(obj, int):
            res = str(obj)
            # print p(res)
            return res

        elif isinstance(obj, numbers.Number):
            res = str(obj)
            # print p(res)
            return res

        elif hasattr(obj, "__iter__"):
            res = map(self.default, obj)
            res = tuple(res)
            # print p(res)
            return res
        else:
            return obj

class ConnectionDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super(ConnectionDecoder, self).__init__(*args, **kwargs)
        # match e.g. u'(10, 15)'
        self.regex_str_tuple = re.compile("""
[(]     # "("
(\d+)   # "10"
[,]     # ","
\s*     # " "
(\d+)   # "15"
[)]     # ")"
""", flags=re.VERBOSE)

    def default(self, obj):
        return self.my_decode(obj)

    def decode(self, o):
        return self.my_decode( super(ConnectionDecoder, self).decode(o) )

    def my_decode(self, obj, escape_keys=False):

        if isinstance(obj, (dict, UserDict)):
            items = map(self.my_decode, obj.items())
            res = dict( items )
            return res
        elif isinstance(obj, tuple):
            return map(lambda x : self.my_decode(x, escape_keys=True), obj)
        elif isinstance(obj, (str, unicode)):
            if escape_keys:
                # e.g.  u'(10, 15)' => ('10', '15')
                res = self.regex_str_tuple.search(obj).groups()
                # ('10', '15') => (10, 15)
                res = map(int, res)
                return tuple(res)

        return obj


class JSONStrMixin():

    def __str__(self):
        return str(ConnectionEncoder().my_encode(
            OrderedDict(sorted(self.items())),
            escape_keys=False)
        )

    def to_json(self):
        return json.dumps(
            OrderedDict(sorted(self.items())),
            indent=4, cls=ConnectionEncoder
        )


if __name__ == '__main__':
    # encoded_json = json.dumps(
    #     {
    #         (1,2) : 15,
    #         (2,3) : 0
    #     }
    #     ,cls = ConnectionEncoder
    # )

    encoded_json = '''{
        "(1, 5)": 9223372036854775807,
        "(1, 14)": 9223372036854775807,
        "(1, 7)": 9223372036854775807,
        "(1, 16)": 9223372036854775807,
        "(1, 9)": 9223372036854775807,
        "(2, 7)": 9223372036854775807,
        "(1, 15)": 9223372036854775807,
        "(1, 3)": 9223372036854775807,
        "(2, 3)": 1,
        "(2, 8)": 9223372036854775807,
        "(2, 4)": 9223372036854775807,
        "(2, 13)": 9223372036854775807,
        "(1, 12)": 9223372036854775807,
        "(2, 15)": 9223372036854775807,
        "(2, 10)": 9223372036854775807,
        "(2, 16)": 9223372036854775807,
        "(1, 6)": 9223372036854775807,
        "(2, 11)": 9223372036854775807,
        "(2, 14)": 9223372036854775807,
        "(1, 8)": 9223372036854775807,
        "(1, 11)": 9223372036854775807,
        "(2, 6)": 9223372036854775807,
        "(1, 2)": 1,
        "(2, 12)": 9223372036854775807,
        "(1, 4)": 9223372036854775807,
        "(2, 5)": 9223372036854775807,
        "(1, 10)": 9223372036854775807,
        "(1, 13)": 9223372036854775807,
        "(2, 9)": 9223372036854775807
    }'''

    print encoded_json
    decoded_json = json.loads(encoded_json, cls = ConnectionDecoder)
    print decoded_json
