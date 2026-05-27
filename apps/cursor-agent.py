# /// script
# requires-python = ">=3.9"
# dependencies = [
#   "marimo>=0.23.8",
#   "mo>=0.3.0",
#   "wigglystuff>=0.5.4"
# ]
# ///


import marimo

__generated_with = "0.23.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Accelerating Developement using Cursor
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Cursor

    > Cursor is a agent harness that leverage foundational models reasoning and code generation capabilities to materialize requirements into code
    """)
    return


@app.cell
def _():
    PREFIX="https://raw.githubusercontent.com/rahul-mishra-msx/marimo-gh/main/apps"
    print(PREFIX)
    mode_data = {
        "plan_mode": {
            "title": "Plan Mode",
            "description": "Researches the codebase, asks clarifying questions, creates a reviewable implementation plan, and lets you edit/review that plan before building.",
            "vid": f"{PREFIX}/cursor-demo.gif"
        },
        "ask_mode": {
            "title": "Ask Mode",
            "description": "Searches and explains your codebase without editing files. In the CLI, Cursor says Ask mode is for exploring code without making changes.",
            "vid": f"{PREFIX}/cursor-demo-ask.gif"
        },
        "agent_mode": {
            "title": "Agent Mode",
            "description": "Can complete coding tasks, search code, read files, edit files, run terminal commands, use browser tools, generate images, and create checkpoints",
            "vid": f"{PREFIX}/cursor-demo-agent.gif"
        },
        "debug_mode": {
            "title": "Debug Mode",
            "description": "Generates hypotheses, adds logging/instrumentation, asks you to reproduce the bug, analyzes runtime logs, makes a targeted fix, then verifies and cleans up instrumentation.",
            "vid": f"{PREFIX}/cursor-demo-debug.gif"
        },
        "multi":{
            "title": "Multiagent Mode",
            "description": "Queue follow-up messages while Agent is working; run subagents in parallel; run background subagents independently; hand work to Cloud Agent; isolate work in Git worktrees.",
            "vid": f"{PREFIX}/cursor-demo-multitask.gif"
        }
    }
    return (mode_data,)


@app.cell
def _(GraphWidget, mo, mode_data):
    cursor_modeOfOperations = mo.ui.anywidget(GraphWidget())
    cursor_modeOfOperations.add_node("Mode of Operations", id="root", size=30)
    cursor_modeOfOperations.attach_node(source="root", name="Plan Mode", data=mode_data["plan_mode"])
    cursor_modeOfOperations.attach_node(source="root", name="Agent Mode", data=mode_data["agent_mode"])
    cursor_modeOfOperations.attach_node(source="root", name="Multitask Mode", data=mode_data["multi"])
    cursor_modeOfOperations.attach_node(source="root", name="Ask Mode", data=mode_data["ask_mode"])
    cursor_modeOfOperations.attach_node(source="root", name="Debug Mode", data=mode_data["debug_mode"])



    mo.vstack([
        mo.md("## Cursor Mode of Execution"),
        cursor_modeOfOperations
    ])
    return (cursor_modeOfOperations,)


@app.cell
def _(cursor_modeOfOperations, mo):
    selected_node_data = (cursor_modeOfOperations.get_selected_node_data() or [{}])[0].get("data", {})
    mo.vstack([
    mo.md(f'''
        # {selected_node_data.get("title", "Select Mode")}

        > {selected_node_data.get("description", "")}
    '''),
        mo.image(src=selected_node_data.get("vid", ""))
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Extensibility Framework of Cursor

    To customize the behaviour of Agent and make it more deterministic and increase quality of results typically these extensibility construct of cursor are used
    """)
    return


@app.cell
def _(mo):
    mo.mermaid('''
    flowchart TD
        agent[Cursor]

        skills([SKILLS])
        hooks([Hooks])
        rules([Rules])
        mcp-server([MCP Servers])
        plugins([Plugins])
        subagent([Sub Agents])
        agentmd([AGENT.md])

        skills --> agent
        hooks --> agent
        rules --> agent
        plugins --> agent
        mcp-server --> agent
        subagent --> agent
        agentmd --> agent
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Flow of Execution and Role of each constructs
    """)
    return


@app.cell
def _(mo):
    mo.hstack([mo.mermaid('''
    flowchart TD
        A[User prompt] --> B[Start Cursor Agent session]

        B --> C[Load persistent project instructions]
        C --> C1[AGENTS.md]
        C --> C2[Cursor Rules]

        C1 --> D[Agent plans task]
        C2 --> D

        D --> E{Need specialized workflow?}
        E -->|Yes| F[Load Skill]
        E -->|No| G[Continue]

        F --> G

        G --> H{Need external tools/data?}
        H -->|Yes| I[Use MCP Server]
        H -->|No| J[Make Changes]

        I --> J

        J --> K[Read files / edit files / run commands]

        K --> L[Hooks fire around events]
        L --> M[Final response or\ncode changes]
    ''')], align="center", justify="center")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Skills

    Skills are reusable instruction modules for coding agents. Each skill is typically defined in a `SKILL.md` file that contains natural-language guidance, rules, examples, and workflow conventions.

    Agents load skills on demand when a task requires that specific expertise.

    ### Example Structure

    ```text
    .agents/
    └── skills/
        └── terraform-style-guide/
            └── SKILL.md
    ```

    ### Example

    In this structure, `terraform-style-guide` is a skill that provides Terraform-specific coding standards and best practices to the agent when needed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Builtin Skills in Cursor
    """)
    return


@app.cell
def _(mo):
    mo.mermaid('''
    flowchart TD
        skills[SKILLS.md]

        c1(["/"create-hook])
        c2(["/"create-subagent])
        c3(["/"create-skill])
        c3(["/"create-rule])
        c4(["/"sdk])


        skills --> c1
        skills --> c2
        skills --> c3
        skills --> c4
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Skills Used in Our Setup
    """)
    return


@app.cell
def _(mo):
    mo.mermaid('''
    flowchart TD
        skills[SKILLS.md]
        t1[Terraform\nStyle Guide]
        t2[Terraform\nRefactor Module]
        t3[Python\nDesign Pattern]
        t4[Terraform Provider\nTest Pattern]


        skills --> t1
        skills --> t2
        skills --> t3
        skills --> t4
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MCP Servers

    MCP servers are integration servers that expose external tools, data sources, and services to a coding agent through the Model Context Protocol.

    In Cursor, MCP servers let the agent connect to systems such as databases, APIs, documentation sources, browsers, design tools, or internal services. Once configured, the agent can discover and use the tools provided by those servers when they are relevant to the task.


    Global MCP servers can be configured in:

    ```text
    ~/.cursor/
    └── mcp.json
    ```

    ### Example Configuration

    ```json
    {
      "mcpServers": {
        "local-tools": {
          "type": "stdio",
          "command": "npx",
          "args": ["-y", "my-mcp-server"]
        }
      }
    }
    ```

    ### Example

    In this structure, `mcp.json` defines one or more MCP servers that Cursor can connect to. The `local-tools` server exposes additional tools to the coding agent, allowing it to perform tasks that require external context or system access.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MCP Servers using in our setup
    """)
    return


@app.cell
def _(mo):
    mo.mermaid('''
    flowchart TD
        mcp[MCP Server]
        t1[Strands MCP Server]
        t2[Langchain Docs MCP Server]
        t3[AWS Agentcore Docs]

        mcp --> t1
        mcp --> t2
        mcp --> t3
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Rules

    Rules are persistent instructions or constraints that guide a coding agent's behavior across tasks. They define how the agent should write, review, structure, or modify code within a project.

    Unlike skills, which are loaded on demand for specific expertise, rules are usually always available to the agent while working in a repository or workspace.

    ### Example Structure

    ```text
    .agents/
    └── rules/
        └── coding-standards.mdc
    ```

    ### Example

    In this structure, `coding-standards.md` is a rules file that defines project-wide coding conventions, formatting expectations, naming patterns, and other guidelines the agent should consistently follow.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Rules in Our Setup
    """)
    return


@app.cell
def _(mo):
    mo.vstack([mo.mermaid('''
    flowchart TD
        rules[Rules]
        ps[Project Structure]
        pl[Python Lint]

        rules --> ps
        rules --> pl
    ''')], align="center")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Subagents

    Subagents are specialized AI agents designed for task-specific workflows. In Cursor, subagents can be used to delegate focused work such as code review, debugging, testing, documentation, refactoring, or architecture analysis.

    A subagent runs with its own role, instructions, and context, helping keep the main agent focused while allowing specialized work to happen separately.

    ### Example Structure

    ```text
    .cursor/
    └── agents/
        └── code-reviewer.md
    ```

    ### Example

    In this structure, `code-reviewer.md` defines a subagent focused on reviewing code. The main coding agent can delegate review-related tasks to this subagent when that expertise is needed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Subagents in Our Setup
    """)
    return


@app.cell
def _(mo):
    mo.vstack([mo.mermaid('''
    flowchart TD
        subagent[Subagents]
        sar[SPEC Alignment\nReviewer]
        arch[Architecture\nOverview]

        subagent --> sar
        subagent --> arch
    ''')], align="center")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Plugins

    Plugins are distributable bundles that package coding-agent components for reuse in Cursor.

    A Cursor plugin can include rules, skills, subagents, commands, hooks, MCP servers, and supporting assets. Plugins make it easier to share a complete agent setup across projects, teams, or organizations.

    ### Cursor Convention

    Cursor plugins are defined as directories that include a required plugin manifest at:

    ```text
    .cursor-plugin/
    └── plugin.json
    ```

    The manifest describes the plugin and can point Cursor to the components included in the plugin.

    ### Example Structure

    ```text
    my-plugin/
    ├── .cursor-plugin/
    │   └── plugin.json
    ├── rules/
    │   └── coding-standards.mdc
    ├── skills/
    │   └── code-reviewer/
    │       └── SKILL.md
    ├── agents/
    │   └── security-reviewer.md
    ├── commands/
    │   └── deploy.md
    ├── hooks/
    │   └── hooks.json
    ├── mcp.json
    ├── assets/
    │   └── logo.svg
    └── README.md
    ```

    ### Example Manifest

    ```json
    {
      "name": "my-plugin",
      "description": "Custom development tools",
      "version": "1.0.0",
      "author": {
        "name": "Your Name"
      }
    }
    ```

    ### Example

    In this structure, `my-plugin` packages multiple Cursor agent components into one reusable bundle. Cursor can discover the included rules, skills, subagents, commands, hooks, and MCP servers from the plugin structure or from paths declared in `.cursor-plugin/plugin.json`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Agent lifecycle events and Hooks
    """)
    return


@app.cell
def _(mo):
    mo.mermaid('''
    flowchart TD
        A[User request] --> B[Agent starts]

        B --> H1[Hook: sessionStart]
        H1 --> C[User prompt submitted]

        C --> H2[Hook: beforeSubmitPrompt]
        H2 --> D[Agent planning / reasoning]

        D --> H3[Hook: afterAgentThought]
        H3 --> E[Tool / action needed]

        E --> H4[Hook: preToolUse]
        H4 --> F[Tool / action execution]

        F --> H5[Hook: postToolUse]
        H5 --> G[Agent observes result]

        F --> X[Hook: postToolUseFailure]
        X --> G

        G --> I{Task complete?}

        I -- No --> D

        I -- Yes --> H6[Hook: afterAgentResponse]
        H6 --> J[Final response]

        J --> H7[Hook: stop]
        H7 --> K[Hook: sessionEnd]
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Hooks Event in Cursor
    """)
    return


@app.cell
def _(mo):
    from wigglystuff import GraphWidget


    CURSOR_HOOK_EVENTS = [
        "workspaceOpen",

        "sessionStart",
        "beforeSubmitPrompt",
        "afterAgentThought",
        "afterAgentResponse",
        "preCompact",
        "stop",
        "sessionEnd",

        "preToolUse",
        "postToolUse",
        "postToolUseFailure",

        "beforeReadFile",
        "afterFileEdit",

        "beforeShellExecution",
        "afterShellExecution",

        "beforeMCPExecution",
        "afterMCPExecution",

        "subagentStart",
        "subagentStop",

        "beforeTabFileRead",
        "afterTabFileEdit",
    ]


    gw = mo.ui.anywidget(widget=GraphWidget())

    gw.add_node(id="hook", name="Hooks")

    for hookName in CURSOR_HOOK_EVENTS:
        gw.attach_node(name=hookName, source="hook")

    gw
    return GraphWidget, gw


@app.cell
def _():
    CURSOR_HOOKS = {
        "workspaceOpen": {
            "description": "Fires when Cursor opens a workspace or when the workspace folder changes.",
            "example": "Initialize project-level hook state, load workspace-specific rules, or log that a new workspace was opened.",
            "diagram": """
    flowchart LR
        A[Open Cursor / change workspace] --> B([workspaceOpen]) --> C[Workspace ready]
    """,
        },

        "sessionStart": {
            "description": "Fires when an Agent's session starts.",
            "example": "Create a session log entry, attach metadata, or initialize per-session counters.",
            "diagram": """
    flowchart LR
        A[User starts Agent] --> B([sessionStart]) --> C[Session active]
    """,
        },

        "beforeSubmitPrompt": {
            "description": "Fires before a user prompt is submitted to the backend.",
            "example": "Validate the prompt, block restricted instructions, or add required context before submission.",
            "diagram": """
    flowchart LR
        A[User writes prompt] --> B([beforeSubmitPrompt]) --> C[Prompt submitted]
    """,
        },

        "afterAgentThought": {
            "description": "Fires after the agent completes a thinking block.",
            "example": "Record that the agent completed a reasoning step or inspect metadata about the thought block.",
            "diagram": """
    flowchart LR
        A[Agent reasoning] --> B([afterAgentThought]) --> C[Next agent step]
    """,
        },

        "afterAgentResponse": {
            "description": "Fires after the agent produces an assistant response.",
            "example": "Log the response, run quality checks, or notify another system that the agent replied.",
            "diagram": """
    flowchart LR
        A[Agent creates response] --> B([afterAgentResponse]) --> C[Response shown]
    """,
        },

        "preCompact": {
            "description": "Fires before Cursor compacts the context window.",
            "example": "Save important context externally before compaction or add a note that should survive summarization.",
            "diagram": """
    flowchart LR
        A[Context getting large] --> B([preCompact]) --> C[Context compacted]
    """,
        },

        "stop": {
            "description": "Fires when the agent loop ends and can optionally provide a follow-up message.",
            "example": "Trigger a final validation step or auto-submit a follow-up instruction if the task is incomplete.",
            "diagram": """
    flowchart LR
        A[Agent loop finishing] --> B([stop]) --> C[Loop stopped]
    """,
        },

        "sessionEnd": {
            "description": "Fires when an Agent or Cmd+K session ends.",
            "example": "Write a final audit log, clean up temporary files, or summarize what happened in the session.",
            "diagram": """
    flowchart LR
        A[Session active] --> B([sessionEnd]) --> C[Session closed]
    """,
        },

        "preToolUse": {
            "description": "Fires before any tool execution.",
            "example": "Check whether a tool call is allowed, enforce policy, or log the tool name before it runs.",
            "diagram": """
    flowchart LR
        A[Agent decides to use tool] --> B([preToolUse]) --> C[Tool runs]
    """,
        },

        "postToolUse": {
            "description": "Fires after a successful tool execution.",
            "example": "Record successful tool usage, inspect outputs, or update an audit trail.",
            "diagram": """
    flowchart LR
        A[Tool runs successfully] --> B([postToolUse]) --> C[Agent observes result]
    """,
        },

        "postToolUseFailure": {
            "description": "Fires after a failed tool execution.",
            "example": "Capture the error, notify the user, retry safely, or write failure details to logs.",
            "diagram": """
    flowchart LR
        A[Tool fails] --> B([postToolUseFailure]) --> C[Agent handles failure]
    """,
        },

        "beforeReadFile": {
            "description": "Fires before the agent reads a file.",
            "example": "Block reads of sensitive files such as .env, secrets.json, or private credentials.",
            "diagram": """
    flowchart LR
        A[Agent requests file read] --> B([beforeReadFile]) --> C[File read allowed / denied]
    """,
        },

        "afterFileEdit": {
            "description": "Fires after the agent edits a file.",
            "example": "Run a formatter, lint the changed file, or record which file was modified.",
            "diagram": """
    flowchart LR
        A[Agent edits file] --> B([afterFileEdit]) --> C[Post-edit processing]
    """,
        },

        "beforeShellExecution": {
            "description": "Fires before a shell command runs and can allow, deny, or ask for permission.",
            "example": "Deny dangerous commands like rm -rf, ask before installing packages, or allow safe test commands.",
            "diagram": """
    flowchart LR
        A[Agent prepares shell command] --> B([beforeShellExecution]) --> C[Command allowed / denied / ask]
    """,
        },

        "afterShellExecution": {
            "description": "Fires after a shell command finishes.",
            "example": "Log the command result, inspect exit codes, or collect test output.",
            "diagram": """
    flowchart LR
        A[Shell command finishes] --> B([afterShellExecution]) --> C[Agent receives command output]
    """,
        },

        "beforeMCPExecution": {
            "description": "Fires before an MCP tool runs and can allow, deny, or ask for permission.",
            "example": "Require approval before calling an external MCP service or block access to restricted MCP tools.",
            "diagram": """
    flowchart LR
        A[Agent prepares MCP call] --> B([beforeMCPExecution]) --> C[MCP call allowed / denied / ask]
    """,
        },

        "afterMCPExecution": {
            "description": "Fires after an MCP tool finishes.",
            "example": "Log the MCP tool result or audit which external system was accessed.",
            "diagram": """
    flowchart LR
        A[MCP tool finishes] --> B([afterMCPExecution]) --> C[Agent receives MCP result]
    """,
        },

        "subagentStart": {
            "description": "Fires before Cursor spawns a subagent or Task tool.",
            "example": "Track delegated work, limit which subagents can run, or log the subagent task description.",
            "diagram": """
    flowchart LR
        A[Agent delegates task] --> B([subagentStart]) --> C[Subagent runs]
    """,
        },

        "subagentStop": {
            "description": "Fires when a subagent completes, errors, or is aborted.",
            "example": "Collect subagent results, record failures, or merge subagent findings into a parent task log.",
            "diagram": """
    flowchart LR
        A[Subagent finishes / errors / aborts] --> B([subagentStop]) --> C[Parent agent receives result]
    """,
        },

        "beforeTabFileRead": {
            "description": "Fires before Tab inline completion reads a file.",
            "example": "Prevent inline completion from reading sensitive files or log which files are used for completion context.",
            "diagram": """
    flowchart LR
        A[Tab completion needs file context] --> B([beforeTabFileRead]) --> C[File read allowed / denied]
    """,
        },

        "afterTabFileEdit": {
            "description": "Fires after Tab inline completion edits a file.",
            "example": "Format the edited file, record the edit, or trigger lightweight validation.",
            "diagram": """
    flowchart LR
        A[Tab completion edits file] --> B([afterTabFileEdit]) --> C[Post-edit processing]
    """,
        },
    }
    return (CURSOR_HOOKS,)


@app.cell
def _(CURSOR_HOOKS, gw, mo):
    hook_name = gw.selected_nodes[0]
    hook_desc = CURSOR_HOOKS.get(hook_name, {}).get("description")
    hook_ex = CURSOR_HOOKS.get(hook_name, {}).get("example")
    hook_dia = CURSOR_HOOKS.get(hook_name, {}).get("diagram")

    mo.md(f'''
    # Event: {hook_name}

    > {hook_desc}

    ## Example
    {hook_ex}

    {mo.mermaid(hook_dia)}
    ''')

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Hooks in Our Setup
    """)
    return


@app.cell
def _(mo):
    mo.vstack([mo.mermaid('''
    flowchart TD
        hooks[Hooks]
        hook1([Prevent File Read])
        hook2([Python Lint])

        hooks --beforeReadFile--> hook1
        hooks --afterFileEdit--> hook2
    ''')], align="center")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Current Setup of Codex and Cursor

    Adding global or local skills from <https://skills.sh>
    ```bash
    $ npx skills add hashicorp/agent-skills # for terraform
    $ npx skills add aws/agent-toolkit-for-aws/skills # for cursor to enable aws-core skills
    ```

    Codex

    ```bash
    $ codex mcp add strands uvx strands-agents-mcp-server
    $ codex plugin marketplace add aws/agent-toolkit-for-aws
    ```

    Cursor

    1. add mcp servers config in `~/.cursor/mcp.json`
    2. add plugins with /plugins.

    configure plugin

    ```json
    {
      "mcpServers": {
        "aws": {
          "command": "uvx",
          "args": [
            "mcp-proxy-for-aws@latest",
            "https://aws-mcp.us-east-1.api.aws/mcp",
            "--metadata", "AWS_REGION=us-west-2"
          ]
        }
      }
    }
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Resources

    1. https://github.com/gitleaks/gitleaks: Scan codebase for credential and secret.
    2. https://github.com/semgrep/semgrep: Semantic Search for Codebases, identify coding style and provide proper feedback to agents.
    3. https://github.com/sverweij/dependency-cruiser: Maps internal Dependencies, agent can validate other dependent modules for regression tests when a module functionality changes.
    4. https://github.com/vladikk/modularity: Best practices to follow when implementing new features for proper modularity.

    5. https://lexler.github.io/augmented-coding-patterns/
    6. https://skills.sh
    7. https://docs.aws.amazon.com/agent-toolkit/latest/userguide/plugins.html
    """)
    return


if __name__ == "__main__":
    app.run()
