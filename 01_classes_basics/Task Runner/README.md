# Task Runner (State Machine)

This project implements a simple **Task Runner** using basic Object-Oriented Programming principles in Python.

The goal of this project is to demonstrate how to manage **state transitions** and **business rules** using a single class, without advanced OOP features such as inheritance, properties, or composition.


## Overview

A `Task` represents a background job (e.g. CI/CD job, cron task, or async worker) that goes through a defined lifecycle.

Each task has:
- A unique ID
- A current status
- A failure counter
- A maximum retry limit

The class enforces strict rules about how and when a task can change its state.

---

## Task States

A task can be in **one of four states**:

- `created` – initial state
- `running` – task is currently executing
- `failed` – task failed but may be retried
- `completed` – task finished successfully (final state)

Once a task is `completed`, it cannot change state again.


## Rules & Logic

- A task can be started only if:
  - It is in `created` or `failed` state
  - The maximum retry limit has not been reached
- A task can fail only while `running`
- A task can complete only while `running`
- Failed tasks can be restarted until the retry limit is exceeded
- All invalid operations are safely ignored (no exceptions)


## Why This Project?

This project focuses on:
- State-based logic
- Defensive programming
- Clean method responsibilities
- Readable and maintainable code

It intentionally avoids advanced Python features to highlight **core class design skills**.


