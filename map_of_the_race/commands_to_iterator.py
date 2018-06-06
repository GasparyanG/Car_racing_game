class Commands:
    def __init__(self, iterator):
        self.iterator = iterator

    def is_used(self, comparable_object):
        raise NotImplementedError()

    def to_command(self):
        raise NotImplementedError()


class NextItem(Commands):
    def is_used(self, comparable_object):
        return comparable_object == "R"

    def to_command(self, data_structure):
        return self.iterator.next_item(data_structure)


class CurrentItem(Commands):
    def is_used(self, comparable_object):
        return comparable_object == "D"

    def to_command(self, data_structure):
        return self.iterator.current_item(data_structure)


class PreviousItem(Commands):
    def is_used(self, comparable_object):
        return comparable_object == "L"

    def to_command(self, data_structure):
        return self.iterator.previous_item(data_structure)    