
class PropertyManager:

    def __init__(self, person_list):

        self.person_list = person_list
        self.keyword_list = self.get_keyword_list()

    def get_keyword_list(self):
        keyword_list = []
        for person in self.person_list:
            for prop in person.property_list:
                if prop.keyword not in keyword_list:
                    keyword_list.append(prop.keyword)
        return keyword_list

    def __str__(self):
        ret_str = "PropertyManager:"
        for keyword in self.keyword_list:
            ret_str += "\n\t{}".format(keyword)
        return ret_str
