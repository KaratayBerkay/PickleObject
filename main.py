import pickle
import codecs
import json


class ExClass(object):
    variable1: str
    variable2: str
    variable3: str
    variable4: str
    variable5: str
    variable6: str

    @staticmethod
    def my_function() -> str:
        return 'This is a example <class> function'


def pickle_object_to_txt(input_object: object, name: str):
    pickled = codecs.encode(pickle.dumps(input_object), "base64").decode()
    dict_pickle_bytes = {name: pickled.__str__().replace('\\', '/')}
    print('pickled data :', type(dict_pickle_bytes))
    print('pickled data.__dict__ : ', dict_pickle_bytes[name])
    with open("pickled.pickle", "wb") as outfile:
        pickle.dump(dict_pickle_bytes, outfile, protocol=pickle.HIGHEST_PROTOCOL)
    with open("pickled.json", "wb") as outfile:
        j_ = json.dumps(dict_pickle_bytes, indent=2).encode('utf-8')
        outfile.write(j_)
    return pickled


def unpickle_object_to_txt(name: str):
    with open('pickled.pickle', 'rb') as openfile:
        un_serialized_data = pickle.load(openfile, encoding='utf-8')[name]
        un_pickled = pickle.loads(codecs.decode(un_serialized_data.encode(), "base64"))
        print('--------------------------------------------')
        print('un-pickled pickle data :', type(un_pickled))
        print('un-pickled pickle data.__dict__ : ', un_pickled.__dict__)
        openfile.close()
    with open('pickled.json', 'rb') as openfile:
        un_jsoned = json.loads(openfile.read())[name]
        un_serialized_data = pickle.loads(codecs.decode(un_jsoned.encode(), "base64"))
        print('--------------------------------------------')
        print('un-pickled json data :', type(un_pickled))
        print('un-pickled json data.__dict__ : ', un_pickled.__dict__)
        return un_pickled, un_jsoned


if __name__ == '__main__':

    ex_class = ExClass()
    ex_class.variable1 = "vaşiable#"
    ex_class.variable2 = "vöriableĞ"
    ex_class.variable3 = "variableÜ"
    ex_class.variable4 = "variable3"
    ex_class.variable5 = "variİble2"
    ex_class.variable6 = "variableŞ"

    pickle_class = pickle_object_to_txt(input_object=ex_class, name="pickle_created")
    unpickle_class = unpickle_object_to_txt(name="pickle_created")


