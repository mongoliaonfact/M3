class FirmProduction:
    '''
        based on the 1976 paper by Paul Douglas, "The Cobb-Douglas
        Production Function Once Again: Its history, Its Testing,
        and Some New Empirical Values.
        source: "https://www.journals.uchicago.edu/doi/pdf/10.1086/260489?casa_token=GVFgLzmop0kAAAAA:IyTR_U_Fd99jYK8RQqvPhMXeSVfvf8eyek2QHkxJmClQnqYkQ_AO5OTqpTXOmHlMeWmSo4nA71c"

        General production is P = bL^k *C^(1-k)
        This, following Euler, was a simple homogenous function of the first degree
        Thus, the value of k by the method of least squares to be .75.
        other studies suggest that the value of k to be:
        National Bureau of Economic Research = 74.1
        Cobb 1930 = .743
        Marjorie Handshaker = .71

        # some changes to the function:

        David Durand (1937) made change and j = 1 - k where j is independently determined

        k + j = 1 --> 'constant return to scale'
        k + j > 1 --> and a 1 percent increase in both L and C would be accompanied by
                        increase of mroe than 1 percent in product, then the system is
                        'increasing return to scale'
        k + j < 1 --> 'diminishing returns to scale'
    '''

    def __init__(self):
        # self.x = x
        pass

    def cobb_douglas(self, total_labor):
        '''
        parameters:
        ___________

        total_labor -  int
        total_kapital - int, constant based on the Melitz model
        tfp - int, total factor productivity, constant

        k - output elasticities of capital and labor respectively

        '''
        tfp = 1
        k = .5
        j = 1 - k
        total_kapital = 3

        total_output = tfp * total_labor ** k * total_kapital ** j

        return round(total_output, 3)

# check
# fp = FirmProduction()
# print(fp.cobb_douglas(2))