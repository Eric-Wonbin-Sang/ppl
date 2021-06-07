from Classes import Person, PropertyManager

from General import Functions, Constants


def get_person_list(json_file_path):
    return [
        Person.Person(person_dict) for person_dict in Functions.get_json_data(json_file_path)
    ]


def get_property_manager(person_list):
    return PropertyManager.PropertyManager(person_list)


def main():

    person_list = get_person_list(Constants.ppl_json_file_path)
    for person in person_list:
        print(person)

    property_manager = get_property_manager(person_list)
    print(property_manager)


if __name__ == '__main__':
    main()
