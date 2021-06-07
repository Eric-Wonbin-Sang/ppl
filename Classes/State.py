from Classes import TimePair, Note

from General import Functions


class State:

    def __init__(self, data_dict):

        self.data_dict = data_dict

        self.value = self.data_dict["value"]
        self.time_pair_list = self.get_time_pair_list()

        self.note_list = self.get_note_list()

    def get_time_pair_list(self):
        return [
            TimePair.TimePair(data_dict) for data_dict in self.data_dict.get("time_pair_list", [])
        ]

    def get_note_list(self):
        return [
            Note.Note(data_dict) for data_dict in self.data_dict.get("note_list", [])
        ]

    def __str__(self):
        ret_str = "State: value = {}".format(self.value)

        if self.time_pair_list:
            ret_str += "\n\ttime_pair_list:"
            for time_pair in self.time_pair_list:
                ret_str += "\n" + Functions.tab_str(time_pair, 2)

        if self.note_list:
            ret_str += "\n\tnote_list:"
            for note in self.note_list:
                ret_str += "\n" + Functions.tab_str(note, 2)

        return ret_str
