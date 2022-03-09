from tkinter import *
from tkinter.ttk import Treeview
import xml.etree.ElementTree as ET

class App:

    def __init__(self, root):

       
            with open("Actividad.xml") as xml:
                read_data = xml.read()

            rootNode = ET.fromstring(read_data)

            self.tree = Treeview(root)
            self.tree.pack(expand=True, fill='y')
            self.walk_dict(rootNode)
        

    def walk_dict(self, d, depth=0, parent=""):

        for child in d:
            print(child.tag, child.attrib)

            node_name = "<" + child.tag + " " + self.create_xml_attribute_string(child.attrib) + ">"

            # With None a unique id is generated automatically.
            item = self.tree.insert(parent, 'end', None, text=node_name)

            if child.__len__() > 0:
                self.walk_dict(child, depth + 1, parent=item)
            else:
                # With None a unique id is generated automatically.
                if(child.text != None):
                    self.tree.insert(item, 'end', None, text=child.text)

    @staticmethod
    def create_xml_attribute_string(attributes):
        attributes_string = ""
        for key, value in attributes.items():
            attributes_string += key + "=\"" + value + "\" "

        return attributes_string

gui = Tk()
gui.title("Datos de estudiante")
gui.config(bg="blue")
gui.geometry("500x600")
App(gui)
gui.mainloop()