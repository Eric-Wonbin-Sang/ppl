
class TimePair:

    def __init__(self, data_dict):

        self.data_dict = data_dict

        self.start_dt = self.data_dict.get("start_dt")
        self.is_start_dt_concrete = self.data_dict.get("is_start_dt_concrete", True)
        self.end_dt = self.data_dict.get("end_dt")
        self.is_end_dt_concrete = self.data_dict.get("is_end_dt_concrete", True)

    def __str__(self):
        ret_str = "TimePair:"
        data_dict = {
            "start_dt": self.start_dt,
            "is_start_dt_concrete": self.is_start_dt_concrete,
            "end_dt": self.end_dt,
            "is_end_dt_concrete": self.is_end_dt_concrete,
        }
        for key, value in data_dict.items():
            ret_str += "\n\t{}: {}".format(key, value)
        return ret_str
