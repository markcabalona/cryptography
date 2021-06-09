import numpy as np

class Key_matrix:    
    def __init__(self, dimension, key):
        self.dim = dimension
        self.key = key.reshape(self.dim,self.dim)
    
    def get_inverse(self):
        ''' returns the invese of the key matrix '''
        return np.linalg.inv(self.key)
    
    def validate_key(self):
        ''' Matrix key has to have an inverse. 
        If the user's key doesn't have one, matrix key will be set to default key '''
        try:
            self.get_inverse()
        except:
            default_key = np.identity(self.dim, dtype = int)
            global valid_key
            return default_key
        return self.key
    


class Translator(Key_matrix):
    def __init__(self, key, message):
        self.key = key.validate_key()
        self.key = np.array(self.key)
        self.key_inv = np.linalg.inv(self.key)
        self.message = message
        self.dim = key.dim

    def encode(self):
        '''
            Steps in encoding:
            1. check if the length of message is divisible by the dimension of matrix key,
                if not, append a space(" ") until it is
            2. convert each character of the message into its corresponding ASCII code.
            3. transfrom the result of step 2 into an array of 1 by (dimension of matrix key) 2d array
            4. multiply each item in the result of step 3 by the matrix key
            
        '''
        #step 1
        if len(self.message) % self.dim != 0:
            self.message = self.message + (" "*(self.dim-(len(self.message) % self.dim)))
        
        numerical_message = list()
        coded_message = list()
        #transforming the message to its numerical value
        #step 2
        for letter in self.message:
                numerical_message.append(ord(letter))

        numerical_message = np.array(numerical_message)

        #grouping the numerical message into 1 by dim arrays
        grouped_message = numerical_message.reshape(round(len(numerical_message)/self.dim),self.dim,1)
        print(np.shape(grouped_message))
        for message in grouped_message:
            coded_message.append(np.dot(self.key,message))
            
        coded_message = np.array(coded_message)
        coded_message = coded_message.reshape((round(len(coded_message)*self.dim),))

        return coded_message



    def decode(self):
        """
            Steps in decoding a message:
            1. get the inverse of matrix key
            2. transfrom the message into an array of 1 by (dimension of matrix key) 2d array.
            3. multiply each 2d array in 3d array by key inverse of matrix key
            4. convert each item in the result of step 3 to its corresponding character in ASCII code
        """
        decoded_message = str()
        self.message = np.array(self.message)
        #step 2
        grouped_message = self.message.reshape(round(len(self.message)/self.dim),self.dim,1)

        for message in grouped_message:
            #step 3
            numerical_message = np.dot(self.key_inv,message)
            for msg in numerical_message:
                for i in msg:
                    #step 4
                    #converting the numeric form to its corresponding letter
                    decoded_message += chr(round(i))
                    
        return decoded_message

