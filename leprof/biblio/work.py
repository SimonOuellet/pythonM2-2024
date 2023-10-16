import shortuuid
class Work:
    """A work is a set of books that are the same work"""
    def __init__(self):
        """Work Constructor"""
        self.workid = None
        self.eans = []
        self.number_of_books = len(self.eans)

    def generate_workid(self)->None:
        """If no workid is set, generate one"""
        if not self.workid:
            self.workid = shortuuid.uuid()

    def gererate_workid_from(source: str)->str:
        """Generate a workid from a string"""
        return shortuuid.uuid(name=source)