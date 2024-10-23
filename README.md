# MiniGit: A Simplified Git Implementation in Python

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [1. Initialize a Repository (`git init`)](#1-initialize-a-repository-git-init)
  - [2. Add Files to the Index (`git add`)](#2-add-files-to-the-index-git-add)
  - [3. Commit Changes (`git commit`)](#3-commit-changes-git-commit)
- [Example Workflow](#example-workflow)
- [Project Structure](#project-structure)
- [Understanding the Code](#understanding-the-code)
- [Limitations](#limitations)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

**MiniGit** is a simplified version of Git implemented in Python. It demonstrates the core concepts of version control systems by allowing you to initialize a repository, add files, and commit changes. This project is intended for educational purposes to help understand how Git works under the hood.

## Features

- **Initialize a Repository**: Create a new MiniGit repository.
- **Add Files**: Add files to the staging area (index).
- **Commit Changes**: Commit staged changes with a message.
- **Object Storage**: Store file contents and commits as hashed objects.

## Prerequisites

- **Python 3.x**: Ensure you have Python 3 installed on your system.
- **Basic Knowledge of Git**: Familiarity with Git concepts will help in understanding MiniGit.

## Installation

1. **Clone the Repository** (Optional):

   If you're accessing this code from a repository, you can clone it:

   ```bash
   git clone https://github.com/MayankShrivastava17/minigit.git
   cd minigit
   ```

## Usage

### 1. Initialize a Repository (`git init`)

To start using MiniGit, you need to initialize a repository. This creates a `.minigit` directory in your current working directory, which will store all MiniGit data.

**Example:**

```python
from minigit import MiniGit

# Initialize the MiniGit repository
repo = MiniGit()
repo.init()
```

**Output:**

```
Initialized empty MiniGit repository in .minigit
```

### 2. Add Files to the Index (`git add`)

Adding files stages them for the next commit. MiniGit will hash the content of the file and store it in the `.minigit/objects` directory.

**Example:**

First, create a sample file to add:

```bash
echo "Hello, MiniGit!" > test.txt
```

Now, add the file using MiniGit:

```python
repo.add("test.txt")
```

**Output:**

```
Added file test.txt
```

### 3. Commit Changes (`git commit`)

Commit the staged changes with a descriptive message. This creates a commit object that captures the state of the index at that point in time.

**Example:**

```python
repo.commit("Initial commit")
```

**Output:**

```
Committed with message: Initial commit
Commit hash: a1b2c3d4e5f6...
```

## Example Workflow

Below is a step-by-step example of using MiniGit to track changes in a project.

**1. Initialize the Repository**

```python
from minigit import MiniGit

repo = MiniGit()
repo.init()
```

**2. Create and Add a File**

Create a new file `hello.txt`:

```bash
echo "Hello, World!" > hello.txt
```

Add the file to the staging area:

```python
repo.add("hello.txt")
```

**3. Commit the Changes**

```python
repo.commit("Add hello.txt")
```

**4. Modify the File and Commit Again**

Make changes to `hello.txt`:

```bash
echo "This is an update." >> hello.txt
```

Add and commit the changes:

```python
repo.add("hello.txt")
repo.commit("Update hello.txt")
```

**5. Check the `.minigit/objects` Directory**

List the contents of the objects directory:

```bash
ls .minigit/objects
```

You will see hashed files representing the stored objects.

## Project Structure

```
your_project/
├── minigit.py
├── test.txt
├── hello.txt
└── .minigit/
    ├── index
    └── objects/
        ├── <file_hashes>
        └── <commit_hashes>
```

- `minigit.py`: The MiniGit class implementation.
- `test.txt`, `hello.txt`: Sample files you're tracking.
- `.minigit/`: Directory storing MiniGit data.
  - `index`: Tracks the staging area.
  - `objects/`: Stores hashed file contents and commits.

## Understanding the Code

Here's a breakdown of how MiniGit works internally.

### The `MiniGit` Class

```python
class MiniGit:
    def __init__(self, repo_dir=".minigit"):
        # Initialization code
```

- **Initialization**: Sets up the repository directory and creates necessary subdirectories and files.

### Hashing Objects

```python
def _hash_object(self, data):
    return hashlib.sha1(data.encode()).hexdigest()
```

- **Purpose**: Generates a SHA-1 hash of the given data, similar to how Git hashes objects.

### Index Management

```python
def _write_index(self, index_data):
    # Writes the index to a file

def _read_index(self):
    # Reads the index from a file
```

- **Index File**: Acts as the staging area, tracking files added before committing.

### Adding Files

```python
def add(self, file_path):
    # Adds a file to the index
```

- **Process**:
  - Reads the file content.
  - Hashes the content and stores it in `objects/`.
  - Updates the index with the file path and its hash.

### Committing Changes

```python
def commit(self, message):
    # Commits the current state of the index
```

- **Process**:
  - Reads the current index.
  - Creates a commit object containing the index and the commit message.
  - Hashes and stores the commit object in `objects/`.

## Limitations

- **No Branching**: Does not support branches or merging.
- **No Diffs**: Cannot show differences between commits.
- **No File Removal**: Does not track file deletions.
- **No Remote Repositories**: Cannot push or pull from remote locations.
- **Limited Error Handling**: Basic validation is implemented.

## Future Enhancements

- **Branch Support**: Implement branching and merging capabilities.
- **Diff Tool**: Add functionality to compare different commits.
- **File Deletion Tracking**: Allow tracking of removed files.
- **Remote Operations**: Enable pushing to and pulling from remote repositories.
- **User Interface**: Develop a command-line interface (CLI) for easier interaction.

## Contributing

Contributions are welcome! If you'd like to contribute to MiniGit, please follow these steps:

1. **Fork the Repository**
2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Commit Your Changes**
   ```bash
   git commit -m "Add YourFeature"
   ```
4. **Push to Your Fork**
   ```bash
   git push origin feature/YourFeature
   ```
5. **Open a Pull Request**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Note**: MiniGit is a simplified educational tool and is not intended to replace Git for production use.
