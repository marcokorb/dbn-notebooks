import os
import pyAgrum as gum
import pyAgrum.lib.notebook as gnb
import pyAgrum.lib.dynamicBN as gdyn


class DBN(object):

    def __init__(self):

        self.twodbn = gum.BayesNet()

        self.evidence_nodes = []
        self.transition_nodes = []
        self.subject_nodes = []
        self.nodes = []

    def load_evidence_nodes(self):

        evidences_nodes = [
            'evca0',
            'evco0',
            'evh0',
            'evhd0',
            'evcat',
            'evcot',
            'evht',
            'evhdt'
        ]

        evca0, evco0, evh0, evhd0, evcat, evcot, evht, evhdt = [
            twodbn.add(gum.LabelizedVariable(s, s, 2)) 
            for s in evidences_nodes
        ]

        self.evidence_nodes = evidences_nodes

    def load_subject_nodes(self):

        # Subjects nodes
        subjects_nodes = [
            'ca0',
            'co0',
            'h0',
            'cat',
            'cot',
            'ht'
        ]

        ca0, co0, h0, cat, cot, ht = [
            twodbn.add(gum.LabelizedVariable(s, s, 2)) 
            for s in subjects_nodes
        ]

        self.subject_nodes = subject_nodes

    def load_nodes(self):
        
        self.load_evidence_nodes()
        self.load_subject_nodes()
        self.nodes = self.evidence_nodes + self.subject_nodes
