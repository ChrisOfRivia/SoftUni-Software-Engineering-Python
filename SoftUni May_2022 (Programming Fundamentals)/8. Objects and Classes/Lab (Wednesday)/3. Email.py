class Email:
    def __init__(self, sender, receiver, content):
        self.is_sent = False
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent:{self.is_sent}"


emails = []

messages = input()
while not messages == 'Stop':
    sender, receiver, content = messages.split()
    email = Email(sender, receiver, content)
    emails.append(email)
    messages = input()

send_emails = [emails[int(x)].send() for x in input().split(", ")]

for email in emails:
    print(email.get_info())


