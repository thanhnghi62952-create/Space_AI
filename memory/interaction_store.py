class InteractionStore:
    def __init__(self):
        self.interactions = []

    def save( self, interaction):
        self.interactions.append(interaction)


    def get_user_history(
            self, user_id
    ):
        return[ i for i in self.interactions
               if i["user_id"] == user_id]