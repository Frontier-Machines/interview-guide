# interview-guide

## The Process

1. 1 hour Google Meet interview.
2. 30 minute Google Meet interview.
3. Roughly half day onsite interview at Frontier Machines headquarters in Mountain View.

## The Interview

The Google Meet interview is about 1 hour and covers three parts:

1. Debugging some code together via Google Meet on your laptop with your AI agent/coding assistant of choice.
2. I'll show you some products and we'll figure out together how we'd get a robot to pack them autonomously. We may do some basic CAD as part of this.
3. Q&A around basic robotics concepts.

## Getting Started

This will help you prep for the interview.

**Step 0.** Install [git](https://git-scm.com/) and clone the repo:
```
git clone https://github.com/Frontier-Machines/interview-guide
```

**Step 1.** Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and then run:
```
uv run main.py
```
Make sure you see two arms moving around like crazy and some squares bouncing around in the rerun visualization.

**Step 2.** Install [Claude Code](https://docs.anthropic.com/en/docs/claude-code) or your favorite coding assistant to help you with this interview.

**Step 3.** Go to https://meet.google.com/ → click "New Meeting" → "Start an instant meeting" → Make sure your video and audio are working and have the right permissions.

**Step 4.** Sign up for [SmallCAD](https://smallcad.com/) and practice the basics: create a sketch with a square inside a circle, extrude the difference, then add a new sketch on top of the extruded face and extrude again. Get comfortable with sketches and extrusions.

**Step 5.** Spend a little time brushing up on robotics concepts.
- Understand fundamentals, not definitions: Be able to explain how things work step-by-step (e.g., what actually happens during a ping, DNS lookup, or control loop).
- Think in tradeoffs: Many questions are about when to use X vs Y (TCP vs UDP, position vs torque control, open vs closed loop).
- Know common failure modes: Be ready to reason about bugs like race conditions, packet loss, sensor noise, or unstable PID gains.
- Connect hardware ↔ software: Understand how physical constraints (motors, voltage, friction) interact with code and control systems.
- Debugging mindset matters: Have a clear, structured approach to diagnosing issues, especially intermittent ones.
- Be comfortable with signals and timing: Latency, bandwidth, synchronization, and real-time behavior show up everywhere.
- Explain concepts intuitively: Use simple mental models (water flow for current, feedback loops for control, etc.).
- Know why things exist: Not just what PWM or a gearbox is, but why engineers use them.
- Expect practical reasoning: Questions often test judgment in messy real-world scenarios, not textbook answers.
- Stay honest and think out loud: Interviewers care more about your reasoning process than perfect answers.

**Step 6.** Watch [this video](https://www.youtube.com/watch?v=L3rLT84qqLk) and consider whether you're willing to spend many hours practicing teleoperation across different tasks until you can perform them reliably.
