class LearningWorkflow: # tạo một người quản lý quá trình học hỏi chuẩn SOP
    def __init__(self, feedback_agent, learning_agent): # khi tạo người quản lý này hãy cho nó 2 nhân viên
        self.feedback_agent = feedback_agent # ghi nhớ ai là nhân viên phụ trách feedback
        self.learning_agent = learning_agent # ghi nhớ ai là nhân viên phụ trách học hỏi

    def run(self, state):# khi bắt đầu quá trình học hãy đưa toàn bộ trạng thái hiện tại của hệ thống cho tôi
        state = self.feedback_agent.run(state) # đầu tiên đưa cho nhân viên feedback xử lý
        state = self.learning_agent.run(state) # đưa dữ liệu state vừa được cập nhật cho nhân viên học hỏi

        return state # trả lại trạng thái mới 