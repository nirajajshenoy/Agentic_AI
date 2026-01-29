def sort_tasks_by_priority(tasks):
    """
    Lower number = higher priority
    """
    return sorted(tasks, key=lambda x: x["priority"])
