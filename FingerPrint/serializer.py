#!/bin/python
#
# LC
# 
# suports serialization of a swirl into xml (and maybe in the future other
# formats
# 

from datetime import datetime
import io
import pickle

"""
"""


class PickleSerializer:
    """
    this class serialize a swirl into a pickle file format

    :type fd: file
    :param fd: the file descritor to be used for serialization
               or deserialization
    """

    def __init__(self, fd):
        self.fd = fd

    def save(self, swirl):
        """
        Saves the given swirl to the file descriptor

        :type swirl: :class:`FingerPrint.swirl.Swirl`
        :param swirl: the Swirl to be serialized
        """
        pickle.dump(swirl, self.fd)

    def load(self):
        """
        Return the Swirl read from the given file descriptor

        :rtype: :class:`FingerPrint.swirl.Swirl`
        :return: the Swirl read from fd
        """
        return pickle.load(self.fd)


class XmlSerializer:
    """
    this serilizes the swirl into xml
    we can have multiple classes for serializing in other format.
    TODO it doesnot work.
    Unused at the moment.
    """

    def __init__(self, fd):
        self.fd = fd

    def save(self, swirl ):
        self.fd.write("<xml>\n")
        self.fd.write("<name>" + swirl.name + "</name>\n")
        self.fd.write("<time>" + swirl.getDate() + "</time>\n")
        self.save_depset(swirl.dependencySet)
        self.fd.write("</xml>")

    def save_depset(self, dependencySet):
        self.fd.write("<depset>\n")
        for i in dependencySet.depSet:
            if isinstance(i, Dependency):
                self.fd.write("<dep>" + i.depname + "</dep>\n")
            else:
                self.save_depset(i)
        self.fd.write("</depset>\n")
    
    def read(self):
        """this should implement the read from xml
        """
        pass
            


