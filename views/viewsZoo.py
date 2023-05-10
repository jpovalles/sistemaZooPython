import model.Animal as animalModel
import model.Habitat as habitatModel
import model.Zoo as zooModel
import controller.zooController as zooControl
import streamlit as st

class sistema:
    def __init__(self):
        self.zoologico = zooModel.Zoo(0)
        self.controlador = zooControl.zooController(self.zoologico, self)