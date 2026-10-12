import tkinter as tk
from tkinter import messagebox, filedialog
import requests
from datetime import datetime


# =========================================================
# OLLAMA SETTINGS
# =========================================================

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:0.5b"


# =========================================================
# MEMORY
# =========================================================

conversation_history = []


# =========================================================
# DISCLAIMER
# =========================================================

DISCLAIMER = (
    "\n\nDisclaimer: This is an AI-generated educational "
    "response and not a medical diagnosis. "
    "It does not replace professional medical advice."
)


# =========================================================
# KNOWLEDGE BASE
# =========================================================

knowledge_base = {

    "Common Cold": {
        "keywords": [
            "sneezing",
            "sneeze",
            "runny nose",
            "stuffy nose",
            "congestion",
            "mild cough"
        ],
        "severity": "Mild",
        "advice": (
            "Rest, drink enough fluids, and use warm fluids "
            "for comfort. Monitor your symptoms."
        )
    },

    "Flu-like Illness": {
        "keywords": [
            "fever",
            "body ache",
            "body pain",
            "chills",
            "fatigue"
        ],
        "severity": "Moderate",
        "advice": (
            "Rest, drink enough fluids, and monitor your "
            "temperature and symptoms."
        )
    },

    "Migraine-like Headache": {
        "keywords": [
            "headache",
            "sensitivity to light",
            "sensitivity to sound"
        ],
        "severity": "Moderate",
        "advice": (
            "Rest in a quiet and dark environment and stay "
            "hydrated."
        )
    },

    "Indigestion": {
        "keywords": [
            "bloating",
            "heartburn",
            "indigestion"
        ],
        "severity": "Mild",
        "advice": (
            "Try smaller meals, avoid foods that trigger "
            "your symptoms, and stay hydrated."
        )
    },

    "Facial Skin Bumps": {
        "keywords": [
            "pimples",
            "small bumps",
            "face bumps",
            "facial bumps",
            "acne"
        ],
        "severity": "Mild",
        "advice": (
            "Keep the skin clean, avoid picking or squeezing the bumps, "
            "and avoid products that irritate the skin. "
            "If the bumps are painful, spreading, persistent, or worsening, "
            "consult a healthcare professional."
        )
    }
}


# =========================================================
# EMERGENCY KEYWORDS
# =========================================================

emergency_keywords = [

    "chest pain",
    "severe chest pressure",
    "difficulty breathing",
    "shortness of breath",
    "cannot breathe",
    "not breathing",
    "severe bleeding",
    "unconscious",
    "loss of consciousness",
    "fainted",
    "seizure",
    "stroke",
    "face drooping",
    "slurred speech",
    "sudden weakness",
    "overdose"
]


# =========================================================
# WARNING KEYWORDS
# =========================================================

warning_keywords = [

    "severe abdominal pain",
    "severe stomach pain",
    "persistent vomiting",
    "vomiting blood",
    "blood in stool",
    "confusion",
    "very high fever",
    "severe dehydration",
    "severe headache",
    "vision loss",
    "difficulty speaking"
]


# =========================================================
# EMERGENCY CHECK
# =========================================================

def check_emergency(symptoms):

    symptoms = symptoms.lower()

    for keyword in emergency_keywords:

        if keyword in symptoms:
            return True

    return False


# =========================================================
# WARNING CHECK
# =========================================================

def check_warning(symptoms):

    symptoms = symptoms.lower()

    for keyword in warning_keywords:

        if keyword in symptoms:
            return True

    return False


# =========================================================
# KNOWLEDGE BASE CHECK
# =========================================================

def check_knowledge_base(symptoms):

    symptoms = symptoms.lower()

    for condition, data in knowledge_base.items():

        for keyword in data["keywords"]:

            if keyword in symptoms:

                return {
                    "condition": condition,
                    "severity": data["severity"],
                    "advice": data["advice"]
                }

    return None


# =========================================================
# OLLAMA RESPONSE
# =========================================================

def ask_ollama(symptoms):

    prompt = f"""
You are a cautious medical information assistant.

User symptoms:
{symptoms}

Provide educational information only.

Rules:
1. Do not diagnose.
2. Give possible common causes only.
3. Give simple low-risk general self-care advice.
4. Do not prescribe medicines.
5. Do not give medication dosages.
6. Explain when professional medical help is needed.
7. If symptoms may be an emergency, recommend immediate
   professional medical attention.
8. Use simple English.
9. Include a disclaimer.

Format:

Possible causes:
- ...

Basic self-care:
- ...

When to seek medical help:
- ...

Disclaimer:
This is an AI-generated educational response and not a
medical diagnosis.
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=120
        )

        if response.status_code == 200:

            return response.json().get(
                "response",
                "No response received."
            ).strip()

        return "Ollama error:\n" + response.text

    except requests.exceptions.ConnectionError:

        return (
            "Could not connect to Ollama.\n\n"
            "Please make sure Ollama is running."
        )

    except requests.exceptions.Timeout:

        return (
            "Ollama took too long to respond.\n"
            "Please try again."
        )

    except Exception as e:

        return "Error: " + str(e)


# =========================================================
# MEDICAL ASSISTANT
# =========================================================

def medical_assistant(symptoms):

    symptoms = symptoms.strip()

    if not symptoms:

        return "Unknown", "Please enter your symptoms."

    # Emergency first

    if check_emergency(symptoms):

        response = """
🚨 EMERGENCY ALERT

The symptoms entered may indicate a potentially
serious or life-threatening situation.

Please seek immediate professional medical attention
or contact your local emergency service.

Do not rely on this AI assistant for emergency
medical decisions.
"""

        return "Severe", response + DISCLAIMER

    # Warning

    if check_warning(symptoms):

        response = """
⚠️ WARNING

The symptoms entered contain a warning sign that
may require prompt medical evaluation.

Please contact a qualified healthcare professional,
especially if the symptoms are severe, worsening,
persistent, or unusual.
"""

        return "Moderate-High", response + DISCLAIMER

    # Knowledge base

    result = check_knowledge_base(symptoms)

    if result:

        response = (
            "Possible condition:\n"
            + result["condition"]
            + "\n\n"
            + "Severity:\n"
            + result["severity"]
            + "\n\n"
            + "Basic self-care:\n"
            + result["advice"]
            + "\n\n"
            + "When to seek medical help:\n"
            + "Contact a healthcare professional if "
              "symptoms become severe, unusual, persistent, "
              "or get worse."
        )

        return result["severity"], response + DISCLAIMER

    # Qwen

    response = ask_ollama(symptoms)

    return "AI-Assessed", response


# =========================================================
# SAVE MEMORY
# =========================================================

def save_conversation(user_input, severity, response):

    conversation_history.append({

        "time": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "user": user_input,

        "severity": severity,

        "assistant": response
    })


# =========================================================
# EXPORT REPORT
# =========================================================

def export_report():

    if not conversation_history:

        messagebox.showinfo(
            "Report",
            "No conversation history available."
        )

        return

    filename = filedialog.asksaveasfilename(

        defaultextension=".txt",

        filetypes=[
            ("Text Files", "*.txt")
        ],

        initialfile="health_report.txt"
    )

    if not filename:

        return

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "AI-POWERED MEDICAL ASSISTANT\n"
        )

        file.write(
            "=" * 60 + "\n\n"
        )

        file.write(
            "Educational demonstration only.\n\n"
        )

        for item in conversation_history:

            file.write(
                "Time: "
                + item["time"]
                + "\n\n"
            )

            file.write(
                "User Symptoms:\n"
                + item["user"]
                + "\n\n"
            )

            file.write(
                "Severity:\n"
                + item["severity"]
                + "\n\n"
            )

            file.write(
                "Assistant Response:\n"
                + item["assistant"]
                + "\n"
            )

            file.write(
                "\n"
                + "-" * 60
                + "\n\n"
            )

        file.write(DISCLAIMER)

    messagebox.showinfo(
        "Report Exported",
        "Health report saved successfully."
    )


# =========================================================
# ANALYZE BUTTON
# =========================================================

def analyze_symptoms():

    symptoms = input_box.get(
        "1.0",
        tk.END
    ).strip()

    if not symptoms:

        messagebox.showwarning(
            "Input Required",
            "Please enter your symptoms."
        )

        return

    analyze_button.config(
        state=tk.DISABLED
    )

    window.update()

    severity, response = medical_assistant(
        symptoms
    )

    chat_box.config(
        state=tk.NORMAL
    )

    chat_box.insert(
        tk.END,
        "\nYou:\n",
        "user"
    )

    chat_box.insert(
        tk.END,
        symptoms
        + "\n\n"
    )

    chat_box.insert(
        tk.END,
        "Assistant:\n",
        "assistant"
    )

    chat_box.insert(
        tk.END,
        response
        + "\n\n"
    )

    chat_box.see(tk.END)

    chat_box.config(
        state=tk.DISABLED
    )

    severity_label.config(
        text="Severity: " + severity
    )

    save_conversation(
        symptoms,
        severity,
        response
    )

    input_box.delete(
        "1.0",
        tk.END
    )

    analyze_button.config(
        state=tk.NORMAL
    )


# =========================================================
# CLEAR CHAT
# =========================================================

def clear_chat():

    chat_box.config(
        state=tk.NORMAL
    )

    chat_box.delete(
        "1.0",
        tk.END
    )

    chat_box.config(
        state=tk.DISABLED
    )

    severity_label.config(
        text="Severity: Not analyzed"
    )


# =========================================================
# GUI
# =========================================================

window = tk.Tk()

window.title(
    "AI-Powered Medical Assistant - GPT 6"
)

window.geometry(
    "900x700"
)

window.minsize(
    800,
    600
)


# =========================================================
# TITLE
# =========================================================

title_label = tk.Label(

    window,

    text="🩺 AI-POWERED MEDICAL ASSISTANT",

    font=("Arial", 22, "bold"),

    pady=15
)

title_label.pack()


subtitle_label = tk.Label(

    window,

    text="Powered by Ollama • Qwen 2.5 0.5B",

    font=("Arial", 11)
)

subtitle_label.pack()


# =========================================================
# CHAT BOX
# =========================================================

chat_box = tk.Text(

    window,

    height=25,

    width=100,

    wrap=tk.WORD,

    font=("Arial", 11),

    state=tk.DISABLED
)

chat_box.pack(

    padx=20,

    pady=15,

    fill=tk.BOTH,

    expand=True
)


# =========================================================
# TEXT TAGS
# =========================================================

chat_box.tag_config(
    "user",
    font=("Arial", 11, "bold")
)

chat_box.tag_config(
    "assistant",
    font=("Arial", 11, "bold")
)


# =========================================================
# SEVERITY
# =========================================================

severity_label = tk.Label(

    window,

    text="Severity: Not analyzed",

    font=("Arial", 12, "bold"),

    pady=5
)

severity_label.pack()


# =========================================================
# INPUT
# =========================================================

input_box = tk.Text(

    window,

    height=4,

    font=("Arial", 11),

    wrap=tk.WORD
)

input_box.pack(

    padx=20,

    pady=10,

    fill=tk.X
)


# =========================================================
# BUTTON FRAME
# =========================================================

button_frame = tk.Frame(
    window
)

button_frame.pack(
    pady=10
)


# =========================================================
# ANALYZE BUTTON
# =========================================================

analyze_button = tk.Button(

    button_frame,

    text="Analyze Symptoms",

    command=analyze_symptoms,

    font=("Arial", 11, "bold"),

    padx=15,

    pady=8
)

analyze_button.grid(
    row=0,
    column=0,
    padx=5
)


# =========================================================
# CLEAR BUTTON
# =========================================================

clear_button = tk.Button(

    button_frame,

    text="Clear Chat",

    command=clear_chat,

    font=("Arial", 11),

    padx=15,

    pady=8
)

clear_button.grid(
    row=0,
    column=1,
    padx=5
)


# =========================================================
# REPORT BUTTON
# =========================================================

report_button = tk.Button(

    button_frame,

    text="Export Report",

    command=export_report,

    font=("Arial", 11),

    padx=15,

    pady=8
)

report_button.grid(
    row=0,
    column=2,
    padx=5
)


# =========================================================
# DISCLAIMER
# =========================================================

disclaimer_label = tk.Label(

    window,

    text=(
        "Educational demonstration only. "
        "Not a medical diagnosis or substitute "
        "for professional medical care."
    ),

    font=("Arial", 9),

    pady=8
)

disclaimer_label.pack()


# =========================================================
# START GUI
# =========================================================

window.mainloop()