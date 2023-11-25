# Utilities for multi-threading and multi-processing

import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def run_in_threads(target, args_list):
    """Run a function in parallel using threads.

    Args:
        target (function): The function to run in parallel.
        args_list (list): A list of argument tuples for each invocation of the function.
    """
    threads = []
    for args in args_list:
        thread = threading.Thread(target=target, args=args)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def run_in_processes(target, args_list):
    """Run a function in parallel using processes.

    Args:
        target (function): The function to run in parallel.
        args_list (list): A list of argument tuples for each invocation of the function.
    """
    processes = []
    for args in args_list:
        process = multiprocessing.Process(target=target, args=args)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

def thread_pool_executor(target, args_list, max_workers=None):
    """Run a function in parallel using a thread pool executor.

    Args:
        target (function): The function to run in parallel.
        args_list (list): A list of argument tuples for each invocation of the function.
        max_workers (int): The maximum number of threads that can be used to execute the given calls.
    """
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(lambda p: target(*p), args_list)

def process_pool_executor(target, args_list, max_workers=None):
    """Run a function in parallel using a process pool executor.

    Args:
        target (function): The function to run in parallel.
        args_list (list): A list of argument tuples for each invocation of the function.
        max_workers (int): The maximum number of processes that can be used to execute the given calls.
    """
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        executor.map(lambda p: target(*p), args_list)
