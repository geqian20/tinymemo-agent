import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key=os.getenv("AI_API_KEY")
base_url=os.getenv("AI_BASE_URL")
model_name=os.getenv("AI_MODEL_NAME")

messages=[
    {"role":"system","content":"你是一个网络安全助教，非常乐于助人，讲解清晰易懂"},
]

client=OpenAI(api_key=api_key,base_url=base_url)

def chat_with_memory(user_input):
    print("正在思考中...")
    messages.append({"role":"user","content":user_input})
    
    try:
        response=client.chat.completions.create(
            model=model_name,
            messages=messages
        )
        
        ai_reply=response.choices[0].message.content
        
        messages.append({"role":"assistant","content":ai_reply})
        
        return ai_reply
        
    except Exception as e:
        return f"发生错误:{e}"
    
if __name__=="__main__":
    
    print("=== AI Agent (记忆版) ===")
    print("输入 'exit' 退出程序")
    
    while True:
        question = input("\n你: ")
        
        if question.lower()=="exit":
            print("再见👋")
            break
        if question.lower()=="history":
            for msg in messages:
                print(f"[{msg['role']}]:{msg['content']}")
                
            print("-----------")
            continue
        
        answer=chat_with_memory(question)
        print(f"AI: {answer}")