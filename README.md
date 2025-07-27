Zetamac Arithmetic Solver

This project contains a Python script that uses the Selenium library to automatically play the arithmetic game on Zetamac. The script can start a game, read the problems, calculate the answers, and submit them in real-time.
Features

    Automated Gameplay: Navigates to the Zetamac website and starts a new game automatically.

    Real-time Problem Solving: Reads arithmetic problems from the screen as they appear.

    Safe Expression Evaluation: Safely parses and solves expressions containing addition, subtraction, multiplication, and division.

    High-Speed Answering: Enters the calculated answer and submits it to proceed to the next problem.

    Game Completion: Runs for the duration of the game (approximately 2 minutes) and attempts to read the final score.

How It Works

The script launches a Firefox browser instance controlled by Selenium. It navigates to the game page, clicks the "Start" button, and then enters a loop. In each iteration of the loop, it:

    Finds the Problem: It locates the HTML element containing the current arithmetic problem.

    Parses and Solves: The text of the problem is passed to a helper function, solve_math, which cleans the string, replaces various operator symbols (like × and –) with standard ones (* and -), and uses eval() to compute the result. This evaluation is restricted to basic arithmetic to prevent security risks.

    Submits the Answer: The script finds the answer input field, types the calculated result, and simulates pressing the "Enter" key.

    Handles State Changes: It keeps track of the last problem solved to avoid re-submitting answers for the same problem. It also includes error handling for when the page updates and elements become "stale."

    Finishes the Game: The loop continues until the game's time limit is reached, after which it waits briefly and attempts to display the final score.

Requirements

    Python 3.6+

    Mozilla Firefox browser

    geckodriver for Firefox

Installation

    Clone the repository:

    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name

    Install the required Python libraries:

    pip install selenium

    Install geckodriver:

        Download the appropriate geckodriver for your operating system from the official releases page.

        Extract the executable and place it in a directory that is included in your system's PATH. (On macOS/Linux, a common location is /usr/local/bin/).

Usage

Once the setup is complete, you can run the solver from your terminal:

python zetamac_solver.py

The script will open a new Firefox window and begin solving the problems. The progress will be printed to the console.
Disclaimer

This script is intended for educational purposes to demonstrate web automation with Selenium. Please be mindful of the terms of service of any website you use automation on. The creators of this script are not responsible for any misuse.
