# 🧠 LangGraph Persistence Notes

## 📌 What is Persistence?

* Persistence in LangGraph refers to the ability to **save and restore the state of a workflow over time** (1:03–1:19).
* It allows you to store **not just the final state values but also all intermediate values** in a database.
* This is **crucial for resuming workflows and understanding execution history** (7:25–9:09).

---

# ✅ Benefits of Persistence

## ⚙️ Fault Tolerance

(10:44–11:15, 38:05–38:20)

* If a workflow crashes, persistence enables it to **resume from the exact point of failure rather than restarting from the beginning**.
* The video demonstrates this by **simulating a crash and then resuming the workflow from the point of interruption** (39:01–44:20).

---

## 💬 Building Chatbots / Short-Term Memory

(11:21–13:17, 36:45–38:00)

* Persistence is essential for **chatbots to resume past conversations and retain context**.
* It works by **storing previous interactions in a database**.

---

## 👨‍💻 Human in the Loop (HITL)

(44:28–47:35)

* This feature allows a **human to pause a workflow**.
* The human can **review, approve, or modify the state before the workflow continues**.
* Persistence ensures that the workflow can be **resumed from the exact point where human intervention is required**.

---

## ⏳ Time Travel

(47:36–57:30)

* Persistence allows users to **travel back in time to a specific checkpoint** in the workflow's execution history.
* From that checkpoint, the workflow can be **rerun again**.
* This is **particularly useful for debugging complex workflows**.

---

# 🏗 Implementation with Checkpointers and Threads

## 💾 Checkpointer

(14:50–17:33)

* Persistence is implemented using **checkpointers**.
* Checkpointers **save the state of the workflow at various checkpoints**.
* These checkpoints are **typically created after each superstep**.
* The state is **stored in a database**.

---

## 🧵 Threads

(20:10–24:11)

* When executing a workflow multiple times, each execution is assigned a **unique thread ID**.
* This allows the persistence mechanism to:

  * **Store state values specific to that execution**
  * **Retrieve the correct workflow state later**
* This prevents conflicts and enables **distinct conversational histories for chatbots**.

---

# 🧪 Code Implementation

(25:35–35:51)

* The video demonstrates how to implement persistence using **`InMemorySaver`**.
* `InMemorySaver` is a type of **checkpointer that saves data to RAM** (used for demo purposes).
* Thread IDs are used to **store and retrieve specific workflow states**.

### Retrieving workflow state

* Retrieve the **final state**

  * `workflow.get_state()`

* Retrieve the **complete history of intermediate states**

  * `workflow.get_state_history()`
