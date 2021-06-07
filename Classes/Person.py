from Classes import Property, Note

from General import Functions


class Person:

    def __init__(self, data_dict):

        self.data_dict = data_dict

        self.property_list = self.get_property_list()
        self.note_list = self.get_note_list()

    def get_property_list(self):
        return [
            Property.Property(data_dict) for data_dict in self.data_dict.get("property_list", [])
        ]

    def get_note_list(self):
        return [
            Note.Note(data_dict) for data_dict in self.data_dict.get("note_list", [])
        ]

    def __str__(self):
        ret_str = "Person Instance"
        for prop in self.property_list:
            ret_str += "\n" + Functions.tab_str(prop)
        return ret_str
