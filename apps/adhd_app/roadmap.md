
---

## **`roadmap.md`**

```markdown
# ADHD Assistant Roadmap

This roadmap outlines the planned development stages for the ADHD Assistant app.

---

## **Phase 1: MVP – Day One Runnable Version**
- WebAgent
  - Create React Native folder structure
  - Stub AI task breakdown
  - Stub brain dump processing
- DevOpsAgent
  - SQLite DB setup
  - Encrypted storage placeholder
  - CLI Pomodoro timer
- ValidatorAgent
  - Validate workspace structure and files
- Main.py
  - Minimal CLI to simulate ADHD productivity sessions
- Documentation
  - README.md
  - roadmap.md

---

## **Phase 2: AI Enhancements**
- Integrate Ollama or other LLM for realistic task breakdown
- Smart prioritization AI based on task importance
- Auto-categorization of brain dumps into projects
- Persistence across sessions

---

## **Phase 3: UX/UI Enhancements**
- React Native front-end MVP
  - Task dashboard
  - Brain dump page
  - Timer visualization
- Minimal desktop or mobile interface
- Theme options for ADHD-friendly UI

---

## **Phase 4: Productivity Tools**
- Full Pomodoro timer with customizable intervals
- Notifications for breaks and focus sessions
- Historical tracking of task completion
- Export/import brain dumps

---

## **Phase 5: Advanced Features**
- Integration with calendars, reminders, and task managers
- AI-powered suggestions for optimal focus sessions
- Gamification for ADHD productivity support
- Multi-user sync (cloud)

---

## **Development Notes**
- Maintain modularity: each agent is independent
- Use SQLite for persistent storage
- Keep CLI mode runnable out-of-the-box for testing
- Document every function in `agents/` for clarity

---

## **Goal**
Provide a **ready-to-run ADHD productivity assistant** that combines AI and Pomodoro workflow, enabling users to **start using it immediately**, while allowing developers to extend its AI capabilities and UI.
