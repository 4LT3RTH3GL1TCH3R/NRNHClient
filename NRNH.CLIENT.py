# -*- coding: utf-8 -*-
import requests
import os
import sys
import platform
import random
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama
init()

# Constants for colors
INFO = Fore.CYAN + Style.BRIGHT
SUCCESS = Fore.GREEN + Style.BRIGHT
ERROR = Fore.RED + Style.BRIGHT
RESET = Style.RESET_ALL

LOG_FILE = "closure_log.txt"

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def pause():
    input(f"\n{INFO}Press Enter to continue...{RESET}")

def log_closure(reason):
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()}: {reason}\n")

def get_discord_user_info(user_id):
    url = f"https://discord.com/api/v9/users/{user_id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            user_data = response.json()
            username = user_data.get('username', 'Unknown')
            avatar_id = user_data.get('avatar', 'Unknown')
            avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.png"
            bio = "Bio data not available without authentication"
            pronouns = "Pronouns not available without authentication"

            print(f"{SUCCESS}Username: {username}{RESET}")
            print(f"{SUCCESS}Avatar URL: {avatar_url}{RESET}")
            print(f"{INFO}Bio: {bio}{RESET}")
            print(f"{INFO}Pronouns: {pronouns}{RESET}")
        else:
            print(f"{ERROR}Failed to fetch user info. Status code: {response.status_code}{RESET}")
    except Exception as e:
        print(f"{ERROR}An error occurred: {e}{RESET}")

def explore_web():
    url = input(f"{INFO}Enter URL to explore: {RESET}")
    if url.startswith("http://") or url.startswith("https://"):
        os.system(f"start {url}" if platform.system() == 'Windows' else f"xdg-open {url}")
    else:
        print(f"{ERROR}Invalid URL format. Please include 'http://' or 'https://' in the URL.{RESET}")
    pause()

def check_ipconfig():
    if platform.system() == 'Windows':
        os.system('ipconfig')
    else:
        os.system('ifconfig')
    pause()

def system_info():
    print(f"{INFO}System Information:{RESET}")
    print(f"{INFO}Platform: {platform.system()} {platform.release()}{RESET}")
    print(f"{INFO}Machine: {platform.machine()}{RESET}")
    print(f"{INFO}Processor: {platform.processor()}{RESET}")
    print(f"{INFO}CPU Cores: {os.cpu_count()}{RESET}")
    pause()

def list_files():
    path = input(f"{INFO}Enter directory path to list files (or press Enter for current directory): {RESET}")
    if not path:
        path = '.'
    try:
        files = os.listdir(path)
        print(f"{INFO}Files in '{path}':{RESET}")
        for file in files:
            print(f"{SUCCESS}{file}{RESET}")
    except FileNotFoundError:
        print(f"{ERROR}Directory not found.{RESET}")
    except PermissionError:
        print(f"{ERROR}Permission denied.{RESET}")
    pause()

def show_datetime():
    now = datetime.now()
    print(f"{INFO}Current Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}{RESET}")
    pause()

def random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            joke = response.json()
            print(f"{SUCCESS}Here's a joke for you:{RESET}")
            print(f"{INFO}{joke['setup']}{RESET}")
            pause()
            print(f"{INFO}{joke['punchline']}{RESET}")
        else:
            print(f"{ERROR}Failed to fetch a joke. Status code: {response.status_code}{RESET}")
    except Exception as e:
        print(f"{ERROR}An error occurred: {e}{RESET}")
    pause()

def simple_calculator():
    try:
        print(f"{INFO}Simple Calculator{RESET}")
        num1 = float(input(f"{INFO}Enter the first number: {RESET}"))
        num2 = float(input(f"{INFO}Enter the second number: {RESET}"))
        operation = input(f"{INFO}Enter operation (+, -, *, /): {RESET}")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print(f"{ERROR}Error: Division by zero is not allowed.{RESET}")
                pause()
                return
            result = num1 / num2
        else:
            print(f"{ERROR}Invalid operation. Please try again.{RESET}")
            pause()
            return

        print(f"{SUCCESS}Result: {result}{RESET}")
    except ValueError:
        print(f"{ERROR}Invalid input. Please enter numbers only.{RESET}")
    pause()

def trivia_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
            "answer": "Paris"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "answer": "Mars"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["Harper Lee", "J.K. Rowling", "Ernest Hemingway", "Jane Austen"],
            "answer": "Harper Lee"
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "options": ["Oxygen", "Gold", "Silver", "Hydrogen"],
            "answer": "Oxygen"
        },
        {
            "question": "How many continents are there on Earth?",
            "options": ["5", "6", "7", "8"],
            "answer": "7"
        }
    ]
    
    question = random.choice(questions)
    print(f"{INFO}{question['question']}{RESET}")
    for i, option in enumerate(question['options']):
        print(f"{INFO}{i + 1}. {option}{RESET}")

    answer = input(f"{INFO}Enter the number of your answer: {RESET}")
    if question['options'][int(answer) - 1] == question['answer']:
        print(f"{SUCCESS}Correct!{RESET}")
    else:
        print(f"{ERROR}Incorrect. The correct answer is {question['answer']}.{RESET}")
    pause()

def discord_stuff_menu():
    while True:
        clear_screen()
        print(f"{INFO}=== Discord Stuff ==={RESET}\n")
        print("1. Get User Info by User ID")
        print("2. Back to Main Menu\n")
        
        choice = input(f"{INFO}Enter your choice (1-2): {RESET}")

        if choice == '1':
            user_id = input(f"{INFO}Enter the Discord User ID: {RESET}")
            get_discord_user_info(user_id)
        elif choice == '2':
            break
        else:
            print(f"{ERROR}Invalid choice. Please select a valid option.{RESET}")
            pause()

def main_menu():
    while True:
        try:
            clear_screen()
            print(f"{INFO}=== Multipurpose Python Client ==={RESET}\n")
            print("1. Discord Stuff")
            print("2. Explore Web")
            print("3. Check IP Configuration")
            print("4. System Information")
            print("5. List Files in Directory")
            print("6. Show Date and Time")
            print("7. Random Joke")
            print("8. Simple Calculator")
            print("9. Trivia Quiz")
            print("10. Exit\n")

            choice = input(f"{INFO}Enter your choice (1-10): {RESET}")

            if choice == '1':
                discord_stuff_menu()
            elif choice == '2':
                explore_web()
            elif choice == '3':
                check_ipconfig()
            elif choice == '4':
                system_info()
            elif choice == '5':
                list_files()
            elif choice == '6':
                show_datetime()
            elif choice == '7':
                random_joke()
            elif choice == '8':
                simple_calculator()
            elif choice == '9':
                trivia_quiz()
            elif choice == '10':
                print(f"{SUCCESS}Exiting the application. Goodbye!{RESET}")
                log_closure("User exited the application")
                pause()
                sys.exit()
            else:
                print(f"{ERROR}Invalid choice. Please select a valid option.{RESET}")
                log_closure("Invalid choice entered")
                pause()
        except Exception as e:
            print(f"{ERROR}An error occurred: {e}{RESET}")
            log_closure(f"An error occurred: {e}")
            pause()

if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        print(f"{ERROR}An error occurred: {e}{RESET}")
        log_closure(f"An error occurred: {e}")
    finally:
        input(f"\n{INFO}Press Enter to exit...{RESET}")
