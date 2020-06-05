import os
import pyAgrum as gum
import pyAgrum.lib.notebook as gnb
import pyAgrum.lib.dynamicBN as gdyn


def create_dbn1():

    twodbn = gum.BayesNet()

    sybjects_nodes = [
        twodbn.add(gum.LabelizedVariable(s, s, 2)) 
        for s in ['ca0', 'co0', 'h0', 'cat', 'cot', 'ht']
    ]

    evidences_nodes = [
        twodbn.add(gum.LabelizedVariable(s, s, 2)) 
        for s in ['evca0', 'evco0', 'evh0', 'evhd0', 'evcat', 'evcot', 'evht']
    ]

    twodbn.addArc('ca0', 'h0')
    twodbn.addArc('co0', 'h0')
    twodbn.addArc('cat', 'ht')
    twodbn.addArc('cot', 'ht')

    twodbn.addArc('ca0', 'evca0')
    twodbn.addArc('co0', 'evco0')
    twodbn.addArc('h0', 'evh0')
    twodbn.addArc('cat', 'evcat')
    twodbn.addArc('cot', 'evcot')
    twodbn.addArc('ht', 'evht')

    twodbn.addArc('ca0', 'cat')
    twodbn.addArc('co0', 'cot')
    twodbn.addArc('h0', 'ht')

    twodbn.cpt('ca0').fillWith([0.468176, 0.531824])
    twodbn.cpt('co0').fillWith([0.468176, 0.531824])
    twodbn.cpt('h0')[{'ca0': 0, 'co0': 0}] = [0.908971, 0.091029]
    twodbn.cpt('h0')[{'ca0': 0, 'co0': 1}] = [0.650269, 0.349731]
    twodbn.cpt('h0')[{'ca0': 1, 'co0': 0}] = [0.650269, 0.349731]
    twodbn.cpt('h0')[{'ca0': 1, 'co0': 1}] = [0.124852, 0.875148]

    twodbn.cpt('evca0')[{'ca0': 0}] = [0.8, 0.2]
    twodbn.cpt('evca0')[{'ca0': 1}] = [0.1, 0.9]

    twodbn.cpt('evco0')[{'co0': 0}] = [0.8, 0.2]
    twodbn.cpt('evco0')[{'co0': 1}] = [0.1, 0.9]

    twodbn.cpt('evh0')[{'h0': 0}] = [0.8, 0.2]
    twodbn.cpt('evh0')[{'h0': 1}] = [0.1, 0.9]

    twodbn.cpt('evcat')[{'cat': 0}] = [0.8, 0.2]
    twodbn.cpt('evcat')[{'cat': 1}] = [0.1, 0.9]

    twodbn.cpt('evcot')[{'cot': 0}] = [0.8, 0.2]
    twodbn.cpt('evcot')[{'cot': 1}] = [0.1, 0.9]

    twodbn.cpt('evht')[{'ht': 0}] = [0.8, 0.2]
    twodbn.cpt('evht')[{'ht': 1}] = [0.1, 0.9]

    # Transitions CTPs
    twodbn.cpt('cat')[{'ca0': 0}] = [0.919, 0.081]
    twodbn.cpt('cat')[{'ca0': 1}] = [0.047, 0.953]

    twodbn.cpt('cot')[{'co0': 0}] = [0.919, 0.081]
    twodbn.cpt('cot')[{'co0': 1}] = [0.047, 0.953]

    twodbn.cpt('ht')[{'cat': 0, 'cot': 0, 'h0': 0}] = [0.919, 0.081]
    twodbn.cpt('ht')[{'cat': 0, 'cot': 0, 'h0': 1}] = [0.85, 0.15]
    twodbn.cpt('ht')[{'cat': 0, 'cot': 1, 'h0': 0}] = [0.85, 0.15]
    twodbn.cpt('ht')[{'cat': 0, 'cot': 1, 'h0': 1}] = [0.35, 0.65]
    twodbn.cpt('ht')[{'cat': 1, 'cot': 0, 'h0': 0}] = [0.85, 0.15]
    twodbn.cpt('ht')[{'cat': 1, 'cot': 0, 'h0': 1}] = [0.35, 0.65]
    twodbn.cpt('ht')[{'cat': 1, 'cot': 1, 'h0': 0}] = [0.35, 0.65]
    twodbn.cpt('ht')[{'cat': 1, 'cot': 1, 'h0': 1}] = [0.047, 0.953]

    return twodbn
