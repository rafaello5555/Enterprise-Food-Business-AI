import os
from speech_to_text import speech_to_text

file_name = "crowd-talking-1"

def stt_testing(file):
    # Correct full path based on the actual folder structure
    full_path = os.path.join(os.getcwd(), "test_speech", file + ".wav")

    # Check if the file exists
    if not os.path.isfile(full_path):
        print("❌ File not found:", full_path)
        return

    print("✅ Found file at:", full_path)
    transcript = speech_to_text(full_path)
    print("📝 The transcript from '" + file + "' is:\n" + transcript)

# Run the function
stt_testing(file_name)
