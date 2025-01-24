# ClickUp CLI 🚀

## Overview

The ClickUp CLI tool allows you to interact with your ClickUp tasks directly
from the terminal. I built this tool because I enjoy working with terminals
and want to make task management more accessible for terminal enthusiasts.
You can view tasks with an intuitive and clean command structure.

---

## Features

- View tasks assigned to you.
- Default filtering for "in progress" and "planned" tasks.
- Option to filter tasks by one or more statuses using a comma-separated list.
- Displays tasks in a detailed, color-coded format, including task status, name,
  URL, and due date.

---

## Installation

### Build and Install

1. Clone the repository:

   ```bash
   git clone git@github.com:osvald0/clickup_cli.git
   cd clickup_cli
   ```

2. Install dependencies using Poetry:

   ```bash
   poetry install
   ```

3. Build and install the CLI tool:

   ```bash
   poetry build
   pip install dist/*.whl
   ```

---

## Development Setup

1. Clone the repository:

   ```bash
   git clone git@github.com:osvald0/clickup_cli.git
   cd clickup_cli
   ```

2. Install dependencies:

   ```bash
   poetry install
   ```

3. Activate the virtual environment:

   ```bash
   poetry shell
   ```

4. Run the CLI tool in development mode:

   ```bash
   poetry run clickup-cli tasks view
   ```

---

## Usage

### Managing Tasks

#### Viewing Tasks

By default, the CLI fetches tasks with "in progress" and "planned" statuses and
displays them in a detailed, color-coded format:

```bash
poetry run clickup-cli tasks view
```

Example Output:

```plaintext
Found 2 tasks assigned to you:
- [in progress] Build Feature A (ID: abc123xyz)
  URL: https://app.clickup.com/t/abc123xyz
  Due Date: 2025-02-01 12:00:00

- [planned] Research Module B (ID: def456uvw)
  URL: https://app.clickup.com/t/def456uvw
  Due Date: 2025-02-10 18:00:00
```

##### Filter by Specific Status

You can filter tasks by a specific status using the `--status` option:

```bash
poetry run clickup-cli tasks view --status "to do"
```

##### Filter by Multiple Statuses

Use a comma-separated list to filter tasks by multiple statuses:

```bash
poetry run clickup-cli tasks view --status "in progress,planned"
```

---

#### Opening a Link from the Terminal

##### On macOS

`open <URL>`

##### On Linux

`xdg-open <URL>`

##### On Windows (Not tested 🪦)

`start <URL>`

##### Notes

- These commands will open the URL in the default web browser set on your system.
- Ensure the URL starts with `http://` or `https://` to avoid errors.

---

## Testing (❌ Pending - No tests yet!)

1. Run unit tests:

   ```bash
   pytest
   ```

2. Add new tests in the `tests/` directory to validate new functionality.

---

## Contribution

Feel free to fork the repository, make improvements, and create a pull request!
Suggestions and enhancements are welcome.

---

## Roadmap

Pending to define... 🤔

## License

GPL v3
