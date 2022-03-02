#!/usr/bin/python3
"""
Base model module

"""
import uuid


class BaseModel:
    '''class defines all commons attributes/methods for other classes'''
    def __init__(self, *args, **kwargs):
        '''function to inicialize all instances atrributes'''
        if (kwargs == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%d:%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%d:%H:%M:%S.%f")

    def __str__(self):
        '''string representation of basemodel'''
        return(f"[{}] ({}) {}"(self.__class__.__name__,
                               self.id, self.__dict__))

    def save(self):
        '''update the public instance attributte'''
        self.update_at = datetime.now()

    def to_dict(self):
        '''
        returns a dictionary containing all
        keys/values of __dict__ instance
        '''
        cpy_dic = dict(self.__dict__)
        cpy_dic['__class__'] = self.__class__.__name__
        cpy_dic['updated_at'] = self.updated_at
        .srtftime("%Y-%m-%d%H:%M :%S.%f")
        cpy_dic['created_at'] = self.created_at
        .strftime("%Y-%m-%d %H:%M:%S.%f")
        return(cpy_dic)