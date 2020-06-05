import os
import pyAgrum as gum
import pyAgrum.lib.notebook as gnb
import pyAgrum.lib.dynamicBN as gdyn


from dbn_v1 import create_dbn1
from dbn_v2 import create_dbn2


if __name__ == '__main__':

    # dbn1 = create_dbn1()
    # dbn2 = create_dbn2()

    twodbn = gum.BayesNet()

    subjects_nodes = [
        twodbn.add(gum.LabelizedVariable(s, s, 2)) 
        for s in ['ca0', 'co0', 'h0', 'cat', 'cot', 'ht']
    ]

    from IPython import embed; embed()
