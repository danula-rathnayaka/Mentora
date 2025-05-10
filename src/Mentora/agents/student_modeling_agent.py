from langchain.chains.llm import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, MessagesPlaceholder, \
    HumanMessagePromptTemplate
from langchain_ollama import OllamaLLM


class StudentModelingAgent:
    def __init__(self, llm_model_name="llama3.2:latest", memory_key="student_profile"):
        self.llm = OllamaLLM(model=llm_model_name, temperature=0)
        self.memory_key = memory_key
        self.memories = {}
        self.prompt_template = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(
                    "You are an intelligent assistant that maintains detailed student learning profiles. "
                    "Use the conversation history to update and summarize the student's strengths, weaknesses, skills, and preferences according to the structure. "
                    "Respond only with the updated profile content. "
                    "Do not include any offers for further assistance, disclaimers, or generic closing statements."
                ),
                MessagesPlaceholder(variable_name=memory_key),
                HumanMessagePromptTemplate.from_template("{input_text}")
            ]
        )

    def _get_memory_for_student(self, student_id: str) -> ConversationBufferMemory:
        if student_id not in self.memories:
            self.memories[student_id] = ConversationBufferMemory(memory_key=self.memory_key, return_messages=True)
        return self.memories[student_id]

    def get_profile(self, student_id: str) -> str:
        memory = self._get_memory_for_student(student_id)
        memory_vars = memory.load_memory_variables({})
        return memory_vars.get(self.memory_key, "")

    def update_profile(self, student_id: str, new_interaction: str) -> str:
        memory = self._get_memory_for_student(student_id)

        chain = LLMChain(llm=self.llm, prompt=self.prompt_template, memory=memory, verbose=False)

        input_text = f"New interaction data:\n{new_interaction}\n\nPlease update the student profile accordingly."

        updated_profile = chain.run({"input_text": input_text})

        memory.save_context({"input": new_interaction}, {"output": updated_profile})

        return updated_profile

    def summarize_performance(self, student_id: str) -> str:
        """
        Generate a concise summary string of the student's latest performance,
        based on the stored profile text.

        Returns a human-readable summary suitable for educators or reports.
        """
        profile_text = self.get_profile(student_id)
        if not profile_text:
            return "No profile data available for this student."

        prompt = f"""
        You are an expert educational assistant. Based on the following student profile information,
        provide a concise summary (about 150 words) of the student's latest academic performance, highlighting:
        - Key strengths
        - Areas needing improvement
        - Recent progress or challenges
        - Notable skills or learning preferences

        Respond clearly and professionally. Avoid any offers for further help, disclaimers, or generic closing remarks.

        Student profile:
        \"\"\"
        {profile_text}
        \"\"\"
        """

        return self.llm.invoke(prompt)
