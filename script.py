import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


def solve_math(expression):

    expr = expression.strip()
    replacements = {
        '×': '*', '·': '*', 'x': '*', 'X': '*',
        '÷': '/', '–': '-', '−': '-', '—': '-'
    }
    
    for old, new in replacements.items():
        expr = expr.replace(old, new)
    
    # Remove equals sign and anything after it
    if '=' in expr:
        expr = expr.split('=')[0].strip()
    
    # Only allow digits, operators, spaces, and parentheses
    expr = re.sub(r'[^\d+\-*/().\s]', '', expr)
    expr = re.sub(r'\s+', ' ', expr).strip()
    
    try:
        result = eval(expr)
        return int(round(result))
    except Exception:
        return None


def zetamac_solver_optimized():
    
    # Setup Firefox
    options = Options()
    driver = webdriver.Firefox(options=options)
    
    try:
        print("Starting Zetamac solver...")
        
        # Navigate to the site
        driver.get("https://arithmetic.zetamac.com/")
        time.sleep(2)
        
        # Start the game
        start_btn = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        start_btn.click()
        print("Game started.")
        time.sleep(2)
        
        solved_count = 0
        last_problem = ""
        start_time = time.time()
        
        # The game runs for 2 minutes, so we'll run for 125 seconds
        while time.time() - start_time < 125:
            try:
                # Get the current problem from the span.problem element
                problem_element = driver.find_element(By.CSS_SELECTOR, "span.problem")
                current_problem = problem_element.text.strip()
                
                # If this is a new problem
                if current_problem and current_problem != last_problem:
                    # Add an equals sign since the element doesn't include it
                    problem_with_equals = current_problem + " ="
                    
                    # Solve the problem
                    answer = solve_math(problem_with_equals)
                    if answer is None:
                        print(f"Could not solve: {current_problem}")
                        continue
                    
                    print(f"Solving: {current_problem} = {answer}")
                    
                    # Find the input field
                    input_field = driver.find_element(By.CSS_SELECTOR, "input.answer")
                    
                    # Clear the field and enter the answer
                    input_field.clear()
                    input_field.send_keys(str(answer))
                    input_field.send_keys(Keys.ENTER)
                    
                    solved_count += 1
                    last_problem = current_problem
                    print(f"Answered. Total solved: {solved_count}")
                    
                    # A very short delay to allow the game to process the answer
                    time.sleep(0.05)
                else:
                    # Wait for a new problem to appear
                    time.sleep(0.02)
                    
            except StaleElementReferenceException:
                # The element became stale, which is expected. Continue the loop.
                continue
            except Exception as e:
                # Check if the game has ended by looking for score display text
                try:
                    body_text = driver.find_element(By.TAG_NAME, "body").text
                    if "game over" in body_text.lower() or "final score" in body_text.lower():
                        print("Game has ended.")
                        break
                except:
                    pass
                
                # If not game over, continue trying
                time.sleep(0.1)
                continue
        
        print(f"\nSession completed. Total problems solved: {solved_count}")
        
        # Wait to allow the final score to be visible
        time.sleep(5)
        try:
            # Try to get the final score from the page
            score_element = driver.find_element(By.CSS_SELECTOR, "span.correct")
            final_score = score_element.text
            print(f"Final score: {final_score}")
        except:
            print("Could not retrieve the final score from the page.")
        
    except Exception as e:

        print(f"An error occurred: {e}")
        
    finally:
        print("finished.")
        # driver.quit()

if __name__ == "__main__":
    zetamac_solver_optimized()
