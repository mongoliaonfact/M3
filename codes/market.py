from production_function import FirmProduction
import numpy as np
from logging import *
import pandas as pd
from firm import Firm


def create_zipf_distr(firm_count=2000):
    '''
    function creates labor for a firm using zipf distribution. It is
    named for the American linguist George Kingsley Zipf, who noted
    that the frequency of any word in a sample of a language is
    inversely proportional to its rank in the frequency table.

    Parameters:
    a --> float or array_like of floats. Distribution parameter.
    Must be greater than 1.

    size --> int or tuple of ints, optional
    Output shape. If the given shape is, e.g., (m, n, k),
    then m * n * k samples are drawn. If size is None (default),
    a single value is returned if a is a scalar. Otherwise, np.array(a).size
    samples are drawn.

    Returns:
    out --> ndarray or scalar. Drawn samples from the
    parameterized Zipf distribution
    '''

    distr_par = 1.7
    output_shape = firm_count
    zipf_distr = np.random.zipf(distr_par, output_shape)
    return zipf_distr


'''
def make_firm_labor_graph(list_of_firms):
    firm_labor = {'firm_labor': [f.get_labor() for f in list_of_firms]}
    frame = pd.DataFrame(firm_labor)
    plotted = (
            ggplot(frame, aes(x='firm_labor'))
            + geom_histogram(binwidth=5))

    return plotted
'''


def get_market_labor(list_of_firms):
    return [f.get_labor() for f in list_of_firms]


def export_entrance_cost(cost=3):
    if cost >= 3:
        return cost
    else:
        return '0'


# in average, firms have 19-30 employee
def get_market_mean_labor(list_of_firms):
    return np.mean(get_market_labor(list_of_firms))


# get total production
def get_market_production(list_of_firms):
    return [f.get_y() for f in list_of_firms]


def get_market_expansion(list_of_firms):
    return [f.get_expansion for f in list_of_firms]


def demo_run_one(number_of_firms=100):
    market_firms = list()
    np.random.seed(1234)

    list_of_firms = list()
    labor_list = create_zipf_distr(number_of_firms)

    for ind, i in enumerate(labor_list):
        each_firm = Firm(ind)
        each_firm.set_labor(i)
        # production function takes unit of labor
        product = each_firm.cobb_douglas(total_labor=i)
        each_firm.set_y(product)
        list_of_firms.append(each_firm)

    # print('id', 'labor', 'y', 'share', 'expand')
    for each_firm in list_of_firms:
        market_total_production = sum(get_market_production(list_of_firms))
        share = round(each_firm.get_y() / market_total_production, 6)
        each_firm.set_share(share)
        # print(market_total_production)

        # copying firm export share
        each_firm.to_expand(share)

        # export sunk cost is cost of exporting with respect to labor
        '''
        to enter, firms must first make an initial investment, 
        modeled as a fixed cost f_e > 0 (measured in units of labor) 
        which thereafter is 'sunk' (Sect. 3).
        '''
        export_sunk_cost = 1

        if each_firm.get_labor() <= export_sunk_cost:
            each_firm.to_expand(0)  # only productive firm can enter the trade

    new_market_production = sum([f.get_expansion for f in list_of_firms])

    for each_firm in list_of_firms:
        each_firm.to_expand(round(each_firm.get_expansion / new_market_production, 6))
        market_firms.append(each_firm)
    return market_firms

print('id', 'labor', 'y', 'share', 'expand')
for i in demo_run_one(10):
    print(i)
