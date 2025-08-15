# Java Project Template - HyperFocus Zone Edition

## Overview
A production-ready Java 8 project template configured for VS Code with Maven support.

## Features
✅ **Java 8 OpenJDK** - Configured with your local installation
✅ **VS Code Integration** - Optimized settings for Java development
✅ **Maven Build System** - Standard project structure
✅ **JUnit Testing** - Ready-to-use test framework
✅ **GitHub Actions CI/CD** - Automated builds and testing

## Project Structure
```
JavaProjectTemplate/
├── src/
│   ├── main/
│   │   └── java/
│   │       └── com/
│   │           └── hyperfocus/
│   │               └── example/
│   │                   └── App.java
│   └── test/
│       └── java/
│           └── com/
│               └── hyperfocus/
│                   └── example/
│                       └── AppTest.java
├── .vscode/
│   ├── settings.json
│   └── launch.json
├── .github/
│   └── workflows/
│       └── ci.yml
├── pom.xml
├── README.md
└── .gitignore
```

## Quick Start
1. Copy this template to your project location
2. Update package names in `pom.xml` and source files
3. Run `mvn clean compile` to build
4. Run `mvn test` to execute tests
5. Use F5 in VS Code to debug

## Maven Commands
- `mvn compile` - Compile the project
- `mvn test` - Run tests
- `mvn package` - Create JAR file
- `mvn clean` - Clean build artifacts

## VS Code Features
- **IntelliSense** - Code completion and suggestions
- **Debugging** - Full debugging support with breakpoints
- **Testing** - Integrated test runner
- **Refactoring** - Automated code improvements
- **Code Actions** - Quick fixes and imports organization
