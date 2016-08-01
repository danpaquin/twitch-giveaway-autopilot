import socket, time, re

class TwitchWinner():
    def __init__(self, chan='', nick='', password=''):
        self.host = "irc.chat.twitch.tv"
        self.port = 6667
        self.chan = chan
        self.nick = nick
        self.password = password # www.twitchapps.com/tmi/
        self.msgTimer = 0
        self.setup()

    def setup(self):
        self.conn = socket.socket()
        self.conn.connect((self.host, self.port))
        self.send_pass(self.password)
        self.send_nick(self.nick)
        self.join_channel(self.chan)
        print("joined %s" %self.chan)

    def pong(self, sender):
        self.conn.send('PONG %s\r\n' %sender)

    def send_message(self, chan, msg):
        message = 'PRIVMSG %s :%s\r\n' % (chan, msg)
        if time.time() - self.msgTimer > 90:
            self.msgTimer = time.time()
            self.conn.send(message)
            print("\nSENT %s\n" % (message))

    def send_nick(self, nick):
        self.conn.send('NICK %s\r\n' %nick)

    def send_pass(self, password):
        self.conn.send('PASS %s\r\n' %password)

    def join_channel(self, chan):
        self.conn.send('JOIN #%s\r\n' %chan)

    def part_channel(self, chan):
        self.conn.send('PART %s\r\n' %chan)

    def get_sender(self, msg):
        result = ""
        for char in msg:
            if char == "!":
                break
            if char != ":":
                result += char
        return result

    def get_message(self, msg):
        result = ""
        i = 3
        while i < len(msg):
            result += msg[i] + " "
            i += 1
        result = result.lstrip(':')
        return result

    def parseMessage(self, msg):
        if len(msg) > 0:
            msg = msg.split(' ')
            if "viewbot" in str(msg).lower():
                self.send_message(self.chan, "I r MrDestructoid")

    def start(self):
        data = ""
        msg_List = [" "] * 2 #array length 2
        counter = 0

        fileName = "%s_%s.txt" %(self.chan, time.time())
        f = open(fileName, 'w+')

        while True:
            try:
                data = data + self.conn.recv(1024)
                data_split = re.split(r"[~\r\n]+", data)
                data = data_split.pop()

                for line in data_split:
                    line = str.rstrip(line)
                    line = str.split(line)

                    if len(line) > 0:
                        if line[0] == 'PING':
                            self.pong(line[1])
                            print("HEY! I was just pinnged")

                        if line[1] == 'PRIVMSG':
                            sender = self.get_sender(line[0])
                            message = self.get_message(line)
                            self.parseMessage(message)

                            index = counter%2
                            msg_List[index] = message.lower()
                            counter += 1
                            if msg_List[0] == msg_List[1]:
                                f.write("%s\n" % message.lower())
                                msg_List = [" ", " "]
                                time.sleep(0.1)
                                self.send_message(self.chan, message)

                            print(sender + ": " + message)

            except KeyboardInterrupt:
                break

            except socket.error as e:
                print("Socket closed: ", e)
                break

        f.close()