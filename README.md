# Aura
V01 of a virtual personal assistant

Here’s a README documentation template for your Aura personal assistant project:

---

# Aura - Personal Assistant

Aura is a voice-activated personal assistant inspired by J.A.R.V.I.S from Iron Man. It allows you to create notepad files, maintain a to-do list in Notion, and perform other tasks with simple voice commands. Aura is designed to work offline and can be integrated with various APIs for enhanced functionality.

## Features

- **Voice Recognition**: Uses speech recognition to capture and interpret voice commands.
- **Text-to-Speech**: Provides spoken feedback using text-to-speech technology.
- **Create Notepad Files**: Quickly create and save text files on your system with voice commands.
- **Maintain To-Do List in Notion**: Manage your tasks in Notion by adding new items to your to-do list.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

Ensure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/)
- [Node.js](https://nodejs.org/en/download/) (for packaging with Electron)

### Clone the Repository

```bash
git clone https://github.com/yourusername/aura-assistant.git
cd aura-assistant
```

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Install Node.js Dependencies (for Electron)

```bash
npm install
```

### Setting Up Notion Integration

1. Create a Notion integration and note down the integration token and database ID. [Notion API Documentation](https://developers.notion.com/docs/getting-started)
2. Create a `.env` file in the project directory and add the following:
   ```env
   NOTION_TOKEN=your_notion_integration_token
   NOTION_DATABASE_ID=your_notion_database_id
   ```

### Run the Application

To run the application:

```bash
python aura.py
```

If packaging as a desktop application with Electron:

```bash
npm start
```

## Configuration

### Notion Integration

Ensure your Notion integration token and database ID are correctly set in the `.env` file.

### Text-to-Speech

The text-to-speech functionality uses `pyttsx3`, which requires no additional configuration. However, you can customize the voice and rate directly in the code if needed.

## Usage

1. **Starting Aura**: Run the application with the provided command.
2. **Voice Commands**:
   - "Create a notepad file": Aura will prompt you to provide a filename and content, and then create the file.
   - "Add a task to Notion": Aura will add a new task to your Notion to-do list.

### Example Commands

- "Create a notepad file named `tasks` with the content `Buy groceries`."
- "Add `Finish the Aura project` to my to-do list in Notion."

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.

---
