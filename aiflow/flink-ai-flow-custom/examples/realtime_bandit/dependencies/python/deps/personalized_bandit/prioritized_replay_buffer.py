from collections import namedtuple
from typing import List, Tuple

import numpy as np
from numpy.lib import index_tricks

from .sum_tree import SumTree

Transition = namedtuple('Transition', ('user_feature', 'arm_feature', 'action', 'reward'))


class PrioritizedExperienceReplay:
    def __init__(
        self,
        memory_size:int=int(1e6),
        alpha=0.6,
        beta=0.4,
        epsilon=1e-4,
        beta_increment_per_sampling=4e-7,
    ) -> None:
        """
        store as (s,a,r,s_) in SumTree
        """
        self.memory_size = memory_size
        self.tree = SumTree(self.memory_size)
        self.priority_max = 0.1
        self.alpha = alpha
        self.beta = beta
        self.epsilon = epsilon
        self.beta_increment_per_sampling = beta_increment_per_sampling

    def push(self, *args):
        """
        Save a Transition
        """
        data = Transition(*args)
        p=(np.abs(self.priority_max)+self.epsilon) ** self.alpha
        self.tree.add(p, data)

    def sample(self, batch_size:int) -> Tuple[List, List, List[float]]:
        assert batch_size > 0
        self.beta = np.min(1, self.beta + self.beta_increment_per_sampling)
        idx_list = []
        data_batch = []
        segment = self.tree.total() / batch_size
        priorities = []

        for i in range(batch_size):
            a = segment * i
            b = a + segment
            s = np.random.uniform(a,b)
            idx, p, data = self.tree.get(s)

            data_batch.append(data)
            priorities.append(p)
            idx_list.append(idx)

        sampling_probs = priorities / self.tree.total()
        is_weight = np.power(self.tree.n_entries * sampling_probs, -self.beta)
        is_weight /= is_weight.max()
        return idx_list, data_batch, is_weight

    def update(self, idx_list, errors):
        self.priority_max = max(self.priority_max, max(np.abs(errors)))
        for i, idx in enumerate(idx_list):
            p = (np.abs(errors[i]) + self.epsilon) ** self.alpha
            self.tree.update(idx, p)
    
    def size(self):
        return self.tree.n_entries
