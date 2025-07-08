class Package:
    import uuid
    def __init__(self, id, sender, recipient, status):
        self.id = id
        self.sender = sender
        self.recipient = recipient
        self.status = status

    def add_to_record(self, record_dict):
        record_dict["id"].append(self.id)
        record_dict["sender"].append(self.sender)
        record_dict["recipient"].append(self.recipient)
        record_dict["status"].append(self.status)

