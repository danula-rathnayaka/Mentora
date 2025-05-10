class LearningPath:
    def __init__(self, path_id: str, student_id: str, course_id: str,
                 start_date: str, end_date: str, current_module: str,
                 completed_modules: list, recommended_resources: list,
                 learning_goals: dict, adaptation_history: list):
        self.__path_id = path_id
        self.__student_id = student_id
        self.__course_id = course_id
        self.__start_date = start_date
        self.__end_date = end_date
        self.__current_module = current_module
        self.__completed_modules = completed_modules  # list of module IDs
        self.__recommended_resources = recommended_resources  # list of resource URLs or IDs
        self.__learning_goals = learning_goals  # e.g., {'master algebra': True, 'improve speed': False}
        self.__adaptation_history = adaptation_history  # records of changes made by adaptive agent

    # Getters and setters

    def get_path_id(self):
        return self.__path_id

    def set_path_id(self, path_id):
        self.__path_id = path_id

    def get_student_id(self):
        return self.__student_id

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_course_id(self):
        return self.__course_id

    def set_course_id(self, course_id):
        self.__course_id = course_id

    def get_start_date(self):
        return self.__start_date

    def set_start_date(self, start_date):
        self.__start_date = start_date

    def get_end_date(self):
        return self.__end_date

    def set_end_date(self, end_date):
        self.__end_date = end_date

    def get_current_module(self):
        return self.__current_module

    def set_current_module(self, current_module):
        self.__current_module = current_module

    def get_completed_modules(self):
        return self.__completed_modules

    def set_completed_modules(self, completed_modules):
        self.__completed_modules = completed_modules

    def get_recommended_resources(self):
        return self.__recommended_resources

    def set_recommended_resources(self, recommended_resources):
        self.__recommended_resources = recommended_resources

    def get_learning_goals(self):
        return self.__learning_goals

    def set_learning_goals(self, learning_goals):
        self.__learning_goals = learning_goals

    def get_adaptation_history(self):
        return self.__adaptation_history

    def set_adaptation_history(self, adaptation_history):
        self.__adaptation_history = adaptation_history
