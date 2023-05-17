import time
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 typing_game.py <path to file>")
        return

    # Read text from a file
    with open(sys.argv[1], 'r') as file:
        lines = file.readlines()

    # Prepare the game
    text = ''.join(lines)
    lines = text.splitlines()

    # Display text and prompt user to start typing
    print("Type the following text:")
    input("Press Enter when ready to start...")

    # Start the timer
    start_time = time.time()

    # Game loop
    correct_words_count = 0
    total_lines = len(lines)
    total_words = 0
    for line in lines:
        # Display the line and prompt for user input
        print()
        print(line)
        user_input = input()

        user_input_words = user_input.split(' ')
        line_words = line.split(' ')
        total_words += len(line_words)
        correct_words = [True for i, x in enumerate(user_input_words) if x == line_words[i]]
        correct_words_count += len(correct_words)


    # Calculate typing speed and accuracy
    end_time = time.time()
    elapsed_time = end_time - start_time
    typing_speed = (correct_words_count / elapsed_time) * 60  # WPM
    accuracy = (correct_words_count / total_words) * 100

    # Display results
    print("\nGame Over!")
    print(f"Your typing speed: {typing_speed:.2f} WPM")
    print(f"Your accuracy: {accuracy: .2f}%")

if __name__ == '__main__':
    main()
