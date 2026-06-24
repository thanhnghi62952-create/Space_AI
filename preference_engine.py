def update_preference(current_preference, feedbacks): # update curent preference base on user's new feedback
    preferences = current_preference.copy() # create a copy của sở thích hiện tại dể làm việc trên đó
    for feedback in feedbacks:# watch the single feedback in the lot of feedbacks
        solution = feedback["solution"] # người dùng đang giá độ hiệu quả của phương pháp nào
        rating = feedback["rating"]# lấy điểm đánh giá the user like it, how level

        if solution not in preferences:# giải pháp có trong danh sách sở thích chưa
            preferences[solution] = 0 # nếu đây là sở thích mới hãy tạo nối với khởi điểm là 0

        if rating >= 4: # nếu người dùng đánh giá tốt 4s hoặc 5s 
            preferences[solution] += rating # tăng mức độ yêu thích của giải pháp
        
        elif rating <= 2: # if the user score low grade 1 point or 2 points
            preferences[solution] -= rating # reduce mức độ yêu thích của giải pháp
  
    return preferences # return current preference was update

def get_top_preference( preferences, top_k=5):
    sorted_preference = sorted(
        preferences.items(),
        key=lambda x: x[1],
        reverse=True
    )
    return
