# AI-POWERED MEDICAL ASSISTANT

## 1. Abstract

The AI-Powered Medical Assistant is a Python-based educational application that uses Ollama and the Qwen 2.5 0.5B language model to provide general health information based on user-entered symptoms.

The system combines a predefined medical knowledge base with an AI language model. Known symptoms are matched with common conditions and basic self-care information. Unknown symptoms are sent to the Qwen model through the Ollama API for a contextual response.

The system also includes severity classification, emergency symptom detection, conversation memory, safety instructions, and health report generation. Emergency-related symptoms are checked before the AI model is used so that potentially serious cases receive an immediate warning.

The application is intended only for educational and demonstration purposes and does not provide medical diagnosis or replace professional medical care.

---

## 2. Introduction

Artificial Intelligence can be used to develop conversational systems that understand natural-language user input. In healthcare-related applications, AI can provide general educational information about symptoms and encourage users to seek professional medical care when appropriate.

This project demonstrates an AI-powered medical assistant using Python, Ollama, and the Qwen 2.5 0.5B model.

The system accepts symptoms from a user, checks a predefined knowledge base, identifies potentially serious symptoms, assigns a severity level, and generates an educational response.

---

## 3. Problem Statement

Users may enter symptoms using natural language, making it difficult for a simple rule-based program to understand every possible input.

The objective is to develop a small AI-powered assistant that can:

- Accept symptom descriptions.
- Match common symptoms with a knowledge base.
- Suggest possible common conditions.
- Provide basic self-care information.
- Classify symptom severity.
- Detect emergency warning signs.
- Use an AI model for unknown symptoms.
- Maintain conversation history.
- Generate a health interaction report.

---

## 4. Objectives

The main objectives are:

1. To develop a Python-based medical information assistant.
2. To integrate the Qwen model through Ollama.
3. To create a knowledge base for common symptoms.
4. To classify cases into severity levels.
5. To detect potentially serious emergency symptoms.
6. To provide basic and low-risk self-care information.
7. To maintain conversation history.
8. To generate a text-based health report.
9. To include safety warnings and medical disclaimers.
10. To demonstrate the use of an LLM in a healthcare-related educational application.

---

## 5. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Ollama | Local AI model execution |
| Qwen 2.5 0.5B | Language model |
| Requests | API communication |
| VS Code | Development environment |
| Text file | Health report storage |

---

## 6. System Requirements

### Hardware

- Computer or laptop
- Minimum 8 GB RAM recommended
- Sufficient storage for the software and AI model
- Internet connection for initial software/model installation

### Software

- Windows operating system
- Python
- VS Code
- Ollama
- Qwen 2.5 0.5B model

---

## 7. System Architecture

The system follows the architecture below:

User
↓
Symptom Input
↓
Safety Check
↓
Emergency Detection
↓
Knowledge Base
↓
Severity Classification
↓
Qwen AI Model
↓
Response Generation
↓
Conversation Memory
↓
Health Report

Emergency symptoms are processed before normal AI generation.

---

## 8. Methodology

The application follows several stages.

### Stage 1: User Input

The user enters symptoms using natural language.

Example:

"I have fever and body pain."

### Stage 2: Safety Check

The program checks the input for potentially serious symptoms.

### Stage 3: Emergency Detection

The system searches for emergency-related keywords such as difficulty breathing, chest pain, severe bleeding, loss of consciousness, and other critical warning signs.

### Stage 4: Knowledge Base Matching

If the symptoms match the predefined knowledge base, the system returns a predefined educational response.

### Stage 5: AI Processing

If the symptoms are not found in the knowledge base, the application sends the input to Qwen through the Ollama API.

### Stage 6: Severity Classification

The application assigns a severity category such as Mild, Moderate, Moderate-High, or Severe depending on the detected symptoms.

### Stage 7: Memory

The system stores the user's input, severity level, timestamp, and assistant response.

### Stage 8: Report Generation

The stored conversation can be exported into a text-based health report.

---

## 9. Knowledge Base

The knowledge base contains common conditions and related keywords.

Examples include:

### Common Cold

Keywords:

- sneezing
- runny nose
- congestion
- mild cough

Severity:

Mild

### Flu-Like Illness

Keywords:

- fever
- body ache
- chills
- fatigue

Severity:

Moderate

### Migraine-Like Headache

Keywords:

- headache
- sensitivity to light
- sensitivity to sound

Severity:

Moderate

### Indigestion

Keywords:

- bloating
- heartburn
- indigestion

Severity:

Mild

---

## 10. Severity Classification

The application uses severity categories to communicate the seriousness of the entered symptoms.

### Mild

Used for common symptoms that may often be managed with basic self-care and monitoring.

### Moderate

Used when symptoms may require closer monitoring or professional medical advice.

### Moderate-High

Used for warning symptoms that may require prompt medical evaluation.

### Severe

Used when potentially emergency-related symptoms are detected.

---

## 11. Emergency Detection

Emergency detection is an important safety feature.

The system checks for potentially serious symptoms before sending normal queries to the AI model.

Examples include:

- chest pain
- difficulty breathing
- severe bleeding
- loss of consciousness
- seizure
- stroke warning signs
- overdose

When an emergency keyword is detected, the system displays an emergency alert and recommends immediate professional medical attention.

---

## 12. AI Integration

The Qwen 2.5 0.5B model is executed locally using Ollama.

Python communicates with the Ollama API using the Requests library.

The basic communication flow is:

Python Application
↓
Ollama API
↓
Qwen 2.5 0.5B
↓
Generated Response
↓
Python Application

The model is instructed to provide educational information rather than a medical diagnosis.

---

## 13. Conversation Memory

The application maintains a conversation history using a Python list.

Each interaction contains:

- Timestamp
- User symptoms
- Severity
- Assistant response

This allows the application to preserve the interaction history during the current program session.

---

## 14. Health Report Generation

The application provides a report command.

When the user enters:

`report`

the application creates:

`health_report.txt`

The report contains:

- Interaction time
- User symptoms
- Severity
- Assistant response
- Medical disclaimer

---

## 15. Safety Features

The application includes several safety mechanisms.

1. Emergency symptoms are checked before normal AI processing.
2. The AI is instructed not to provide a diagnosis.
3. The AI is instructed not to prescribe medicines.
4. Medication dosages are not automatically generated.
5. Users are advised to contact healthcare professionals when symptoms are serious or worsening.
6. Every response includes a disclaimer.
7. Emergency situations are directed toward immediate professional care.

---

## 16. Implementation

The application is implemented using Python functions.

Important functions include:

### check_emergency()

Detects potentially emergency-related symptoms.

### check_warning()

Detects warning symptoms requiring prompt evaluation.

### check_knowledge_base()

Matches user symptoms against predefined conditions.

### ollama_response()

Sends unknown symptoms to Qwen through Ollama.

### medical_assistant()

Combines safety checks, knowledge-base matching, and AI processing.

### save_conversation()

Stores interaction history.

### export_report()

Creates the health report.

---

## 17. Test Cases

| Test Case | Input | Expected Result |
|---|---|---|
| 1 | Sneezing and runny nose | Mild |
| 2 | Fever and body ache | Moderate |
| 3 | Headache and light sensitivity | Moderate |
| 4 | Severe stomach pain | Moderate-High |
| 5 | Chest pain and difficulty breathing | Severe / Emergency |
| 6 | Unknown symptoms | Qwen response |
| 7 | `report` | Health report generated |
| 8 | `exit` | Program closes |

---

## 18. Results

The application successfully demonstrates:

- Symptom input processing.
- Knowledge-base matching.
- Severity classification.
- Emergency detection.
- Qwen integration.
- Conversation history.
- Health report generation.
- Safety disclaimers.

The system can provide different responses depending on the user's input.

---

## 19. Advantages

- Simple user interface.
- Uses a local AI model.
- Does not require an external AI API key.
- Provides contextual AI responses for unknown symptoms.
- Includes emergency detection.
- Stores interaction history.
- Generates a report.
- Demonstrates practical use of Python and LLM technology.

---

## 20. Limitations

The system has several limitations.

1. Keyword matching cannot understand every medical situation.
2. The Qwen model may generate incorrect or incomplete information.
3. The system cannot perform physical examinations.
4. The system cannot measure vital signs.
5. The system cannot confirm a medical diagnosis.
6. The system should not be used for emergency decision-making.
7. The current memory is session-based.
8. The knowledge base contains only a limited number of conditions.

---

## 21. Future Enhancements

Future versions could include:

- A graphical user interface.
- Voice input.
- Multilingual support.
- Larger medical knowledge bases.
- Database-based patient history.
- Secure user authentication.
- Retrieval-Augmented Generation (RAG).
- Medical-document analysis.
- Better contextual conversation memory.
- Structured PDF health reports.
- Doctor or hospital directory integration.
- More advanced safety and validation mechanisms.

---

## 22. Conclusion

The AI-Powered Medical Assistant demonstrates how Python, a local LLM, and rule-based safety mechanisms can be combined to create an educational healthcare assistant.

The system combines a predefined knowledge base with the Qwen language model to provide general health information. Emergency detection is performed before normal AI processing, and safety disclaimers are included in the responses.

The project provides practical experience in Python programming, API communication, local LLM integration, natural-language processing, rule-based systems, conversation memory, and report generation.

The application is intended strictly as an educational demonstration and should not be used as a substitute for professional medical diagnosis or treatment.

---

## 23. Medical Disclaimer

This project is an academic demonstration of an AI-powered conversational system. It does not provide medical diagnosis, treatment, or professional medical advice. Users should consult qualified healthcare professionals for medical concerns. Potential emergencies should be handled through appropriate emergency medical services rather than this application.