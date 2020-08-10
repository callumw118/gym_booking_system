class Member:
    def __init__(self, full_name, membership, status="Active", id=None):
        self.full_name = full_name
        self.membership = membership
        self.status = status
        self.id = id