class RewardModel:
    def calculate_reward(
            self,
            feedback
    ):
        if feedback > 0:
            return 1
        return -1