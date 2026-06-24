def build_experience(interactions): # build experience base on user's history interaction 
    experience = {} # tạo một sổ kinh nghiệm trống 

    for interaction in interactions: # duyệt từng interaction từng cái một 
        rating = interaction.rating # lấy điểm đánh giá 

        solutions = interaction.solutions.split(",") # tách giải pháp thành từng phần riêng 

        for solutions in solutions: # duyệt từng giải pháp một
            solution = solution.strip() # xóa khoản trắng dư thừa
            if solution not in experience: # kiểm tra giải pháp có trong hồ sơ sở thích, lịch sử chưa
                experience[solution] = 0 # nếu hoàn toàn mới hãy tạo nó với khởi điểm ban đầu là 0
            if rating >= 4: # nếu đánh giá cao người dùng thích giải pháp này
                experience[solution] += rating #cộng  thêm điểm tăng mức độ yêu thích
            elif rating <= 2: # nếu người dùng không thích
                experience[solution] -= (3 - rating) # giảm điểm yêu thích

    return experience