import pandas as pd
import numpy as np
from scipy.stats import kstest


chat_id = 425946970 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    p_value = kstest(x, y)[1]
    return p_value < 0.05 # Ваш ответ, True или False
