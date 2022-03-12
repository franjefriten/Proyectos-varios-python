import json
import numpy as np  

def max0(listtup):
    cand = (0, 0)
    for i in range(len(listtup)):
        if cand < listtup[i]:
            cand = listtup[i]
    for i in range(len(listtup)):
        if cand == listtup[i]:
            return i

class friends():

    def __init__(self):
        self.friends = []
        self.relations = []

    def add_friend(self, nombre):
        self.friends.append({"id": len(self.friends), "name": nombre})
    
    def add_SetFrienship(self, num1, num2):
        self.relations.append( (num1, num2) )
        if len(self.relations) > 1:
            for i in range(len(self.relations)-1, 0, -1):
                max_index1, max_index2 = max0(self.relations[:i]), max0(self.relations[i:])
                self.relations[max_index1], self.relations[max_index2] = self.relations[max_index2], self.relations[max_index1]
    
    def __str__(self):
        print("Friends: ")
        for friend in self.friends:
            for k, v in friend.items():
                print(str(k)+": "+str(v), end="\t")
            print("\n")
        print("Friendships: ")
        alreadyPrinted = []
        for relation in self.relations:
            if relation[::-1] not in self.relations:
                print( str(relation[0]) + " -> " + str(relation[1]) )
            else:
                if relation[::-1] not in alreadyPrinted:
                    print( str(relation[0]) + " <-> " + str(relation[1]) )
                    alreadyPrinted.append( relation )


    def len(self):
        print(self.friends)

    def get_friends(self, name):
        if name not in self.friends: return None
        else:
            for friend in self.friends:
                if friend["name"] == name:
                    id = friend["id"]

            for relation in self.relations:
                if relation[0] == id:
                    id_fr = relation[1]
                    for friend in self.friends:
                        if friend["id"] == id_fr:
                            print(friend["name"])

    def count_relations(self):
        print(len(self.relations))

#    def find_most_connected(self):
#        number_of_friends = []
#        for persona in self.friends:
#            number_of_friends.append( {"id": persona["id"], "nof": self.friends.get_friends( persona["name"] ) } )
#        cand = number_of_friends[0]
#        for f in number_of_friends:
#            if f["nof"] > cand:
#                cand = f["nof"]
#        return cand["id"]


amigps = friends()
amigps.add_friend("John")
amigps.add_friend("Fred")
amigps.add_friend("James")
amigps.add_friend("Jeff")
amigps.add_SetFrienship(0, 1)
amigps.add_SetFrienship(1, 2)
amigps.add_SetFrienship(3, 2)
amigps.add_SetFrienship(1, 0)
amigps.add_SetFrienship(2, 0)
amigps.add_SetFrienship(2, 1)
amigps.count_relations()
amigps.len()
amigps.find_most_connected()




