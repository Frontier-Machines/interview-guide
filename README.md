# interview-guide

## Getting Started

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

**Step 3.** Sign up for a free [Onshape](https://www.onshape.com/en/pricing) plan and practice making a sketch with a circle and square inside the circle, then extrude circle - square. Be comfortable with basic shapes in sketches and extruding them.

**Step 4.** Spend a little time brushing up on robotics concepts.
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
