import numpy as np


class Matrix_key:
    def __init__(self,dimension: int, key:list):
        self.dimension = dimension
        self.key = np.array(key)
        self.key = np.reshape(self.key,(self.dimension,self.dimension))
        # self.default_key = np.identity(dimension,dimension)
    
    def validate_key(self):
        validity = bool()
        try:
            np.linalg.inv(self.key)
            validity = True
        except:
            validity = False
            self.key = np.identity(self.dimension,int)
        return validity

class Decipher():
    def __init__(self, key:Matrix_key, message:list, mode:str):
        self.message = message
        self.key = key
        self.mode = mode

        if self.mode.lower() == "encode":
            for i in range(len(self.message)):
                self.message[i] = ord(self.message[i])
            if len(self.message) % self.key.dimension != 0:
                for i in range(self.key.dimension - (len(self.message) % self.key.dimension)):
                    self.message.append(ord(" "))
    
    def convert(self):
        self.message = np.array(self.message)
        message = self.message.reshape((round(len(self.message)/self.key.dimension), self.key.dimension))

        converted_message = list()
        if self.mode.lower() == "encode":
            for i in message:
               converted_message.append(np.dot(i,self.key.key))

            return np.array(converted_message).flatten()

        else:#decode
            print(np.linalg.inv(self.key.key))
            for i in message:
                converted_message.append(np.dot(i,np.linalg.inv(self.key.key)))
            
            print(np.array(converted_message).flatten())
            
        return ''.join(map(str,self.translate(np.array(converted_message).flatten())))

    def translate(self,message):
        translated_message = list()
        if self.mode.lower() == "encode":
            for letter in message:
               translated_message.append(ord(letter))

        else:
            for letter in message:
                translated_message.append(chr(round(letter)))

        return translated_message
        


# print("start")
# dimension = 2
# #key = [0,0,0,0]
# key = [1,2,3,4]

# message_str = "h"
# message_int = [200,336]
# print(ord("c"))


# key1 = Matrix_key(2,key)
# if key1.validate_key():
#     print("valid")
# else:
#     print("invalid key ", key1.key, " will be used")

# out = Decipher(key1,list(message_str),"encode")
# out1 = Decipher(key1, message_int,"decode")

# print(out.convert(),"\n\n#####################################\n\n",out1.convert())
# print("end")





