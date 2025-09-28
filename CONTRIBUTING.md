# 🤝 Contributing to Threat Detection System

Thanks for your interest in contributing! This project is a modular, production-grade ML pipeline for cybersecurity threat detection. We welcome improvements, bug fixes, and new features.

---

## 🧭 Project Philosophy

- **Modularity**: Each component should be independently testable and replaceable.
- **Clarity**: Code must be well-documented and readable.
- **Automation**: CI/CD, containerization, and orchestration are first-class citizens.
- **Security**: Handle sensitive data responsibly and follow best practices.

---

## 🛠️ Getting Started

1. Fork the repository
2. Clone your fork:  
   `git clone https://github.com/yourusername/threat-detection-system.git`
3. Install dependencies:  
   `make install`
4. Run tests:  
   `make test`

---

## 🧪 Testing Guidelines

- Use `pytest` for all tests
- Place tests in the `tests/` directory
- Ensure coverage for new features
- Run `pytest tests/` before submitting

---

## 📦 Code Standards

- Follow PEP8 for Python
- Use docstrings for all functions
- Keep functions small and focused
- Prefer pure functions for feature engineering and detection logic

---

## 🚀 Submitting Changes

1. Create a new branch:  
   `git checkout -b feature/my-feature`
2. Commit with clear messages:  
   `git commit -m "Add threat scoring module"`
3. Push and open a pull request
4. Describe your changes and link related issues

---

## 📋 Issue Reporting

- Use GitHub Issues for bugs, enhancements, or questions
- Include steps to reproduce and expected behavior
- Tag with appropriate labels (e.g., `bug`, `enhancement`, `question`)

---

## 🧠 Contributor Roles

- **Core Maintainers**: Review and merge PRs, manage releases
- **Collaborators**: Submit features, fix bugs, improve docs
- **Reviewers**: Provide feedback on PRs and architecture

---

## 📄 License

By contributing, you agree that your code will be licensed under the MIT License.
