import numpy as np
from langchain_core.vectorstores.utils import _cosine_similarity

x = np.array([[1.0, 2.0]]) 
y = np.array([])


result = _cosine_similarity(x, y)
print(result.shape)  # Got (0,), expected (1, 0)