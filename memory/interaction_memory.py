from database.crud import create_interaction

interaction_history = [] # tạo một cuốn sách ghi chép trống

def save_interaction( # I wanna record lần tương tác của người dùng
        user_id, # ai interaction
        goal_id, # mục tiêu nào 
        solutions, # giải pháp nào
        prompt, # prompt là gì
        image_url, # ảnh nào được sử dụng
        rating, # người dùng đánh giá bao nhiêu 
        comment # nhận xét là gì
):
    interaction = { # tạo một phiếu ghi lại toàn bộ thông tin của lần tương tác này
        "user_id": user_id,
        "goal_id": goal_id,
        "solutions": solutions,
        "prompt": prompt,
        "image_url": image_url,
        "rating": rating,
        "comment": comment
    }
    interaction_history.append(interaction) # ghi phiếu này vào cuốn sổ lịch sử

def get_history(): # ai đó muốn xem toàn bộ lịch sử hảy show ra
    return interaction_history # đưa toàn bộ bản ghi đã lưu cho người yêu cầu

def save_interaction( db, interaction_data):
    return create_interaction(db, interaction_data)