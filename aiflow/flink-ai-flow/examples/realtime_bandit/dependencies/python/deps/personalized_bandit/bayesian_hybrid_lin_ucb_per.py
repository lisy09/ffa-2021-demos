from typing import Dict, List
import numpy as np
from .prioritized_replay_buffer import PrioritizedExperienceReplay

class HybridArm:
    """
    Representation of each arm. Containing a set of arm-specific features of size d, common(user) features k.
    """
    def __init__(
        self,
        id,
        feature_dim: int,
        common_feature_dim: int,
        alpha: float,
    ) -> None:
        self.id = id
        self.d = feature_dim
        self.k = common_feature_dim
        self.alpha = alpha
        #Li lines 8-10
        self.A = np.identity(self.d)
        self.Ainv = np.linalg.inv(self.A)
        self.B = np.zeros(self.d, self.k)
        self.b = np.zeros(self.d, 1)

    @property
    def getP(
        self,
        A0inv,
        b0,
        betaHat,
        z,
        x,
    ):
        self.thetaHat = np.dot(self.Ainv, self.b - np.dot(self.B, betaHat))

        zTranspose = np.transpose(z)
        BTranspose = np.transpose(self.B)
        xTranspose = np.transpose(x)

        self.s1 = np.dot(zTranspose, np.dot(A0inv, z))
        v0 = np.dot(A0inv, np.dot(BTranspose, np.dot(self.Ainv, x)))
        self.s2 = np.dot(zTranspose, v0)

        self.s3 = np.dot(xTranspose, np.dot(self.Ainv, x))
        self.s4 = np.dot(xTranspose, np.dot(self.Ainv, np.dot(self.B, v0)))

        # Li line 13
        self.s = self.s1 - 2*self.s2 + self.s3 + self.s4

        self.p = np.dot(zTranspose, betaHat) + np.dot(xTranspose, self.thetaHat) + self.alpha * np.sqrt(self.s)
        return self.p
    
    def getEP(
        self,
        betaHat,
        z,
        x,
    ):
        thetaHat = np.dot(self.Ainv, self.b - np.dot(self.B, betaHat))
        return np.dot(np.transpose(z), betaHat) + np.dot(np.transpose(x), thetaHat)

    def update(
        self,
        z,
        x,
        reward,
    ):
        self. A += np.dot(x, np.transpose(x))
        self.Ainv = np.linalg.inv(self.A)
        self.B += np.dot(x, np.transpose(z))
        self.b += reward * x

class UpdateRecord:
    def __init__(self,
        action: int,
        user_state,
        arm_state,
        reward,
    ) -> None:
        self.action = action
        self.user_state = user_state
        self.arm_state = arm_state
        self.reward = reward

class BayesianHybridLinUCBPER:
    def __init__(self,
        n_arms: int,
        alpha: int = 2,
        arm_feature_dim: int=0,
        user_feature_dim: int=0,
        return_list: bool=True,
        memory_size: int=int(1e5),
        priority_alpha: float=0.6,
        priority_beta: float=0.4,
        priority_epsilon: float=0.001,
        beta_increment_per_sampling: float=0.4e-6,
        batch_size: int=128,
        epochs: int=10,
    ) -> None:
        self.n_arms = n_arms
        self.alpha = alpha
        self.arm_feature_dim = arm_feature_dim
        self.user_feature_dim = user_feature_dim
        self.return_list = return_list

        self.memory_size = memory_size
        self.priority_alpha = priority_alpha
        self.priority_beta = priority_beta
        self.priority_epsilon = priority_epsilon
        self.beta_increment_per_sampling = beta_increment_per_sampling
        self.batch_size = batch_size
        self.epochs = epochs

        self.reset()

    def predict(self, user_feature, arm_feature_list):
        predict_ucb = [self.arms[i_arm].getP(
            A0inv=self.A0inv,
            b0=self.b0,
            betaHat=self.betaHat,
            z=user_feature,
            x=arm_feature_list[i_arm],
        )
            for i_arm in range(self.n_arms)]
        if self.return_list:
            return predict_ucb
        else:
            return int(np.argmax(predict_ucb))

    def _update(
        self,
        record: UpdateRecord,
        weight = 1.0,
    ):
        current_arm = self.arms[record.action]
        # lines 17-18
        current_arm_B_transpose = np.transpose(current_arm.B)
        self.A0 += weight * np.dot(current_arm_B_transpose,
                          np.dot(current_arm.Ainv, current_arm.B))
        self.b0 += weight * np.dot(current_arm_B_transpose,
                          np.dot(current_arm.Ainv, current_arm.b))
        # update the arm-specific matrices: lines 19-21
        current_arm.update(
            z=record.user_state,
            x=record.arm_state,
            reward=record.reward,
        )
        # update the general matrices again: lines 22-23
        self.A0 += weight * np.dot(record.user_state,
                          np.transpose(record.user_state))
        current_arm_B_transpose = np.transpose(current_arm.B)
        self.A0 -= weight * np.dot(current_arm_B_transpose,
                          np.dot(current_arm.Ainv, current_arm.B))
        self.b0 += weight * record.reward * record.user_state
        self.b0 -= weight * np.dot(current_arm_B_transpose,
                          np.dot(current_arm.Ainv, current_arm.b))


    def batch_update(
        self,
        record_list: List[UpdateRecord],
    ):
        for record in record_list:
            self.per_memory.push(
                # 'user_feature', 'arm_feature', 'action', 'reward'
                record.user_state,
                record.arm_state,
                record.action,
                record.reward,
            )
            self._update(record)

        self.A0inv = np.linalg.inv(self.A0)
        self.betaHat = np.dot(self.A0inv, self.b0)

        # update model from sampled experiences
        if self.per_memory.size() != self.per_memory.memory_size:
            return
        for _ in range(self.epochs):
            idx_list, data_batch, is_weights = self.per_memory.sample(batch_size=self.batch_size)
            errors = []
            for data, is_weight in zip(data_batch, is_weights):
                reward = data.reward
                arm_state = data.arm_feature
                user_state = data.user_feature
                action = data.action
                record = UpdateRecord(
                    action=action,
                    user_state=user_state,
                    arm_state=arm_state,
                    reward=reward,
                )
                current_arm = self.arms[action]
                errors.append(reward - current_arm.getEP(
                    betaHat=self.betaHat,
                    z=user_state,
                    x=arm_state,
                ))

                self._update(record, weight=is_weight)
            self.A0inv = np.linalg.inv(self.A0)
            self.betaHat = np.dot(self.A0inv, self.b0)
            self.per_memory.update(idx_list, errors)

    def reset(self):
        self.arms = Dict[int, HybridArm]()
        for i_arm in range(self.n_arms):
            self.arms[i_arm] = HybridArm(
                id=i_arm,
                feature_dim=self.arm_feature_dim,
                common_feature_dim=self.user_feature_dim,
                alpha=self.alpha,
            )

        self.A0 = np.identity(self.user_feature_dim)
        self.A0inv = np.linalg.inv(self.A0)
        self.b0 = np.zeros(self.user_feature_dim, 1)
        self.betaHat = np.dot(self.A0inv, self.b0)

        self.per_memory = PrioritizedExperienceReplay(
            memory_size=self.memory_size,
            alpha=self.priority_alpha,
            beta=self.priority_beta,
            epsilon=self.priority_epsilon,
            beta_increment_per_sampling=self.beta_increment_per_sampling,
        )
