def learn_from_experience(experience):
    preferences = {}

    for solution, score in experience.items():

        if score > 0:
            preferences[solution] = score
    return preferences
