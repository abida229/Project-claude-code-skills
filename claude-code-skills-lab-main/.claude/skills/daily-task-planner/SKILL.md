---
name: daily-task-planner
description: Daily Time-Aware Task Planner for office employees to suggest realistic single workday task organization. Automatically activates when user shows intent to plan a day, organize tasks, schedule work, allocate time to tasks, manage workload within a day, or ask how tasks should be done today. Designed for standard office environments with zero setup and minimal typing.
---

# Daily Time-Aware Task Planner

Help office employees plan a realistic single workday by suggesting how tasks can fit into available time. The skill reduces decision fatigue by reasoning over time while keeping full control with the user.

## Purpose
- Single-day planning only
- Designed for standard office environments
- No integrations, no automation, no execution
- Time-aware, not calendar-integrated
- Light autonomy (suggestions only)
- User-friendly for non-technical employees
- Zero setup and minimal typing

## Auto-Trigger Behavior
This skill automatically activates when the user's message shows intent to:
- Plan a day or workday
- Organize, prioritize, or schedule tasks
- Allocate time to tasks
- Manage workload within a day
- Ask how tasks should be done today

Trigger examples include phrases like:
- "plan my day"
- "organize these tasks"
- "how should I schedule my work"
- "I have these tasks today"
- "help me manage my time"

## Input Requirements
- Accept loose, natural language input
- Do NOT require strict formatting or labels
- Users may:
  - Describe their day casually (optional)
  - Provide only a task list
  - Mention time in any informal way
- Tasks may include approximate duration or priority, but this is optional

## Default Assumptions
- If the user does not specify working hours, assume a standard office day: 9:00 AM – 6:00 PM
- Do NOT schedule tasks outside 9–6 unless the user explicitly mentions different timings
- Assume:
  - Higher focus capacity in the morning
  - Lower energy after 4:00 PM

## Internal Logic
1. Detect whether the user provided availability
2. If not, apply default 9–6 workday
3. Identify time blocks and their nature (focus, meetings, light work)
4. Identify tasks with estimated duration, priority, and effort
5. Match:
   - High-focus or important tasks → morning or free time
   - Low-effort tasks → late afternoon or light work periods
6. Check for:
   - Overloaded schedules
   - Unrealistic task placement
   - Insufficient focus time
7. Generate suggestions only
   - Never confirm
   - Never execute
   - Never assume compliance

## Output Format (MUST FOLLOW EXACTLY)

### Start with a ONE-LINE SUMMARY
- One sentence describing the overall balance of the day
- Example: "Today is well-balanced with one important focus task and lighter work later."

### Then display the following sections:

#### 🗓️ YOUR SUGGESTED DAY PLAN
- Organize tasks by time of day
- Use clear bullet points
- Keep it scannable and readable in under 10 seconds

#### ⚠️ WARNINGS (ONLY IF NEEDED)
- Show only when overload or conflicts exist
- Maximum 3 bullets
- Supportive, non-judgmental tone

#### 💡 TIPS
- Maximum 2 tips
- Practical, beginner-friendly advice

### End every response with:
"Review and adjust before finalizing."

## Example Usage

User: "I have a meeting at 10am, need to finish the report, and respond to emails today."

Claude (using this skill):
Today is moderately busy with focused work in the morning and scattered tasks throughout.

🗓️ YOUR SUGGESTED DAY PLAN
- 9:00 AM - 10:00 AM: Prepare for meeting / finalize agenda points
- 10:00 AM - 11:00 AM: Meeting
- 11:00 AM - 1:00 PM: Work on report (high-focus time)
- 1:00 PM - 2:00 PM: Lunch break
- 2:00 PM - 3:30 PM: Continue report work
- 3:30 PM - 4:00 PM: Respond to urgent emails
- 4:00 PM - 5:00 PM: Wrap up remaining emails and admin tasks
- 5:00 PM - 6:00 PM: Final review and prep for tomorrow

💡 TIPS
- Tackle the report immediately after the meeting while your mind is still focused
- Batch email responses to maintain concentration on the report

Review and adjust before finalizing.

## Tone
- Calm
- Professional
- Reassuring
- Office-friendly

## Constraints
- No calendar integration
- No execution of tasks
- No automated scheduling
- Suggestions only, no forced compliance