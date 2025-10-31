import streamlit as st

st.set_page_config(page_title="AI Task Tracker", layout="wide")
st.title("Task Tracker — Demo")

statuses = ["To Do", "In Progress", "Done"]

# Initialize tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = [
        {"name": "Design login UI", "status": "To Do"},
        {"name": "Build database", "status": "In Progress"},
        {"name": "Setup GitHub repo", "status": "Done"},
    ]

# Add new task
new_task = st.text_input("Add a new task")
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append({"name": new_task, "status": "To Do"})
         # rerun immediately to refresh columns
        st.rerun()

# Display tasks in columns
col1, col2, col3 = st.columns(3)
columns = [col1, col2, col3]

for idx, status in enumerate(statuses):
    col = columns[idx]
    col.subheader(status)
    
    # Filter tasks for this status
    tasks_in_status = [t for t in st.session_state.tasks if t["status"] == status]
    
    for i, task in enumerate(tasks_in_status):
        col.write(f"- {task['name']}")
        
        # Dropdown to change status
        new_status = col.selectbox(
            "Change status",
            options=statuses,
            index=statuses.index(task["status"]),
            key=f"{task['name']}{status}{i}"  # stable unique key
        )
        
        if new_status != task["status"]:
            # Update original task
            for t in st.session_state.tasks:
                if t is task:
                    t["status"] = new_status
                    break
             # immediately refresh UI
            st.rerun()
