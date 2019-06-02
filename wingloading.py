import math
from openmdao.api import ExplicitComponent

e =  0.81
C_D0 = 0.01225
n = 1.108


class wingloading(ExplicitComponent):
      
    def setup(self):\
        self.add_input('q')
        self.add_input('AR')
        self.add_input('v')
        self.add_output('W_S')        
        self.declare_partials('*','*',method = 'cs')
        

    def compute(self, inputs, outputs):
        q = inputs['q']
        v = inputs['v']
        AR = inputs['AR']
        G = 840/60/(v*3.28084)
        T_W_C = G + 2*(C_D0/(math.pi*e*AR))**0.5
        T_W_T = 2*n*(C_D0/(math.pi*e*AR))**0.5
        W_S_tu = (T_W_T  + (T_W_T**2 - 4*n**2*C_D0/(math.pi*e*AR))**0.5)/(2*n**2/(math.pi*e*AR*q))        
        W_S_cl = ((T_W_C - G) + ((T_W_C-G)**2-4*C_D0/(math.pi*e*AR))**0.5)/(2/(math.pi*e*AR*q))
        outputs['W_S_tu'] = min(W_S_cl,W_S_tu)

                    
    #def compute_partials(self, inputs, partials):

