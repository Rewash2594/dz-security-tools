# identity-trust-graph

A cognitive tool for modeling and reasoning about **identity-based trust relationships** in modern systems.

This project does **not** perform exploitation, enumeration, or system interaction.
Its sole purpose is to make **implicit authority paths explicit**.

---

## Problem Statement

Modern security failures rarely originate from a single vulnerable host.
They emerge from **chains of trust between identities**:

- users
- roles
- service accounts
- automation
- delegated permissions

These relationships form a graph that is often:
- undocumented
- implicit
- distributed across systems

When this graph is not understood, both attackers and defenders
misjudge risk, escalation potential, and detection boundaries.

---

## Core Question

> *If I control this identity, what other identities or privileges become reachable through trust?*

This tool exists to answer that question **clearly and explicitly**.

---

## Design Principles

- **Identity-first reasoning**  
  Hosts execute. Identities authorize.

- **Input minimalism**  
  The tool operates on structured descriptions, not live systems.

- **No automation of attacks**  
  This is a reasoning aid, not an exploitation framework.

- **Graph over events**  
  Relationships matter more than individual actions.

---

## What the Tool Does

Given a simple description of identities and trust relationships, the tool:

1. Builds a **directed trust graph**
2. Identifies **implicit authority chains**
3. Outputs **reachable identities and roles** from a given starting point
4. Highlights **high-risk delegation paths**

The output focuses on *why* control can propagate, not *how* to exploit it.

---

## What the Tool Does NOT Do

- ❌ Enumerate systems
- ❌ Execute commands
- ❌ Interact with real environments
- ❌ Exploit vulnerabilities
- ❌ Replace security tooling

This tool is intentionally **non-operational**.

---

## Example Use Case

Given an environment where:
- a developer role can trigger a CI pipeline
- the pipeline runs as a service account
- the service account has administrative permissions

The tool reveals the **authority chain**:

developer → CI pipeline → service account → admin role


Even if no exploit exists, **control already propagates**.

---

## Example Input

```yaml
identities:
  - user: alice
    roles: [developer]

  - service: ci_pipeline
    runs_as: service_account_ci

trust:
  - from: developer
    to: ci_pipeline

  - from: service_account_ci
    to: admin_role

Example Output

alice → developer → ci_pipeline → service_account_ci → admin_role

Risk Level: High
Reason: Indirect authority chain through automation trust
