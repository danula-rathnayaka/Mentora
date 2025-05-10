class Assignment:
    def __init__(self, assignment_id: str, title: str, description: str,
                 course_id: str, due_date: str, max_score: float,
                 assigned_date: str, submission_type: str,
                 resources: list, status: str, student_scores: dict,
                 feedback: dict):
        self.__assignment_id = assignment_id
        self.__title = title
        self.__description = description
        self.__course_id = course_id
        self.__due_date = due_date
        self.__max_score = max_score
        self.__assigned_date = assigned_date
        self.__submission_type = submission_type  # e.g., "online quiz", "essay", "project"
        self.__resources = resources  # URLs or file references to supporting materials
        self.__status = status  # e.g., "assigned", "submitted", "graded"
        self.__student_scores = student_scores  # {student_id: score}
        self.__feedback = feedback  # {student_id: feedback_text}

    # Getters and setters

    def get_assignment_id(self):
        return self.__assignment_id

    def set_assignment_id(self, assignment_id):
        self.__assignment_id = assignment_id

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_course_id(self):
        return self.__course_id

    def set_course_id(self, course_id):
        self.__course_id = course_id

    def get_due_date(self):
        return self.__due_date

    def set_due_date(self, due_date):
        self.__due_date = due_date

    def get_max_score(self):
        return self.__max_score

    def set_max_score(self, max_score):
        self.__max_score = max_score

    def get_assigned_date(self):
        return self.__assigned_date

    def set_assigned_date(self, assigned_date):
        self.__assigned_date = assigned_date

    def get_submission_type(self):
        return self.__submission_type

    def set_submission_type(self, submission_type):
        self.__submission_type = submission_type

    def get_resources(self):
        return self.__resources

    def set_resources(self, resources):
        self.__resources = resources

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_student_scores(self):
        return self.__student_scores

    def set_student_scores(self, student_scores):
        self.__student_scores = student_scores

    def get_feedback(self):
        return self.__feedback

    def set_feedback(self, feedback):
        self.__feedback = feedback
