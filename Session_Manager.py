import time

sessions = {}


def start_session(user_id, session_duration):
    session_start_time = time.time()
    session_end_time = session_start_time + session_duration
    return f"user for user ID {user_id} started, the session will last {session_duration} "
    
def is_session_active(user_id):
    if user_id not in sessions:
        return False
    
    session_start_time, session_duration = sessions[user_id]
    current_time = time.time()

    if current_time <= session_start_time +session_duration:
        return True
    else:
        return False
    
def end_session(user_id):
    if user_id in sessions:
        del sessions[user_id]
        return f"Session for user {user_id} has been ended manually."
    else:
        return f"No active session found for user {user_id}."
    
    


    



user_id = "12345"
session_duration = 3600  

print(start_session(user_id, session_duration))
import time

sessions = {}


def start_session(user_id, session_duration):
    session_start_time = time.time()
    session_end_time = session_start_time + session_duration
    return f"user for user ID {user_id} started, the session will last {session_duration} "
    
def is_session_active(user_id):
    if user_id not in sessions:
        return False
    
    session_start_time, session_duration = sessions[user_id]
    current_time = time.time()

    if current_time <= session_start_time +session_duration:
        return True
    else:
        return False
    
def end_session(user_id):
    if user_id in sessions:
        del sessions[user_id]
        return f"Session for user {user_id} has been ended manually."
    else:
        return f"No active session found for user {user_id}."
    
    print(start_session(user_id, session_duration))



    



user_id = "12345"
session_duration = 3600  

print(start_session(user_id, session_duration))
# Check if the session is active
print(is_session_active(user_id))  # Should return True

# End the session manually
print(end_session(user_id))

# Check if the session is active again
print(is_session_active(user_id)) 




