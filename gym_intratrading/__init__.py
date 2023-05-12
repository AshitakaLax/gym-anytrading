from gym.envs.registration import register
from copy import deepcopy

from . import datasets


# register(
#     id='forex-v0',
#     entry_point='gym_intratrading.envs:ForexEnv',
#     kwargs={
#         'df': deepcopy(datasets.FOREX_EURUSD_1H_ASK),
#         'window_size': 24,
#         'frame_bound': (24, len(datasets.FOREX_EURUSD_1H_ASK))
#     }
# )

# register(
#     id='stocks-v0',
#     entry_point='gym_intratrading.envs:StocksEnv',
#     kwargs={
#         'df': deepcopy(datasets.STOCKS_GOOGL),
#         'window_size': 30,
#         'frame_bound': (30, len(datasets.STOCKS_GOOGL))
#     }
# )

register(
    id='intra-stocks-v0',
    entry_point='gym_intratrading.envs:IntraStocksEnv',
    kwargs={
        'df': deepcopy(datasets.TQQQ),
        'window_size': 30,
        'frame_bound': (30, len(datasets.TQQQ))
    }
)
