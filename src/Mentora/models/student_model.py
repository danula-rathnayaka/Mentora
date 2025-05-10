class Student:
    def __init__(self, student_id: str, first_name: str, last_name: str, email: str,
                 date_of_birth: str, profile_picture_url: str, enrollment_date: str,
                 learning_preferences: dict, current_level: str, skills: dict,
                 engagement_metrics: dict, progress: dict, privacy_consent: bool):
        self.__student_id = student_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__date_of_birth = date_of_birth
        self.__profile_picture_url = profile_picture_url
        self.__enrollment_date = enrollment_date
        self.__learning_preferences = learning_preferences  # e.g., {'content_type': 'video', 'pace': 'fast'}
        self.__current_level = current_level  # e.g., "Grade 8", "Intermediate Algebra"
        self.__skills = skills  # e.g., {'algebra': 'proficient', 'geometry': 'beginner'}
        self.__engagement_metrics = engagement_metrics  # e.g., {'avg_session_time': 30, 'login_frequency': 5}
        self.__progress = progress  # e.g., {'course_id': 'completed', 'assignment_id': 'pending'}
        self.__privacy_consent = privacy_consent

    # Getters and setters for each attribute

    def get_student_id(self):
        return self.__student_id

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def get_profile_picture_url(self):
        return self.__profile_picture_url

    def set_profile_picture_url(self, profile_picture_url):
        self.__profile_picture_url = profile_picture_url

    def get_enrollment_date(self):
        return self.__enrollment_date

    def set_enrollment_date(self, enrollment_date):
        self.__enrollment_date = enrollment_date

    def get_learning_preferences(self):
        return self.__learning_preferences

    def set_learning_preferences(self, learning_preferences):
        self.__learning_preferences = learning_preferences

    def get_current_level(self):
        return self.__current_level

    def set_current_level(self, current_level):
        self.__current_level = current_level

    def get_skills(self):
        return self.__skills

    def set_skills(self, skills):
        self.__skills = skills

    def get_engagement_metrics(self):
        return self.__engagement_metrics

    def set_engagement_metrics(self, engagement_metrics):
        self.__engagement_metrics = engagement_metrics

    def get_progress(self):
        return self.__progress

    def set_progress(self, progress):
        self.__progress = progress

    def get_privacy_consent(self):
        return self.__privacy_consent

    def set_privacy_consent(self, privacy_consent):
        self.__privacy_consent = privacy_consent

    def __str__(self):
        return (
            f"Student ID: {self.__student_id}\n"
            f"Name: {self.__first_name} {self.__last_name}\n"
            f"Email: {self.__email}\n"
            f"Date of Birth: {self.__date_of_birth}\n"
            f"Profile Picture URL: {self.__profile_picture_url}\n"
            f"Enrollment Date: {self.__enrollment_date}\n"
            f"Learning Preferences: {self.__learning_preferences}\n"
            f"Current Level: {self.__current_level}\n"
            f"Skills: {self.__skills}\n"
            f"Engagement Metrics: {self.__engagement_metrics}\n"
            f"Progress: {self.__progress}\n"
            f"Privacy Consent: {self.__privacy_consent}"
        )
