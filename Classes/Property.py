from Classes import State, Note

from General import Functions


class Property:

    def __init__(self, data_dict):

        self.data_dict = data_dict

        self.keyword = self.data_dict["keyword"]
        self.state_list = self.get_state_list()
        self.note_list = self.get_note_list()

    def get_state_list(self):
        return [
            State.State(data_dict) for data_dict in self.data_dict.get("state_list", [])
        ]

    def get_note_list(self):
        return [
            Note.Note(data_dict) for data_dict in self.data_dict.get("note_list", [])
        ]

    def __str__(self):
        ret_str = "Property: keyword = {}".format(self.keyword)

        if self.state_list:
            ret_str += "\n\tstate_list:"
            for state in self.state_list:
                ret_str += "\n" + Functions.tab_str(state, 2)

        if self.note_list:
            ret_str += "\n\tnote_list:"
            for note in self.note_list:
                ret_str += "\n" + Functions.tab_str(note, 2)

        return ret_str
