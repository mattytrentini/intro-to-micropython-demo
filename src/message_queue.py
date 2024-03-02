_messages = []

def add_message(message) -> None:
    _messages.append(message)

def pop_message() -> str:
    return _messages.pop(0)

def message_count() -> int:
    return len(_messages)