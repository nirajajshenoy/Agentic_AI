from study_agent import study_topic
from calendar_agent import schedule_meeting
from priority_manager import sort_tasks_by_priority

# --------------------------------
# AGENT GOAL
# --------------------------------
GOAL = "Execute study and meeting tasks based on user-defined priority"

# --------------------------------
# PERCEPTION MODULE (User Input)
# --------------------------------
def perceive_tasks_from_user():
    tasks = []

    print("\n🧠 Task 1: Study Topic")
    topic = input("Enter topic to study: ")
    study_priority = int(input("Enter priority for study task (lower = higher priority): "))

    tasks.append({
        "type": "study",
        "topic": topic,
        "priority": study_priority
    })

    print("\n📅 Task 2: Schedule Meeting")
    title = input("Enter meeting title: ")
    start = input("Enter start time (YYYY-MM-DDTHH:MM:SS): ")
    end = input("Enter end time (YYYY-MM-DDTHH:MM:SS): ")
    attendees_input = input("Enter attendee emails (comma separated): ")
    meeting_priority = int(input("Enter priority for meeting task (lower = higher priority): "))

    attendees = [email.strip() for email in attendees_input.split(",")]

    tasks.append({
        "type": "schedule_meeting",
        "title": title,
        "start": start,
        "end": end,
        "attendees": attendees,
        "priority": meeting_priority
    })

    return tasks


# --------------------------------
# AGENT LOOP
# --------------------------------
def agent():
    print("🎯 Agent Goal:", GOAL)

    tasks = perceive_tasks_from_user()
    ordered_tasks = sort_tasks_by_priority(tasks)

    print("\n⚙️ Executing tasks based on priority...\n")

    for task in ordered_tasks:
        if task["type"] == "study":
            print(f"📘 Studying topic: {task['topic']}")
            study_topic(task["topic"])

        elif task["type"] == "schedule_meeting":
            schedule_meeting(task)


# --------------------------------
# RUN AGENT
# --------------------------------
if __name__ == "__main__":
    agent()
