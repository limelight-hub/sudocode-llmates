# 📚 Self-Study Curriculum

Start from 2025-09-06

## **Week 1: LLM APIs 101**

**📖 Reading Materials**

* [OpenAI Docs: Chat Completions](https://platform.openai.com/docs/guides/chat)
* [Anthropic Docs: Messages API](https://docs.anthropic.com/en/api/overview)
* [Gemini API Docs](https://ai.google.dev/gemini-api/docs)

**🎯 Learning Goals**

* Hiểu cách gọi API từ nhiều nhà cung cấp LLM.
* Biết dùng params cơ bản (`temperature`, `top_p`, `max_tokens`).
* Biết dùng streaming response.

**📝 Exercises**

1. Call OpenAI API và in ra response.
2. Call Claude API và so sánh format input/output.
3. Call Gemini API với input text (nếu có key).

**💻 Mini Project**

* Tạo **CLI chatbot**: nhập câu hỏi → chọn model (GPT/Claude/Gemini) → trả lời.
* Thêm flag `--stream` để chạy streaming.

**📦 Deliverables**

* Notebook demo 3 API.
* CLI chatbot script (`chatbot.py`).

---

## **Week 2: Prompt Engineering**

**📖 Reading Materials**

* [Google Gemini Prompt Engineering](https://ai.google.dev/gemini-api/docs/prompting-strategies).
* [Claude Prompt Engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview).
* [OpenAI Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering).

**🎯 Learning Goals**

* Hiểu zero-shot, few-shot, chain-of-thought.
* Biết cách viết system/user/assistant messages.
* Biết cách ép LLM trả JSON output.

**📝 Exercises**

1. Viết prompt để tóm tắt văn bản thành 3 bullet points.
2. Viết prompt few-shot để phân loại sentiment (positive/negative/neutral).
3. Viết prompt để sinh JSON có schema:

   ```json
   {"title": string, "category": string, "summary": string}
   ```

**💻 Mini Project**

* Build **Movie Recommender**: input “tâm trạng” → output JSON list phim `{title, genre, why_recommended}`.

**📦 Deliverables**

* Notebook với 3 prompt styles.
* Script `movie_recommender.py`.

---

## **Week 3: Function Calling & Tools**

**📖 Reading Materials**

* [OpenAI Docs: Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)
* [OpenAI Docs: Function Calling](https://platform.openai.com/docs/guides/function-calling)
* [Claude Docs: Tools](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)
* [Google Gemini Docs: Function Calling](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting)

**🎯 Learning Goals**

* Phân biệt structured outputs và function calling.
* Biết cách define structured outputs và function calling schema.
* Biết cách cho LLM chọn tool khi cần.
* Hiểu khi nào nên dùng tool vs trả text.

**📝 Exercises**

1. Tạo function `calculator` và để LLM gọi khi gặp phép toán.
2. Tạo function `get_weather(city)` → trả kết quả giả lập.

**💻 Mini Project**

* Build **Smart Assistant** với 2 tool:

  * `calculator`
  * `weather`
* Assistant tự quyết định khi nào dùng tool.

**📦 Deliverables**

* Notebook demo function calling.
* Script `assistant_tools.py`.

---

## **Week 4: Memory & LangChain Intro**

**📖 Reading Materials**

* [LangChain Memory](https://blog.langchain.com/memory-for-agents/)
* [LangGraph Memory](https://learn.deeplearning.ai/courses/long-term-agentic-memory-with-langgraph/lesson)

**🎯 Learning Goals**

* Hiểu short-term vs long-term memory.
* Biết cách add memory vào chatbot.
* Biết cách làm personalization.

**📝 Exercises**

1. Build chatbot với `ConversationBufferMemory`.
2. Chuyển sang `ConversationSummaryMemory`.

**💻 Mini Project**

* Build **Mentor-Bot**:

  * Nhớ tên user.
  * Nhớ sở thích user.
  * Trả lời cá nhân hóa dựa trên memory.

**📦 Deliverables**

* Notebook memory demo.
* Script `mentor_bot.py`.

---

## **Week 5: Retrieval-Augmented Generation (RAG)**

**📖 Reading Materials**

* [LangChain RAG](https://python.langchain.com/docs/tutorials/rag/)
* [RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch)


**🎯 Learning Goals**

* Hiểu embeddings & vector DB.
* Biết cách build pipeline index → retrieve → answer.
* Biết cách QA với tài liệu.

**📝 Exercises**

1. Index 5 bài Wikipedia với FAISS.
2. Query → retrieve top 3 → feed vào GPT để trả lời.

**💻 Mini Project**

* Build **PDF-QA Bot**:

  * Input: PDF (lecture notes).
  * Chunk → embed → store → retrieve → GPT trả lời.

**📦 Deliverables**

* Notebook indexing & retrieval.
* Script `pdf_qa_bot.py`.

---

## **Week 6: Backend (FastAPI + PostgreSQL + Redis)**

**📖 Reading Materials**

* [FastAPI Docs](https://fastapi.tiangolo.com/)
* [redis-py](https://redis.readthedocs.io/)
* [SQLAlchemy Docs](https://docs.sqlalchemy.org/en/20/)

**🎯 Learning Goals**

* FastAPI API + `.env`.
* PostgreSQL (SQLAlchemy + Alembic) lưu hội thoại.
* Redis session/memory + cache.
* LangChain vào chat endpoint (SSE optional).

**📝 Exercises**

1. Skeleton FastAPI (`app/main.py`, routers `health`, `chat`), cấu hình ENV.
2. Kết nối Postgres; migration đầu tiên; CRUD messages.
3. Kết nối Redis; lưu session theo `session_id`.
4. POST `/v1/chat`: nhận `{session_id, message}` → lưu DB → reply (SSE optional).
5. GET `/health`: kiểm tra Postgres/Redis.

**💻 Mini Project**

* Chatbot Backend: FastAPI + LangChain + Postgres + Redis
  * Endpoints: POST `/v1/chat`, GET `/health`
  * Docker Compose deploy.

**📦 Deliverables**

* `app/` (core/config, db/session, models, schemas, routers), `docker-compose.yml`, `.env.example`.
* Run: `docker compose up -d`, `alembic upgrade head`, `uvicorn app.main:app --reload`.