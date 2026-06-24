from database.models import User
from database.models import RecommendationHistory
from database.models import UserPreference
from database.models import Feedback
from database.models import Interaction
def create_user(
        db,
        user
):
    db_user = User(
        username=user.username,
        email=user.email,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
def get_user(
        db,
        user_id
):
    return db.query(
        User
    ).filer(
        User.user_id == user_id).first()

def create_history(db, history_data): # create a new history (db) is the door to connent database histort data là dữ liệu người dùng gửi lên
    history = RecommendationHistory(# create a new history table from user data (như cách fill a form)
        user_id=history_data.user_id,
        goal_id=history_data.goal_id,
        prompt=history_data.prompt,
        image_url=history_data.image_url,
        rating=history_data.rating
    )
    db.add(history) # move object in hàng chờ lưu
    db.commit()# save data = the data table will appear here
    db.refresh(history) #sync take the new data from database đưa trở lại (đồng bộ tham số)
    return history # trả lại kết quả vừa được lưu
    #lấy mẫu hồ sơ từ kho của mô hình(dòng import ở trên)
def create_preference(db, preference_data): # create a new habit (db) là trung gian nói chuyện với database(preference data) thông tin sở thích mà người dùng gửi lên 
    preference = UserPreference( # tạo môt form mới
        user_id=preference_data.user_id, # lấy user_id từ dữ liệu người dùng gửi lên take note in
        preference_type=preference_data.preference_type, # what is type of habit

        preference_value=preference_data.preference_value,# what is user like specificly       
        score=preference_data.score # how much level
    )
    db.add(preference)# đặt vào danh sách chờ lưu chưa lưu vào database
    db.commit()# thật sự lưu vào database
    db.refresh(preference)#update new data

    return preference #trả lại phiếu sở thích vừa được lưu
# lệnh import lấy mẩu phản hồi đã được định nghĩa sẳn để sử dụng từ kho database
def create_feedback( db, feedback_data): # crear a new feedback (db) to connect database (feedback_data) thông tin phản hồi mà người dùng gửi
    feedback = Feedback( #tạo một phiếu mới ở bộ nhớ chưa save vào database
        user_id=feedback_data.user_id, # record người dùng nào đã gửi phản hồi
        goal_id=feedback_data.goal_id, # phản hồi này liên quan tới mục tiêu nào
        rating=feedback_data.rating, # người dùng chấm điểm bao nhiêu
        comment=feedback_data.comment # what feedback the users writed 
    )
    db.add(feedback) # đặt phiếu phản hồi này vào danh sách chờ lưu
    db.commit()# save feedback in database
    db.refresh(feedback) # đồng bộ dữ liệu mới nhất từ database

    return feedback
def create_interaction( db, interaction_data):
    interaction = Interaction(
        user_id=interaction_data.user_id,
        goal_id=interaction_data.goal_id,
        solutions=interaction_data.solutions,
        prompt=interaction_data.prompt,
        image_url=interaction_data.image_url,
        rating=interaction_data.rating,
        comment=interaction_data.comment
    )
    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return interaction
def get_user_by_username(db, username):
    return db.query(User).filter(User.username == username).first()

def get_user_interactions(db, user_id):
    return db.query(Interaction).filter(Interaction.user_id == user_id).all()