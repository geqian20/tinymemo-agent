# TinyMemo Agent

**一个拥有会话内记忆的轻量级 Python 命令行对话 Agent。**

A lightweight Python conversational agent with in-session memory, built with the OpenAI SDK.

TinyMemo Agent 通过维护对话历史，让 AI 能够结合之前的提问和回答进行连续交流。项目保留了简单直观的单文件结构，适合 Python 初学者学习 API 调用、多轮对话和基础上下文维护。

默认角色是网络安全助教，可以通过修改系统提示词切换为其他助手。

## 功能

- **多轮对话**：使用 `messages` 列表保存当前会话的提问和回复。
- **上下文传递**：每次请求都带上完整的当前对话历史。
- **历史查看**：输入 `history` 查看聊天记录，包括系统提示词。
- **环境变量配置**：通过 `.env` 设置 API 密钥、接口地址和模型名称。
- **角色定制**：修改 `test3.py` 中的 `system` 消息即可调整助手角色。

## 快速开始

准备 Python 3.10 或更高版本，以及所用模型服务的 API 密钥。

下载本仓库并进入项目目录，然后创建虚拟环境：

```bash
python -m venv .venv
```

macOS / Linux：

```bash
source .venv/bin/activate
```

Windows PowerShell：

```powershell
.venv\Scripts\Activate.ps1
```

安装依赖：

```bash
python -m pip install -r requirements.txt
```

将 `.env.example` 复制为 `.env`，填入自己的配置：

```dotenv
AI_API_KEY=your_api_key_here
AI_BASE_URL=https://api.openai.com/v1
AI_MODEL_NAME=your_model_name_here
```

`AI_BASE_URL` 和 `AI_MODEL_NAME` 请按模型服务提供方的配置填写；也可以使用兼容该 SDK 的 Chat Completions 接口。不要提交含有真实密钥的 `.env` 文件。

在项目目录运行：

```bash
python test3.py
```

## 使用示例

下面是输入流程示例，具体回复由模型生成：

```text
你: 请用简单的语言解释什么是防火墙。
你: 给我一个生活中的类比。
你: history
你: exit
```

第二个问题会连同前面的对话一起发送，因此模型能够参考上一轮内容。

| 输入 | 作用 |
| --- | --- |
| 普通文本 | 向 AI 提问 |
| `history` | 显示当前对话历史 |
| `exit` | 退出程序 |

## 记忆如何工作

1. 在 `messages` 列表中设置助手的系统提示词。
2. 将用户的新消息追加到列表。
3. 将列表传给模型，获得回复。
4. 将回复追加到列表，供后续对话使用。

这里的“记忆”是保存在 Python 进程内的**会话内记忆**。程序退出后历史会丢失，不会保存到磁盘，也不会训练或更新模型。

## 当前限制

- 尚未实现持久化存储、历史摘要或上下文长度控制；长对话会增加请求用量，也可能达到模型的上下文限制。
- 当前是一个教学用途的对话 Agent，没有工具调用、任务规划或自主执行能力。
- 请求失败时会显示错误信息；失败的用户消息仍保留在历史中。
- 对话历史会发送到你配置的模型服务。

## 项目结构

```text
tinymemo-agent/
├── test3.py          # 命令行对话与会话记忆
├── requirements.txt  # Python 依赖
├── .env.example      # 环境变量示例，不含真实密钥
├── .gitignore        # 忽略本地配置、虚拟环境和缓存
└── README.md
```
