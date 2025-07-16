# Teach Me Logic Plan – Project NEXI

---

## 📌 Assigned Task

**Engineer:** M Ehtesham Ul Hassan Malik  
**Task Title:** Teach Me Logic Plan  
**Goal:** Draft logic for how Nexi learns from user input.  
**Deadline:** 19/07/2025 (Saturday)  

### 📝 Task Description

Design the logic for how the robot learns from user-defined input.

**Steps:**
1. Design flow for user saying: _“This is a mobile phone”_ → system saves → confirms next time.
2. Handle confirmation, update, and overwrite behavior.
3. Show how this learning is saved and retrieved.

**Output:** Flowchart + pseudocode or brief write-up  
**Success Criteria:** Input → confirmation → storage → reuse logic clearly shown  
**Verification:** Diagram or pseudocode that covers normal + error cases

---

## Goal

Enable Nexi to intelligently respond to "teach me" inputs like:

> “This is a mobile phone.”

With the ability to:
- Confirm learning
- Store user-defined knowledge
- Handle duplicates or updates
- Recall information when asked later

---

## 🛠️ Tools Used

- ✅ **Draw.io** – Flowchart creation  
- ✅ **Markdown** – Documentation  
- ✅ **Pseudocode** – Logic structuring  
- ✅ **Regex Patterns** – For intent detection

---

## System Flow Summary

- User provides input: _“This is a fan”_  
- Nexi detects teachable pattern  
- Nexi asks for confirmation  
- If approved:
  - Saves label and description in memory
  - If label already exists, prompts for overwrite
- If denied:
  - Discards the learning attempt

---

## Pseudocode Logic

```python
Function handle_user_input(user_input):

    If input_matches_teach_me_pattern(user_input):

        Extract label_from_input (e.g., "mobile", "dog", "car")

        Ask user: "Should I remember this as 'label_from_input'?"

        If user_response == "Yes":

            If label_already_exists(label_from_input):

                Ask user: "You already said this is 'old_label'. Do you want to update it to 'label_from_input'?"

                If user_response == "Yes":
                    Update memory with new label
                    Say: "Got it! I’ve updated it to 'label_from_input'."
                Else:
                    Say: "Okay, I’ll keep the original label."

            Else:
                Save new label to memory
                Say: "Got it! I’ll remember that."

        Else:
            Say: "Okay, I won’t save it."

    Else:
        Pass input to regular Q&A logic

```
## Teachable Input Patterns
```python
Function input_matches_teach_me_pattern(text):

    Define patterns:
        - "this is a ..."
        - "that is a ..."
        - "remember this is ..."
        - "nexi, remember this is ..."
        - "learn this: this is ..."
        - "it's called a ..."

    For each pattern in patterns:
        If text matches pattern:
            Return True

    Return False
```
## Example Scenario
User: "This is a flower."
Nexi: "Should I remember this as 'flower'?"
User: "Yes"
Nexi: "Got it! I’ll remember that."

Later...
User: "What is this?"
Nexi: "That’s a flower. You taught me that."

## Outcome
- Pattern-based detection for teaching
- Confirmation and overwrite logic
- Memory structure supports long-term reuse
- Ready for integration with JSON memory and speech modules

