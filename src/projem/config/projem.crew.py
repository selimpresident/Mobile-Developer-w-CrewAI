import os
from crewai import Agent, Task, Crew, Process
from tools.custom_tool import CustomTool
import yaml

# Çevre Değişkenleri
os.environ["SERPER_API_KEY"] = "Your_Serper_API_Key"
os.environ["OPENAI_API_KEY"] = "Your_OpenAI_API_Key"

def load_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

# YAML dosyalarından agent ve task'ları yükleme
agents_config = load_yaml('src/projem/config/agents.yaml')
tasks_config = load_yaml('src/projem/config/tasks.yaml')

agents = []
tasks = []

for agent_config in agents_config['agents']:
    tools = [CustomTool(name=tool) for tool in agent_config.get('tools', [])]
    agent = Agent(
        role=agent_config['role'],
        goal=agent_config['goal'],
        backstory=agent_config['backstory'],
        tools=tools,
        verbose=True,
        memory=True
    )
    agents.append(agent)

for task_config in tasks_config['tasks']:
    agent_role = task_config['agent']
    assigned_agents = [agent for agent in agents if agent.role == agent_role]
    task = Task(
        description=task_config['description'],
        expected_output=task_config['expected_output'],
        agent=assigned_agents[0] if assigned_agents else None
    )
    tasks.append(task)

# Crew oluşturma
crew = Crew(
    agents=agents,
    tasks=tasks,
    process=Process.sequential
)

# Crew'u başlatma
result = crew.kickoff(inputs={'topic': 'Yeni Mobil Uygulama'})
print(result)
