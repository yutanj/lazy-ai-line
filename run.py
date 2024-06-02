# from gpt3contextual import ContextualChatGPT

# cc = ContextualChatGPT("sk-proj-C6FBwdsKEV8z6ADWIZeWT3BlbkFJAVvZe74Tr31yq4Vt4crN")

# while True:
#     text = input("Human> ")
#     resp, prompt, completion = cc.chat_sync("contextkey_1234", text)
#     print(f"AI> {resp}")

from gpt3contextual import ContextualChatGPT, ContextManager

cm = ContextManager(username="兄", agentname="妹", chat_description="仲良しの兄妹の会話です。丁寧語は使いません。")
cc = ContextualChatGPT("sk-proj-C6FBwdsKEV8z6ADWIZeWT3BlbkFJAVvZe74Tr31yq4Vt4crN", context_manager=cm)

while True:
    text = input(f"{cm.username}> ")
    resp, prompt, completion = cc.chat_sync("user1234567890", text)
    print(f"{cm.agentname}> {resp}")

