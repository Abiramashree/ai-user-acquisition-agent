import random

class AdCopyAgent:
    def __init__(self, product, audience, cta, platform):
        self.product = product
        self.audience = audience
        self.cta = cta
        self.platform = platform
        self.memory = []  # Stores feedback

    def plan(self):
        return f"Goal: Persuasive ad copy for {self.platform}. Audience: {self.audience}. CTA: {self.cta}"

    def tool_call_trending(self):
        # Mock trending phrases
        trends = {
            "Instagram": ["Limited Time", "Your Move", "You Deserve This"],
            "Google Search": ["Save Now", "Top Rated", "Must Try"],
        }
        return trends.get(self.platform, ["Act Now", "Don't Miss Out"])

    def generate_prompt(self):
        trends = ", ".join(self.tool_call_trending())
        return f"""
        Write 3 ad copy variants for a product called "{self.product}".
        Target Audience: {self.audience}
        Call to Action: {self.cta}
        Platform: {self.platform}
        Trending phrases to optionally include: {trends}
        Return each with a label (Copy A, Copy B, Copy C).
        """

    def execute(self, llm):
        prompt = self.generate_prompt()
        return llm(prompt)  # External LLM call (OpenAI, Claude, etc.)

    def reflect_on_outputs(self, outputs):
        # Simple simulated reflection logic
        scores = {
            "Copy A": random.randint(1, 10),
            "Copy B": random.randint(1, 10),
            "Copy C": random.randint(1, 10),
        }
        best = max(scores, key=scores.get)
        return f"Reflection: {best} has the highest emotional clarity score."

    def update_memory(self, copy_label, feedback_score):
        self.memory.append({"copy": copy_label, "feedback": feedback_score})
        return f"Feedback recorded: {copy_label} rated {feedback_score}/10."

